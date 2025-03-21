# Introduction to Profiling Code in Python

Profiling is an essential process in optimizing code performance by identifying
bottlenecks and inefficient code segments. Python offers several tools for
profiling, each tailored to different needs and scenarios. In this chapter,
we'll explore three of the most common modules for profiling Python code:

- **timeit**: A simple module for timing small code snippets, ideal for
  micro-benchmarks.

- **cProfile**: A built-in profiler that provides a comprehensive overview
  of function call times.

- **line_profiler**: An external module for line-by-line profiling to
  pinpoint exact lines causing slowdowns.

# timeit

The `timeit` module is designed to measure the execution time of small code
snippets. It is ideal for micro-benchmarks and comparing different
implementations of a function.

## Using timeit

You can use `timeit` from the command line or within your code.

### Command Line Usage

Suppose you want to compare the performance of two different methods of list
creation:

```{bash}
python -m timeit "x = [i for i in range(1000)]"
python -m timeit "x = list(range(1000))"
```

Sample output:

```{bash}
10000 loops, best of 5: 29 usec per loop
10000 loops, best of 5: 22 usec per loop
```

From the output, using `list(range(1000))` is slightly faster.

### Using timeit in Code

You can use the `timeit` function within your code for more complex timing.

```{python}
import timeit

setup_code = '''
def list_comprehension():
    return [i for i in range(1000)]

def list_constructor():
    return list(range(1000))
'''

test_code1 = 'list_comprehension()'
test_code2 = 'list_constructor()'

# Time the first function
time1 = timeit.timeit(stmt=test_code1, setup=setup_code, number=10000)
print(f'List comprehension: {time1} seconds')

# Time the second function
time2 = timeit.timeit(stmt=test_code2, setup=setup_code, number=10000)
print(f'List constructor: {time2} seconds')
```

Sample output:

```{bash}
List comprehension: 0.287 seconds
List constructor: 0.217 seconds
```

### Timing a Function Call

You can also time a specific function directly:

```{python}
import timeit

def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

time_taken = timeit.timeit(stmt='fibonacci_iterative(500)', globals=globals(), number=1000)
print(f'Time taken: {time_taken} seconds')
```

## Tips for Using timeit

- **Repeat Measurements**: By default, `timeit` runs the code multiple
  times to get an average execution time, reducing the impact of transient
  system load.

- **Minimal Overhead**: `timeit` disables garbage collection and other
  interpreter features to minimize overhead.

- **Use `repeat`**: For more robust measurements, use `timeit.repeat()` to
  run multiple sets of measurements.

### Example with repeat

```{python}
import timeit

times = timeit.repeat(stmt='fibonacci_iterative(500)', globals=globals(), number=1000, repeat=5)
print(f'Minimum execution time: {min(times)} seconds')
```

# cProfile

`cProfile` is a built-in Python module that collects statistics about the
frequency and duration of function calls, helping you understand which parts of
your code are consuming the most time.

## Using cProfile

To profile a script using `cProfile`, you can run it from the command line:

```{bash}
python -m cProfile my_script.py
```

Alternatively, you can use it within your code:

```{python}
import cProfile

def my_function():
    # Your code here

cProfile.run("my_function()")
```

### Interpreting the Output

The profiler will output a table with columns like:

- **ncalls**: Number of calls.
- **tottime**: Total time spent in the given function (excluding time made in calls to sub-functions).
- **cumtime**: Cumulative time spent in this and all sub-functions.
- **percall**: Time per call (tottime/cumtime divided by ncalls).

## Saving and Viewing Profile Data

You can save the profiling data to a file for later analysis:

- From the command line:

```{python}
python -m cProfile -o profiling_results script.py
```

- From inside the script:

```{python}
import cProfile

cProfile.run("my_function()", "profiling_results")
```

Use the `pstats` module to read and manipulate the saved data:

```{python}
import pstats

p = pstats.Stats("profiling_results")
p.sort_stats("cumtime").print_stats(10)
```

This will print the top 10 functions sorted by cumulative time.

## Visualizing Profiling Data

For better visualization, you can use tools like `SnakeViz` or `gprof2dot` to
generate graphical representations.

### Using SnakeViz

- Install SnakeViz:

```{bash}
pip install snakeviz
```

- Visualize with SnakeViz:

```{bash}
snakeviz profiling_results
```

This will open a web browser displaying an interactive visualization.

# line_profiler

`line_profiler` is a third-party module that provides line-by-line profiling of
functions, allowing you to pinpoint the exact lines of code that are
performance bottlenecks.

## Installation

Install `line_profiler` using pip:

```{bash}
pip install line_profiler
```

## Using line_profiler

`line_profiler` works by decorating the functions you want to profile with
`@profile`. It then runs the code and provides timing information for each
line.

### Example: Profiling a Function Line by Line

Let's revisit the Fibonacci example.

```{python}
# fibonacci_line_profile.py
from line_profiler import profile

@profile
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    fibonacci(20)
```

### Running line_profiler

Run the profiler using the `kernprof` script that comes with `line_profiler`:

```{bash}
kernprof -l fibonacci_line_profile.py
```

This will execute the script and create a `fibonacci_line_profile.py.lprof`
file containing the profiling data.

### Viewing the Results

Use `line_profiler` to view the results:

```{bash}
python -m line_profiler fibonacci_line_profile.py.lprof
```

Sample output:

```{bash}
Timer unit: 1e-06 s

Total time: 0.014789 s
File: a.py
Function: fibonacci at line 3

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     3                                           @profile
     4                                           def fibonacci(n):
     5     21891       3834.7      0.2     25.9      if n <= 1:
     6     10946       1912.5      0.2     12.9          return n
     7     10945       9041.9      0.8     61.1      return fibonacci(n-1) + fibonacci(n-2)

  0.01 seconds - a.py:3 - fibonacci
```

The output shows:

- **Hits**: Number of times each line was executed.
- **Time**: Total time spent on that line.
- **Per Hit**: Average time per execution.
- **% Time**: Percentage of total time spent on that line.
- **Line Contents**: The code line.

From the output, we can see that line 7 (`return fibonacci(n-1) +
fibonacci(n-2)`) is consuming most of the execution time.

## Profiling Multiple Functions

You can profile multiple functions by decorating them with `@profile`.

```{python}
@profile
def function_one():
    # Code here

@profile
def function_two():
    # Code here
```

## Notes and Tips

- **Do Not Use @profile in Production**: The `@profile` decorator is
  injected by `line_profiler` at runtime. Remove or comment out `@profile`
  decorators when not profiling.

- **Overhead**: Profiling adds overhead to execution time. Do not measure
  performance with profiling enabled.

- **Selective Profiling**: Only decorate functions you need to profile to
  reduce overhead.

## Alternative Usage: IPython Integration

If you use IPython or Jupyter notebooks, `line_profiler` integrates with the
`%lprun` magic command.

### Example

```{python}
%load_ext line_profiler

def fibonacci(n):
    # Function code

%lprun -f fibonacci fibonacci(30)
```

This will profile the `fibonacci` function line by line without modifying the
code with `@profile`.
