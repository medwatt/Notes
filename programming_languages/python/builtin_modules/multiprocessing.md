# Multiprocessing

The [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html)
module allows you to create programs that can run multiple processes
simultaneously, taking full advantage of multiple CPU cores. This is especially
useful for CPU-bound tasks that benefit from parallel execution.

## Classes and Methods

The `multiprocessing` module has several classes and methods that allow you to
create and manage processes, as well as share data between them.

### Process Management

-   **`Pool`**: Mannages a group of worker processes and automatically
    distributes tasks to them.
-   **`Process`**: Creates and manages individual processes manually,
    providing more control over process creation, task assignment, and
    communication.

#### Pool Methods

The methods below are used with a `Pool` object for distributing tasks to
worker processes.

-   **`apply()`**: Applies a function to a single set of arguments and
    returns the result.
-   **`map()`**: Applies a function to each element in the list of
    arguments and returns a list of the results.
-   **`starmap()`**: Similar to `map()`, but applies a function to a
    list of argument tuples.

#### Process Methods

The following methods are used with a `Process` object for creating and
managing individual processes:

- **`start()`**: Starts the process and runs its target function in a
  new subprocess.
- **`join()`**: Waits for the process to finish. It ensures that the
  parent process waits for the child process to complete before moving on.
- **`is_alive()`**: Checks if the process is still running. Returns
  `True` if the process is active, otherwise `False`.
- **`terminate()`**: Immediately stops the process.

#### Inter-Process Communication (IPC)

- **`Queue`**: A process-safe FIFO queue for passing data between
  processes.
- **`Shared Memory`**: Shares simple data (e.g., integers, arrays)
  between processes through `Value` and `Array` objects.
- **`Pipe`**: A two-way communication channel between two processes for
  sending and receiving data.
- **`Manager`**: Shares complex objects (e.g., lists, dictionaries)
  between processes via proxy objects. Simplifies synchronization for shared
  state across processes.

### Synchronization Primitives

-   **`Lock`**: Provides mutual exclusion to shared resources.
-   **`Semaphore`**: Controls access to a resource with a counter.
-   **`Event`**: Manages an internal flag that can be set or cleared.
-   **`Condition`**: Allows one or more processes to wait until notified.
-   **`Barrier`**: Blocks a set number of processes until they all reach the barrier.

## Examples

### Pool

The `map()` method applies the function to each element in the list of
arguments and returns a list of the results.

```python
import numpy as np
from multiprocessing import Pool

def f(arr):
    return arr / np.sqrt(np.sum(arr**2))

arrays = [
    np.array([1, 2, 3]),
    np.array([4, 5, 6]),
    np.array([7, 8, 9])
]

# Create a pool with 3 worker processes
with Pool(3) as p:
    results = p.map(f, arrays)
```

Use the `starmap()` method to apply a function to a list of argument tuples.

```python
from multiprocessing import Pool

def f(arg1, arg2):
    return arg1 + arg2

args = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4)
]

# Create a pool with 4 worker processes
with Pool(4) as p:
    results = p.starmap(f, args) # OUTPUT: [2, 4, 6, 8]
```

#### Picklable Objects

The objects that can be passed as argument are limited to those that can be
pickled, which means they can be serialized and deserialized by the `pickle`
module.

- **Picklable Objects**: These include most Python objects such as
  booleans, numbers, strings, lists, tuples, dictionaries.

- **Non-Picklable Objects**: These include file handles such as
  `open('file.txt')`, instances of `Thread` and `Process`, lambdas,
  closures, etc.

### Process

Unlike the `Pool` class, which applies a function to a list of arguments in
parallel and returns a list of the results, the `Process` class does not
return a value directly, because a process does not return a result like a
function call does.

To retrieve the result of a process, you can use one of the following approaches:

- Use a `Value` or `Array` object to store the result in shared
  memory. The process can write to the shared memory object, and the main
  program can read the result from it.

- Use a `Queue` to communicate the result from the process to the main
  program. The process can put the result into the queue, and the main program
  can retrieve it from the queue.

- Use a `Pipe` to communicate the result from the process to the main
  program. The process can send the result through the pipe, and the main
  program can receive it from the other end.

- Use a `Manager` to share complex data structures (like lists and
  dictionaries) across processes, using proxy objects to allow safe and
  synchronized access.

#### Value and Array

