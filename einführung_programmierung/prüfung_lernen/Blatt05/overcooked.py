recipes = [
    ("Daiquiri", ["Rum", "Limette", "Zucker"]),
    ("Mojito", ["Rum", "Limette", "Zucker", "Minze", "Soda"]),
    ("Whiskey Sour", ["Whiskey", "Zitrone", "Zucker"]),
    ("Tequila Sour", ["Tequila", "Zitrone", "Zucker"]),
    ("Moscow Mule", ["Vodka", "Limette", "Ginger ale"]),
    ("Munich Mule", ["Gin", "Limette", "Ginger ale"]),
    ("Cuba Libre", ["Rum", "Coke"])
    ]


def mixable(recipes, ingredients: list[str]) -> list:
    result = []
    for recipe in recipes:
        if all(ingredient in ingredients for ingredient in recipe[1]):
            result.append(recipe[0])
    return result


if __name__ == "__main__":
    print(mixable(recipes, ["Rum", "Whiskey", "Limette", "Zucker", "Coke", "Zitrone"]))
    print(mixable(recipes, ["Rum", "Vodka", "Limette", "Zucker", "Ginger ale"]))
    print(mixable([], ["Orangensaft"]))
