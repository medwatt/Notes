# Random Numbers

The [`random`](https://docs.python.org/3/library/random.html) module provides
functions for generating random numbers and selecting random elements from a
sequence. The sequence of random numbers generated depends on the seed. If the
seeding value is same, the sequence will be the same.

## Methods

It has the following methods:

- `random.seed(a=None, version=2)`: Initialize the random number generator. The
  `a` argument is an optional seed value for the generator.

- `random.random()`: Return a random float in the range \[0.0, 1.0).

- `random.uniform(a, b)`: Return a random float in the range \[a, b\].

- `random.randint(a, b)`: Return a random integer in the range \[a, b\].

- `random.randrange(start, stop=None, step=1)`: Return a randomly selected
  element from the range object `range(start, stop, step)`.

- `random.choice(sequence)`: Return a randomly selected element from the given
  sequence (such as a list or tuple).

- `random.shuffle(sequence)`: Shuffle the elements of the given sequence in
  place and return None.

- `random.sample(population, k)`: Return a list of `k` unique elements chosen
  randomly from the given population.

## Example


```python
import random

# Set the seed to 0
random.seed(0)

# Generate a random float between 0 and 1
x = random.random()
print(x)  # Output: a random float between 0 and 1

# Generate a random float between 1 and 10
y = random.uniform(1, 10)
print(y)  # Output: a random float between 1 and 10

# Generate a random integer between 1 and 10
z = random.randint(1, 10)
print(z)  # Output: a random integer between 1 and 10

# Select a random element from a list
elements = ['a', 'b', 'c', 'd']
element = random.choice(elements)
print(element)  # Output: a random element from the list

# Select 3 random elements from a list without replacement
selected = random.sample(elements, 3)
print(selected)  # Output: a list of 3 random elements from the list
```


