# itertools

The `itertools` module provides functions for working with iterators. These
functions are designed to be efficient and flexible, and are often used in
combination with each other to create sophisticated iterators.

## Methods

Some of the most commonly used functions in the `itertools` module are:

- `count(start=0, step=1)`: This function returns an iterator that generates a
  sequence of integers, starting from `start` and incrementing by `step` at
  each iteration.

  ```python
  for i in itertools.count(10, 3):
      print(i)
      if i > 20:
          break
  # Output: 10 13 16 19 22
  ```

- `cycle(iterable)`: This function returns an iterator that repeats the
  elements of `iterable` indefinitely.

  ```python
  for i in itertools.cycle([1, 2, 3]):
      print(i)
  # Output: 1 2 3 1 2 3 1 2 3 ...
  ```

- `repeat(elem, times=None)`: This function returns an iterator that repeats
  the element `elem` a number of times specified by `times`. If `times` is not
  specified, the iterator will repeat `elem` indefinitely.

  ```python
  for i in itertools.repeat(10, 3):
      print(i)
  # Output: 10 10 10
  ```

- `chain(*iterables)`: This function returns an iterator that concatenates the
  elements of the input iterables.

  ```python
  for i in chain([1, 2, 3], [4, 5, 6]):
      print(i)
  # Output: 1 2 3 4 5 6
  ```

- `compress(data, selectors)`: This function returns an iterator that filters
  the elements of `data` using the corresponding elements of `selectors`, which
  should be a sequence of booleans.

  ```python
  for i in itertools.repeat(10, 3):
      print(i)
  # Output: 10 10 10
  ```

- `zip(*iterables)`: This function returns an iterator that aggregates the
  elements of the input iterables.

  ```python
  for i in itertools.zip([1, 2, 3], [4, 5, 6]):
      print(i)
  # Output: (1, 4) (2, 5) (3, 6)
  ```

- `accumulate(iterable, func=operator.add)`: This function returns an iterator
  that returns the accumulated sums, products, minimums, or maximums of the
  elements in `iterable`. The function `func` specifies the operation to be
  used for the accumulation.

  ```python
  for i in itertools.accumulate([1, 2, 3, 4]):
      print(i)
  # Output: 1 3 6 10
  ```

- `product(*iterables, repeat=1)`: This function returns an iterator that
  produces the cartesian product of the input iterables. The optional argument
  `repeat` allows you to specify the number of times each element of the input
  iterables should be repeated in the cartesian product.

  ```python
  for i in itertools.product([1, 2], [3, 4]):
      print(i)
  # Output: (1, 3) (1, 4) (2, 3) (2, 4)
  ```

- `permutations(iterable, r=None)`: This function returns an iterator that
  produces all permutations of the elements in `iterable`. The optional
  argument `r` allows you to specify the length of the permutations.

  ```python
  for i in permutations([1, 2, 3]):
      print(i)
  # Output: (1, 2, 3) (1, 3, 2) (2, 1, 3) (2, 3, 1) (3, 1, 2) (3, 2, 1)
  ```

- `combinations(iterable, r)`: This function returns an iterator that produces
  all combinations of `r` elements from the elements in `iterable`.

  ```python
  for i in itertools.combinations([1, 2, 3], 2):
      print(i)
  # Output: (1, 2) (1, 3) (2, 3)
  ```

- `groupby(iterable, key=None)`: This function returns an iterator that returns
  pairs `(key, group)`, where `key` is the value returned by the function `key`
  applied to the first element in `group`, and `group` is an iterator over the
  elements in `iterable` with the same value of `key`.

  ```python
  for key, group in groupby([1, 2, 2, 3, 3, 3]):
      print(key, list(group))
  # Output:
  # 1 [1]
  # 2 [2, 2]
  # 3 [3, 3, 3]
  ```

- `tee(iterable, n=2)`: This function returns a tuple of `n` independent
  iterators over the elements in `iterable`.

  ```python
  i1, i2 = tee([1, 2, 3])
  print(list(i1))
  print(list(i2))
  # Output:
  # [1, 2, 3]
  # [1, 2, 3]
  ```
