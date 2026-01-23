from __future__ import annotations

from game.factories.duckworth import DuckworthCentreFactory
from game.factories.enemy_factory import EnemyFactory
from game.worlds.base import GameWorld


class DuckworthCentre(GameWorld):
    def _create_factory(self) -> EnemyFactory:
        return DuckworthCentreFactory()
