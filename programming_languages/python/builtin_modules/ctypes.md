# The `ctypes` Library

One common library for interfacing Python with C shared libraries is the
`ctype` library.

## C Data Types in `ctypes`

The `ctypes` library provides the following C compatible data types:

1. **Integer Types**: `c_int`, `c_long`, `c_short`, `c_longlong` and (unsigned versions) `c_uint`, `c_ulong`, `c_ushort`, `c_ulonglong`.

2. **Boolean Type**: `c_bool`.

3. **Floating Point Types**: `c_float`, `c_double`.

4. **Character Types**: `c_char` (single character) and `c_wchar` (wide character).

5. **Strings**: `c_char_p`, `c_wchar_p`: Pointers to null-terminated character arrays.

6. **Arrays**: `type * length` (e.g., `c_int * 5` for an array of five integers).

7. **Structures and Unions**: `Structure`, `Union`.

8. **Pointers**: `POINTER(type)`: Defines a pointer to a specified type.

9. **Void Pointer**: `c_void_p`: A generic pointer.

10. **Function Pointers**: `CFUNCTYPE`: Creates C callable function pointers from Python functions.

## Getting and Setting Data Type Values

In Python, scalar data types like integers and floats are **immutable**. Once a
Python integer is created, its value cannot be changed. If you assign a new
value to a variable that holds an integer, Python creates a **new object** in
memory and assigns that object to the variable.

```{python}
x = 42
print(hex(id(x)))  # Memory address of the Python integer object

x = 100  # A new Python object is created for 100, `x` points to this new object
print(hex(id(x)))  # New memory address for the new Python object
```

In contrast, `ctypes` scalar variables (such as `c_int`, `c_float`, etc.) are
**mutable**. The value stored in the underlying C memory can be modified
without creating a new object, using the `value` attribute.

```{python}
from ctypes import c_int, addressof

# Create a python object containing a `ctypes` variable
# pointing to a memory location holding the value 10
i = c_int(100000)

print(i.value) # Print the value actual C data
print(hex(id(i))) # Print the address of the python object
print(hex(addressof(i))) # Print the address of the actual C data

i.value = 200000  # Modify the value in the existing C memory
print(i.value)  # The value is updated
print(hex(addressof(i)))  # The memory address remains the same
```

## Working With Strings

In `ctypes`, there are two string types: `c_char_p` for byte strings and
`c_wchar_p` for wide-character (Unicode) strings.

When creating string variables in `ctypes`, it's important to remember that:

- **`c_char_p`** expects a **byte string** (`b"string"`) in Python, not a normal string (`"string"`).

- **`c_wchar_p`** expects a **wide string** (`u"string"` in Python 2 or `"string"` in Python 3).

```{python}
from ctypes import c_char_p, c_wchar_p

# Create a ctypes string (byte string)
s = c_char_p(b"Hello!")

# Access and print the value
print(s.value)  # Outputs: b'Hello!'

# Create a wide character string
ws = c_wchar_p("Hello!")

# Access and print the value
print(ws.value)  # Outputs: 'Hello!'
```

## Working With Pointers

In C, pointers are used to reference memory locations. In `ctypes`, you can
work with pointers using two main approaches:

- `POINTER(type)`: Defines a **pointer type** that can point to any
  variable of the specified `ctypes` type.

- `pointer()`: Creates a pointer to an existing `ctypes` variable.

### Using `POINTER(type)`

`POINTER(type)` is used to declare a pointer type that can later point to any
variable of the specified `type`.

```{python}
from ctypes import c_int, POINTER

# Define a pointer type that can point to an integer (c_int)
IntPointer = POINTER(c_int)

# Create an integer
i = c_int(42)

# Create a pointer to the c_int variable
p = IntPointer(i)

# Access and print the value via the pointer
print(p.contents.value)  # Outputs: 42

# Modify the value through the pointer
p.contents.value = 100
print(i.value)  # Outputs: 100
```

### Using `pointer()`

The `pointer()` function creates a pointer to an existing `ctypes` object
directly.

```{python}
from ctypes import c_int, pointer

# Create a ctypes integer
i = c_int(42)

# Create a pointer to the c_int variable using pointer()
p = pointer(i)

# Access and print the value via the pointer
print(p.contents.value)  # Outputs: 42

# Modify the value through the pointer
p.contents.value = 100
print(i.value)  # Outputs: 100
```

## Working with Arrays

In `ctypes`, arrays are defined by multiplying a data type by a length (e.g.,
`c_int * 5` for an array of five integers). These arrays are stored
contiguously in memory, similar to C arrays.

```{python}
from ctypes import c_int

# Create a one-dimensional array of 5 integers
IntArray = c_int * 5
arr = IntArray(1, 2, 3, 4, 5)

# Access and print array elements
for i in arr:
    print(i)  # Outputs: 1, 2, 3, 4, 5

# You can modify array elements by accessing them via index
arr[2] = 10
print(arr[2])  # Outputs: 10
```

You can also create multi-dimensional arrays by nesting array types.

