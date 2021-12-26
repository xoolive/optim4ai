# Mixed integer linear programming

[« Previous](../4_linear) \| [Home ↑](../) \| [Next »](../6_complexity)

With _linear programming_ we have studied a special case of constrained optimization where both the objective function and the constraints are linear. The solution approaches (_simplex_ and others) are based on the properties of these problems: continuous and convex set of feasible solutions, convex objective function. This leads to polynomial approaches and very powerful algorithms.

Many practical cases, however, show features that linear constraints with continuous variables cannot represent: discrete choices, some non-linearities (min, max, absolute, boolean relations, etc.) We must use integer or binary variable to represent them. Unfortunately, even with linear constraints and objective, it is not possible to rely on the same smart properties as for linear programming. In general, these problems are much more difficult to solve.

**Mixed integer linear programming** (MILP) is dedicated to adapting linear programming to discrete (integer or binary) or mixed continuous/discrete variables.

|     | Topic                                                     |
| --- | --------------------------------------------------------- |
| 5.1 | Linear relaxation of a MILP problem (notebook)            |
| 5.2 | Branch & Bound (notebook)                                 |
| 5.3 | [Modelling and solving MILP problems with Python](python) |
