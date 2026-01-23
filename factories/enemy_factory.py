from __future__ import annotations

from abc import ABC, abstractmethod

from game.core.enemy import Enemy


class EnemyFactory(ABC):

    @property
    @abstractmethod
    def world_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def create_piranha(self) -> Enemy:
        raise NotImplementedError

    @abstractmethod
    def create_goomba(self) -> Enemy:
        raise NotImplementedError

    @abstractmethod
    def create_koopa(self) -> Enemy:
        raise NotImplementedError