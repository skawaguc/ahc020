from __future__ import annotations


class Edge:
    def __init__(self, idx: int, u: int, v: int, cost: int) -> None:
        """コンストラク.

        Args:
            i (int): 要素番号
            u (int): 節点
            v (int): 節点
            cost (int): コスト
        """
        self.i = idx
        self.u = u
        self.v = v
        self.cost = cost

    def __lt__(self, other: Edge) -> bool:
        return self.cost < other.cost
