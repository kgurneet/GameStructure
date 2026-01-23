from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Enemy:
    
    name: str
    emoji: str
    power: int

    def describe(self) -> str:
        return f"{self.emoji} {self.name} (power={self.power})"

    def __str__(self) -> str:
        return self.describe()