from __future__ import annotations

from game.core.enemy import Enemy


class PiranhaPlant(Enemy):
    def __init__(self) -> None:
        super().__init__(name="Piranha Plant", emoji="🌿", power=2)


class PoisonPiranhaPlant(Enemy):
    def __init__(self) -> None:
        super().__init__(name="Poison Piranha Plant", emoji="☠️", power=4)


class GiantPiranhaPlant(Enemy):
    def __init__(self) -> None:
        super().__init__(name="Giant Piranha Plant", emoji="🦖", power=7)
