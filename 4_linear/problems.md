# Modelling LP problems

[« Previous](.) \| [Up ↑](.) \| [Next »](.)

## The production problem

A pasta factory wants to minimise the production costs for a number of products while satisfying customer demand. Each product can be produced either inside the company or outside, at a higher cost.

The inside production is constrained by the company's resources, while outside
production is considered unlimited.

The demand goes as follows:

- 100 units of kluski pasta: 0.6€/unit (internal) and 0.8€/unit (external);
- 200 units of capellini pasta: 0.8€/u. (internal) and 0.9€/u. (external);
- 300 units of fettucine pasta: 0.3€/u. (internal) and 0.4€/u. (external).

The factory is constrained by its resources. They only have 20 units of flour and 40 boxes of eggs. In order to produce internally:

- one unit of kluski pasta requires 0.5 u. of flour and 0.2 box of eggs;
- one unit of capellini pasta requires 0.4 u. of flour and 0.4 b. of eggs;
- one unit of fettucine pasta requires 0.3 u. of flour and 0.6 b. of eggs.

## Manufacturing of a stainless steel

Source: Prins & Sevaux 2011

The MAE company received an order of 5 tons of special steel for the manufacture of boat hulls. This steel must have particular characteristics given in Table 1 below:

### Tab. 1: Composition of the steel

| Chemical element | Minimum percentage | Maximum percentage |
| ---------------- | :----------------: | :----------------: |
| Carbon (C)       |         2          |         3          |
| Copper (Cu)      |        0,4         |        0,6         |
| Manganese (Mn)   |        1,2         |        1,65        |

To make this steel, MAE has seven raw materials. The characteristics, availability and purchasing costs are given in Table 2 below.

### Tab. 2: Composition, inventory level and cost of raw materials

| Raw material       | C % | Cu % | Mn % | Inventory ton | cost k€/ton |
| ------------------ | :-: | :--: | :--: | :-----------: | :---------: |
| Ferro alloy #1     | 2,5 |  0   | 1,3  |       4       |    1,20     |
| Ferro alloy #2     |  3  |  0   | 0,8  |       3       |    1,50     |
| Ferro alloy #3     |  0  | 0,3  |  0   |       6       |    0,90     |
| Copper alloy #1    |  0  |  90  |  0   |       5       |    1,30     |
| Copper alloy #2    |  0  |  96  |  4   |       2       |    1,45     |
| Aluminium alloy #1 |  0  | 0,4  | 1,2  |       3       |    1,20     |
| Aluminium alloy #2 |  0  | 0,6  |  0   |       2       |    1,00     |

We want to determine the composition of the steel in order to minimize production costs.

<div class="alert alert-warning"><b>Exercice:</b><br>
Write the set of variables for each of the two introductory problems. Write the constraints and objective function.
</div>

<details>
    <summary><b>1. The production problem</b> (click to unfold)
    </summary>
    <div>

<p>We need <b>decision variables</b> associated with the internal and external production of each category of pasta. Let's name them $i_1, i_2, i_3, e_1, e_2, e_3$.</p>

<p>The production is <b>constrained</b> by the total amount of resources:</p>

<ul>
    <li>in terms of flour: $$0.5\,i_1 + 0.4\,i_2 + 0.3\,i_3 \leq 20$$</li>
    <li>in terms of eggs: $$0.2\,i_1 + 0.4\,i_2 + 0.6\,i_3 \leq 40$$</li>
</ul>

<p>The demand must be met with internal or external production:</p>

$$
\left\{\begin{array}{l}
i_1 + e_1 = 100\\
i_2 + e_2 = 200\\
i_3 + e_3 = 300
\end{array}
\right.
$$

<p>The <b>objective</b> is to minimise the total cost:</p>

$$ \min 0.6\,i_1 + 0.8\,e_1 + 0.8\,i_2 + 0.9\,e_2 + 0.3\,i_3 + 0.4\,e_3 $$

</div>
</details>
<details>
    <summary><b>2. Manufacturing of the stainless steel</b> (click to unfold)
    </summary>
    <div>

Let's name:

<ul>
    <li>$c_i, i \in 1..7$ the cost of a raw material in k€/ton;</li>
    <li>$q_i$, the inventory of material;</li>
    <li>$p_{\min}^j, j \in 1..3$ the minimum percentage for each element;</li>
    <li>$p_{\max}^j, j \in 1..3$ the maximum percentage for each element;</li>
    <li>$p_{i,j}$ the percentage of element $j$ in material $i$ (in %);</li>
    <li>$S$ the total steel quantity</li>
</ul>

We need <b>decision variables</b> to determine the quantity of each material used for the steel: $$x_i, i \in 1..7$$

The problem is subject to the following <b>constraints</b>:

<ul>
<li>satisfaction constraints:</li>
  $$\sum x_i = S$$

<li>elements percentage:</li>
  $$\forall j \in 1..3 \quad S\,p_{\min}^j \leq \sum p_{i,j}\,x_i \leq S\,p_{\max}^j$$

<li>available quantity:</li>
  $$\forall i \in 1..7 \quad x_i \leq q_i$$

<li>positivity</li>
$$\forall i \in 1..7 \quad x_i \geq 0$$
</ul>

The <b>objective</b> if to minimise the cost of raw materials used: $$\min z = \sum c_i\cdot x_i$$

</div>
</details>

<div class="alert alert-danger"><b>Scope of the course:</b><br>
This section will focus on problems using continuous variables and for which the constraints and objective function are all linear with respect to the decision variables.<br/>
This requires sometimes some extra thinking, as everything must be written exclusively as a linear combination of decision variables.
</div>

There is an important distinction to make here: when we implement such optimisation problem in a programming language (e.g. Python), it is very common to confuse **input variables** (all that is constant at the time of the definition of the problem) and **decision variables** (all that is subject to optimisation during the resolution process).

In linear programming, it is perfectly acceptable to multiply input variables, to calculate sine values or to perform more complicated calculations through `if` branches and `for` loops, as long as the result is **constant during the whole resolution process**.

[« Previous](.) \| [Up ↑](.) \| [Next »](.)
