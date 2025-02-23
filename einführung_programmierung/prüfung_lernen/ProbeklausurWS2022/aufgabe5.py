# Aufgabe 5 (Dataclasses) #####################################################

from dataclasses import dataclass


@dataclass
class Vehicle:
    seats: int
    hp: int
    ccm: int
    weight: int

    def fun_factor(self):
        fun = (10 * self.hp + self.ccm) / self.weight
        return fun

    def __post_init__(self):
        if not (self.seats > 0 and self.seats < 10):
            raise ValueError
        if not (self.hp > 0 and self.ccm > 0 and self.weight > 0):
            raise ValueError

    def __gt__(self, other: 'Vehicle') -> bool:
        if self.fun_factor() > other.fun_factor():
            return True
        else:
            return False


@dataclass
class Car(Vehicle):
    spoiler: bool

    def fun_factor(self):
        factor = super().fun_factor()
        if self.spoiler is True:
            return factor * 1.2
        return factor


@dataclass
class Motorcycle(Vehicle):
    sidecar: bool

    def __post_init__(self):
        if self.sidecar is True:
            if not (self.seats == 2 or self.seats == 3):
                raise ValueError
        if not self.sidecar:
            if not (self.seats == 1 or self.seats == 2):
                raise ValueError

    def fun_factor(self):
        #factor = super().fun_factor()
        if self.sidecar is False:
            return super().fun_factor() * 0.5
        if self.sidecar is True:
            return super().fun_factor() * 2.4


def coolness(vehicle: Vehicle) -> float:
    coolness = vehicle.hp / vehicle.weight if vehicle.weight <= 3500 else 0
    match vehicle:
        case Car(spoiler=True):
            return coolness * 1.2
        case Motorcycle(sidecar=True):
            return coolness * 0.8
        case _:
            return coolness


v = Vehicle(3, 5000, 5, 2000)
v1 = Vehicle(4, 5000, 3, 1400)
c = Car(3, 5000, 5, 600, True)
m = Motorcycle(2, 5000, 5, 1700, True)

#print(m.fun_factor())
#print(Vehicle.__gt__(v, v1))
print(coolness(v))
print(coolness(m))
print(coolness(c))
