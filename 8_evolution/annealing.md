# Simulated annealing

[« Previous](./bestiary) \| [Up ↑](.) \| [Next »](./genetic)

**Simulated annealing** is a **trajectory method**: we manipulate one element of population at a time and construct a series of $x_i$ in order to make it converge toward an optimum.

Simulated annealing is inspired by metallurgy:

- we first pick an initial solution $x_0$ with an **energy** $E_0$ and a high **initial temperature** $T_0$;
- after each iteration, we pick a $x_{i+1}$ "near" $x_i$, and evaluate the **variation of energy** $\Delta E$:

  - if $\Delta E < 0$, modification is applied;
  - otherwise, we accept it _with a probability of_ $\displaystyle e^{-\frac{\Delta E}{T}}$;

- temperature follows a decreasing function.

<div class="alert alert-warning"><b>Exercice</b><br/>
Implement simulated annealing on the function of your choice.<br/>
Of course, you are encouraged to pick one in the bestiary.
</div>

This exercice may look very easy, but you will realise there is a lot left to your consideration:

- choice of parameters,
- definition of a neighbourhood,
- definition of a decreasing function for the temperature,
- etc.

And of course, what will work for a type of problem may not be that efficient for other types of problems.

[« Previous](./bestiary) \| [Up ↑](.) \| [Next »](./genetic)
