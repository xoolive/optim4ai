import numpy as np
from docplex.mp.model import Model

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
m = Model("steel_manufacturing")

x_i = m.continuous_var_list(na, lb=0, ub=q_i, name="x")

# Constraints
m.add_constraint(m.sum(x_i) == steel)
m.add_constraints(
    m.sum(x_i[i] * p_ij[i, j] for i in range(na)) <= p_max[j] * steel
    for j in range(ne)
)
m.add_constraints(
    m.sum(x_i[i] * p_ij[i, j] for i in range(na)) >= p_min[j] * steel
    for j in range(ne)
)

# The objective function
m.minimize(m.sum(x * c for x, c in zip(x_i, c_i)))

m.print_information()

print()

if m.solve():  # check the problem is really solved
    m.print_solution()

    print()
    print("Solution to the problem:")
    print(dict((var.name, var.solution_value) for var in x_i))
    print(f"Objective function: {m.objective_value:.2f} euros")

else:
    print(m.get_solve_status())
