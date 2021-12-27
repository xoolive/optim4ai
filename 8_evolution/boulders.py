import numpy as np


class Boulders:
    def __init__(self, n: int) -> None:
        self.boulders = np.random.uniform(0.0, 1.0, (n, 3))
        self.boulders[:, 2] = 1 / (3 ** np.random.choice(range(2, 4), (n)))

    def __call__(self, x: float, y: float) -> float:
        res = 0
        for i in range(self.boulders.shape[0]):
            eval_ = (
                (x - self.boulders[i, 0]) ** 2
                + (y - self.boulders[i, 1]) ** 2
                - self.boulders[i, 2] ** 2
            )
            if eval_ < 0:
                res += eval_
        return res

    def grid(self, resolution: int = 100):

        vec = np.linspace(0, 1, resolution)
        X, Y = np.meshgrid(vec, vec)
        Z = np.zeros(X.shape)

        for i in range(self.boulders.shape[0]):
            eval_ = (
                (X - self.boulders[i, 0]) ** 2
                + (Y - self.boulders[i, 1]) ** 2
                - self.boulders[i, 2] ** 2
            )
            Z[eval_ < 0] += eval_[eval_ < 0]

        return X, Y, Z
