# Multiprocessing

The [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html)
module allows you to write concurrent programs that can take full advantage of
multiple processors or CPU cores on a given machine.

## Classes and Methods

The `multiprocessing` module has several classes and methods that allow you to
create and manage processes, as well as share data between processes. Here are
some of the most commonly used classes and methods in the `multiprocessing`
module.

- `Pool`: This class allows you to create a pool of worker processes that can
  be used to parallelize the execution of a function. It has a `map()` method
  that applies the function to each element in the list of arguments and
  returns a list of the results.

- `Process`: The `Pool` class is a convenient way to parallelize the execution
  of a function across multiple processes and get the results, but it is
  limited to applying a function to a list of arguments. The `Process` class is
  more flexible and allows you to create custom processes with complex
  behavior, but it requires more code to set up and manage and does not
  directly return a result.

- `Lock`: A lock can be used to prevent multiple processes from accessing a
  shared resource at the same time, ensuring that the resource is used in a
  thread-safe manner.

- `Semaphore`: A semaphore can be used to ensure that only a certain number of
  processes can access a shared resource at the same time.

- `Event`: An event can be used to signal that a particular condition has been
  met, allowing processes to wait for the event to be set before continuing
  execution.

- `Barrier`: A barrier can be used to ensure that a group of processes all
  reach a certain point in their execution before any of them can continue.

- `Condition`: A condition variable can be used to wait for a particular
  condition to be met before continuing execution.

- `Manager`: This class represents a manager process that controls a shared
  memory map. It can be used to create shared objects such as queues,
  dictionaries, and arrays that can be used to share data between processes.

The objects that can be shared between processes are limited to those that can
be pickled, which means they can be serialized and deserialized by the `pickle`
module.

The `multiprocessing` module provides several classes for sharing objects
between processes, such as `Queue`, `Value`, and `Array`, which are implemented
using `pickle` and can be shared between processes (i.e., they are thread- and
process-safe).

## Example

### Pool

In this example, the function `f` will be executed in parallel by the worker
processes in the pool. The `map()` method applies the function to each element
in the list of arguments and returns a list of the results.

You can use the `with` statement to ensure that the worker processes are closed
and joined properly when you are finished using the `Pool` object. This is
recommended to avoid leaving orphaned processes.

```python
from multiprocessing import Pool

def f(arg):
    return arg ** 2

# Create a pool with 4 worker processes
with Pool(4) as p:
    # Use map() to apply the function to a list of arguments
    results = p.map(f, [1, 2, 3, 4]) # OUTPUT: [1, 4, 9, 16]
```

You can use the `starmap()` method to apply a function to a list of argument
tuples.

```python
from multiprocessing import Pool

def f(arg1, arg2):
    return arg1 + arg2

# Create a pool with 4 worker processes
with Pool(4) as p:
    # Apply the function to a list of argument tuples in parallel
    results = p.starmap(f, [(1, 1), (2, 2), (3, 3), (4, 4)]) # OUTPUT: [2, 4, 6, 8]
```

Similar to `map()` and `starmap()`, the `apply()` method can be used when the
function takes a single argument.

### Process

Unlike the `Pool` class which applies a function to a list of arguments in
parallel and returns a list of the results, the `Process` class does not return
a result because a process does not return a value like a function does.

To get the result of a process, you can use one of the following approaches:

- Use a `Queue` to communicate the result from the process to the main program.
  The process can put the result in the queue, and the main program can
  retrieve it from the queue.

- Use a `Value` or `Array` object to store the result in shared memory. The
  process can write to the shared memory object, and the main program can read
  the result from it.

- Use a `Pipe` to communicate the result from the process to the main program.
  The process can send the result through the pipe, and the main program can
  receive it on the other end.

#### Value and Array

The `Value` and `Array` classes provide wrappers around C-level objects that
can be shared between processes.

```python
from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

num = Value('d', 0.0)
arr = Array('i', range(10))

p = Process(target=f, args=(num, arr))
p.start()
p.join()

print(num.value)
print(arr[:])
```

#### Queue

```python
from multiprocessing import Process, Queue

# Create a queue to hold the results
queue = Queue()

# Define the function that will be run in the process
def f(arg, queue):
    result = arg[0] + arg[1]
    queue.put(result)

# Create a list of processes
arg_list = [(1,1), (2,2), (3,3), (4,4)]
processes = [Process(target=f, args=(arg, queue)) for arg in arg_list]

# Start the processes
for p in processes:
    p.start()

# Wait for the processes to complete
for p in processes:
    p.join()

# Get the results from the queue
results = []
while not queue.empty():
    results.append(queue.get())
```

#### Manager

If you need to share larger or more complex data structures between processes,
you may want to consider using a `Manager` object, which provides more flexible
and powerful ways of sharing data between processes.

```python
from multiprocessing import Process, Manager

def f(d, key1, key2, value):
    d[key1][key2] = value + 1

# Create a manager and a dictionary of dictionaries
manager = Manager()
d = manager.dict()
d["dict1"] = manager.dict()
d["dict2"] = manager.dict()

# Create a list of processes
arg_list = [("dict1", "key1", 11), ("dict1", "key2", 12), ("dict2", "key1", 21), ("dict2", "key2", 22)]
processes = [Process(target=f, args=(d, *arg)) for arg in arg_list]

# Start the processes
for p in processes:
    p.start()

# Wait for the processes to complete
for p in processes:
    p.join()

# Print the dictionaries
print(d["dict1"])
print(d["dict2"])
```

#### Pipe

```python
from multiprocessing import Process, Manager, Pipe
import random

# Create a manager and a dictionary
manager = Manager()
d = manager.dict()
d[1] = 1

def f(conn, data):
    d[1] += 1
    data[str(random.randint(1,1000))] = random.randint(1,1000)
    conn.send(data)
    conn.close()

# Create a list of pipes
pipes = [Pipe() for _ in range(4)]

# Create a list of processes
processes = [Process(target=f, args=(child_conn, d)) for _, child_conn in pipes]

# Start the processes
for p in processes:
    p.start()

# Wait for the processes to complete
for p in processes:
    p.join()

# Collect the results
for parent_con, _  in pipes:
    d = parent_con.recv()
    print(d)
```
