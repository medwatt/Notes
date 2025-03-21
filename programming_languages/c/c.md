# Introduction

## Comments

```cpp
// This is a single line comment, supported from C99 onwards.

/* This is a multi-line comment that can
also be used as a single line comment. */
```

## Data Types

The C standard specifies minimum sizes for the basic data types. The exact
sizes depend on the compiler and architecture of the system. The table below
shows only typical values. The actual range and limits of these types are
defined in the `<limits.h>` and `<float.h>` headers.


| Data Type | Meaning               | Size (in Bytes) |
| --        | --                    | --              |
| `char`    | Character             | 1               |
| `int`     | Integer               | 2          |
| `float`   | Floating-point        | 4               |
| `double`  | Double Floating-point | 8               |


C provides modifiers such as `short` or `long`, and `signed` or
`unsigned` to alter the basic data types.

- For numeric types, the default is `signed`.

- `int` can be omitted when using modifiers like `short` or `long`.
  For example, use `long var` instead of `long int var`.

### Integer Types

Integer literals in C can be represented in different bases (decimal, octal,
and hexadecimal), each indicated by specific prefixes:

```cpp
int d = 42;    // Decimal constant (base 10)
int o = 052;   // Octal constant (base 8, prefix '0')
int x = 0xAF;  // Hexadecimal constant (base 16, prefix '0x')
```

Suffixes, `U` for unsigned and `L` for long, must also be specified to
ensure that the integer literal is treated appropriately by the compiler:

```{cpp}
unsigned long ulNum = 4294967295UL; // Treated as an unsigned long
```

Since C99, `long long` and `unsigned long long` are also supported for very
large literals:

```{cpp}
long long llNum = 9223372036854775807LL; // Large signed integer
```

The C99 standard also introduced `<stdint.h>`, which defines fixed-width
integers. These types ensure precise width requirements across different
platforms:

```{cpp}
uint32_t u32 = 32;   // Unsigned 32-bit integer
uint8_t u8 = 255;    // Unsigned 8-bit integer
int64_t i64 = -65;   // Signed 64-bit integer
```

### Boolean Type

C89 does not have a built-in Boolean type. One way to work around this
limitation is to use macros:

```cpp
#define BOOL int
#define TRUE 1
#define FALSE 0
```

This method uses `#define` to create integer constants (`TRUE` as 1 and
`FALSE` as 0) and defines `BOOL` as an alias for `int`. However, these
are merely integer aliases and not true Boolean types. As a result, it is
possible to unintentionally assign any integer value to a `BOOL` variable,
without receiving compiler warnings, potentially leading to logical errors in
the program.

C99 addresses this by introducing the `_Bool` type, which strictly accepts
`0` (false) and `1` (true). C99 also provides a new header `<stdbool.h>`
that provides a macro, `bool`, that stands for `_Bool` and macros named
`true` and `false` which stand for 1 and 0, respectively.

```{cpp}
#include <stdbool.h>

bool flag = true;  // flag is of type _Bool, strictly Boolean
```

### Floating Point Types

C has three floating point types: `float`, `double`, and `long double`. A
floating point constant that does not end with `f` is considered a
`double`.

```cpp
float f = 0.314f;        // Suffix 'f' or 'F' indicates the type float
double d = 0.314;        // No suffix indicates double
long double ld = 0.314l; // Suffix 'l' or 'L' indicates long double
double sd = 1.2e3;       // Scientific notation is typically used for doubles
```

## C Operators

### Arithmetic Operators

- Basic Arithmetic Operators: These are used for simple mathematical
  calculations.

    ```{cpp}
    int a = 20, b = 4;
    printf("%d \n", a + b);  // Adds a and b: 24
    printf("%d \n", a - b);  // Subtracts b from a: 16
    printf("%d \n", a * b);  // Multiplies a and b: 80
    printf("%d \n", a / b);  // Divides a by b: 5 (integer division)
    ```

- The division operator (`/`) behaves differently based on the data
  types of the operands.

    ```{cpp}
    int intResult1 = 7 / 3;         // Integer division: results in 2, remainder discarded
    int intResult2 = 7.0 / 3;       // Floating-point division, but casts to int: results in 2
    double doubleResult1 = 7.0 / 3; // Floating-point division: results in approximately 2.33
    double doubleResult2 = 7 / 3;   // Integer division first, converted to double: results in 2.0
    ```

- Modulus Operations:

    - `%` Operator: Used for integers to find the remainder after
      division.

    - `fmod` Function: Used for floating-point numbers to perform
      modulus operations.

    ```{cpp}
    printf("%d \n", 5 % 3);             // Remainder of 5 divided by 3: 2
    printf("%.1f \n", fmod(20.5, 4.2)); // Outputs the remainder of 20.5 divided by 4.2
    ```

- The increment (`++`) and decrement (`--`) operators modify the value
  of the variable they are applied to directly, eliminating the need for an
  explicit assignment operator.

    ```cpp
    int a = 20;
    printf("%d \n", --a); // Decrement a before using its value: outputs 19
    printf("%d \n", a--); // Use a's current value, then decrement: outputs 19, a becomes 18
    printf("%d \n", ++a); // Increment a before using its value: outputs 19
    printf("%d \n", a++); // Use a's current value, then increment: outputs 19, a becomes 20
    ```

### Relational Operators

Relational operators check if a specific relation between two operands is true.
The result is evaluated to `1` (which means true) or `0` (which means false).

```cpp
int a = 20, b = 4;
printf( "%d \n", a == b ); // 0
printf( "%d \n", a != b ); // 1
printf( "%d \n", a > b  ); // 1
printf( "%d \n", a < b  ); // 0
printf( "%d \n", a >= b ); // 1
printf( "%d \n", a <= b ); // 0
```

### Logical Operators

Logical operators evaluate the truthiness of conditions involving two or more
operands. These operators include `&&` (logical AND), `||` (logical OR),
and `!` (logical NOT). The result of a logical operation is either `1`
(true) or `0` (false), similar to relational operators.

```cpp
int a = 5, b = 10, c = 20;

printf( "%d \n", c > b && b > a    ); // 1
printf( "%d \n", a > b || c > b    ); // 1
printf( "%d \n", !(c > b && a > b) ); // 1
```

