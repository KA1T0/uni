recipes = [
    ("Daiquiri", ["Rum", "Limette", "Zucker"]),
    ("Mojito", ["Rum", "Limette", "Zucker", "Minze", "Soda"]),
    ("Whiskey Sour", ["Whiskey", "Zitrone", "Zucker"]),
    ("Tequila Sour", ["Tequila", "Zitrone", "Zucker"]),
    ("Moscow Mule", ["Vodka", "Limette", "Ginger ale"]),
    ("Munich Mule", ["Gin", "Limette", "Ginger ale"]),
    ("Cuba Libre", ["Rum", "Coke"])
    ]


def mixable(recipes, ingredients: list[str]) -> list[str]:
    result = []
    for recipe, ingredient in recipes:
        vorhanden = True
        for i in ingredient:
            if i not in ingredients:
                vorhanden = False
                break
        if vorhanden is True:
            result += [recipe]
    return result
    #    if all(i in ingredients for i in ingredient):
    #        result.append(recipe)
    # return result


if __name__ == "__main__":
    print(mixable(recipes, ["Rum", "Whiskey", "Limette", "Zucker", "Coke", "Zitrone"]))
    print(mixable(recipes, ["Rum", "Vodka", "Limette", "Zucker", "Ginger ale"]))
    print(mixable([], ["Orangensaft"]))
