import numpy as np
import gurobipy as grb


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

m = grb.Model("steel_manufacturing")

# Decision variables
x_i = m.addVars(na, lb=0, ub=q_i, name="x")

# Constraints

# a. equality constraint (single constraint)
m.addConstr(x_i.sum() == steel)

# b. percentage constraints
m.addConstrs(
    grb.quicksum(x_i[i] * p_ij[i, j] for i in range(na)) <= p_max[j] * steel
    for j in range(ne)
)
m.addConstrs(
    grb.quicksum(x_i[i] * p_ij[i, j] for i in range(na)) >= p_min[j] * steel
    for j in range(ne)
)

# The objective function
m.setObjective(grb.quicksum(x_i[i] * c_i[i] for i in range(na)))

m.update()
m.optimize()

# /!\ Never remove this line
# The problem may return wrong solution if the status is:
# - GRB.INF_OR_UNBD: the polyhedron is open
# - GRB.INFEASIBLE: the polyhedron is empty and no solution exists

assert m.status == grb.GRB.OPTIMAL

# Now access the solution

print()
print("Solution to the problem:")
print(dict((var.VarName, var.X) for var in x_i.values()))
print(f"Objective function: {m.objval:.2f} tons")
