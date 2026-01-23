from __future__ import annotations

from game.factories.enemy_factory import EnemyFactory
from game.factories.lockhart import LockhartHallFactory
from game.worlds.base import GameWorld


class LockhartHall(GameWorld):
    def _create_factory(self) -> EnemyFactory:
        return LockhartHallFactory()
