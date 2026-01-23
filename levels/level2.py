from __future__ import annotations

from game.core.enemy import Enemy
from game.levels.base import GameLevel


class Level2(GameLevel):
    @property
    def name(self) -> str:
        return "Level 2: Midterm Mayhem"

    def _build_enemies(self) -> list[Enemy]:
        enemies: list[Enemy] = []
        enemies.extend(self._repeat([self.factory.create_piranha()], 6))
        enemies.extend(self._repeat([self.factory.create_goomba()], 9))
        enemies.extend(self._repeat([self.factory.create_koopa()], 6))
        return enemies
