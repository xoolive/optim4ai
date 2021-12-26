import numpy as np
import pulp

c_ij = [
    [8, 6, 7, 8, 9],
    [11, 7, 5, 8, 10],
    [8, 10, 9, 11, 6],
    [10, 9, 7, 8, 7],
    [11, 6, 9, 7, 8],
]
n = len(c_ij)

# New problem
prob = pulp.LpProblem("Assignment", pulp.LpMaximize)

# Decision variables
x_ij = np.array(
    [
        [
            pulp.LpVariable(f"x_{i}_{j}".format(i, j), cat=pulp.LpBinary)
            for j in range(n)
        ]
        for i in range(n)
    ]
)

# Constraints
for i in range(n):
    prob += pulp.lpSum(x_ij[i, :]) == 1
for j in range(n):
    prob += pulp.lpSum(x_ij[:, j]) == 1

# Objective function
prob += pulp.lpSum(c_ij * x_ij)

# Problem solving
status = prob.solve()

assert pulp.LpStatus[prob.solve()] == "Optimal"

print()
print("Objective: ", pulp.value(prob.objective))

print("Variables:")
res = np.fromiter((pulp.value(x) for x in x_ij.ravel()), dtype=int)
print(res.reshape(n, n))
