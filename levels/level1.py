from __future__ import annotations

from game.core.enemy import Enemy
from game.levels.base import GameLevel


class Level1(GameLevel):
    @property
    def name(self) -> str:
        return "Level 1: Syllabus Scramble"

    def _build_enemies(self) -> list[Enemy]:
        enemies: list[Enemy] = []
        enemies.extend(self._repeat([self.factory.create_piranha()], 3))
        enemies.extend(self._repeat([self.factory.create_goomba()], 6))
        enemies.extend(self._repeat([self.factory.create_koopa()], 3))
        return enemies

