# Linear programming

[« Previous](../3_pytorch) \| [Home ↑](../) \| [Next »](../5_milp)

**Linear Programming** (LP) is in some sense the fundamental tool of optimisation and Operations Research (OR). Many real-life problems can be modelled with linear objective function and constraints, and, to date, the Simplex Method for solving LPs is one of the most efficient and powerful algorithms in Operations Research.

|     | Topics                                     |
| --- | ------------------------------------------ |
| 4.1 | [Example problems and modelling](problems) |
| 4.2 | Graphical resolution (notebook)            |
| 4.3 | The simplex algorithm (notebook)           |
| 4.4 | [Solving LP problems with Python](python)  |

Notebook sessions can be run on:

- your own computer: there are no specific requirements besides the `numpy`, `matplotlib` and `scipy` libraries.

- the computer in the classroom. Activate the environment before running Jupyter lab:

  ```bash
  # The following commands only work in the classroom
  module load python/3.7
  source activate ~x.olive/students
  ```

- [Google Colab](https://colab.research.google.com/github/xoolive/optim4ai/) is a good fallback option, but data files must be uploaded, and solutions to exercices must be checked separately from the [Github folder](https://github.com/xoolive/optim4ai/tree/master/2_gradient/solutions).
