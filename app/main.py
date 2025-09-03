from __future__ import annotations
from typing import Any


class Animal:

    alive: list[Animal] = []

    def __init__(
            self,
            name: str,
            *args: Any,
            **kwargs,
    ) -> None:

        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):

    def hide(self) -> None:

        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, other: Animal) -> None:
        if isinstance(other, Herbivore):
            if not other.hidden:
                other.health -= 50
                other.health = max(0, other.health)
                other.die()
