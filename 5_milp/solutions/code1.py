A2 = [[0.0, 1.0], [1.0, 2.0], [1.0, 1.0], [1.0, -1.0]]
b2 = [6.0, 15.0, 10.0, 2.0]

res = linprog(-c, A_ub=A2, b_ub=b2, method="simplex")
LPVisu(A2, b2, c, integers=True, obj=-res.fun, xk=res.x)
