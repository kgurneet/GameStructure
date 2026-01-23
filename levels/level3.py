from __future__ import annotations

from game.core.enemy import Enemy
from game.levels.base import GameLevel


class Level3(GameLevel):
    @property
    def name(self) -> str:
        return "Level 3: Finals Frenzy"

    def _build_enemies(self) -> list[Enemy]:
        enemies: list[Enemy] = []
        enemies.extend(self._repeat([self.factory.create_piranha()], 12))
        enemies.extend(self._repeat([self.factory.create_goomba()], 12))
        enemies.extend(self._repeat([self.factory.create_koopa()], 12))
        self._rng.shuffle(enemies)
        return enemies
