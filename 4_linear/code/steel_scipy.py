import numpy as np
from scipy.optimize import linprog

na = 7  # number of alloys
ne = 3  # number of elements
steel = 5.0  # total steel quantity

p_min = np.array([2, 0.4, 1.20])
p_max = np.array([3, 0.6, 1.65])

# equality constraints
A_eq = [np.ones(na)]

# Inequality constraints (percentage)
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
p_ji = np.transpose(p_ij)


# Inequality constraints (availability)
availability_ineq = np.eye(na)

q_i = [4.0, 3.0, 6.0, 5.0, 2.0, 3.0, 2.0]

# Global inequality constraints
A_ub = np.r_[
    availability_ineq,
    -1 * p_ji / steel,
    p_ji / steel,
]
b_ub = np.r_[q_i, -1 * p_min, p_max]

# Objective function
c_i = [1.2, 1.5, 0.9, 1.3, 1.45, 1.2, 1.0]

# Resolution
res = linprog(
    c_i,
    A_eq=A_eq,
    b_eq=steel,
    A_ub=A_ub,
    b_ub=b_ub,
)
print(res)

print()
print("Solution to the problem:")
print(dict((f"x_{i}", x) for i, x in enumerate(res.x)))
print("Solution to the problem (rounded):")
print(dict((f"x_{i}", x.round(5)) for i, x in enumerate(res.x)))

print(f"Objective function: {res.fun:.2f} tons")
