col = [2, 4, 5]

B1 = np.concatenate(
    (
        A[0:, col[0] - 1 : col[0]],
        A[0:, col[1] - 1 : col[1]],
        A[0:, col[2] - 1 : col[2]],
    ),
    axis=1,
)
print("B1=", B1)

cB1 = np.concatenate(
    (
        c[col[0] - 1 : col[0]],
        c[col[1] - 1 : col[1]],
        c[col[2] - 1 : col[2]],
    ),
    axis=0,
)
print("cB1=", cB1)

xB1 = np.dot(inv(B1), b)
print("xB1=", xB1)

zB1 = np.dot(cB1, xB1)
print("zB1=", zB1)
