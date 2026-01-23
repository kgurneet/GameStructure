from __future__ import annotations

from game.factories.centennial import CentennialHallFactory
from game.factories.enemy_factory import EnemyFactory
from game.worlds.base import GameWorld


class CentennialHall(GameWorld):
    def _create_factory(self) -> EnemyFactory:
        return CentennialHallFactory()
