# Solving MILP problems with Python

[« Previous](.) \| [Up ↑](.) \| [Next »](../6_complexity)

We remind the three dedicated libraries which we can use for solving LP and MILP problems:

- the [PuLP library](https://coin-or.github.io/pulp/), with the default open-source solver CBC. This solver falls behind its commercial counterparts but is sufficient for demonstration purposes within this course. It is possible to run a PuLP model with both solvers below (without catchy customisations);

- the [IBM Decision Optimization CPLEX Modeling `docplex`](https://ibmdecisionoptimization.github.io/docplex-doc/) for Python. Be careful as it may fall behind your version of Python. You are entitled to an academic license for education purposes if you register online. **Commercial use is prohibited**.

- the [Gurobi Python interface](https://www.gurobi.com/documentation/9.5/quickstart_windows/cs_python.html). You are entitled to an academic license for education purposes if you register online. **Commercial use is prohibited**.

## The assignment problem

In the classical _assignment problem_, we look for an assignment of $n$ candidates on $n$ positions. For each couple (candidate, position) we have a measure of the interest of this association. The goal is to find the global assignment that maximises the interest. It is a _combinatorial problem_, as there are $n!$ possible assignments of the candidates on the positions.

In order to model this problem, we will use binary variables to represent the assignment of candidate $i$ on position $j$. The constraints must ensure that there is exactly one candidate assigned on each position.

Gains are modelled with the following matrix:

```python
c_ij = [
    [ 8,  6,  7,  8,  9],
    [11,  7,  5,  8, 10],
    [ 8, 10,  9, 11,  6],
    [10,  9,  7,  8,  7],
    [11,  6,  9,  7,  8]
]
```

<div class="alert alert-warning"><b>Exercice:</b>

You will find in the <code>code/</code> folder an implementation of the assignment problem with the three libraries.<br/>
Replace integer variables with continous variables (think twice about the bounds) and run the solver again.

</div>

<details>
    <summary><b>Solution</b> (click to unfold)</summary>
    <p>We benefit here from the unimodularity of the A matrix: the vertices of the polyhedron $P = \{x \geq 0 \,|\, Ax = b\}$ all have integral components</p>
    <p>A $m \times n, m\leq n$ matrix, is unimodular iff all the determinant values of $m \times m$ submatrices are 1 or -1.</p>
</details>

## The unit commitment problem

An energy company owns two power plants with the following features:

- Plant 1 operates between 50 and 400MW for a cost of 20€/MWh
- Plant 2 operates between 20 and 200MW for a cost of 40€/MWh

The two plants must produce in order to meet an electricity demande given in the file `demand.txt` (one line per hour for one week).

You must note that if a power plant produces electricity, it must run at least two consecutive hours.

<div class="alert alert-warning"><b>Exercice:</b>

Model and implement the unit commitment problem with the library of your choice.

</div>

[« Previous](.) \| [Up ↑](.) \| [Next »](../6_complexity)
