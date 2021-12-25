# Gradient descent methods

[« Previous](../1_introduction) \| [Home ↑](../) \| [Next »](../3_pytorch)

In this section, we will go through a particular class of problems where functions are differentiable.

This topic is often referred to as **Non-Linear Programming**, in contrast with [Linear Programming](../4_linear/) which we will study in a further section.

|     | Topics                                                      |
| --- | ----------------------------------------------------------- |
| 2.1 | [Example problems, modelling](problems)                     |
| 2.2 | A walk through gradient methods (notebook)                  |
| 2.3 | [Solve the city placement problem](city_problem) (notebook) |

Notebook sessions can be run on:

- your own computer: there are no specific requirements besides the `numpy`, `matplotlib` and `scipy` libraries.

- the computer in the classroom. Activate the environment before running Jupyter lab:

  ```bash
  # The following commands only work in the classroom
  module load python/3.7
  source activate ~x.olive/students
  ```

- [Google Colab](https://colab.research.google.com/github/xoolive/optim4ai/) is a good fallback option, but data files must be uploaded, and solutions to exercices must be checked separately from the [Github folder](https://github.com/xoolive/optim4ai/tree/master/2_gradient/solutions).
