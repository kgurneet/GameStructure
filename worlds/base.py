from __future__ import annotations

from abc import ABC, abstractmethod

from game.factories.enemy_factory import EnemyFactory
from game.levels.base import PlayResult
from game.levels.level1 import Level1
from game.levels.level2 import Level2
from game.levels.level3 import Level3


class GameWorld(ABC):
    """
    A world owns a single enemy factory and creates levels from it.
    """

    def __init__(self) -> None:
        self._factory = self._create_factory()

    @property
    def factory(self) -> EnemyFactory:
        return self._factory

    @abstractmethod
    def _create_factory(self) -> EnemyFactory:
        raise NotImplementedError

    def create_level(self, number: int) -> Level1 | Level2 | Level3:
        if number == 1:
            return Level1(self.factory)
        if number == 2:
            return Level2(self.factory)
        if number == 3:
            return Level3(self.factory)
        raise ValueError(f"Invalid level number: {number}")

    def play_level(self, number: int) -> PlayResult:
        return self.create_level(number).play()

