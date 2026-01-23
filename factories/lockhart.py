from __future__ import annotations

from game.enemies.goomba import GrandGoomba
from game.enemies.koopa import SuperKoopa
from game.enemies.piranha import GiantPiranhaPlant
from game.factories.enemy_factory import EnemyFactory
from game.core.enemy import Enemy


class LockhartHallFactory(EnemyFactory):
    @property
    def world_name(self) -> str:
        return "Lockhart Hall"

    def create_piranha(self) -> Enemy:
        return GiantPiranhaPlant()

    def create_goomba(self) -> Enemy:
        return GrandGoomba()

    def create_koopa(self) -> Enemy:
        return SuperKoopa()