The `Value` and `Array` classes provide wrappers around C-level objects that
can be shared between processes.

```python
from multiprocessing import Process, Value, Array

def modify_shared_data(shared_val, shared_arr):
    # Increment the shared value
    with shared_val.get_lock():  # Lock to prevent race conditions
        shared_val.value += 1

    # Increment each element of the shared array
    for i in range(len(shared_arr)):
        shared_arr[i] += 1

# Shared integer and array
shared_val = Value('i', 0)  # Shared integer, initialized to 0
shared_arr = Array('i', [1, 2, 3, 4, 5])  # Shared array of integers

# Create two processes to modify shared data
p1 = Process(target=modify_shared_data, args=(shared_val, shared_arr))
p2 = Process(target=modify_shared_data, args=(shared_val, shared_arr))

p1.start()
p2.start()

p1.join()
p2.join()

# Final results
print(f"Final Value: {shared_val.value}")  # Final value of the shared integer
print(f"Final Array: {shared_arr[:]}")     # Final state of the shared array
```

 - When creating a `Value` or `Array`, you specify a format code to define the type:

    - **`'f'`**: Float
    - **`'i'`**: Signed integer
    - **`'c'`**: Single character
    - **`'b'`**: Signed char
    - **`'h'`**: Short
    - **`'l'`**: Long
    - **`'d'`**: Double precision float

- By default, `Value` and `Array` include an internal lock to ensure
  safe access by multiple processes. You can disable the lock using
  `lock=False` for performance optimization, but only when you're certain no
  race conditions will occur (e.g., in read-only scenarios).

#### Queue

```python
from multiprocessing import Process, Queue

def producer(q, items):
    for item in items:
        print(f"Producer put: {item}")
        q.put(item)

def consumer(q):
    while not q.empty():
        item = q.get()
        print(f"Consumer got: {item}")

# Create a queue to hold the results
q = Queue()

# Create multiple producers
p1 = Process(target=producer, args=(q, ['apple', 'banana', 'cherry']))
p2 = Process(target=producer, args=(q, ['dog', 'elephant', 'frog']))

# Create multiple consumers
c1 = Process(target=consumer, args=(q,))
c2 = Process(target=consumer, args=(q,))

# Start the producer processes
p1.start()
p2.start()

p1.join()
p2.join()

# Start the consumer processes
c1.start()
c2.start()

c1.join()
c2.join()
```

Basic Operations on the `Queue` object:

- **`put()`**: Add an item to the queue.
- **`get()`**: Retrieve and remove an item from the queue.
- **`qsize()`**: Return the approximate size of the queue (may not be
  accurate due to timing issues).
- **`empty()`**: Return `True` if the queue is empty.
- **`full()`**: Return `True` if the queue is full (used with a limited
  size queue).

#### Pipe

`Pipe` is a two-way communication channel between two processes. A pipe creates
two endpoints, typically referred to as `conn1` and `conn2`. Each process holds
one end of the pipe for communication. One process writes data to one end of
the pipe, and another process reads it from the other. It is useful for
scenarios where you only need to communicate between two processes, making it
simpler than a `Queue`.

```python
from multiprocessing import Process, Pipe

def worker1(conn, name, value):
    msg = f"Worker 1 ({name}) sends value {value}"
    conn.send(msg)  # Send a message
    print(f"Worker 1 sent: {msg}")

    response = conn.recv()  # Receive response from Worker 2
    print(f"Worker 1 received: {response}")
    conn.close()

def worker2(conn, multiplier):
    msg = conn.recv()  # Receive the message from Worker 1
    print(f"Worker 2 received: {msg}")

    # Extracting value from the message
    value = int(msg.split()[-1])
    response_value = value * multiplier
    response_msg = f"Worker 2 multiplied value by {multiplier} and got {response_value}"

    conn.send(response_msg)  # Send the processed result back to Worker 1
    print(f"Worker 2 sent: {response_msg}")
    conn.close()

# Create a Pipe
conn1, conn2 = Pipe()

# Create two processes, passing arguments to each worker
p1 = Process(target=worker1, args=(conn1, 'Alice', 10))  # Worker 1 has a name and a value
p2 = Process(target=worker2, args=(conn2, 5))  # Worker 2 has a multiplier argument

# Start both processes
p1.start()
p2.start()

# Wait for both processes to complete
p1.join()
p2.join()
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

### Synchronization Primitives

#### Lock

A `Lock` ensures mutual exclusion, meaning that only one process can hold the
lock at a time. This is useful when multiple processes need to access shared
resources and we want to avoid race conditions.

```python
from multiprocessing import Process, Lock

