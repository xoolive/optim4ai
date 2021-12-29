# A quick introduction to complexity

[« Previous](../5_milp) \| [Home ↑](../) \| [Next »](../7_constraints)

<style>
blockquote {
    background: #e5e5e5;
    padding: 1em 1em .1em 2em;
    margin: 0 0 1em 0;
    font-style: normal;
    border-left: 3px solid;
}
</style>

This short interlude will bring notions of **complexity**, in order to explain why and how some problems are really more difficult to address than others. There is a fair share of theoritical content in this domain, and the point here is not to explain the proofs to all claims.

## Introduction problem

<div class="alert alert-warning"><b>Exercice:</b> Model the knapsack problem<br/>
You have a set of objects to put in a knapsack, a maximum capacity $C$, and a weight $w_i$ for many objects you want to put in the knapsack. Each object has an important for your trip that you can evaluate. You must decide which objects to put in the knapsack in order to maximize the sum of values $v_i$ of the chosen objects while respecting the capacity of the knapsack. You can put an object only one time in the knapsack.
</div>

<details><summary><b>Solution:</b> (click to unfold)</summary>
<ul>
<li>Attribute a binary decision variable $t_i$ for each object you consider for the knapsack (1: take it; 0: leave it)</li>
<li>Capacity constraint: $\sum t_i\cdot w_i \leq C$</li>
<li>Maximise $\sum t_i\cdot v_i$</li>
</ul>
</details>

Here, there is no analytical solution to the problem, which means the naive approach would enumerate all possibilities. But **we really hope we can do better** because the search space is _huge_. Besides, finding a solution, even suboptimal, can be complex.

We usually consider as correct all computer programs or algorithms (like the simplex, or a Branch & Bound) which address a mathematical problem and return a correct solution. Implicitely, we expect that such a program does return a solution for any _instance_, and that it handles situations when there is no solution as well.

However, when using a computer, we are usually limited by two parameters:

- _space_ refers to all what can be stored at a single time. If a programs consumes out all the memory available on a computer, it will not be able to terminate properly;
- _time_ refers to when we can expect to get the solution to that problem.

> Before we go further, let's recall the city placement problem in a discrete version. We could say that since we are going to print out our map, we can consider a 1000 × 1000 pixel grid and determine which pixel would match each city best: that would be 1'000'000 possibilities per city, let's write it $10^6$.
>
> If we have 2 or 3 cities, we can consider evaluating all possibilities to find the optimum. But for a problem with 36 cities, that is a total of about $10^{6×36}=10^{216}$ combinations to evaluate before finding the minimum. Even with a computer evaluating each combination in one nanosecond (which is actually not reasonable today), we would still need around $10^{207}$ seconds to find the optimum.
>
> The universe is only 14 billion years old and we expect a solution within a lifetime... or actually, more within few seconds for tasks looking simple.

<div class="alert alert-danger"><b>Let's cool down now</b><br/>
In spite of those scary figures, most problems we looked at in the previous sections looked rather simple to solve with dedicated algorithms and frameworks.
</div>

## Time and space complexity

So we need a theory to try to predict:

- if algorithms are going to be efficient,
- if we were just lucky with some instances of a particular problem.

In practice, when talking about (space or) time complexity, we use an asymptotic notation with a big $O$ notation: $O(n)$ for linear problems, $O(n^2)$ for quadratic problem, $O(2^n)$ for exponential problems, etc.

We will also talk about:

- the complexity of an algorithm for what happens during the worst-case scenario: a _bubble sort_ would be linear in a sorted list, but a _quick sort_ is guaranteed to terminate in $O(n\cdot\log(n))$ for any situation;
- the complexity of a problem, for the complexity of the best known algorithm: the best know sorting algorithm is in $O(n\cdot\log(n))$ so is the _sorting problem_.

In practice, when implementing a sorting algorithm, we still try to go for optimisations which would bring a better complexity in most cases. For example, the sorting algorithm in Python is called _Tim sort_, named after Tim Peters, for extra nice properties it ensures. But the most important is to ensure that even the worst case scenario is not out of control.

## Polynomial algorithms

If the big $O$ notation of a problem remains polynomial, we keep the problem within the polynomial category, even with crazy degrees and constants of polynoms. We consider these problems as easy, tractable and we usually find a way to make them run in reasonable time.

Many problems are known to be polynomial:

- the sorting problem;
- finding the shortest path in a graph;
- computing the inverse of a matrix;
- the primality test of an integer;
- the assignment problem.

[Linear programming](../4_linear) is a polynomial problem, but keep in mind the **simplex algorithm is not**: there are a particular category of LP problems where it becomes exponential; however, it remains polynomial in most situations. Other methods (like the interior-points) are however polynomial.

For some problem, the best known algorithm is exponential:

- the knapsack problem;
- the graph colouring problem;
- [Mixed integer linear programming](../5_milp) (MILP);
- [Constraint programming](../7_constraints) (CP)

but we do not know whether these problems really are exponential.

## NP-completeness

**NP problems** are a particular class of problems:

- we do not know whether we can find a solution in polynomial time;
- we can however **verify whether a candidate solution is correct in polynomial time**

So basically, all polynomial problems are NP problems.

There is a special subset of NP problems called **NP-complete problems**. These problems are "at least as difficult as any problem in NP".

We can put in this category many well known problems, such as MILP and CP, just by transforming any instance of these problems in another NP-complete problem (we name this transformation a _reduction_)

<div class="alert alert-danger"><b>Key take-aways</b><br/>
You should remember that 
<ul>
<li>LP is a polynomial problem: it is (relatively) easy to solve;</li>
<li>MILP and CP are NP-complete problems: some problems are <b>really</b> hard to solve;</li>
</ul>

In general, there are always instances of NP-complete problems which can be easy to solve. You often need to find smart tricks to optimise a problem: sometimes MILP is more suitable (imagine you are lucky with the linear relaxation!), sometimes CP is more suitable, but that is addressed in next section.

</div>

[« Previous](../5_milp) \| [Home ↑](../) \| [Next »](../7_constraints)
