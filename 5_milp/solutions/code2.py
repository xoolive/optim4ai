A_add = [[1.0, 2.0]]
b_add = [np.floor(49 / 3)]

res = linprog(-c, A_ub=A + A_add, b_ub=b + b_add, method="simplex")
print(res)

LPVisu(A, b, c, A_cuts=A_add, b_cuts=b_add, integers=True, obj=-res.fun)
