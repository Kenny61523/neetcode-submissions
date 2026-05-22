class CountSquares:

    def __init__(self):
        self.cntPoints = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.cntPoints[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for x, y in self.points:
            if abs(x - px) != abs(y - py) or x == px or y == py:
                continue
            res += self.cntPoints[(x, py)] * self.cntPoints[(px, y)]
        
        return res
            
        