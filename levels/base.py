from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from random import Random
from typing import Iterable

from game.core.enemy import Enemy
from game.factories.enemy_factory import EnemyFactory


@dataclass(frozen=True, slots=True)
class PlayResult:
    world: str
    level: str
    spawns: tuple[str, ...]
    total_power: int
    badge: str


class GameLevel(ABC):
   

    def __init__(self, factory: EnemyFactory, rng: Random | None = None) -> None:
        self._factory = factory
        self._rng = rng or Random()
        self._enemies: list[Enemy] | None = None

    @property
    def factory(self) -> EnemyFactory:
        return self._factory

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def _build_enemies(self) -> list[Enemy]:
        raise NotImplementedError

    def enemies(self) -> list[Enemy]:
        if self._enemies is None:
            self._enemies = self._build_enemies()
        return self._enemies

    def spawn_log(self) -> tuple[str, ...]:
        return tuple(enemy.describe() for enemy in self.enemies())

    def total_power(self) -> int:
        return sum(e.power for e in self.enemies())

    def play(self) -> PlayResult:
        total = self.total_power()
        badge = self._badge_for(total)
        return PlayResult(
            world=self.factory.world_name,
            level=self.name,
            spawns=self.spawn_log(),
            total_power=total,
            badge=badge,
        )

    @staticmethod
    def _badge_for(total_power: int) -> str:
        if total_power <= 20:
            return "📘 Freshman Explorer"
        if total_power <= 60:
            return "📗 Campus Adventurer"
        if total_power <= 120:
            return "📕 Legend of the Lecture Halls"
        return "🏆 Mythic Marathoner"

    def _repeat(self, enemies: Iterable[Enemy], times: int) -> list[Enemy]:
        out: list[Enemy] = []
        for _ in range(times):
            out.extend(enemies)
        return out
