A_add = [[0.0, -1.0]]
b_add = [-6.0]

res = linprog(-c, A_ub=A + A_add, b_ub=b + b_add, method="simplex")
print(res)
LPVisu(
    A + A_add,
    b + b_add,
    c,
    integers=True,
    obj=-res.fun,
    xk=res.x,
    x1_gui_bounds=(-1, 7.7),
)
