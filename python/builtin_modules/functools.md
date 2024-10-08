# functools

The [`functools`](https://docs.python.org/3/library/functools.html) module
provides a variety of tools for working with functions. It includes functions
for creating decorators, partial functions, and other utility functions for
    functional programming.

## Methods

Some of the most commonly used functions in the `functools` module are:

- `functools.partial(func, *args, **keywords)`: Returns a new function that is
  a partial application of the function `func`, with some of the arguments
  fixed. This can be used to create a new function with fewer arguments from an
  existing function.

  ```python
  import functools

  # Define a function that takes three arguments
  def add(x, y, z):
      return x + y + z

  # Use partial to create a new function that takes only two arguments
  add_two = functools.partial(add, y=1, z=2)

  # Call the new function
  result = add_two(3)
  print(result)  # Output: 6
  ```

- `functools.partialmethod(func, *args, **keywords)`: This function is similar
  to `functools.partial`, but it is intended to be used as a method of an
  object instance, rather than as a standalone function.

- `functools.reduce(func, iterable, initial=None)`: Applies the function `func`
  to the elements of the iterable, reducing them to a single value. The
  `initial` argument is an optional initial value that is used as the first
  argument to `func`.

  ```python
  import functools

  # Define a function that takes two arguments and returns their product
  def multiply(x, y):
      return x * y

  # Use reduce to compute the product of the numbers in the list
  numbers = [1, 2, 3, 4, 5]
  product = functools.reduce(multiply, numbers)
  print(product)  # Output: 120
  ```

- `functools.lru_cache(maxsize=128, typed=False)`: This is a decorator that
  wraps a function and applies a least-recently-used (LRU) cache to the
  function. The optional argument `maxsize` specifies the maximum size of the
  cache, and the optional argument `typed` specifies whether the cache should
  consider the types of the arguments when determining whether a value is in
  the cache.

  ```python
  import functools

  # Define a recursive function to compute the nth Fibonacci number
  @functools.lru_cache(maxsize=None)
  def fibonacci(n):
      if n < 2:
          return n
      return fibonacci(n-1) + fibonacci(n-2)

  # Compute the first 10 Fibonacci numbers
  for i in range(10):
      print(fibonacci(i))
  ```
