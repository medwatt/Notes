# Threading

The `threading` module in Python provides support for creating and managing
multiple threads of execution within a program.

Python's `threading` module is built on top of the Python interpreter, and it
is subject to the Python **Global Interpreter Lock** (GIL). The GIL is a
mechanism that ensures that only one thread can execute at a time. This is
necessary to protect the integrity of Python objects, but it also means that
Python threads are not suitable for CPU-intensive tasks that can benefit from
parallel execution.

It's important to note that `threading` is not always the best solution to a
problem. In some cases, it may be more appropriate to use a different
concurrency model, such as the `asyncio` module or the `multiprocessing`
module. It's also important to consider the overhead of creating and managing
threads, as well as the potential for race conditions and other synchronization
issues.

Here are some guidelines for choosing between `threading`, `asyncio`, and
`multiprocessing`:

- Use `threading` if you want to run multiple independent tasks concurrently
  within a single program, and at least one of those tasks is likely to be
  blocked waiting for some external event (such as user input, network data, or
  I/O operations).

- Use `asyncio` if you need to perform a large number of I/O-bound or
  high-latency operations concurrently. `asyncio` allows you to wait for these
  operations to complete without blocking the event loop, which makes it
  well-suited to tasks that involve a lot of waiting.

- Use `multiprocessing` if you want to take advantage of multiple processors or
  CPU cores to speed up the execution of a program. It's a good choice for
  CPU-intensive tasks that can be parallelized, such as data processing or
  scientific simulations.

It is also worth noting that `threading`, `asyncio`, and `multiprocessing` are
not mutually exclusive, and you can use a combination of these approaches to
achieve your desired concurrency model. For example, you might use `threading`
to run multiple independent tasks concurrently within a program, and use
`multiprocessing` to parallelize CPU-intensive tasks.

## Classes and Methods

Here are some of the key classes and methods in the `threading` module:

- `Thread`: This class represents a thread, and it can be used to create a new
  thread by passing a function to run in the new thread. The `Thread` class has
  several methods and attributes that can be used to manage the thread, such as
  `start`, `join`, and `is_alive`. The `start` method starts the thread's
  execution, while the `join` method blocks the calling thread until the thread
  terminates.

  It's worth noting that the `join` method is optional and may not be needed
  in all cases. It is used to synchronize the execution of threads, and it
  can be useful if you want to ensure that a certain thread has completed
  before moving on to the next step in your program. However, if you do not
  need to synchronize the execution of threads, you can omit the `join`
  method and allow the threads to run concurrently.

- `Lock`: This class represents a lock, which can be used to synchronize access
  to shared resources by multiple threads. A `Lock` object has two methods,
  `acquire` and `release`. When a thread acquires a lock, it blocks other
  threads from acquiring the same lock until it has released it. A Lock is
  often used to protect a shared variable or resource from being accessed or
  modified by multiple threads simultaneously.

- `Semaphore`: This class represents a semaphore, which is a synchronization
  object that controls access to a shared resource by multiple threads. A
  `Semaphore` object has methods such as `acquire` and `release` that can be
  used to synchronize the execution of threads. It is often used to control
  access to a shared resource that has a limited capacity, such as a pool of
  connections or a buffer. A `Semaphore` has a counter that is decremented each
  time a thread acquires the semaphore, and incremented each time a thread
  releases the semaphore. When the counter reaches zero, subsequent threads
  that try to acquire the semaphore are blocked until the semaphore is
  released.

- `Condition`: This class represents a condition variable, which is a
  synchronization object that can be used to synchronize the execution of
  threads. A `Condition` object has methods such as `wait`, `notify`, and
  `notify_all` that can be used to control the execution of threads. A
  `Condition` has an associated lock, and threads that want to wait for the
  condition to be signaled must acquire the lock and then call the `wait`
  method. When the condition is signaled by another thread, the waiting threads
  are awakened and the lock is reacquired. A `Condition` is often used to
  implement complex synchronization scenarios, where threads need to wait for
  multiple events or conditions to occur before they can proceed.

- `Event`: This class represents an event, which is a synchronization object
  that can be used to signal between threads. An `Event` object has methods
  such as `set`, `clear`, and `wait` that can be used to signal and wait for
  events. An `Event` has a flag that can be set or cleared, and threads can
  wait for the flag to be set by calling the `wait` method. When the flag is
  set, the waiting threads are awakened. An `Event` is often used to implement
  simple signaling scenarios, where one thread needs to signal another thread
  that an event has occurred.

- `Timer`: This class represents a timer, which is a thread that executes a
  specified function after a specified delay. A `Timer` object has a `start`
  method that can be used to start the timer.


## Example

### I/O bound task

Here, we consider a simple program where the execution thread is blocked by
some external event.

