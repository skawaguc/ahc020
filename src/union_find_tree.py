from __future__ import annotations


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

