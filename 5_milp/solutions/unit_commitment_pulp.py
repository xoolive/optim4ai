# %%

import matplotlib.pyplot as plt
import numpy as np
import pulp


costs = np.array([20, 40])
p_max = np.array([400, 200])
p_min = np.array([50, 20])

demand = np.loadtxt("demand.txt")


n = len(p_max)
duration = len(demand)

prod = np.empty((duration, n), dtype=object)
on_off = np.empty((duration, n), dtype=object)

for t in range(duration):
    for c in range(n):
        prod[t, c] = pulp.LpVariable(f"prod_{t}_{c}", 0, p_max[c])
        on_off[t, c] = pulp.LpVariable(f"on_off_{t}_{c}", cat="binary")


# --- Problem definition
pb = pulp.LpProblem("unit_commitment", pulp.LpMinimize)

# --- Objective function
pb += pulp.lpSum(list(np.ravel(prod * costs)))

# --- Constraints
for t in range(duration):
    pb += pulp.lpSum(list(prod[t, :])) == demand[t]

    # stay within p_min and p_max
    for c in range(n):
        pb += prod[t, c] >= on_off[t, c] * p_min[c]
        pb += prod[t, c] <= on_off[t, c] * p_max[c]

# [off = 0, on = 1, off = 0] is the only possible configuration
for c in range(n):
    for t in range(1, duration - 1):
        pb += on_off[t, c] <= on_off[t - 1, c] + on_off[t + 1, c]

# --- Resolution
assert pulp.LpStatus[pb.solve()] == "Optimal"

for t in range(duration):
    for c in range(n):
        prod[t, c] = prod[t, c].value()
        on_off[t, c] = on_off[t, c].value()

total_costs = np.sum(prod * np.array(costs))

print("Total costs: %d €" % total_costs)

# %%
fig, ax = plt.subplots(figsize=(10, 7))

ax.plot(demand, linestyle="--", color="#bab0ac", label="Demand")
ax.plot(prod[:, 0], label="Plant #1")
ax.plot(prod[:, 1], label="Plant #2")
ax.legend(fontsize=14, loc=1)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_position(("data", 0))

ax.xaxis.set_major_locator(plt.MultipleLocator(24))
ax.xaxis.set_minor_locator(plt.MultipleLocator(6))
ax.xaxis.set_minor_formatter(plt.ScalarFormatter())
ax.tick_params(labelsize=14, pad=10)
ax.tick_params(axis="x", which="minor", labelsize=8)
ax.grid(axis="x", which="both", color="#bab0ac", linestyle="dashed", alpha=0.6)

plt.show()

# %%
