from dataclasses import dataclass


@dataclass
class Foo:
    bar: str

    def __add__(self, other: str | int) -> str:
        match other:
            case str():
                return self.bar + other
            case int():
                return self.bar + str(other)


f = Foo("Hallo")
print(f)
print(f + " Welt")   # Ausgabe: Hallo Welt
print(f + 123)        # Ausgabe: Hallo123
