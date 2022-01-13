import numpy as np
import pulp


na = 7  # number of alloys
ne = 3  # number of elements
steel = 5.0  # total steel quantity

p_min = np.array([2, 0.4, 1.20])
p_max = np.array([3, 0.6, 1.65])

p_ij = np.array(
    [
        [2.5, 0.0, 1.3],
        [3.0, 0.0, 0.8],
        [0.0, 0.3, 0.0],
        [0.0, 90.0, 0.0],
        [0.0, 96.0, 4.0],
        [0.0, 0.4, 1.2],
        [0.0, 0.6, 0.0],
    ]
)

q_i = [4.0, 3.0, 6.0, 5.0, 2.0, 3.0, 2.0]
c_i = [1.2, 1.5, 0.9, 1.3, 1.45, 1.2, 1.0]

# Definition of the problem
prob = pulp.LpProblem("steel_manufacturing", pulp.LpMinimize)

# Decision variables
# /!\ it is very important that all variables have a different name
x_i = np.array([pulp.LpVariable(f"x_{i}", 0, q) for i, q in enumerate(q_i)])

# Constraints

# a. equality constraints
prob += pulp.lpSum(x_i) == steel

# b. percentage constraints
expression = (p_ij.T * x_i).sum(axis=1)
for e, min_, max_ in zip(expression, p_min, p_max):
    prob += e >= min_ * steel
    prob += e <= max_ * steel

# The objective function (this is an affine expression)
prob += pulp.lpSum(x_i * c_i)

print(prob)

solution = prob.solve()

# /!\ Never remove this line
# The problem may return wrong solution if the status is:
# - Unbounded: the polyhedron is open
# - Infeasible: the polyhedron is empty and no solution exists

assert pulp.LpStatus[solution] == "Optimal"

# Now access the solution

print("Solution to the problem:")
print(dict((f"x_{i}", pulp.value(x)) for i, x in enumerate(x_i)))

print(f"Objective function: {pulp.value(prob.objective):.2f} euros")
