from __future__ import annotations

from game.core.enemy import Enemy


class KoopaTroopa(Enemy):
    def __init__(self) -> None:
        super().__init__(name="Koopa Troopa", emoji="🐢", power=2)


class DryBonesKoopa(Enemy):
    def __init__(self) -> None:
        super().__init__(name="Dry Bones Koopa", emoji="🦴", power=4)


class SuperKoopa(Enemy):
    def __init__(self) -> None:
        super().__init__(name="Super Koopa", emoji="🚀", power=7)

