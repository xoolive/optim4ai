import numpy as np
import gurobipy as grb

c_ij = [
    [8, 6, 7, 8, 9],
    [11, 7, 5, 8, 10],
    [8, 10, 9, 11, 6],
    [10, 9, 7, 8, 7],
    [11, 6, 9, 7, 8],
]
n = len(c_ij)

# New problem
m = grb.Model("assignment")

# Decision variables
x_ij = m.addVars(n, n, vtype=grb.GRB.BINARY)

# Constraints
m.addConstrs(grb.quicksum(x_ij[i, j] for i in range(n)) == 1 for j in range(n))
m.addConstrs(grb.quicksum(x_ij[i, j] for j in range(n)) == 1 for i in range(n))

# Objective function
m.setObjective(
    grb.quicksum(x_ij[i, j] * c_ij[i][j] for i in range(n) for j in range(n)),
    grb.GRB.MAXIMIZE,
)

# Problem solving
m.update()
m.optimize()

# /!\ Never remove this line
# The problem may return wrong solution if the status is:
# - GRB.INF_OR_UNBD: the polyhedron is open
# - GRB.INFEASIBLE: the polyhedron is empty and no solution exists

assert m.status == grb.GRB.OPTIMAL

print()
print("Solution to the problem:")
print(f"Objective function: {m.objval}")
print("Variables:")
res = np.fromiter((var.X for var in x_ij.values()), dtype=int)
print(res.reshape(n, n))
