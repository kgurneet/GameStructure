from __future__ import annotations

from game.core.enemy import Enemy


class Goomba(Enemy):
    def __init__(self) -> None:
        super().__init__(name="Goomba", emoji="🍄", power=1)


class Galoomba(Enemy):
    def __init__(self) -> None:
        super().__init__(name="Galoomba", emoji="🥔", power=3)


class GrandGoomba(Enemy):
    def __init__(self) -> None:
        super().__init__(name="Grand Goomba", emoji="👑", power=6)