```python
def do_io_bound_task(i):
    print(f"Staring task {i}")
    time.sleep(1) # This simulates an I/O bound task
    print(f"Done task {i}")
```

Without threading, a new function call is made only after the previous one is
completed.

```python
# This takes at least 5 seconds to complete
for i in range(5):
    do_io_bound_task(i)

# OUTPUT:
## Staring task 0
## Done task 0
## Staring task 1
## Done task 1
## Staring task 2
## Done task 2
## Staring task 3
## Done task 3
## Staring task 4
## Done task 4
```

The multithreaded version is given below.

```python
threads = [] # threads list

for i in range(5):
    t = Thread(target=do_io_bound_task, args=(i,)) # `args` is a tuple/list of all the arguments
    threads.append(t)

for t in threads:
    t.start() # Launch the threads

for t in threads:
    t.join() # Wait for the threads to finish before continuing

# OUTPUT:
## Staring task 0
## Staring task 1
## Staring task 2
## Staring task 3
## Staring task 4
## Done task 0
## Done task 3
## Done task 1
## Done task 2
## Done task 4
```

- When a thread reaches a `sleep` or other blocking operation, it is removed
  from the execution queue and placed in the waiting queue. This allows other
  threads to run while the sleeping thread is waiting.

- Only one thread is executed at a time (due to the global interpreter lock).

- If a task is I/O bound (i.e., it involves a lot of waiting for external
  events or resources), then the CPU may sit idle while waiting for the I/O
  operation to complete. In this case, multithreading can be useful because it
  allows other threads to use the CPU while the I/O-bound thread is waiting.

- The sequence in which threads finish is non-deterministic, meaning that it is
  not guaranteed to be the same from one execution to the next.

- All Python threads share the same memory space, which means that they can
  access and modify the same variables and data structures. This can lead to
  race conditions and other synchronization issues if multiple threads attempt
  to access and modify shared data at the same time (this is explored in the
  following section).

### CPU bound task

In this example, multithreading does not provide any benefits because the
thread is CPU bound and can only run one at a time due to the Python Global
Interpreter Lock (GIL).

```python
def do_cpu_bound_task(i):
    print(f"Staring task {i}")
    s = 0
    for _ in range(10_000_000):
        s += 1
    print(f"Done task {i}")

threads = []

for i in range(5):
    t = Thread(target=do_cpu_bound_task, args=(i,))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()
```

## Memory Sharing

- In this example, we consider the task of counting the number of times a
  letter appears in a given text.
- The texts are downloaded from a remote web page. Hence, this is an I/O bound
  task where multithreading can improve the overall execution time.

```python
url_list = [
    "http://shakespeare.mit.edu/allswell/full.html",
    "http://shakespeare.mit.edu/julius_caesar/full.html",
    "http://shakespeare.mit.edu/romeo_juliet/full.html",
    "http://shakespeare.mit.edu/macbeth/full.html",
    "http://shakespeare.mit.edu/hamlet/full.html"
]
```

### Singlethreaded

```python
import json
import urllib

def count_letters(url, frequency_dict):
    response = urllib.request.urlopen(url)
    txt = str(response.read())
    for c in txt:
        c = c.lower()
        if c in frequency_dict:
            frequency_dict[c] += 1

# initialize a frequency dictionary
frequency_dict = {}
for c in "abcdefghijklmnopqrstuvwxyz":
    frequency_dict[c] = 0

for url in url_list:
    count_letters(url, frequency_dict)

print(json.dumps(frequency_dict, indent=4))
```

### Multithreaded

```python
# Initialize a frequency dictionary
frequency_dict = {}
for c in "abcdefghijklmnopqrstuvwxyz":
    frequency_dict[c] = 0

for url in url_list:
    t = Thread(target=count_letters, args=(url, frequency_dict))
    t.start()

for t in threads:
    t.join()

print(json.dumps(frequency_dict, indent=4))
```

Although the execution time is reduced with multithreading, the dictionaries
returned by the singlethreaded and multithreaded processes will not match. This
is because all the threads have access to the same memory space, and it is
possible for multiple threads to read and modify shared variables independently
of each other. As a result, changes made by one thread may not be visible to
other threads when accessing the same variable.

### Using a Lock

To resolve this issue, a shared variable should only be accessed by one thread
at a time. This can be achieved using a `Lock` (or mutex) object. The process
works as follows:

- A thread that wants to access and update a shared variable requests a `Lock`.
  When the thread acquires the `Lock`, no other thread can access or modify the
  variable.
- If the `Lock` is available (not held by another thread), the thread acquires
  it. All other threads that require access to the variable will be blocked
  from execution until the `Lock` is released.
- The thread releases the `Lock` once it is no longer needed, allowing other
  threads to acquire it.
- It is generally a good idea to use locks sparingly, since acquiring and
  releasing locks can add overhead to your program. Instead of using locks to
  synchronize access to every shared variable, it may be more efficient to use
  locks only around critical sections of code where multiple threads are
  accessing or modifying shared data.

