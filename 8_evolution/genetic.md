# Genetic algorithms

[« Previous](./annealing) \| [Up ↑](.) \| [Next »](./cmaes)

**Genetic algorithms** are a **population method**: we manipulate a population of $n$ elements at each iteration and make it evolve. The idea here is to mimic how chromosoms replicate:

- first, initialise a population of size $n$;
- then at each iteration, select pairs of individuals,
- combine them using crossover,
- mutate the resulting individual then add it to the new population,
- repeat until the new population is full.

```raw
initialize population
foreach iteration:
    evaluate population
    append the k best elements into your new population
    for a1, a2 in selection(population):
        b1, b2 = cross(a1, a2)
        "sometimes" mutate b1 and/or b2
        append b1, b2 to your new population
```

There are many possible strategies for selection, crossover, and mutation.

## Initialisation

This is usually an easy step: generate individuals according to a random uniform or normal law.

## Evaluation

That is also an easy step: evaluate all your individuals and store the results.

## Selection

Which individuals should pass on their genetic information to the next generation? We could imagine a simple schemes of taking the best individuals globally, say 20% of them, and mutating each of these experts for the next generation. In a simple problem like this one, such a method might work. However, we would lose important genetic diversity, one of the main advantages of our large population.

We can use here for example:

- the _tournament_ strategy: pick two elements at random, only sample the one with the better evaluation;
- the _Russian roulette_ strategy: pick elements with a weighted probability according to their evaluation.

## Crossover

Considering we have such a large population, is there some way to combine individual solutions to lead to better solutions? For example, could we make an individual which inherits information from two parent individuals? This is the idea behind crossover, the other operator in genetic algorithms besides mutation. It is based on sexual reproduction where the genetic information of two parent individuals is mixed to create an offspring individual. The idea of combining the information from multiple individuals together to create the next generation is something we'll explore in more detail next class when discussing evolutionary strategies

We can use for example, for two parents $(a_0, ...)$ and $(b_0, ...)$:

- _one-point crossover_: pick an index $i$, then make $(a_0, ... a_i, b_{i+1}, ...)$;
- _uniform crossover_: determine for each index $i$ if you pick $a_i$ or $b_i$;

## Mutation

Mutation is usually a simple operation which is applied with a given probability, the _mutation rate_, where a small noise is added to the child individual. It is designed to improve diversity in our population.

<div class="alert alert-warning"><b>Exercice</b><br/>
Implement genetic algorithms on the Rastrigin's function in dimension 10.<br/>
You may also try a different problem.

</div>

Another problem which is easy to debug is to try to decode a hidden message. Imagine you have a function giving you the number of letters placed in the correct position with respect to a hidden message: try to decode the message with genetic algorithms: start with a population of individuals being strings of size `n`, with letters picked in:

```python
import string

letters = (
    string.ascii_uppercase + # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    string.ascii_lowercase + # abcdefghijklmnopqrstuvwxyz
    string.punctuation + # !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
    ' '
)
```

Use the following function to evaluate your population:

```python
def evaluate(candidate, solution="Grab your towel and don't panic!"):
    return sum(c == s for c, s in zip(candidate, solution))
```

[« Previous](./annealing) \| [Up ↑](.) \| [Next »](./cmaes)
