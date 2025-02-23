import pygame
from dataclasses import dataclass
from asteroids import (
    Vec2D, GameObject, Projectile, Ammunition, Health, Ship, Asteroid
)
import random


@dataclass
class Game:
    width: int
    height: int
    ship: Ship
    objects: list[GameObject]
    bonus: int = 0

    def __post_init__(self):
        self.objects.append(self.ship)

    def draw(self, screen: pygame.Surface):
        for obj in self.objects:
            obj.draw(screen)

    def remove_dead(self):
        alive = []
        for obj in self.objects:
            if obj.alive:
                alive += [obj]
        self.objects = alive

    def generate_asteroid(self) -> Asteroid:
        p = Vec2D(random.randint(0, self.width), 0)
        return Asteroid(p, random.randint(10, 30), True, (255, 255, 255), 0,
                        random.random() < 0.01)

    def generate_health_item(self, anywhere: bool) -> Health:
        p = Vec2D(random.randint(0, self.width), random.randint(0, self.height // 2) if anywhere else 0)
        return Health(p, 5, True, (50, 255, 0), 0, 10)

    def generate_ammunition_item(self, anywhere: bool) -> Ammunition:
        p = Vec2D(random.randint(0, self.width), random.randint(0, self.height // 2) if anywhere else 0)
        return Ammunition(p, 5, True, (0, 50, 255), 0, 7)

    def update(self, input_direction: Vec2D, delta: float, shoot: bool, ga: bool, gh: bool, gm: bool):
        self.ship.position.x += input_direction.x * delta
        self.ship.position.y += input_direction.y * delta
        for obj in self.objects:
            obj.update(self.width, self.height, delta)

        for obj in self.objects:
            for obj2 in self.objects:
                if obj is not obj2 and obj.is_colliding(obj2):
                    obj.on_collision(obj2)
                    if (isinstance(obj, Asteroid) and isinstance(obj2, Projectile)
                            and obj.special):
                        self.bonus += 20
        if self.bonus:
            self.objects += [self.generate_health_item(True)]
            self.objects += [self.generate_ammunition_item(True)]
            self.bonus -= 1
        if shoot:
            self.objects.append(self.ship.shoot())
        if ga:
            self.objects += [self.generate_asteroid()]
        if gh:
            self.objects += [self.generate_health_item(False)]
        if gm:
            self.objects += [self.generate_ammunition_item(False)]
        self.remove_dead()


#########################################


def main(game: Game, resolution: tuple[int, int], speed: int, spawn_rate_a: int, spawn_rate_h: int, spawn_rate_m: int, usefont: bool):
    pygame.display.init()
    pygame.display.set_caption("Asteroids")
    pygame.font.init()
    font = None
    if usefont:
        font = pygame.font.SysFont('', 40)
    fpsClock = pygame.time.Clock()
    delta = 1 / 60
    screen = pygame.display.set_mode((resolution[0], resolution[1] + 30))
    frame = 0
    while True:

        screen.fill((0, 0, 0))

        v = Vec2D(0, 0)
        s = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game.ship.alive:
                        s = True
                    else:
                        game = new_game(resolution)
                        pygame.quit()
                        main(game, resolution, speed, spawn_rate_a, spawn_rate_h, spawn_rate_m, usefont)
                        return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            v.y -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            v.x += 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            v.y += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            v.x -= 1

        if game.ship.alive:
            game.update(v, delta, s, frame % spawn_rate_a == 0, (frame + 150) % spawn_rate_h == 0, frame % spawn_rate_m == 0)
        else:
            if font:
                game_over = font.render('- GAME OVER -', False, (255, 255, 255))
                restart = font.render("press SPACE to restart", False, (255, 255, 255))
                c_game_over = game_over.get_rect(center=(resolution[0] / 2, resolution[1] / 2))
                c_restart = restart.get_rect(center=(resolution[0] / 2, resolution[1] / 2 + resolution[1] // 10))
                screen.blit(game_over, c_game_over)

                if pygame.time.get_ticks() % 1000 > 500:
                    screen.blit(restart, c_restart)
            else:
                print(f'- GAME OVER - press SPACE to restart{10 * " "}\r', end="")

        game.draw(screen)

        pygame.draw.rect(screen, (50, 50, 50), (0, resolution[1], resolution[0], 30))
        if font:
            score = font.render(f'health: {game.ship.hp} - ammunition: {game.ship.shots} - score: {frame // 60}', False, (255, 255, 255))
            screen.blit(score, (0, resolution[1]))
        elif frame % 10 == 0:
            print(f'health: {game.ship.hp} - ammunition: {game.ship.shots} - score: {frame // 60}{10 * " "}\r', end="")
        delta = fpsClock.tick(60) * speed / 10
        pygame.display.flip()
        if game.ship.alive:
            frame += 1


def new_game(resolution: tuple[int, int]) -> Game:
    ship = Ship(Vec2D(resolution[0] // 2, resolution[1] // 2), 10, True, (0, 200, 200), 20, 100)
    game = Game(1000, 680, ship, [])
    return game


if __name__ == "__main__":
    resolution = (1000, 680)
    game = new_game(resolution)
    main(game, resolution, 2, 5, 150, 100, usefont=True)
