from __future__ import annotations

from game.enemies.goomba import Goomba
from game.enemies.koopa import KoopaTroopa
from game.enemies.piranha import PiranhaPlant
from game.factories.enemy_factory import EnemyFactory
from game.core.enemy import Enemy


class DuckworthCentreFactory(EnemyFactory):
    @property
    def world_name(self) -> str:
        return "Duckworth Centre"

    def create_piranha(self) -> Enemy:
        return PiranhaPlant()

    def create_goomba(self) -> Enemy:
        return Goomba()

    def create_koopa(self) -> Enemy:
        return KoopaTroopa()