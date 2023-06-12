from __future__ import annotations
import math


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


class UnionFindTree:
    def __init__(self, n: int) -> None:
        """コンストラク.

        Args:
            n (int): 要素数
        """
        self.__par = [i for i in range(n)]
        self.__rnk = [0] * n
        self.__cnt = [1] * n

    def find(self, x: int) -> int:
        """xの根を取得する.

        Args:
            x (int): 要素

        Returns:
            int: 根
        """
        if self.__par[x] == x:
            return x
        self.__par[x] = self.find(self.__par[x])
        return self.__par[x]

    def unite(self, x: int, y: int) -> None:
        """xとyを結合する.

        Args:
            x (int): 要素
            y (int): 要素
        """
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        self.__cnt[x] = self.__cnt[y] = self.__cnt[x] + self.__cnt[y]
        if self.__rnk[x] < self.__rnk[y]:
            self.__par[x] = y
        else:
            self.__par[y] = x
            if self.__rnk[x] == self.__rnk[y]:
                self.__rnk[x] += 1

    def same(self, x: int, y: int) -> bool:
        """xとyが同じグループかどうか判定する.

        Args:
            x (int): 要素
            y (int): 要素

        Returns:
            bool: xとyが同じグループであれば真、なければ偽
        """
        return self.find(x) == self.find(y)


def get_input() -> tuple[int, int, int, list[int], list[int], list[int], list[int], list[int], list[int], list[int]]:
    """標準入力を取得する.

    Returns:
        tuple[int, int, int, list[int], list[int], list[int], list[int], list[int], list[int], list[int]]: 標準入力
    """
    N, M, K = list(map(int, input().split()))
    x, y = [int()]*N, [int()]*N
    for i in range(N):
        x[i], y[i] = list(map(int, input().split()))
    u, v, w = [int()]*M, [int()]*M, [int()]*M
    for i in range(M):
        u[i], v[i], w[i] = list(map(int, input().split()))
        u[i] -= 1
        v[i] -= 1
    a, b = [int()]*K, [int()]*K
    for i in range(K):
        a[i], b[i] = list(map(int, input().split()))
    return N, M, K, x, y, u, v, w, a, b


def solve() -> tuple[list[int], list[int]]:
    """求解処理.

    Returns:
        tuple[list[int], list[int]]: 電源、出力電力
    """
    # 各辺について電源のON/OFFを求める
    # クラスカル法
    B = [0] * M
    es = [Edge(i, u[i], v[i], w[i]) for i in range(M)]
    es.sort()
    uft = UnionFindTree(N)
    for i in range(M):
        e = es[i]
        if not uft.same(e.u, e.v):
            uft.unite(e.u, e.v)
            B[e.i] = 1

    # 各頂点について整数値の出力強度を求める
    # 各住民について最も近い放送局の出力強度を設定
    P = [0] * N
    for k in range(K):
        min_i, min_dist = 0, 1e16
        for i in range(N):
            dist = (a[k]-x[i])**2 + (b[k]-y[i])**2
            if dist < min_dist:
                min_i = i
                min_dist = dist
        P[min_i] = max(P[min_i], int(math.ceil(math.sqrt(min_dist))))

    return P, B


def output() -> None:
    """結果を出力する.
    """
    print(*P)
    print(*B)


if __name__ == "__main__":
    # 入力
    N, M, K, x, y, u, v, w, a, b = get_input()

    # 求解
    P, B = solve()

    # 出力
    output()
