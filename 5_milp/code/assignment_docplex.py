import numpy as np
from docplex.mp.model import Model

c_ij = [
    [8, 6, 7, 8, 9],
    [11, 7, 5, 8, 10],
    [8, 10, 9, 11, 6],
    [10, 9, 7, 8, 7],
    [11, 6, 9, 7, 8],
]
n = len(c_ij)

# New problem
m = Model("assignment")

# Decision variables
x_ij = m.binary_var_matrix(n, n)

# Constraints
m.add_constraints(m.sum(x_ij[i, j] for i in range(n)) == 1 for j in range(n))
m.add_constraints(m.sum(x_ij[i, j] for j in range(n)) == 1 for i in range(n))

# Objective function
m.maximize(m.sum(x_ij[i, j] * c_ij[i][j] for i in range(n) for j in range(n)))

# Problem solving

if m.solve():  # check the problem is really solved
    m.print_solution()

    print()
    print(f"Objective function: {m.objective_value}")
    print("Solution to the problem:")
    res = np.fromiter((var.solution_value for var in x_ij.values()), dtype=int)
    print(res.reshape(n, n))
else:
    print(m.get_solve_status())
