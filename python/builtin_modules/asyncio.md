# asyncio

The `asyncio` module provides support for **asynchronous programming**. It is
well-suited for I/O-bound and high-concurrency applications, such as
networking, web scraping, and interacting with databases.

In traditional **synchronous programming**, a program will execute one task at
a time and will wait for that task to complete before moving on to the next
task. In contrast, asynchronous programming allows a program to execute
multiple tasks at the same time without waiting for one task to complete before
starting another. This can lead to more efficient use of resources and can make
programs more responsive to user input.

It is easy to confuse asynchronous programming with multithreaded programming
because both techniques can be used to achieve concurrent execution of code.
However, they work in fundamentally different ways.

- In a multithreaded program, multiple threads of execution are created, and
  the operating system is responsible for scheduling the threads (for example,
  when to switch to another thread) and allocating resources to them. This can
  lead to more efficient use of CPU resources, but it also introduces the need
  for synchronization primitives such as locks and semaphores to prevent race
  conditions and other issues, which is not trivial to get right.

- On the other hand, an asynchronous program typically only has a single thread
  of execution, and the program uses an event loop to schedule and run
  asynchronous tasks. When an asynchronous task yields control back to the
  event loop, the event loop can schedule another task to run. This allows for
  more precise control over task switching and eliminates the need for explicit
  synchronization.

The writing of asynchronous code uses the concept of **coroutines**, which are
similar to traditional functions (similar to generators), but can be paused and
resumed at a later time. When a coroutine is paused, it yields control back to
the calling code, allowing other code to run in the meantime. When the
coroutine is resumed, it picks up where it left off and continues executing.

The `asyncio` module provides an **event loop**, which can be thought of as a
central control unit that is responsible for managing the execution of
coroutines, scheduling callbacks and handling I/O operations. It listens for
events, and when an event occurs, it runs the appropriate code to handle that
event. Some of the events that the event loop listens for include:

- The completion of an asynchronous task: When an asynchronous task completes,
  the event loop can be notified so that it can schedule another task to run.

- The arrival of data on a network socket: When data is received on a network
  socket, the event loop can be notified so that it can read the data and
  process it.

- The expiration of a timer: The event loop can be configured to run a task
  after a certain amount of time has passed, using a timer.

- A signal being raised: The event loop can be configured to run a task when a
  signal is raised, such as when the user closes the program.


## Coroutines

`asyncio` provides the `async`/`await` keywords for defining coroutines. The
`async` keyword is used to define an asynchronous function, and the `await`
keyword is used to indicate that the execution of the function should be paused
at that point and control should be returned to the event loop. The event loop
will then schedule other tasks to run, and when the task that `await` is
waiting on completes, the event loop will resume the execution of the `async`
function and return the result of the awaited task. Note that the `await`
keyword can only be used within a function that is defined as `async`.

To run an `async` function, you need to schedule it to be executed by the event
loop. There are several ways to do this, but the most common way is to use the
`asyncio.run` function, which creates an event loop, schedules the function to
be run, and runs the event loop until the function completes.

Note that when an `async` function is called, it returns a `coroutine` object.
The `coroutine` object represents the asynchronous task, that may not be
executed immediately. The `coroutine` object can be used to interact with the
event loop, for example to schedule the task to be run, or to cancel the task
if needed.


### Using the async / await keywords

```python
import asyncio

async def main_async_function():
    print("Starting main function")
    result1 = await my_async_function1()
    result2 = await my_async_function2()
    print("Done with main function")
    return result1, result2

async def my_async_function1():
    print("Hello from my async function 1")
    await asyncio.sleep(3)
    print("Done with async function 1")
    return "my_async_function1 result"

async def my_async_function2():
    print("Hello from my async function 2")
    await asyncio.sleep(2)
    print("Done with async function 2")
    return "my_async_function2 result"

result = asyncio.run(main_async_function())
print(result)


# Starting main function
# Hello from my async function 1
# Done with async function 1
# Hello from my async function 2
# Done with async function 2
# Done with main function
# ('my_async_function1 result', 'my_async_function2 result')
```

In the example above, the `asyncio.run` function creates an event loop and
schedules `main_async_function` to be run. The function runs until
`my_async_function1` is called using the `await` keyword. This causes the
execution of `main_async_function` to be suspended until `my_async_function1`
completes. Even though `my_async_function1` also has an `await` keyword and
control is indeed returned to the event loop to allow other tasks to run, but
because there's only one task to run (`main_async_function`), and this task is
waiting for the completion of `my_async_function1`, `main_async_function` will
not be scheduled to run again until `my_async_function1` completes. As a
result, `my_async_function2` runs only after `my_async_function1` finishes.

### Using the gather function

If you want `my_async_function2` to run while `my_async_function1` is blocking,
you can use the `asyncio.gather()` function to schedule both functions to run
concurrently. The `asyncio.gather()` function returns a new awaitable that will
wait for all the awaitables passed as argument to be done.

```python
import asyncio

async def main_async_function():
    print("Starting main function")
    result1, result2 = await asyncio.gather(my_async_function1(), my_async_function2())
    print("Done with main function")
    return result1, result2

async def my_async_function1():
    print("Hello from my async function 1")
    await asyncio.sleep(3)
    print("Done with async function 1")
    return "my_async_function1 result"

async def my_async_function2():
    print("Hello from my async function 2")
    await asyncio.sleep(2)
    print("Done with async function 2")
    return "my_async_function2 result"

result = asyncio.run(main_async_function())
print(result)

# Starting main function
# Hello from my async function 1
# Hello from my async function 2
# Done with async function 2
# Done with async function 1
# Done with main function
# ('my_async_function1 result', 'my_async_function2 result')
```

### Creating tasks

Another way to achieve the same goal of running `my_async_function1` and
`my_async_function2` concurrently is through the use of the
`asyncio.create_task()` function.

```python
import asyncio

async def main_async_function():
    print("Starting main function")
    task1 = asyncio.create_task(my_async_function1())
    task2 = asyncio.create_task(my_async_function2())
    result1 = await task1
    result2 = await task2
    print("Done with main function")
    return result1, result2

async def my_async_function1():
    print("Hello from my async function 1")
    await asyncio.sleep(3)
    print("Done with async function 1")
    return "my_async_function1 result"

async def my_async_function2():
    print("Hello from my async function 2")
    await asyncio.sleep(2)
    print("Done with async function 2")
    return "my_async_function2 result"

result = asyncio.run(main_async_function())
print(result)

# Starting main function
# Hello from my async function 1
# Hello from my async function 2
# Done with async function 2
# Done with async function 1
# Done with main function
# ('my_async_function1 result', 'my_async_function2 result')
```

### Don't wait

If you don't want to access the result of an `async` function and you don't care
about when it completes, then you don't need to use the `await` keyword.

```python
import asyncio

async def main_async_function():
    print("Starting main function")
    task1 = asyncio.create_task(my_async_function1())
    task2 = asyncio.create_task(my_async_function2())
    print("main function doing other work")
    await asyncio.sleep(3)
    print("Done with main function")

async def my_async_function1():
    print("Hello from my async function 1")
    await asyncio.sleep(2)
    print("Done with async function 1")

async def my_async_function2():
    print("Hello from my async function 2")
    await asyncio.sleep(1)
    print("Done with async function 2")

asyncio.run(main_async_function())

```

```python
# Starting main function
# main function doing other work
# Hello from my async function 1
# Hello from my async function 2
# Done with async function 2
# Done with async function 1
# Done with main function
```