```python
from threading import Thread, Lock

def count_letters_multithreaded(url, frequency_dict, lock):
    # Begin: I/O bound
    response = urllib.request.urlopen(url)
    # End: I/O bound
    txt = str(response.read())
    lock.acquire()
    # Begin: CPU bound
    for c in txt:
        c = c.lower()
        if c in frequency_dict:
            frequency_dict[c] += 1
    # End: CPU bound
    lock.release()

# Initialize a frequency dictionary
frequency_dict = {}
for c in "abcdefghijklmnopqrstuvwxyz":
    frequency_dict[c] = 0

lock = Lock() # lock object
threads = []

for url in url_list:
    t = Thread(target=count_letters_multithreaded, args=(url, frequency_dict, lock))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(json.dumps(frequency_dict, indent=4))
```

### Using a Semaphore

In this example, we are using a `Semaphore` to control access to the network
when downloading a list of images from a website. By using a `Semaphore` with a
capacity of 10, we are limiting the number of concurrent network connections to
10, which can help avoid overloading the network and the server. The threads
acquire the semaphore before making a network request, and they release the
semaphore after the request is complete. This ensures that at most 10 threads
can access the network at the same time, and the remaining threads are blocked
until one of the other threads has released the semaphore.

```python

import threading
import requests

# Create a semaphore with a capacity of 10
semaphore = threading.Semaphore(10)

# Create a shared resource
results = []

def download_image(url):
    # Acquire the semaphore
    semaphore.acquire()
    try:
        # Download the image
        response = requests.get(url)
        image = response.content
        # Save the image to the shared resource
        results.append(image)
    finally:
        # Release the semaphore
        semaphore.release()

# Create a list of URLs to download
urls = [
    'https://example.com/image1.jpg',
    'https://example.com/image2.jpg',
    'https://example.com/image3.jpg',
    # ...
]

# Create a thread for each URL
threads = [threading.Thread(target=download_image, args=(url,)) for url in urls]

# Start the threads
for thread in threads:
    thread.start()

# Wait for the threads to complete
for thread in threads:
    thread.join()
```

### Using a Condition

In this example, we have a producer thread that generates data and a consumer
thread that processes the data. To ensure that the consumer thread only starts
processing the data when it is available, we use a `Condition` to synchronize
the execution of the threads. The producer thread acquires the condition, adds
the data to the shared resource, and then notifies the consumer thread that new
data is available. The consumer thread acquires the condition, waits for the
notification, and then processes the data. This ensures that the consumer
thread does not start processing the data until it is available, and the
producer thread does not add new data to the resource until the consumer thread
has finished processing the previous data.

Note that the producer does not explicitly know when the consumer has finished
processing the data. While the consumer is processing the data, the producer is
blocked and cannot add new data to the resource. When the consumer finishes
processing the data and releases the `Condition`, the producer can acquire the
`Condition`, add new data to the resource, and notify the consumer again. This
ensures that the consumer has finished processing the previous data before the
producer adds new data to the resource.

```python
import threading

# Create a condition
condition = threading.Condition()

# Create a shared resource
resource = []

def producer():
    # Acquire the condition
    with condition:
        # Generate some data
        data = generate_data()
        # Add the data to the shared resource
        resource.append(data)
        # Notify the consumer that new data is available
        condition.notify()

def consumer():
    # Acquire the condition
    with condition:
        # Wait for new data to be available
        condition.wait()
        # Process the data
        process_data(resource.pop())

# Create a producer and a consumer
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start the producer and the consumer
producer_thread.start()
consumer_thread.start()

# Wait for the producer and the consumer to complete
producer_thread.join()
consumer_thread.join()
```

### Using an Event

In this example, we have two threads: a waiter thread that waits for an event
to be set, and a setter thread that generates some data and sets the event. The
setter thread uses the `Event` object to signal the waiter thread that the data
is ready. When the setter thread sets the event, the waiter thread wakes up and
starts processing the data. The `Event` object allows the setter thread to
signal the waiter thread without the need for polling or busy waiting. The
`Event` object can be used to signal a single thread or multiple threads that
are waiting for the event. The `clear` method can be used to reset the event,
and the `is_set` method can be used to check the state of the event.

```python
import threading

# Create an event
event = threading.Event()

def waiter():
    while True:
        # Wait for the event to be set
        event.wait()
        # Process the data
        process_data()
        # Reset the event
        event.clear()

def setter():
    while True:
        # Generate some data
        data = generate_data()
        # Set the event
        event.set()

# Create a waiter and a setter
waiter_thread = threading.Thread(target=waiter)
setter_thread = threading.Thread(target=setter)

# Start the waiter and the setter
waiter_thread.start()
setter_thread.start()
```
