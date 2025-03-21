# Introduction to Asynchronous Programming

## Synchronous vs Asynchronous Programming

In **synchronous programming**, tasks are executed sequentially. A task must
complete before the next one begins. This means the CPU can spend a significant
amount of time waiting, especially when dealing with I/O-bound operations, such
as file reads or network requests.

In contrast, **asynchronous programming** allows tasks to "pause" while waiting
for something to complete. The waiting tasks yield control back to the program,
allowing the program to handle other operations. This improves efficiency and
is especially useful in I/O-bound or high-concurrency scenarios.

## Multithreading vs Asynchronous Programming

Multithreading and asynchronous programming are both ways to perform multiple
tasks concurrently, but they operate differently.

**Multithreading** spreads tasks across multiple threads within a single
process, and it is the operating system's duty to manage the switching between
threads.

**Asynchronous programming** handles multiple tasks in a single thread, and it
is up to the programmer to manage the points at which control is yielded so
that the program can perform other tasks.

## Subroutines vs Coroutines

In synchronous programming, **subroutines** represent the basic units of work
(like functions). When a subroutine is called, the program follows the typical
function call stack: one function calls another, and control moves down the
stack until the function completes.

In asynchronous programming, **coroutines** replace subroutines as the
fundamental unit of work. Coroutines are special types of functions that can
pause execution (using the `await` keyword) to let other tasks run and then
resume execution later.

## The Event Loop

In synchronous code, a **call stack** is used to manage the sequence of
function calls. In asynchronous code, the **event loop** takes on this role.
The event loop is responsible for managing the tasks and deciding which one
should run next. When a coroutine yields control by encountering an `await`
statement, the event loop can switch to another task that is ready to run.

The event loop ensures that only one coroutine is running at a time, but
multiple coroutines can be in a "paused" state, waiting for some I/O to
complete. When the waiting operation is done, the event loop resumes the
coroutine from the point it was paused.

# Introduction to the `asyncio` Module

Python's `asyncio` module provides the building blocks for asynchronous
programming, including the event loop, coroutines, tasks, and more.

## Examples

### Using `async` and `await`

- Use `async def` to define a coroutine.

- Inside the coroutine, use the `await` keyword to pause execution and
  yield control back to the event loop. Execution of the coroutine will be
  resumed when the awaited operation completes.

- Objects that can be used in an `await` expression are called **awaitables**.

```{python}
import asyncio

async def main_async_function():
    print("Starting main function")
    result1 = await my_async_function1()
    result2 = await my_async_function2()
    print("Done with main function")
    return result1, result2

async def my_async_function1():
    print("Hello from my async function 1")
    await asyncio.sleep(3)  # Simulating an I/O-bound operation
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

-  Use the `asyncio.run` function to run an asynchronous function in a
   region running synchronous code.

- In the above example, the `asyncio.run` function creates an event loop
  and schedules `main_async_function` to be run.

- `main_async_function` runs until `my_async_function1` is called
  using the `await` keyword. This causes the execution of
  `main_async_function` to be suspended until `my_async_function1`
  completes.

- Even though `my_async_function1` also has an `await` keyword and
  control is indeed returned to the event loop to allow other tasks to run,
  but because there's only one task to run (`main_async_function`), and
  this task is waiting for the completion of `my_async_function1`,
  `my_async_function2` runs only after `my_async_function1` finishes.

### Using `asyncio.gather`

- `asyncio.gather` allows you to run multiple coroutines concurrently and
collect their results.

    ```{python}
    results = await asyncio.gather(coroutine1(), coroutine2(), ...)
    ```

- With `asyncio.gather`, we can modify the previous example to allow
  `my_async_function2` to run while `my_async_function1` is blocking.

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

### Using `asyncio.create_task`

- Another way to achieve the same goal of running `my_async_function1`
  and `my_async_function2` concurrently is through the use of the
  `asyncio.create_task` function.

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

- When `asyncio.create_task` is called, it schedules a coroutine for
  execution and immediately returns a **Task** object. This Task object is a
  subclass of a **Future** and represents a placeholder for the result of the
  coroutine, which will be available at some point in the future.

- In this case, `task1` and `task2` are **Future** objects, as they
  represent work that will be completed in the future. These Futures will
  contain the results of `my_async_function1` and `my_async_function2` once
  those functions finish execution.

- A Future can be awaited to retrieve a result. The `await task1` and
  `await task2` statements tell Python to wait until the Future is resolved
  and its result is ready. This is the case in the above example.

- A Future can be ignored if we don't need its result or care when the
  scheduled task completes. This is the case in the example below where no
  `await` keyword is used after the tasks are created. Despite this, the
  tasks are still scheduled to run. When the `await asyncio.sleep(3)` is
  reached, the event loop begins pauses the execution of
  `main_async_function` and begins the execution of `task1` and then
  `task2`.

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


# Starting main function
# main function doing other work
# Hello from my async function 1
# Hello from my async function 2
# Done with async function 2
# Done with async function 1
# Done with main function
```

# Asynchronous Context Managers and Asynchronous Iterators

## Asynchronous Context Managers

Just like synchronous context managers in Python help manage resources by
implementing `__enter__` and `__exit__` methods, asynchronous context
managers help manage resources in an asynchronous environment. They use
`__aenter__` and `__aexit__` methods, which are coroutine functions.

Asynchronous context managers are useful for managing asynchronous operations
like opening and closing database connections or file streams without blocking
the main application flow.

### Example

Consider an asynchronous file reader that opens a file, reads its contents, and
then automatically closes the file, even if an exception occurs.

```{python}
import asyncio

class AsyncFileReader:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    async def __aenter__(self):
        # Open the file in a separate thread to prevent blocking the async loop
        self.file = await asyncio.to_thread(open, self.filename, 'r')
        return self.file

    async def __aexit__(self, exc_type, exc, tb):
        # Close the file in a separate thread to ensure the async loop is not blocked
        await asyncio.to_thread(self.file.close)

async def read_file():
    # Use the asynchronous context manager to handle the file
    async with AsyncFileReader('example.txt') as f:
        # Read the file's contents in a separate thread and print them
        contents = await asyncio.to_thread(f.read)
        print(contents)

asyncio.run(read_file())
```

- The function `asyncio.to_thread` is used to run blocking I/O-bound
  operations asynchronously by executing them in a separate thread. This avoids
  blocking the main event loop. The function is particularly useful for
  integrating synchronous code (that performs I/O or other blocking operations)
  into an asynchronous application without causing performance bottlenecks.

## Asynchronous Iterators

Asynchronous iterators are objects that implement an asynchronous
`__aiter__()` method to return an asynchronous iterator and an
`__anext__()` method that is a coroutine and yields values asynchronously.
This is particularly useful when iterating over data that is received
incrementally from an asynchronous source, like network data or large file
reads.

### Example

Consider an asynchronous iterator that retrieves messages from a server.

```{python}
import asyncio

class AsyncMessageReader:
    def __init__(self, messages):
        self.messages = messages

    def __aiter__(self):
        return self

    async def __anext__(self):
        if not self.messages:
            raise StopAsyncIteration
        return await asyncio.sleep(1, self.messages.pop(0))

async def process_messages():
    async for message in AsyncMessageReader(['Hello', 'World', 'Async', 'Python']):
        print(message)

asyncio.run(process_messages())
```