### Bitwise Operators

Bitwise operators can be used to perform bit level operations on the operands.
All supported bitwise operators are listed below:

- `&` - bitwise AND
- `|` - bitwise inclusive OR
- `^` - bitwise exclusive OR (XOR)
- `~` - bitwise not (one's complement)
- `<<` - logical left shift
- `>>` - logical right shift

```cpp
unsigned int a = 29;       //   29 = 0001 1101
unsigned int b = 48;       //   48 = 0011 0000

printf( "%d \n", a & b  ); //   32 = 0001 0000
printf( "%d \n", a | b  ); //   61 = 0011 1101
printf( "%d \n", a ^ b  ); //   45 = 0010 1101
printf( "%d \n",   ~a   ); //  -30 = 1110 0010
printf( "%d \n", a << 2 ); //  116 = 0111 0100
printf( "%d \n", a >> 2 ); //    7 = 0000 0111
```

#### Masking

Masking refers to the process of extracting the desired bits from, or
transforming the desired bits in, a variable by using logical bitwise
operations.

A mask defines which bits you want to keep, and which bits you want to clear.
This is accomplished by doing:

- Bitwise ANDing in order to extract a subset of the bits in the value
- Bitwise ORing in order to set a subset of the bits in the value
- Bitwise XORing in order to toggle a subset of the bits in the value

```cpp
uint8_t val = 0x3B;                 // 0011 1011    --> b7 b6 ... b0

printf( "%X \n", val | (1 << 6  )); // set b6         --> 0x7B = 0111 1011
printf( "%X \n", val ^ (1 << 2  )); // toggle b2      --> 0x7B = 0011 1111
printf( "%X \n", val & ~(1 << 4 )); // clear b4       --> 0x2B = 0010 1111
printf( "%X \n", val >> 4       );  // select b7...b4 --> 0x03 = 0000 0011
printf( "%X \n", val & 0xF      );  // select b3...b0 --> 0x0B = 0000 1010
```

### Comma Operator

The comma operator first evaluates its left operand and discards its value. It
then evaluates its right operand, and the value of this rightmost operand
becomes the result of the operation.

```cpp
int x = 42, y = 42;

printf("%i\n", (++x, y)); // Outputs "42"
//           ^     ^ this is a comma operator
//           this is a separator
```

The comma operator is often used in the initialization section as well as in
the updating section of a `for` loop.

```cpp
for(int sumk = 1, k = 1; k < 10; k++, sumk += k)
    printf("\%5d\%5d\n", k, sumk);
```

### Cast Operator

The cast operator in C explicitly converts the value of an expression to a
specified type, ensuring operations between different data types are handled
correctly.

```cpp
int x = 3, y = 4;
printf("%f\n", (double)x / y); // Outputs "0.750000"
```

Here, the value of `x` is converted to a `double`, promoting the division
to a floating-point division.

### Pointer Operators

- Address-of operator: The unary `&` operator returns the address of an
  object in memory.

    ```cpp
    int var = 10;
    int *ptr = &var; // ptr now holds the address of var
    ```

- Dereference operator: The unary `*` operator dereferences a
  pointer.

    ```cpp
    int value = 5;
    int *ptr = &value;
    int dereferencedValue = *ptr; // dereferencedValue is now 5
    *ptr = 10; // value is now 10
    ```

### Access Operators

The dot (`.`) and arrow (`->`) operators are used for accessing members
of a structure (`struct`).

```{cpp}
struct MyStruct {
    int x;
    int y;
};

// Creating a struct instance and a pointer to it
struct MyStruct myObject;
struct MyStruct *p = &myObject;

// Assigning values to struct members
myObject.x = 42;
myObject.y = 123;

// Using the dot operator to access members directly
printf(".x = %i, .y = %i\n", myObject.x, myObject.y);

// Accessing the same members via a pointer using the arrow operator
printf("->x = %i, ->y = %i\n", p->x, p->y);

// Equivalent access using the dot operator with dereference
printf(".x = %i, .y = %i\n", (*p).x, (*p).y);
```

- The dot operator is used directly with `struct` instances.

- The arrow operator is syntactic sugar for dereferencing followed by member
  access. That is, instead of writing `(*p).x`, we can write `p->x`.

# Control Structures

## Conditional Statements

### If Statements

```cpp
int num = 45;

if (num < 25) {
    printf( "%d < 25", num );
} else if (num < 50) {
    printf( "%d < 50", num );
} else {
    printf( "%d >= 50", num );
}
```

- The parentheses around the condition expression are mandatory.

- If the `if` or `else` statement contains only 1 statement (such as
  in the example above), then the curly brackets can be omitted.

### Ternary Operator

The statement `a = b ? c : d;` is equivalent to:

```cpp
if (b)
    a = c;
else
    a = d
```

### Switch Statements

```cpp
int a = 1;

switch (a) {
    case 1:
        printf("a is 1");
        break;
    case 2:
        printf("a is 2");
        break;
    default:
        printf("a is neither 1 nor 2");
        break;
}
```

- A `break` statement is necessary to exit a switch block. Without a
  `break`, the execution continues through subsequent case statements until a
  `break` is found or the switch block ends even when the switch values do
  not match the switch expression.

- The GCC compiler supports case ranges like `case 0 ... 9`, but
  this is not in standard C, where you must list each case individually.

## Loops

### For Loops

For loops provide a way to execute a block of code repeatedly with a counter.

```cpp
for (int i = 0; i < 10; i++){
    printf( "%d ", i);
}
```

- In C99, the loop index can be declared inside the `for` loop (as shown
  above). In older versions of C, the loop index has to be declared outside
  the for loop.

- For an infinite loop, use `for (;;;)`.

### While Loops

While loops execute a block of code as long as a specified condition remains
true.

```cpp
int i = 0;
while (i < 10) {
    printf( "%d ", i++);
}
```

### Do ... While Loops

Do...while loops ensure that the code block is executed at least once before
the condition is tested:

```cpp
int i = 0;

do {
    printf( "%d ", i++);
} while (i < 10)
```

## Controlling Loop Execution

### Break Statement

The `break` statement immediately terminates the loop in which it is placed,
transferring control to the statement following the loop:

```cpp
int i = 1;

while (1) {
    printf( "%d ", i++);
    if (i > 5) break;
}
```

### Continue Statement

The `continue` statement skips the current iteration of the loop and proceeds
with the next iteration:

```cpp
for (int i=1; i<=10; i++){
    if (i % 2 == 0) continue;
    printf( "%d ", i);
}
```

### Goto Statement

The `goto` statement provides a way to jump to another part of the program.
However, its use is generally discouraged as it can make code difficult to
understand and maintain:

```cpp
for (int i = 0; i < 10; i++) {
    if (i == 5) {
        goto cleanup;  // Jumps to the cleanup label
    }
    printf("%d ", i);
}

cleanup:
printf("Cleanup code runs here.\n");
```

# Pointers

A pointer variable is a variable that holds the memory address of another
object, instead of some value like a regular variable.

A pointer is declared much like any other variable, except an asterisk (`*`)
is placed between the type and the name of the variable.

Given a type `T`, the type `T*` or `T *` denotes a pointer to a variable
of type `T`. For example, `int *ptr` or `int *ptr` defines `ptr` as a
variable that holds the address of integer objects.

The style choice between the two forms depends on the adopted coding standards:

- **`T* ptr`**: This notation emphasizes that `ptr` is of type
  "pointer to T".

- **`T *ptr`**: This style places the asterisk next to the variable
  name, which can make it clearer that `ptr` is a pointer. This approach is
  useful when declaring multiple pointers in the same statement. For
  example, `T *ptr, *ptr2;` clearly declares both `ptr` and `ptr2` as
  pointers.

It is important to note the difference in the meaning of `*` in different
contexts.

- In declaration statements, `int *ptr`, the `*` simply instructs
  the compiler to treat `ptr` as an integer pointer.

- In assignment statements, `*ptr = 5`, the `*` is used to refer to
  the content of the location `ptr` is pointing to.

Like any other variable, pointers have a specific type. For instance, we cannot
assign the address of a `short int` to a pointer of type `long int`.

Although we cannot declare a variable to be of type `void`, we can declare a
pointer to be of type `void*`. Void pointers hold addresses without type
restrictions, making them ideal for generic programming. They allow writing
functions that work with any data type. Before dereferencing, the void pointer
must be cast to a specific type pointer. However, since the compiler is unable
to check the correctness of such references, the use of `void*` pointers is
strongly discouraged.

## Pointer Arithmetic

There are four arithmetic operators that can be used on pointers: `++`,
`--`, `+`, and `-`. These work the same way as we would expect except
that the value that gets added (subtracted) to (from) the pointer depends on
the data type of the object that the pointer points to. That is, if `T *ptr =
&x`, then `ptr + 2` actually means `ptr + 2*sizeof(T)`.

The `++` and `--` operators have greater precedence than `*`. That is,
`*ptr++` is equivalent to `*(ptr++)` and not `(*ptr)++`.

## Constant Pointers

- Pointer to a `const int`: The pointer can point to different integers
  but the integer's value cannot be changed through this pointer.

    ```cpp
    int b;
    const int *p = &b;
    *p = 100; // Compiler Error
    ```

- `const` pointer to `int`: The integer pointed to by `p` can be
  changed through this pointer, but `p` itself cannot be reassigned to point
  to another integer.

    ```cpp
    int a, b;
    int* const p = &b;
    *p = 100;
    p = &a; // Compiler Error
    ```

# Functions

The structure for defining a function includes a return type, the function
name, and optionally a list of parameters:

```cpp
return_type function_name([parameter_list]) {
   // Body of the function
}
```

- **Return Type**: Every function in C89 defaults to `int` if no return
  type is specified. Since C99, explicitly stating the return type is required.
  If a function does not return a value, its type should be declared as
  `void`.

- **Parameter List**: It can be empty, or it can specify multiple
  parameters separated by commas, each with a defined type. If there are no
  parameters, the list should either be empty or contain the keyword `void`
  to indicate this explicitly.

- **Local Variables**: C89 requires that all local variables must be
  declared at the beginning of the function before any executable statements.
  C99 relaxed this rule, allowing variables to be declared throughout the
  function body, similar to C++.

To execute a function, call it using its name followed by parentheses enclosing
any arguments required by the function. The returned value can be captured or
ignored:

```{cpp}
int result = function_name(arg1, arg2);
```

## Function Prototype

A function prototype is required if the function is defined after the
`main()` function. This tells the compiler about the function's name, return
type, and parameter types.

```cpp
// Function prototype
return_type function_name([parameter_list_data_types]);

int main() {
    // Usage of the function
}

// Function definition
return_type function_name([parameter_list]) {
   // Function body
}
```

## Function Parameters

**Passing by Value**: By default, C passes all function parameters by value.
This means that a copy of the actual parameter is made, and modifications to
the parameter within the function do not affect the original variable.

**Modifying Values**: To modify the original variables or to return multiple
values via functions, use pointers:

```cpp
void modify(int *x) {
    *x = 10;  // Changes the original integer passed to the function
}
```

## Variable Arguments

In C, you can create functions that accept any number of arguments using the
`stdarg.h` library. This is useful for making flexible functions like
`printf`:

```{cpp}
#include <stdio.h>
#include <stdarg.h>

// Define a function that can take any number of arguments.
void custom_printf(const char* format, ...) {
    va_list args;                 // Declare a variable to hold the arguments.
    va_start(args, format);       // Start collecting arguments after 'format'.
    vprintf(format, args);        // Print the arguments as specified in 'format'.
    va_end(args);                 // Clean up the system's memory.
}

int main() {
    // Use the custom printf function
    custom_printf("This includes different types: %d, %f, %s\n", 10, 3.14, "example string");
    return 0;
}
```

- **`va_list`**: A type used to hold information about the variable
  arguments.

- **`va_start`**: A macro that sets up the `va_list`.

- **`va_arg`**: This macro isn't shown in the example but is used to
  access each argument in the list.

- **`va_end`**: Macro that cleans up the variable argument list.

## Function Pointers

Functions are automatically treated as pointers. This means the `&` can be
omitted when assigning a function to a pointer and the `*` when calling it
through a pointer.

```cpp
int my_function(int a, int b) {
    return 2 * a + 3 * b;
}

// Declare a function pointer and assign it directly to 'my_function'.
int (*my_pointer)(int, int) = my_function;

// Use the function pointer to call the function.
int result = my_pointer(4, 2);
printf("Result: %d\n", result);

// Function pointers can also be passed to other functions.
void call_function(int (*func)(int, int)) {
    int a = 4;
    int b = 2;
    int result = func(a, b);  // Use the function pointer 'func'.
    printf("Result: %d\n", result);
}

int main() {
    call_function(my_function);  // Pass 'my_function' directly.
    return 0;
}
```

# Arrays

## 1-dimensional Arrays

A 1-dimensional array in C is a collection of elements of the same type placed
in contiguous memory locations. They can be declared in the following ways:

- Initialization to Zero:

    ```cpp
    int A[5] = {0}; // Initializes all elements to 0.
    ```

- Partial Initialization:

    ```cpp
    int A[5] = {1, 2}; // First two elements are 1 and 2, rest are 0.
    ```

- Automatic Size Deduction:

    ```cpp
    int A[] = {1, 2, 3, 4, 5}; // Size is automatically deduced to be 5.
    ```

- Designated Initializers (C99):

    ```cpp
    int A[5] = {[0] = 1, [4] = 2}; // First element is 1, fifth is 2, others are 0.
    ```

The array name, such as `A` in the examples, is a pointer to the first
element of the array. Accessing elements can be done via `*(A+i)`, or
equivalently `A[i]`.

We can use both notations at the same time. So, if `A+i` is a pointer to the
element at index `i`, then `(A+i)[j]` is the value of the element at index
`i+j`.

To determine the number of elements in an array, divide the total size of the
array by the size of one element:

```{cpp}
int array[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
size_t length = sizeof(array) / sizeof(array[0]);
```

1D arrays can be passed to functions by passing a pointer to the first element:

```cpp
void processArray(int *array) {
    // Function body
}
```

## 2-dimensional Arrays

A multi-dimensional array can be seen as an array of arrays.

### Regular Arrays

When declaring a regular multi-dimensional array, the size of all dimensions
except the first must be specified explicitly at the time of declaration.

```{cpp}
int matrix[][3] = {
    {1, 2, 3},  // Row 0
    {4, 5, 6},  // Row 1
    {7, 8, 9}   // Row 2
};
```

A pointer to a regular 2D array, where each row contains `n` integers can be
declared as follows:

```{cpp}
int (*ptr)[3] = matrix; // Pointer to an array of three integers
```

Each `ptr + i` is a pointer to the `i-th` row of the matrix. To access the
`j-th` element of the `i-th` row:

```{cpp}
int value = (*(ptr + i))[j];

// Or equivalently
int value = ptr[i][j];
```

### Irregular Arrays

For arrays with sub-arrays of different lengths, use pointers to pointers:

```cpp
int row0[] = {1, 2, 3};
int row1[] = {4, 5, 6, 7};
int row2[] = {8, 9};
int (*B)[] = {row0, row1, row2};
int **ptr  = B;
```

### Passing 2D Arrays to Functions

Depending on the uniformity of the array's dimensions, different methods are
used:

- For regular arrays:
    ```{cpp}
    #include <stdio.h>

    void printMatrix(int rows, int cols, int array[][cols]) {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                printf("%d ", array[i][j]);
            }
            printf("\n");
        }
    }

    int main() {
        int matrix[3][3] = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        printMatrix(3, 3, matrix);
        return 0;
    }
    ```

- For irregular arrays:

    ```{cpp}
    #include <stdio.h>
    #include <stdlib.h>

    void printIrregularMatrix(int **array, int numRows, int *rowSizes) {
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < rowSizes[i]; j++) {
                printf("%d ", array[i][j]);
            }
            printf("\n");
        }
    }

    int main() {
        int *matrix[3]; // Array of pointers to int
        int rowSizes[] = {3, 4, 2}; // Sizes of each row

        matrix[0] = (int *)malloc(3 * sizeof(int));
        matrix[1] = (int *)malloc(4 * sizeof(int));
        matrix[2] = (int *)malloc(2 * sizeof(int));

        // Initialize the matrix
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < rowSizes[i]; j++) {
                matrix[i][j] = i * j; // Just an example value
            }
        }

        printIrregularMatrix(matrix, 3, rowSizes);

        // Clean up memory
        for (int i = 0; i < 3; i++) {
            free(matrix[i]);
        }

        return 0;
    }
    ```

# Strings

## String Literals

- String literals in C are sequences of characters terminated by a null
  character (`\0`) and are typically allocated in read-only memory.

    ```cpp
    char *str = "abc"; // `str` points to {'a','b','c','\0'}
    ```

- Modifying string literals results in undefined behavior, although it is
  acceptable to change the pointer itself to point to another string.

    ```cpp
    char *str = "abc";
    str[0] = 'F'; // Undefined behavior
    str = "def"; // Valid, modifies the pointer
    ```

- To prevent accidental modification of string literals, pointers should
  be declared with `const` to get a compile-time error.

    ```cpp
    const char *str = "abc";
    ```

- For modifiable strings, a character array should be initialized with a string literal.

    ```cpp
    char str[] = "abc"; // Creates a local, modifiable array
    ```


- C supports wide character strings, defined as arrays of the type
  `wchar_t`. This feature allows strings where more than 256 different
  possible characters are needed. They end with a zero-valued `wchar_t`.
  These strings are not supported by the `<string.h>` functions. Instead,
  they have their own functions, declared in `<wchar.h>`.

    ```cpp
    wchar_t *str = L"abc";
    ```

## The String Library

Three types of functions exist in the [string library](https://en.wikibooks.org/wiki/C_Programming/String_manipulation):

- the `mem` functions manipulate sequences of arbitrary characters without regard to the null character
- the `str` functions manipulate null-terminated sequences of characters
- the `strn` functions manipulate sequences of non-null characters

Commonly used functions include:

- `strlen`: Returns the length of a string excluding the null terminator.
- `strcpy` and `strncpy`: Copy strings.
- `strcat` and `strncat`: Concatenate strings.
- `strcmp` and `strncmp`: Compare two strings.
- `strchr` and `strrchr`: Search for a character in a string.

Less commonly-used functions include:

- `memchr` \- Find a byte in memory
- `memcmp` \- Compare bytes in memory
- `memcpy` \- Copy bytes in memory
- `memmove` \- Copy bytes in memory with overlapping areas
- `memset` \- Set bytes in memory
- `strcoll` \- Compare bytes according to a locale-specific collating sequence
- `strcspn` \- Get the length of a complementary substring
- `strerror` \- Get error message
- `strpbrk` \- Scan a string for a byte
- `strspn` \- Get the length of a substring
- `strstr` \- Find a substring
- `strtok` \- Split a string into tokens
- `strxfrm` \- Transform string

### Length of a String

- `strlen`: This function returns the number of bytes in the string to
  which `s` points, not including the terminating null byte.  It can only
  be used when the string is guaranteed to be null-terminated.

    ```cpp
    size_t strlen(const char *s);
    ```

### Copying Strings

- Since strings in C are represented as arrays of characters, and arrays are
  pointers, writing `s1 = s2`, where `s1` is of type `char *`, only copies the
  address of `s2` instead of the content. Note that we cannot assign to arrays
  in C.

- The `strcpy` function copies the C string pointed to by `s2` (including the
  terminating null byte) into the array pointed to by `s1`. You must ensure
  that `s1` is large enough to contain all the characters of `s2` otherwise
  `strcpy` will overwrite memory past the end of the buffer, causing a buffer
  overflow.

    ```cpp
    char *strcpy(char *restrict s1, const char *restrict s2);
    ```

### Concatenating two Strings

- `strcat`: This function appends a copy of the string pointed to by
  `s2` (including the terminating null byte) to the end of the string
  pointed to by `s1`. Before calling `strcat`, the destination must
  currently contain a null-terminated string or the first character must
  have been initialized with the null character.

    ```cpp
    char *strcpy(char *restrict s1, const char *restrict s2);
    ```

### Comparing two Strings

- `strcmp`: This function takes two strings as arguments and returns a
  value less than zero if the first is lexographically less than the
  second, a value greater than zero if the first is lexographically greater
  than the second, or zero if the two strings are equal.

    ```cpp
    int strcmp(const char *s1, const char *s2);
    ```

### String Indexing

- `strchr`: This function returns a pointer to the first occurrence of
  `c` (converted to a `char`) in the string pointed to by `s`. The
  function `strrchr` returns the last occurence.

    ```cpp
    char *strrchr(const char *s, int c);
    ```

### Converting Strings to Number

Since C99, the C library has a set of safe conversion functions that interpret
a string as a number. Their names are of the form `strtoX`, where `X` is
one of `l`, `ul`, `d`, etc to determine the target type of the
conversion.

# Standard I/O (stdio)

The C Standard Input/Output library provides functions for reading and writing
data. It includes basic operations like printing to the screen, reading user
input, and working with files. To use these functions, include the
`<stdio.h>` header.

## Basic Functions

- `printf`: Prints formatted output to `stdout`.
- `scanf`: Reads formatted input from `stdin`.
- `puts`: Writes a string to `stdout`, appending a newline.
- `gets` (deprecated): Unsafe due to potential buffer overflow.
- `fgetc`: Reads a character from a file.
- `fputc`: Writes a character to a file.
- `fgets`: Reads a string from a file.
- `fputs`: Writes a string to a file.
- `fprintf`: Like `printf`, but outputs to a file.
- `fscanf`: Like `scanf`, but reads from a file.
- `fopen`, `fclose`, `fread`, `fwrite`, `fseek`, `ftell`: File handling operations.

### `printf`

A `printf` format specifier takes this form:

```{cpp}
%[flags][width][.precision][length]specifier
```

- **Specifier**: Determines how the argument is interpreted and displayed.

    - `d` or `i`: Signed integers
    - `u`: Unsigned integers
    - `o`: Octal
    - `x` or `X`: Hexadecimal (lowercase or uppercase)
    - `f` or `F`: Decimal floating-point
    - `e` or `E`: Scientific notation (lowercase or uppercase)
    - `g` or `G`: Automatically chooses `f` or `e` (lowercase or uppercase)
    - `a` or `A`: Hexadecimal floating-point (lowercase or uppercase)
    - `c`: Single character
    - `s`: String
    - `p`: Pointer address
    - `n`: Writes number of characters printed so far into the provided integer pointer (rarely used)

- **Flags** (optional):

    - `-`: Left-justify the output within the given field width.
    - `+`: Always show the sign (`+` or `-`) for numeric types.
    - (space): Inserts a leading space for positive numbers.
    - `0`: Pads numeric output with zeros instead of spaces.
    - `#`: Alters the output form (e.g., forces a decimal point for `f`, prefix `0x` for `x`, etc.).

- **Width** (optional): A positive integer or `*`. Controls the minimum field width.

    - Example: `%5d` ensures at least 5 characters are used.
    - Using `*` reads the width from an `int` argument before the actual data argument.

- **Precision** (optional): A period (`.`) followed by a positive integer or `*`. Controls how many digits appear after the decimal point for floating-point values or the maximum characters printed for strings.

    - Example: `%.2f` prints a float with 2 decimal places.
    - Using `.*` reads the precision from an `int` argument before the data argument.

- **Length** (optional): Adjusts the type for integers or floats.

    - `h`: Short (`short int`)
    - `hh`: `signed char`
    - `l`: Long (`long int` or `double` if with `f`/`e`/`g`)
    - `ll`: Long long
    - `L`: Long double
    - `z`: Size type (`size_t`)
    - `t`: Pointer difference type (`ptrdiff_t`)

```{cpp}
printf("%d", 42);         // Prints "42"
printf("%5d", 42);        // Prints "   42" (width 5)
printf("%-5d", 42);       // Prints "42   " (left-justified)
printf("%+d", 42);        // Prints "+42"
printf("%#x", 255);       // Prints "0xff" (hex prefix)
printf("%.2f", 3.14159);  // Prints "3.14"
printf("%.*f", 3, 3.14159);// Precision read from next argument => "3.142"
```

# Enumerations

Enumerations, or `enum`, represent a user-defined data type in C that
consists of named integer constants, providing a way to group related values
under a single type for clarity and ease of maintenance.

The syntax for defining an enumeration is as follows:

```cpp
enum [tag_name]
{
    label[ = integer];
    label[ = integer];
    ...
    label[ = integer];
} [other_variables];
```

Each label in an enumeration is associated with an integer. If a specific
integer is not assigned to a label, it automatically takes the value one
greater than the previous label, starting from 0 for the first label if not
explicitly initialized.

## Examples

```cpp
enum Day { SUN, MON, TUE, WED, THU, FRI, SAT };
enum Mood { HAPPY = 3, SAD = 1, ANXIOUS = 4, SLEEPY = 2 };
enum Constants { BASE, ONE, TWO, NEGATIVE = -1, ANOTHER_ZERO = 0 };
```

In these examples:

- `Day` labels increment from 0, so `SUN` is 0, `MON` is 1, and so on.

- `Mood` has specific values assigned to each label. For instance, `HAPPY` is explicitly set to 3.

- `Constants` demonstrates that labels can share the same value (`ANOTHER_ZERO` and `BASE` both are 0).

## Declaration of Enumeration Variables

Variables of an enumeration type can be declared at the time of definition
using the optional `[other_variables]` placeholder or after the enumeration
is defined:

```cpp
enum Day today = THU; // today is assigned the value 4
enum Mood myMood = SLEEPY; // myMood is assigned the value 2
```

## Enumeration Names

There are several possibilities and conventions to name an enumeration:

- The tag name follows the `enum` keyword and can be used in variable
  declarations along with the `enum` keyword:

    ```{cpp}
    enum Color { RED, GREEN, BLUE };
    enum Color primaryColor = RED;
    ```

- The second possibility is to use the `typedef` keyword:

    ```cpp
    typedef enum { RED, GREEN, BLUE } Color;
    Color favoriteColor = BLUE; // Directly use Color instead of enum Color
    ```

- Enumerations can also be declared without a tag name, treating
  enumeration constants as global constants:

    ```{cpp}
    enum { PI = 3.142 };
    ```

# Structures and Unions

## Structures

Structures are used to group different types of data together under one name,
providing a way to model composite data entities.

A structure is defined using the `struct` keyword. It is typically placed
outside of and before the `main()` function to ensure that it is accessible
throughout the file.

The syntax for defining a structure is as follows:

```cpp
struct [strut_tag]
{
    member definition;
    member definition;
    ...
    member definition;
} [other_variables];
```

Just like with enumerations, a structure with a tag name or
with the `typedef` keyword.

```cpp
struct Employee {
    char id[7];
    int age;
    double wage;
};
```

The above `struct` is defined only with the tag name. Therefore, we need to
use the type `struct Employee` when declaring new variables.

```cpp
struct Employee emp = { "293145", 31, 45.28 };
```

Members of a structure are accessed using the dot operator (`.`) if there is
a structure variable:

```{cpp}
printf("Employee ID: %s\n", emp.id);
emp.wage = 50.00;
```

If there is a pointer to a structure, the arrow operator (`->`) is used to
access its members:

```{cpp}
struct Employee *empPtr = &emp;
printf("Employee Wage: %.2f\n", empPtr->wage);
empPtr->age = 32;
```

### Bit-fields

Bit-fields allow for a more efficient use of memory where variables occupy only
as many bits as necessary, rather than defaulting to a larger standard size
like a full `int` or `char`.

```cpp
struct date {
    unsigned day : 5;   // 5 bits for day (range 0-31)
    unsigned month : 4; // 4 bits for month (range 0-15)
    unsigned year : 11; // 11 bits for year (range 0-2047)
};

struct date today = {10, 6, 2010};
```

In this `date` structure, `day`, `month`, and `year` are packed into
potentially fewer bytes, depending on the system and compiler optimizations.

## Unions

A union is a user-defined data type similar to structures but with a unique
characteristic: all members of a union share the same memory location. This
means that at any given moment, a union can store only one of its members. The
size of a union is determined by the size of its largest member, ensuring that
any member can be stored in it.

```cpp
union Bitfields {

    unsigned char wholebyte;

    struct individualbits {
        unsigned bit0 : 1;
        unsigned bit1 : 1;
        unsigned bit2 : 1;
        unsigned bit3 : 1;
        unsigned bit4 : 1;
        unsigned bit5 : 1;
        unsigned bit6 : 1;
        unsigned bit7 : 1;
    } bits;
};

union Bitfields byte;

byte.wholebyte = 'A'; // byte is now 'A'

byte.bits.bit2 = 1; // byte is now 4
```

# Storage Classes

Storage classes in C define the visibility, lifetime, and linkage of variables
and functions within a program. They play a crucial role in how the duration
and scope of variables are managed during the runtime of a program.

## `auto`

```cpp
auto int i = 3;
```

- The `auto` keyword specifies that a variable has automatic storage
  duration, which is the default for local variables within functions or
  blocks. The variable is automatically allocated upon entering the block and
  deallocated when the block is exited.

- This keyword is largely redundant and mostly used for historical or
  documentation purposes, as local variables within functions are automatically
  assumed to be `auto`.

## `register`

```cpp
register size_t size = 467;
```

- The `register` keyword suggests that the variable should be stored in
  a CPU register instead of RAM to optimize access speed. However, the actual
  usage of a register for the variable is at the compiler's discretion; modern
  compilers often ignore this hint due to advanced optimization techniques.

- Variables declared with `register` cannot have their addresses taken,
  which means they cannot be referenced or used as arrays whose addresses are
  passed to functions.

## `static`

The `static` keyword has multiple uses depending on the context in which it
is applied. It can modify the storage class of variables and functions within
functions and at the file scope.

### Used Inside Functions

When used inside a function, `static` causes the variable to maintain its
state between function calls. Unlike local variables with automatic storage,
which are reinitialized every time a function is entered, `static` variables
preserve their value throughout the life of the program and initialize only
once.

```{cpp}
void foo() {
    static int a = 0; // Persistent storage across function calls
    int b = 0; // Automatic storage, recreated with each function call

    a += 10;
    b += 10;
    printf("static int a = %d, int b = %d\n", a, b);
}
```

### Used at File Scope

At the file scope, `static` restricts the visibility of variables and
functions to the file in which they are declared. Essentially, `static` at
the file level makes these variables and functions private to the file,
preventing other files from accessing them.

```{cpp}
static int counter; // Accessible only within this file

static int increment(int value) {
    return counter += value;
}
```

## `extern`

The `extern` keyword is used for declaring variables or functions that are
defined in another file. This approach facilitates access to global variables
across different files within the same program.

```{cpp}
/* file1.c */
int counter = 2; // Has external linkage

/* file2.c */
#include <stdio.h>
extern int counter; // Declares counter from file1.c

int main(void) {
    printf("%d\n", counter);
    return 0;
}
```

`extern` declares the variable `counter` which is defined elsewhere. During
the linking process, the linker resolves this external reference to `counter`
defined in `file1.c`.

# Type Quantifiers

Type qualifiers provide additional information about the variables they
precede, influencing how the compiler treats the data stored in these
variables. They are primarily used to enforce specific memory access behaviors.

## `const`

The `const` qualifier is used to declare that the value of a variable should
not be changed after initialization. This doesn't prevent the variable from
being modified through other means, such as using pointers, but it informs the
compiler that the code intends the value to remain constant. This can help
optimize the code and also serves as documentation that helps prevent
accidental modification of the variable.

```{cpp}
const int maxLimit = 100; // maxLimit should not be modified

int *ptr = (int *)&maxLimit;
*ptr = 200; // Modifies maxLimit despite const, leading to undefined behavior
```


## `volatile`

The `volatile` keyword is used to indicate that a variable's value can change
at any time, not only as a result of program control flow.

There are two main reasons to uses volatile variables:

- To interface with hardware that has memory-mapped I/O registers.

- When using variables that are modified outside the program control flow
  (e.g., in an interrupt service routine).

The compiler will not optimize anything that has to do with the volatile
variable.

```{cpp}
volatile int *statusRegister; // Points to a hardware status register

while (*statusRegister == 0) {
    // Wait for status register to change
}
```

## `restrict`

Introduced in C99, the `restrict` qualifier is used with pointer variables.
It tells the compiler that for the lifetime of the pointer, only the pointer
itself or a value directly derived from it (not any other independent pointer)
will be used to access the object to which it points. This allows for more
aggressive optimizations by the compiler.

```{cpp}
void updateValues(int *restrict ptr1, int *restrict ptr2, int value) {
    *ptr1 += value;
    *ptr2 += value; // Compiler may optimize as no overlap is assumed
}
```

# Preprocessor and Macros

The C preprocessor handles source code before compilation, performing text
substitutions, file inclusion, and conditional compilations.

## Macros

Macros are created using the `#define` directive. They allow for text
substitution in the code where the macro is called.

### `#define`

Function-like macros can replace simple functions, avoiding function call
overhead. Care is needed as they do not perform type checking and can evaluate
their arguments multiple times.

```{cpp}
#define ABS(x)  ((x < 0) ? -(x) : (x))

#define POW(X, Y) \
({ \
    int i, result = 1; \
    for (i = 0; i < Y; ++i) \
        result *= X; \
    result; \
})
```

### `#undef`

The `#undef` directive is used to undefine a macro, effectively removing its
definition from the code. This can be useful for managing scope, preventing
macro redefinition conflicts, and controlling conditional compilation in
complex projects.

```{cpp}
#define TEMP 100
#undef TEMP
// TEMP is no longer defined here
```


## Preprocessor Directives

### Header Include Guards

To prevent multiple inclusions of the same header file, which can lead to
definition conflicts, include guards are used. These are typically done using
`#ifndef`, `#define`, and `#endif`.

```{cpp}
#ifndef MY_FUNCS_H
#define MY_FUNCS_H
// Content of my_funcs.h
#endif
```

`#pragma once` is an alternative to include guards that serves the same
purpose but with less code. It is not part of the standard C, thus its support
can vary across compilers.

```{cpp}
#pragma once
// Content of my_funcs.h
```

### Conditional Compilation

#### `#if defined(...)` and `#ifdef`

These directives check whether a macro is defined and are used to compile code
conditionally based on the macro's definition.

- `#ifdef` can be used when checking a single condition.

    ```{cpp}
    #ifdef DEBUG
    // Debug-specific code
    #endif
    ```

- `#if defined(...)` can be used with logical operators for more complex
  conditions.

    ```{cpp}
    #if defined(DEBUG) && !defined(RELEASE)
    // Code for debug only, not for release
    #endif
    ```

Alongside `#if` and `#ifdef`, the `#else` and `#elif` (else if)
directives provide additional branching capabilities for conditional
compilation.

```{cpp}
#ifdef WINDOWS
    #define PLATFORM "Windows"
#elif defined(LINUX)
    #define PLATFORM "Linux"
#else
    #define PLATFORM "Unknown"
#endif
```

#### `#if 0`

This directive is useful for temporarily disabling code blocks:

```{cpp}
#if 0
// Code here is not compiled
#endif
```

# Memory Management

In C, managing memory dynamically is crucial for applications where the amount
of memory needed is not known beforehand or can change during runtime. The C
Standard Library provides several functions for dynamic memory management via
the `<stdlib.h>` header, which include `malloc`, `calloc`, `realloc`,
and `free`. These functions operate on the heap, allowing for flexible memory
usage.


## Allocating Memory

- `malloc` (Memory ALLOCation) allocates a specified amount of
  memory without initializing it. It returns a pointer to the beginning of the
  block, or `NULL` if the allocation fails.

- `calloc` (Contiguous ALLOCation) also allocates memory for an
  array of elements of a given size, initializing them to zero.

```{cpp}
// Using malloc to allocate space for 10 integers
int *p = malloc(10 * sizeof(int));

// Using calloc to allocate and initialize space for 10 integers
int *q = calloc(10, sizeof(int));
```

Both functions return `NULL` if memory allocation fails, which should be
checked to avoid dereferencing a null pointer, a common source of runtime
errors and crashes.

```{cpp}
int *p = malloc(10 * sizeof(int));

if (!p) {
    perror("malloc() failed");
    exit(EXIT_FAILURE);
}
```

## Freeing Memory

Dynamically allocated memory must be freed using `free` when it is no longer
needed to prevent memory leaks.

```cpp
int *p = malloc(10 * sizeof(int));

if (p == NULL){
    perror("malloc() failed");
    return -1;
}

/* Do something with the allocated memory */

free(p); // Release memory when no longer needed
```

The memory pointed to by `p` is reclaimed after the call to `free`, so
accessing that freed memory block via `p` will lead to undefined behavior.
Pointers that reference memory elements that have been freed are commonly
called dangling pointers, and present a security risk. The pointer should
either be repurposed (hold the address of another object) or invalidated (set
to null).

## Reallocating Memory

`realloc` is used for:

- Expanding or reducing the size of an existing memory block.

- Allocating a new memory block if the original pointer is `NULL`.

```{cpp}
void *realloc(void *ptr, size_t new_size);
```

- **`ptr`**: A pointer to the memory block previously allocated with
  `malloc`, `calloc`, or `realloc`. If `ptr` is `NULL`,
  `realloc` acts like `malloc`.

- **`new_size`**: The new size for the memory block in bytes

`realloc` may return a pointer to the same memory block or to a new location,
depending on the memory allocation requirements and system optimizations.

When `realloc` fails (returns `NULL`) and is attempting to expand a memory
block, the original memory block remains allocated. In this case, freeing the
original memory block is necessary to avoid memory leaks before terminating or
redirecting the flow of the program.

```cpp
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *p = malloc(10 * sizeof(int));
    if (p == NULL)
    {
        perror("malloc() failed");
        return EXIT_FAILURE;
    }

    p[0] = 42;
    p[9] = 15;

    /* Reallocate array to a larger size, storing the result into a
     * temporary pointer in case realloc() fails. */
    {
        int *temporary = realloc(p, 1000000 * sizeof(int));
        /* realloc() failed, the original allocation was not free'd yet. */
        if (NULL == temporary)
        {
            perror("realloc() failed");
            free(p); /* Clean up. */
            return EXIT_FAILURE;
        }
        p = temporary;
    }
    /* From here on, array can be used with the new size it was
     * realloc'ed to, until it is free'd. */
    /* The values of p[0] to p[9] are preserved, so this will print:
       42 15
       */
    printf("%d %d\n", p[0], p[9]);
    free(p);

    return EXIT_SUCCESS;
}
```

# Structuring and Building a C Project

## Typical Project Layout

A standard C project might be organized as follows:

- **src/**: Contains `.c` files. `main.c` usually includes the
  `main()` function that initiates the program.

- **include/**: Stores header files that declare the interfaces of modules
  (functions, data structures, constants).

- **build/**: Used for storing object files and other build artifacts to
  avoid cluttering the main directory.

- **bin/**: The destination for the final executable after the build
  process.

- **Makefile**: Describes the process to compile and link the project
  using `make`.

## Source and Header Interaction

Each `.c` file in the `src/` directory typically has a corresponding header
file in `include/`. This setup facilitates modular programming by separating
implementation in `.c` files from interfaces in `.h` files. Source files
include these headers to access functionality from other modules.

 To ensure the compiler finds these headers, use the `-I` compiler option:

```{cpp}
gcc -Iinclude -c src/main.c -o build/main.o
```

`-Iinclude` tells GCC to add the `include/` directory to the list of paths
it searches for header files.

## Makefile Basics

`make` reads instructions from a file named `Makefile` by default. These
instructions detail how to compile individual `.c` files into `.o` files
and how to link those object files into a final executable. Makefiles rely on
the concept of targets, dependencies, and rules:

- **Targets**: What to build (e.g., executables, object files).

- **Dependencies**: Files that must be present or up-to-date to execute a rule.

- **Rules**: Commands that create a target from dependencies.

```{make}
# Compiler and linker configurations
CC = gcc
CFLAGS = -Iinclude -Wall
LDFLAGS = -Llib
LDLIBS = -lm

# Put the names of all binary targets here
TARGET = bin/my_program

# Lists of source and object files
SOURCES = $(wildcard src/*.c)
OBJECTS = $(SOURCES:src/%.c=build/%.o)

# Default target
all: $(TARGET)

# Linking the executable from object files
$(TARGET): $(OBJECTS)
    $(CC) $(LDFLAGS) $^ -o $@ $(LDLIBS)

# Compiling source files into object files
build/%.o: src/%.c
    $(CC) $(CFLAGS) -c $< -o $@

# Cleaning up
clean:
    rm -rf $(TARGET) $(OBJECTS)
```

# C Libraries

## Common Standard Libraries

- **`<stdio.h>`**: Standard input/output. Provides `printf`, `scanf`, file operations, etc.
- **`<stdlib.h>`**: General utilities. Contains memory management (`malloc`, `free`), program control (`exit`, `abort`), and more.
- **`<string.h>`**: String handling. Functions like `strlen`, `strcpy`, `strcmp`.
- **`<math.h>`**: Common math operations. Contains trigonometric, exponential, and logarithmic functions.
- **`<time.h>`**: Time and date utilities. Functions to get system time, measure intervals, format dates.
- **`<ctype.h>`**: Character classification and conversion. Macros for checking digits, letters, etc.
- **`<stdarg.h>`**: Variable arguments handling. Declares `va_list`, `va_start`, `va_arg`, `va_end`.
- **`<limits.h>`**: Defines constants for fundamental data type limits, e.g., `INT_MAX`.
- **`<float.h>`**: Defines constants related to floating-point limits.
- **`<stdbool.h>`**: Defines `bool`, `true`, `false`.

## Third-Party Libraries

Below are popular third-party libraries. They are developed outside the
standard library but are widely used in C projects. Each entry includes a brief
description and a link for more information:

