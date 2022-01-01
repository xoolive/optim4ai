from typing import TypeVar

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from numpy.typing import NDArray

F = TypeVar("F", float, NDArray[np.float64])

__all__ = [
    "himmelblau",
    "rastrigin",
    "boulders",
    "animate_function",
    "contour_function",
]


def himmelblau(x: F, y: F) -> F:
    return (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2


def rastrigin(*X: F, **kwargs: np.float64) -> F:
    A = kwargs.get("A", 10)
    return A + sum([(x ** 2 - A * np.cos(2 * np.pi * x)) for x in X])


class boulders:
    def __init__(self, n: int) -> None:
        self.boulders = np.random.uniform(0.0, 1.0, (n, 3))
        self.boulders[:, 2] = 1 / (3 ** np.random.choice(range(2, 4), (n)))

    def __call__(self, x: F, y: F) -> np.ndarray:
        shape = getattr(x, "shape", tuple())
        z = np.zeros(shape)
        for i in range(self.boulders.shape[0]):
            eval_ = (
                (x - self.boulders[i, 0]) ** 2
                + (y - self.boulders[i, 1]) ** 2
                - self.boulders[i, 2] ** 2
            )
            z[eval_ < 0] += eval_[eval_ < 0]
        return z


def anim_to_html(anim: animation.Animation):
    plt.close(anim._fig)
    return anim.to_html5_video()


animation.Animation._repr_html_ = anim_to_html


def animate_view(ax):
    def animate(i):
        ax.view_init(-10 - 10 * np.cos(i / 5), 30 + 4 * i)
        return []

    return animate


def animate_function(fun, X, Y, **kwargs):
    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(projection="3d"))
    ax.view_init(-20, 30)
    ax.plot_surface(X, Y, fun(X, Y, **kwargs), cmap=plt.cm.viridis)
    return animation.FuncAnimation(
        fig, animate_view(ax), frames=90, interval=200, blit=True
    )


def contour_function(fun, X, Y, **kwargs):
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.contour(X, Y, fun(X, Y, **kwargs), alpha=0.5)
    for loc in ["right", "top"]:
        ax.spines[loc].set_visible(False)
    for loc in ["left", "bottom"]:
        ax.spines[loc].set_position(("data", 0))
        ax.spines[loc].set_color("#bab0ac")
    ax.tick_params(labelsize=14, color="#bab0ac", size=10)
    return ax
