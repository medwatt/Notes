# Typing

The `typing` module in Python provides support for type hints, allowing for
more readable code and better static analysis.

## Examples

### Simple Variables

```{python}
from typing import Any
from typing import Final
from typing import Optional
from typing import Union

# Built-in types
integer_var: int = 42
float_var: float = 3.14
string_var: str = "Hello, World!"
boolean_var: bool = True
bytes_var: bytes = b"bytes"

# Any type (can be of any type)
any_var: Any = "Could be anything"

# Constants should not be reassigned
PI: Final[float] = 3.14159

# Optional type (can be None)
optional_str: Optional[str] = None

# Union type (either int or str)
int_or_str: Union[int, str] = "Hello"
```

### Literal Types

```{python}
from typing import Literal

def set_status(status: Literal["open", "closed"]) -> None:
    print(f"Status set to {status}")

# Usage
set_status("open")
```

### Generic Types and Collections

```{python}
from typing import List, Tuple, Set, Dict

# Lists
names: List[str] = ["Alice", "Bob", "Charlie"]

# Nested lists
list_of_lists: List[List[int]] = [[1, 2], [3, 4]]

# Tuples
coordinates: Tuple[float, float] = (10.0, 20.0)

# Sets
unique_ids: Set[int] = {1, 2, 3}

# Dictionaries
user_info: Dict[str, int] = {"age": 30, "score": 100}
```

### TypedDict

A `TypedDict` allows you to define dictionaries where you specify the types for
the values associated with each key. A `TypedDict` is useful when you need a
dictionary with a specific structure and want type hints for better code
analysis and error detection.

```{python}
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
    active: bool

user: User = {"name": "Alice", "age": 30, "active": True}
```

### Enum

```{python}
from enum import Enum
from typing import Literal

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

def paint(color: Color) -> None:
    print(f"Painting with color {color.name}")

# Usage
paint(Color.RED)
```

### Annotating Classes

```{python}
from typing import List

class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

# Usage
point: Point = Point(1.0, 2.0)
```

### Iterables, Sequences, and Iterators

```{python}
from typing import Iterable, Sequence, Iterator

def process_items(items: Iterable[int]) -> None:
    for item in items:
        print(item)

# Usage with list, tuple
def first_item(sequence: Sequence[str]) -> str:
    return sequence[0]

def generate_numbers() -> Iterator[int]:
    for i in range(5):
        yield i

# Usage
process_items([1, 2, 3])
first = first_item(["apple", "banana"])
numbers: Iterator[int] = generate_numbers()
```

### Callable

```{python}
from typing import Callable

# A function that takes two ints and returns a float
Operation = Callable[[int, int], float]

def add(a: int, b: int) -> float:
    return float(a + b)

def operate(a: int, b: int, func: Operation) -> float:
    return func(a, b)

# Usage
result: float = operate(5, 3, add)
```

### TypeAlias

```{python}
from typing import List, TypeAlias

Vector: TypeAlias = List[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# Usage
vec: Vector = [1.0, 2.0, 3.0]
scaled_vec = scale(2.0, vec)
```

### NewType

```{python}
from typing import NewType

UserId = NewType('UserId', int)

def get_user_name(user_id: UserId) -> str:
    # Implementation here
    return "User Name"

# Usage
user_id = UserId(524313)
user_name: str = get_user_name(user_id)
```

### Generic

A generic allows you to write flexible and reusable code components that can
operate with various data types while still being type-checked.

```{python}
from typing import TypeVar, List

T = TypeVar('T')  # Declare type variable

def first_element(items: List[T]) -> T:
    return items[0]  # Return the first element of a list

# This function can now handle lists of any type
print(first_element([1, 2, 3]))  # Output: 1
print(first_element(["apple", "banana", "cherry"]))  # Output: apple
```

### External Modules

```{python}
import numpy as np
from numpy.typing import NDArray
from typing import Any

# 1D array of floats
array_1d: NDArray[np.float64] = np.array([1.0, 2.0, 3.0])

# Function accepting a 1D array of floats
def process_1d_array(arr: NDArray[np.float64]) -> None:
    print(arr)


# 2D array of integers
array_2d: NDArray[np.int_] = np.array([[1, 2], [3, 4]])

# Function accepting a 2D array of integers
def process_2d_array(arr: NDArray[np.int_]) -> None:
    print(arr)
```

