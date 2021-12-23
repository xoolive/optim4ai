import scipy.optimize as sopt

maxSteps = 19
epsilon = 0.001
X = np.zeros((maxSteps, 2))
X[0, :] = np.array([-5, -4])
grad_norm_tab = np.zeros(maxSteps)
grad_norm = np.linalg.norm(func_der(X[0, :]))
val_tab = np.zeros(maxSteps)
val_tab[0] = func(X[0, :])
i = 1

while i < maxSteps and grad_norm > epsilon:
    grad = func_der(X[i - 1, :])
    grad_norm = np.linalg.norm(grad)
    grad_norm_tab[i - 1] = grad_norm
    # print("Iteration", i, "grad_norm =", grad_norm)
    d = -grad / grad_norm

    def g(alpha):
        return func(X[i - 1, :] + alpha * d)

    res = sopt.minimize_scalar(g)
    alpha = res.x
    X[i, :] = X[i - 1, :] + alpha * d
    val_tab[i] = func(X[i, :])
    i += 1

X = X[:i, :]
grad_norm_tab = grad_norm_tab[:i]
val_tab = val_tab[:i]

X0 = np.arange(-6, 6, 0.1)
X1 = np.arange(-6, 6, 0.1)
levels = np.array([0.15, 0.2, 0.25, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0])

fig, ax = plot_contours_func(
    func,
    X0,
    X1,
    levels=levels,
    xp=X.T,
    plot_line=True,
    add_levels=False,
    f_der=func_der,
)
clean_axis(ax)

print("Nb iterations", i, "grad_norm =", grad_norm)
print("fopt:", func(X[i - 1, :]))
print("xopt:", X[i - 1, :])

fix, ax = plt.subplots()
ax.plot(np.log(grad_norm_tab[: i - 1]))
clean_axis(ax)


X0 = np.arange(-3.05, -2.9, 0.01)
X1 = np.arange(-1.8, -1.6, 0.01)
fig, ax = plot_contours_func(
    func, X0, X1, xp=X[4:, :].T, plot_line=True, add_levels=False
)
clean_axis(ax, center=(X0.min(), X1.min()))
