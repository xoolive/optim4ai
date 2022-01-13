import gurobipy as grb

m = grb.Model("pasta")

x_i = m.addVars(3, lb=0, name="x_i")
x_e = m.addVars(3, lb=0, name="x_e")

req_flour = [0.5, 0.4, 0.3]
m.addConstr(grb.quicksum(req_flour[i] * x_i[i] for i in range(3)) <= 20)

req_eggs = [0.2, 0.4, 0.6]
m.addConstr(grb.quicksum(req_eggs[i] * x_i[i] for i in range(3)) <= 40)

demand = [100, 200, 300]
m.addConstrs(x_i[i] + x_e[i] == demand[i] for i in range(3))

costs_i = [0.6, 0.8, 0.3]
costs_e = [0.8, 0.9, 0.4]
m.setObjective(
    grb.quicksum(x_i[i] * costs_i[i] + x_e[i] * costs_e[i] for i in range(3))
)


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
print(dict((var.VarName, var.X) for var in x_e.values()))
print(f"Objective function: {m.objval:.2f}€")
