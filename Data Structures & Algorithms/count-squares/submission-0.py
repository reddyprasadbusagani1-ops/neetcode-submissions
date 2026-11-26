
from collections import defaultdict
from typing import List

class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        total = 0

        for (x1, y1), freq in self.points.items():

            side = abs(x1 - x)

            if side == 0 or abs(y1 - y) != side:
                continue

            p2 = (x, y1)
            p3 = (x1, y)

            total += (
                freq
                * self.points.get(p2, 0)
                * self.points.get(p3, 0)
            )

        return total
