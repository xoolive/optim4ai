Nsteps = 20
alpha = 0.1
X = np.zeros((Nsteps, 2))
X[0, :] = np.array([-5, -4])
for i in range(1, Nsteps):
    grad = func_der(X[i - 1, :])
    d = -grad / np.linalg.norm(grad)
    X[i, :] = X[i - 1, :] + alpha * d

X0 = np.arange(-6, 6, 0.1)
X1 = np.arange(-6, 6, 0.1)
levels = np.array([0.15, 0.2, 0.25, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0])
fig, ax = plot_contours_func(
    func, X0, X1, levels=levels, xp=X.T, plot_line=True, add_levels=False
)
clean_axis(ax)

print("fopt:", func(X[Nsteps - 1, :]))
print("xopt:", X[Nsteps - 1, :])
