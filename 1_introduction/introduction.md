# Introduction to optimisation topics

[« Previous](./environment) \| [Up ↑](.) \| [Next »](../2_gradient)

An **optimisation problem** is usually defined as a function to minimise:

$$\min_x f(x)$$

- $x$ is a set of unknown _variables_, or **decision variables**;
- variables are defined on a given domain, e.g. $\mathbb{R}$, $\mathbb{N}$, or $\\{0,...4\\}$;
- $f$ is an **objective function**, or sometimes _evaluation function_.

**Modelling a problem** consists in identifying decision variables and an objective function.

<div class="alert alert-warning"><b>Example:</b>
Find the optimal angle to fire a cannon to maximize the distance it travels down range.
</div>

<details><summary><b>Solution</b> (click to unfold)</summary>

<ul>
<li>Define the referential, sum the forces applying to a cannon ball of mass $m$, integrate, etc.</li>
  $$y = -\frac{g}{2 v_0^2\, \cos^2 \alpha} x^2 + \tan \alpha\, x$$

<li>The range of the cannonball writes:</li>
  $$ d = \frac{v_0^2\, \sin (2\alpha)}{g} $$

<li>The sine function is continuous and differentiable:</li>
  $$\alpha_{max} = 45^{\circ}$$

</ul>

</details>

**Constraint optimisation** adds up to this definition with a slight addition:

$$\min_x f(x) \textsf{ with } c(x)$$

- $c$ is a **constraint**, i.e. a function from the domain of $x$ with values taken among $\left\\{\top, \bot\right\\}$.

In case of non-constrained optimisation, we have $$\forall x: c(x)$$

There is no general method to find the optimum to such problem, however there are general methods to solve problems fitting a given _paradigm_ (see the cannon ball problem, that was easy, right?)

<div class="alert alert-danger"><b>Scope of the course</b><br/>
During this course, we will go through various paradigms, fitting different characteristics of the problems we analyse.
Depending on how we choose to model problems (discrete domains, differentiable functions, linear functions, black box models, etc.), we will be able to choose which method is the best fit.
</div>

The main characteristic of each of these optimisation paradigms is:

- **genericity**: methods should be applicable to wide range of problems;
- **efficiency**: methods should converge to the solution with reasonable resources (basically, a personal laptop);
- **robustness**: methods should be stable even with noise in data, or with floating point arithmetics.

During the course of this class, we will in particular look through:

- differentiable functions;
- global and local optimisation;
- linear functions;
- discrete optimisation: values in domains such as $\mathbb{Z}$ or $\\{0, 1\\}$;
- satisfaction problem when $f$ is constant but $c$ is not;
- stochastic methods when two executions of the same problem may not return the same solution.

[« Previous](./environment) \| [Up ↑](.) \| [Next »](../2_gradient)