```{python}
from ctypes import c_int

# Define a 3x3 two-dimensional array of integers
IntArray2D = (c_int * 3) * 3
arr_2d = IntArray2D(
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# Access and print array elements
for row in arr_2d:
    for element in row:
        print(element, end=' ')
    print()  # Outputs the 3x3 matrix

# You can access individual elements using standard indexing for
# multidimensional arrays
print(arr_2d[1][1])  # Outputs: 5
arr_2d[2][2] = 10    # Modify an element
print(arr_2d[2][2])  # Outputs: 10
```

## Working With Structures and Unions

`ctypes` allows defining C-style **structures** and **unions**, which group
different fields into a single object.

```{python}
from ctypes import Structure, c_int, c_float

# Define a Point structure
class Point(Structure):
    _fields_ = [("x", c_int), ("y", c_float)]

# Create an instance of the structure
p = Point(10, 20.5)

# Access and print the structure fields
print(p.x, p.y)  # Outputs: 10 20.5
```

## Working With Function Pointers

A **function pointer** is used when interfacing with C functions take function
pointers as arguments to allow callbacks.

```{python}
from ctypes import CFUNCTYPE, c_int

# Define a callback function type that takes two integers and returns an
# integer
CALLBACK_TYPE = CFUNCTYPE(c_int, c_int, c_int)

# Define a Python function that matches the callback signature
def add_func(a, b):
    print(f"Adding {a} + {b}")
    return a + b

# Create a function pointer to the Python function
callback = CALLBACK_TYPE(add_func)

# Now you can pass this `callback` to a C function that expects this kind of
# function pointer
```

# Examples

## Basic Example

1. Create a C library:

```{c}
// math_functions.c
#include <stdio.h>

double add(double a, double b) {
    return a + b;
}
```

2. Compile it into a shared library:

```{sh}
gcc -shared -fPIC math_function.c -o math_function.so
```

3. Use `ctypes` in Python:

```{python}
# math_functions.py
from ctypes import CDLL, c_double

# Load the shared library
lib = CDLL('./math_function.so')

# Set argument and return types of the C function
lib.add.argtypes = [c_double, c_double]
lib.add.restype = c_double

# Call the functions
result_add = lib.add(10.5, 5.5)

print("Add:", result_add)
```

## Example Using Strings

```{c}
// string_functions.c
#include <string.h>

void to_uppercase(char* input, char* output) {
    int i;
    for (i = 0; input[i]; i++) {
        output[i] = toupper(input[i]);
    }
    output[i] = '\0';
}
```

```{python}
from ctypes import CDLL, c_char_p, create_string_buffer

# Load the library
lib = CDLL('./libstring_functions.so')

# Set argument types
lib.to_uppercase.argtypes = [c_char_p, c_char_p]

# Prepare input and output buffers
input_str = b'Hello World'
output_buffer = create_string_buffer(len(input_str) + 1)  # +1 for null terminator

# Call the function
lib.to_uppercase(input_str, output_buffer)

print("Output:", output_buffer.value.decode())
```

The `create_string_buffer` function is used to allocate a buffer for the
output. This buffer acts as an array of characters that the C function can
safely modify.

## Example Using Pointers and Arrays

```{c}
// array_functions.c
#include <stdio.h>

void scale_array(int* arr, int count, int factor) {
    for (int i = 0; i < count; i++) {
        arr[i] *= factor;
    }
}
```

```{python}
from ctypes import CDLL, POINTER, c_int

lib = CDLL('./libarray_functions.so')

# Define the function arguments and return type
lib.scale_array.argtypes = [POINTER(c_int), c_int, c_int]
lib.scale_array.restype = None

# Create an array of integers
array_type = c_int * 5
numbers = array_type(1, 2, 3, 4, 5)

# Call the C function
lib.scale_array(numbers, len(numbers), 3)

# Display scaled array
print("Scaled array:", list(numbers))
```

## Example With Structures and Unions

```{c}
// data_structures.c
#include <stdio.h>

typedef struct {
    int id;
    double balance;
} Account;

void display_account(Account* acc) {
    printf("Account ID: %d, Balance: %.2f\n", acc->id, acc->balance);
}
```

```{python}
from ctypes import Structure, c_int, c_double, POINTER, CDLL

class Account(Structure):
    _fields_ = [("id", c_int),
                ("balance", c_double)]

lib = CDLL('./libdata_structures.so')
lib.display_account.argtypes = [POINTER(Account)]
lib.display_account.restype = None

# Create an instance of Account
acc = Account(id=12345, balance=1000.75)

# Use the function
lib.display_account(acc)
```

## Function Pointers

Callbacks allow passing Python functions to C code as function pointers.

```{c}
// callback_example.c
#include <stdio.h>

// Define a function pointer type
typedef int (*CallbackFunc)(int, int);

void process_numbers(int a, int b, CallbackFunc callback) {
    int result = callback(a, b);
    printf("Result from callback: %d\n", result);
}
```

```{python}
from ctypes import CDLL, CFUNCTYPE, c_int

# Load the shared library
lib = CDLL('./libcallback_example.so')

# Define the callback function type
CALLBACKFUNC = CFUNCTYPE(c_int, c_int, c_int)

# Define the argument and return types
lib.process_numbers.argtypes = [c_int, c_int, CALLBACKFUNC]
lib.process_numbers.restype = None

# Define a Python callback function
@CALLBACKFUNC
def add(a, b):
    return a + b

# Call the C function with the callback
lib.process_numbers(5, 3, add)
```
