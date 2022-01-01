# CMA-ES

[« Previous](./genetic) \| [Up ↑](.) \| [Next »](../9_further)

Covariance Matrix Adaptation Evolutionary Strategy, or **CMA-ES**, is one of the most well-known evolutionary algorithms in general and is a state-of-the-art algorithm for continuous optimization. The strength of this method is that it adapts the distribution it uses to generate the next population based on the current distribution of individuals. The adaptive distribution of CMA-ES means it will cross search spaces faster and narrow in more exactly on optimal points.

In practice, we use dedicated libraries, like [cma](https://github.com/CMA-ES/pycma):

```python
pip install cma
```

<div class="alert alert-warning"><b>Exercice</b><br/>
Implement simulated annealing on the function of your choice.<br/>
Of course, you are encouraged to pick one in the bestiary, or even the city placement problem.
</div>

## Theory

(from Dennis Wilson's [course](https://github.com/d9w/evolution))

We start by creating a random individual $\mathbf{y}$ which will be our first expert. We also create a diagonal covariance matrix $\mathbf{C}$.

$$
\forall l=1, \ldots, \lambda : \;\;
  \begin{cases}
   & \mathbf{w}_l
          \leftarrow \sigma \sqrt{ \mathbf{C} } \,
          \mathbf{N}_l(\mathbf{0}, \mathbf{1}),\\[2mm]
   & \mathbf{y}_l \leftarrow \mathbf{y}  + \mathbf{w}_l, \\[2mm]
   & F_l \leftarrow F(\mathbf{y}_l),
  \end{cases}
$$

In the first step, $\lambda$ offspring $\mathbf{y}_l$ are created by transforming standard normally distributed random vectors using a transformation matrix $\sqrt{\mathbf{C}}$ which is given by Cholesky decomposition of the covariance matrix $\mathbf{C}$ and the global step size factor $\sigma$. We also evaluate every individual, creating $F$.

$$\mathbf{y} \leftarrow \mathbf{y} + \langle \mathbf{w} \rangle$$

Here the best $\mu$ mutations are recombined forming the recombinant $\mathbf{y}$ (center of mass individual) for the next generation.

$$
\mathbf{s} \leftarrow \left(1-\frac{1}{\tau}\right)\mathbf{s}
+ \sqrt{\frac{\mu}{\tau} \left(2-\frac{1}{\tau}\right)} \,
  \frac{\langle \mathbf{w} \rangle}{\sigma}
$$

Vector $\langle \mathbf{w} \rangle$ combines individuals from two consecutive generations so $\langle \mathbf{w} \rangle/\sigma$ represents the tendency of evolution in the search space. Here, this information is cumulated in the $\mathbf{s}$ vector, which exponentially decays with the time constant $\tau$. A good default for this is $\tau=\sqrt{n}$.

$$
\mathbf{C} \leftarrow
  \left(1-\frac{1}{\tau_{\mathrm{c}}}\right)\mathbf{C}
  + \frac{1}{\tau_{\mathrm{c}}} \mathbf{s} \mathbf{s}^T
$$

Here, the direction vector $\mathbf{s}$ is used to update the covariance matrix $\mathbf{C}$ with time constant $\tau_{\mathrm{c}} \propto n^2$

$$
\mathbf{s}_\sigma
\leftarrow \left(1-\frac{1}{\tau_\sigma}\right) \mathbf{s}_\sigma
+ \sqrt{\frac{\mu}{\tau_\sigma}
\left(2-\frac{1}{\tau_\sigma}\right)} \,
\langle \mathbf{N}(\mathbf{0}, \mathbf{1}) \rangle
$$

$$
\sigma \leftarrow \sigma\exp\left[
\frac{\| \mathbf{s}_{\sigma} \|^2 - n} {2 n \sqrt{n} } \right]
$$

The distribution standard deviation $\sigma$ is then calculated using the cumulated step size adaptation (CSA) technique with time constant $\tau_\sigma = \sqrt{n}$ (initially $\mathbf{s}_\sigma = \mathbf{0}$). $\langle \mathbf{N}(\mathbf{0}, \mathbf{1}) \rangle$ is the distribution we calculated in (L1).

So instead of simply using a Normal distribution to create the next generation, CMA-ES transforms a normal distribution by the covariance matrix $\mathbf{C}$. It also moves at self-adjusting $\sigma$. This makes its movement around the search space much more effective, as it is informed by the shape of the search space given through the fitness values $F$.

[« Previous](./genetic) \| [Up ↑](.) \| [Next »](../9_further)