def worker(lock, shared_resource):
    with lock:  # Acquire the lock before accessing the shared resource
        print(f"{shared_resource}: Accessing shared resource")

if __name__ == '__main__':
    lock = Lock()
    processes = [Process(target=worker, args=(lock, f"Process {i}")) for i in range(5)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()
```

- The lock ensures that only one process at a time can access the shared
  resource (`print` in this case).

- Without the lock, multiple processes could print at the same time,
  causing mixed-up or overlapping output.

#### Semaphore

A `Semaphore` allows a limited number of processes to access a resource at the
same time. It uses a counter to track how many processes can access the
resource simultaneously. Once the counter reaches zero, any further processes
trying to access the resource will be blocked until the counter increases.

```python
from multiprocessing import Process, Semaphore
import time

def worker(sem, worker_id):
    with sem:  # Acquire the semaphore
        print(f"Worker {worker_id} is accessing the resource")
        time.sleep(1)  # Simulate work
    print(f"Worker {worker_id} is done")

if __name__ == '__main__':
    sem = Semaphore(2)  # Allow up to 2 processes to access the resource at the same time

    processes = [Process(target=worker, args=(sem, i)) for i in range(5)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()
```

- Only two workers can access the resource simultaneously (because
  `Semaphore(2)`).

- Other workers must wait until one of the active workers releases the
  semaphore (after `time.sleep(1)`).

#### Event

An `Event` object manages an internal flag that can be set (`set()`) or
cleared (`clear()`). Processes can wait for the flag to be set using
`wait()`. It is useful for signaling between processes.

```python
from multiprocessing import Process, Event
import time

def worker(event, worker_id):
    print(f"Worker {worker_id} waiting for event to be set")
    event.wait()  # Block until the event is set
    print(f"Worker {worker_id} received the event!")

if __name__ == '__main__':
    event = Event()

    processes = [Process(target=worker, args=(event, i)) for i in range(3)]

    for p in processes:
        p.start()

    time.sleep(2)
    print("Main process setting the event")
    event.set()  # Signal all processes to continue

    for p in processes:
        p.join()
```

- All workers wait at `event.wait()` until the event is set by the main
  process.

- Once the main process calls `event.set()`, all waiting workers are
  unblocked and continue execution.

#### Condition

A `Condition` allows processes to wait for a condition to be met, and another
process can notify them when the condition is true. It’s more flexible than
`Event`, as it allows processes to wait for and respond to specific
conditions using `notify()` and `wait()`.

```python
from multiprocessing import Process, Condition
import time

def consumer(cond, worker_id):
    with cond:
        print(f"Worker {worker_id} waiting for condition")
        cond.wait()  # Wait until the condition is notified
        print(f"Worker {worker_id} received the condition")

def producer(cond):
    time.sleep(2)
    with cond:
        print("Producer is notifying all workers")
        cond.notify_all()  # Notify all waiting workers

if __name__ == '__main__':
    cond = Condition()

    processes = [Process(target=consumer, args=(cond, i)) for i in range(3)]

    for p in processes:
        p.start()

    Process(target=producer, args=(cond,)).start()

    for p in processes:
        p.join()
```

- The consumers are waiting for the `Condition` object to be notified.

- The producer waits 2 seconds, then calls `cond.notify_all()`, which
  wakes up all waiting consumers.

#### Barrier

A `Barrier` blocks processes until a set number of processes have reached the
barrier. Once all processes have reached the barrier, they can continue
executing.

```python
from multiprocessing import Process, Barrier
import time

def worker(barrier, worker_id):
    print(f"Worker {worker_id} waiting at the barrier")
    barrier.wait()  # Block until all processes have reached the barrier
    print(f"Worker {worker_id} passed the barrier")

if __name__ == '__main__':
    barrier = Barrier(3)  # Create a barrier for 3 processes

    processes = [Process(target=worker, args=(barrier, i)) for i in range(3)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()
```

- All workers wait at `barrier.wait()` until all 3 processes reach the barrier.

- Once all processes have reached the barrier, they all continue executing.
