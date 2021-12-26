# Solving LP problems with Python

[« Previous](.) \| [Up ↑](.) \| [Next »](../5_milp)

In the notebook, we illustrated how the `linprog` function in `scipy.optimize` implements the simplex, provided we construct the `A`, `b` and `c` matrices.

We implemented below the steel manufacturing problem with the `linprog` function (note the equality and inequality constraints).

<div>
<script src="https://emgithub.com/embed.js?target=https://raw.githubusercontent.com/xoolive/optim4ai/blob/master/4_linear/code/steel_scipy.py&style=github-gist&showLineNumbers=on&showCopy=on"></script>
</div>

This process of constructing such large matrices is error-prone, and in practice, we use dedicated libraries:

- the [PuLP library](https://coin-or.github.io/pulp/), with the default open-source solver CBC. This solver falls behind its commercial counterparts but is sufficient for demonstration purposes within this course. It is possible to run a PuLP model with both solvers below (without catchy customisations);

- the [IBM Decision Optimization CPLEX Modeling `docplex`](https://ibmdecisionoptimization.github.io/docplex-doc/) for Python. Be careful as it may fall behind your version of Python. You are entitled to an academic license for education purposes if you register online. **Commercial use is prohibited**.

- the [Gurobi Python interface](https://www.gurobi.com/documentation/9.5/quickstart_windows/cs_python.html). You are entitled to an academic license for education purposes if you register online. **Commercial use is prohibited**.

<div class="alert alert-warning"><b>Exercice:</b>

You will find in the <code>code/</code> folder an implementation of the steel manufacturing problem with the three libraries. Implement the pasta production problem with the library of your choice.

</div>

[« Previous](.) \| [Up ↑](.) \| [Next »](../5_milp)
