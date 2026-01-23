from __future__ import annotations

from game.enemies.goomba import Galoomba
from game.enemies.koopa import DryBonesKoopa
from game.enemies.piranha import PoisonPiranhaPlant
from game.factories.enemy_factory import EnemyFactory
from game.core.enemy import Enemy


class CentennialHallFactory(EnemyFactory):
    @property
    def world_name(self) -> str:
        return "Centennial Hall"

    def create_piranha(self) -> Enemy:
        return PoisonPiranhaPlant()

    def create_goomba(self) -> Enemy:
        return Galoomba()

    def create_koopa(self) -> Enemy:
        return DryBonesKoopa()
