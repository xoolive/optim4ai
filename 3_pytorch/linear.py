import matplotlib.pyplot as plt
import torch
from torch import optim
from tqdm import tqdm
from matplotlib import animation


x = 2 * torch.rand(100, 1, device=0)
y = 3 * x + 4 + torch.randn(100, 1, device=0)


a = torch.rand(1, requires_grad=True, device=0)
b = torch.rand(1, requires_grad=True, device=0)

optimizer = optim.Adam([a, b], lr=5e-1)
n_epochs = 200

loss_values = list()
history = list()

for i in tqdm(range(n_epochs)):

    yhat = a * x + b
    loss = ((y - yhat) ** 2).mean()
    loss.backward()
    loss_values.append(loss.cpu().detach().numpy().item())
    history.append(torch.concat([a, b]).detach())

    optimizer.step()
    optimizer.zero_grad()

fig, ax = plt.subplots(figsize=(10, 7))
ax.scatter(x.cpu(), y.cpu())
a_b = torch.concat(history).reshape(-1, 2).cpu()

ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_position(("data", 0))
ax.xaxis.set_major_locator(plt.NullLocator())
ax.yaxis.set_major_locator(plt.NullLocator())

ax.set_ylim((0, 12))

a_, b_ = a_b[0]
(line,) = ax.plot([0, 2], [b_, 2 * a_ + b_], "r-")


def animate(i):
    a_, b_ = a_b[i]
    line.set_data([0, 2], [b_, 2 * a_ + b_])
    return [line]


animation = animation.FuncAnimation(
    fig, animate, frames=n_epochs, interval=50, blit=True
)
plt.show()
