# Arrays

We first need to **import** NumPy:

```python
import numpy as np
```

## Homogeneous Arrays

An abridged version of the
[syntax](https://numpy.org/doc/stable/reference/generated/numpy.array.html) to
create an array with objects of the same type is:

```python
np.array(object, dtype=None, order='K')
```

- `dtype` specifies the desired data-type for the array.
- `order` spcifies the memory layout of the array. NumPy defaults to row-major
  (`order='C')` ordering.

![Memory layout of arrays](./media/rowcolumnarrays.jpg)

A few examples are given below:

```python
vec  = np.array([1, 2, 3])                            # shape = (3,)
mat1 = np.array([[1, 2, 3]])                          # shape = (1, 3)
mat2 = np.array([[1, 2, 3], [4, 5, 6]])               # shape = (2, 3)
mat3 = np.array([[1, 2], [4, 255]], dtype=np.float32) # shape = (2, 2)
mat4 = np.array([[1+1j, 2+2j], [3+3j, 4+4j]])         # shape = (2, 2)
```

We can visualize the **shapes** and **axes** in the figure below:

![Shapes and axes of NumPy arrays](./media/axis.png)

We can get the array **dimension,** **shape,** and **size** (number of
elements), and **data type** using the *attributes* given below:

```python
mat2.ndim       # => 2
mat2.shape      # => (2, 3)
mat2.size       # => 6
mat2.dtype.name # => 'int64'
```

We can **convert** the elements of an array from one **type** to another using
[`np.asaray`](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html),
which is a function that is generally used to convert some input data into an
array.

```python
mat3.astype(np.int8) # => [[1, 2] [4, -1]]
```

### Array Creating Functions

An array can be constructed by any of the array-creation routines found
[here](https://numpy.org/doc/stable/reference/routines.array-creation.html).
The most common ones are presented below.

#### `np.arange`

We can generate an array in the half-open interval `[start, stop)` with
evenly-spaced (`step`) values using `np.arange`.

```python
# np.arange([start=0, ] stop [, step=1])
np.arange(1, 10, 2) # => [1, 3, 5, 7, 9]
```

#### `np.linspace`

We can generate an array of `num` evenly-spaced numbers in the closed-interval
`[start, stop]` using `np.linspace`.

```python
# np.linspace(start, stop, num=50, endpoint=True)
np.linspace(1, 10, num=4) # => [1.,  4.,  7., 10.]
```

A similar function is `np.logspace`, which returns numbers spaced evenly on a
log scale.

```python
np.logspace(1, 4, num=4)       # => [10.,  100.,  1000., 10000.]
10 ** np.linspace(1, 4, num=4) # => [10.,  100.,  1000., 10000.]
```

#### `np.meshgrid`

We can create a rectangular grid out of an array of `x` values and an array of
`y` values using `np.meshgrid`. Creation of these rectangular grids is useful
for a number of tasks, such as sampling a function `f(x, y)` over a range of
values of `x` and `y`.

```python
x = np.arange(1, 4, 1) # => [1, 2, 3]
y = np.arange(5, 8, 1) # => [5, 6, 7]
# np.meshgrid(x, y, sparse=False)
xx, yy = np.meshgrid(x, y)
z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
```

This would result in the following `xx` and `yy` matrices, such that the
pairing of the corresponding element in each matrix gives the `x` and `y`
coordinates of a point in the grid.

```python
xx = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
yy = np.array([[5, 5, 5], [6, 6, 6], [7, 7, 7]])
```

#### Others

Some common functions for creating arrays include:

```python
np.zeros(4)          # 1D array of zeros
np.zeros((3, 3))     # 3x3 array of zeros
np.zeros((3, 3)) + 5 # 3x3 array of fives
np.ones((2, 3))      # 2x3 array of ones
np.eye(4)            # 4x4 identity array
np.diag((1, 2, 3))   # 3x3 diagonal array
```

### Saving Arrays

#### CSV Format

Save an array to
a [text](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html)
file. If the filename ends in `.gz`, the file is automatically saved in
compressed gzip format.

```python
arr = np.array([0, 1, 2, 3, 4, 5])
# save array to csv file
np.savetxt('data.csv', arr, delimiter=',')
# load array from csv file
arr2 = np.loadtxt('data.csv', delimiter=',')
```

#### NPY Format

Save an array to
a [binary](https://numpy.org/doc/stable/reference/generated/numpy.save.html)
file in NumPy `.npy` format.

```python
arr = np.array([0, 1, 2, 3, 4, 5])
# save array to npy file
np.save('data.npy', arr)
# load array from npy file
arr2 = np.load('data.npy')
```

#### NPZ Format

Save several arrays into a single file in
[compressed](https://numpy.org/doc/stable/reference/generated/numpy.savez_compressed.html)
`.npz` format.

```python
arr1 = np.array([0, 1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8, 9])
# save arrays to npz file
np.savez_compressed('data.npz', some_keyname_1=arr1, some_keyname_2=arr2)
# load arrays from npy file
data_dict = np.load('data.npz')
arr3 = data_dict['some_keyname_1']
arr4 = data_dict['some_keyname_2']
```

### Printing Options

We can print out the content of a NumPy array using the
[`print`](https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html)
function. If an array is too large to be printed, NumPy automatically skips the
central part of the array and only prints the corners. To disable this
behaviour and force NumPy to print the entire array:

```python
import sys
np.set_printoptions(threshold=sys.maxsize)
```

## Structured Arrays

We can define arrays with separate data types for each column. For example,
suppose we want to create an array that holds the name of a country in one
column and the population in another. The first column therefore holds objects
of type `string`, while the second column holds objects of type `int`.

To store such a structure, we first need to define a new data type:

```python
dt = np.dtype([('country', 'S20'), ('population', 'i4')])
```

The first entry identifies the name of the column. The second entry
identifies the type and size.

- `S20` means a binary string of no more than 20 characters. To get unicode
  strings, we replace `('country', 'S20')` with `('country', np.unicode, 20)`.
- `i4` means an integer of size 4 bytes.

With the new data type defined, we can now create our array:

```python
population_table = np.array([
    ('Netherlands', 16928800),
    ('Belgium', 11007020),
    ('United Kingdom', 62262000)],
    dtype=dt)
```

`population_table` acts like dictionary. We can access the content of the
country column with `population_table['country']`. This returns a 1D array.

# Random Numbers

We can create arrays with **random** elements. We first need to import the
`random` submodule:

```python
from numpy import random
```

We can generate arrays with random elements using the following:

| function                                        | description                                                           |
| ---                                             | ---                                                                   |
| `rand(d0, d1, …, dn)`                           | Uniformly distributed random values in a given shape.                 |
| `randn(d0, d1, …, dn)`                          | Return a sample (or samples) from the “standard normal” distribution. |
| `randint(low, high=None, size=None, dtype=int)` | Return random integers from low (inclusive) to high (exclusive).      |

Some common distributions from which we can generate random numbers are given below:

| function                                  | description                                                                                                           |
| ---                                       | ---                                                                                                                   |
| `binomial(n, p, size=None)`               | Draw samples from a binomial distribution.                                                                            |
| `laplace(loc=0.0, scale=1.0, size=None)`  | Draw samples from the Laplace or double exponential distribution with specified location (or mean) and scale (decay). |
| `geometric(p, size=None)`                 | Draw samples from the geometric distribution.                                                                         |
| `normal(loc=0.0, scale=1.0, size=None)`   | Draw random samples from a normal (Gaussian) distribution.                                                            |
| `standard_normal(size=None)`              | Draw samples from a standard Normal distribution (mean=0, stdev=1).                                                   |
| `logistic(loc=0.0, scale=1.0, size=None)` | Draw samples from a logistic distribution.                                                                            |
| `exponential(scale=1.0, size=None)`       | Draw samples from an exponential distribution.                                                                        |
| `chisquare(df, size=None)`                | Draw samples from a chi-square distribution.                                                                          |
| `standard_t(df, size=None)`               | Draw samples from a standard Student’s t distribution with df degrees of freedom.                                     |
| `uniform(low=0.0, high=1.0, size=None)`   | Draw samples from a uniform distribution.                                                                             |

For example:

```python
# generate a 2x3 array of uniformly distributed random values
np.random.rand(2, 3)

# generate array of 5 random numbers from 10 to 50
np.random.randint(10, 50, 5)

# generate 3x3 array of random numbers from 10 to 50
np.random.randint(10, 50, size=(3, 3))

# generate 3x2 array of random numbers from the binomial distribution
np.random.binomial(10, 0.4, size=(3, 2))
```

**Note**: If we want the random numbers not to change from session to session
so we can reproduce the same results, we can fix the `seed`:

```python
np.random.seed(111)
np.random.randint(10, 50, 5)
```

However, it is often useful to create a separate `RandomState` object for
various parts of our code. Working with multiple, separate `RandomState`
objects can also be useful if we run our code in non-sequential order -- for
example if we are experimenting with our code in interactive sessions or
Jupyter Notebook environments.

The example below shows how we can use a `RandomState` object to create the same
results that we obtained via `np.random.rand` in the previous code snippet:

```python
rng1 = np.random.RandomState(seed=111)
rng1.rand(2, 3)
```

# Slicing and Indexing

For 1D arrays, slicing works the same way as with regular python list slicing:

```python
a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

a[:5]      # => [0, 1, 2, 3, 4]
a[5:]      # => [5, 6, 7, 8, 9]
a[4:7]     # => [1, 2, 3, 4, 5, 6]
a[1:7:2]   # => [1, 3, 5]
a[::-1]    # => [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
a[-3:3:-1] # => [7, 6, 5, 4]
```

For 2D arrays, we have a slightly different notation:

```python
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

b[0, 0]      # => 1
b[-1, -1]    # => -9
b[0]         # => [1, 2, 3]
b[ : , 0]    # => [1, 4, 7]
b[ : , :2]   # => [[1, 2], [4, 5], [7, 8]]
b[ : , 1:3]  # => [[2, 3], [5, 6], [8, 9]]
b[1:3 , 1:3] # => [[5, 6], [8, 9]]
```

**Note**: In all the above examples, when we index an array, we are creating a
pointer, **not a copy**.

Consider the example below:

```python
a = np.array([[1, 2, 3], [4, 5, 6]])

# create a variable that points to the row at index 0
row_0 = a[0]
row_0 += 99 # increment each element in row_0
```

The first row of the original array is also modified since `row_0` is not a
copy of the first row, but a pointer to the first row. To avoid modifying the
original array, we need to make a copy:

```python
row_0 = a[0].copy()
row_0 += 99
```

We can also index elements in an array by passing their indicies directly in a
list. When indexing items this way, a copy is made and the original array
remains untouched.

For 1D arrays:

```python
a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# indexing a single element
n = a[0] # => 0

# indexing items at index 0 and 7
n = a[[0, 7]] # => [0, 7]
```

For 2D arrays:

```python
a = np.array([[1, 2, 3], [4, 5, 6]])

# index columns 2 and 0
n = a[:, [2, 0]] # => [[3, 1], [6, 4]]

# index elements at index (1, 2) and (0, 0)
n = a[[1, 0], [2, 0]] # => [6, 1]
```

## Ellipsis

The ellipsis, `...`, is used to slice higher-dimensional array.

```python
a = np.array([ [[0, 1], [2, 3]], [[4, 5], [6, 7]] ])

# element at index (1, 0, 1)
n = a[1, 0, 1] # => 5

# any element from axis 0, elements at index 1 from axis 1,
# elements at index 0 from axis 2
n = arr[:, 1, 0] # => [2, 6]

# any element from axis 0, any element from axis 1,
# elements at index 1 from axis 2
n = arr[:, :, 0] # => [[1, 3], [5, 7]]
```

In the last case, we can use `...` to insert the two  (or as many as needed)
full slices (`:`).

```python
n = arr[..., 0] # => [[1, 3], [5, 7]]
```

# Array Manipulation

## Array Reshaping

In practice, we often run into situations where existing arrays do not have the
right shape to perform certain computations. Even though the size of NumPy
arrays is fixed, this does not mean that we have to create new arrays and copy
values from the old array to the new one if we want arrays of different shapes
-- the size is fixed, but the shape is not. NumPy provides a `reshape` method
that allow us to obtain a **view** of an array with a different shape.

```python
ary1d = np.array([1, 2, 3, 4, 5, 6])
ary2d_view = ary1d.reshape(2, 3) # => [ [1, 2, 3] , [4, 5, 6] ]
```

To show that both arrays point to the same memory location:

```python
np.may_share_memory(ary2d_view, ary1d) # => True
```

While we need to specify the desired elements along each axis, we need to make
sure that the reshaped array has the same number of elements as the original
one. However, we do not need to specify the number elements in each axis; NumPy
can figure out how many elements to put along an axis if only **one** axis is
unspecified (by using the placeholder -1):

```python
ary1d.reshape(2, -1) # creates a 2x3 array
ary1d.reshape(-1, 2) # creates a 3x2 array
```

## Flattening an Array

There are three ways to flatten (collapse into one dimension) an array:

1. `arr.reshape(-1)`: returns a 1D flattened **view** of the array
2. `arr.flatten()`: returns a 1D flattened **copy** of the array
3. `arr.ravel()`: works the same way as `arr.reshape(-1)` and a **copy** is
   made **only if needed**

## Concatenating Arrays

Sometimes, we are interested in merging different arrays. Unfortunately, there
is no efficient way to do this without creating a new array, since NumPy arrays
have a fixed size. To combine two or more array objects, we can use NumPy's
`concatenate` function as shown in the following examples:

```python
vec = np.array([1, 2, 3])

# stack to the end of the list
np.concatenate((vec, vec))  # => [1, 2, 3, 1, 2, 3]
# stack the vectors row-wise
np.row_stack((vec, vec))    # => [[1, 2, 3], [1, 2, 3]]
# stack the vectors column-wise
np.column_stack((vec, vec)) # => [[1, 1], [2, 2], [3, 3]]

mat = np.array([[1, 2, 3]])

# stack along the first (0) axis
np.concatenate((mat, mat), axis=0) # => [[1, 2, 3] , [1, 2, 3]]
np.vstack((mat, mat))              # => [[1, 2, 3] , [1, 2, 3]]

# stack along the second axis
np.concatenate((mat, mat), axis=1) # => [[1, 2, 3, 1, 2, 3]]
np.hstack((mat, mat))              # => [[1, 2, 3, 1, 2, 3]]
```

## Adding Dimension

### newaxis

New dimensions can be added to an array by using slicing and `np.newaxis`.

```python
arr = np.array([1, 2, 3, 4]) # shape = (4,)
# insert axis along the first axis
row = arr[np.newaxis, :] # shape = (1,4)
# insert axis along the second axis
col = arr[:, np.newaxis] # shape = (4,1)
```

Note that `np.newaxis` is an alias for `None`. Therefore, `arr[:, np.newaxis]`
is the same as `arr[:, None]`, but `arr[:, np.newaxis]` is more explicit.

### expand_dims

`np.expand_dims(arr, axis)` inserts a new axis that will appear at the `axis`
position in the expanded array shape. Negative numbers for `axis` follow
standard Python rules for negative indexing.

```python
arr = np.array([1, 2, 3, 4]) # shape = (4,)
# insert axis along the first dimension
np.expand_dims(arr, 0) # shape = (1, 4)
# insert axis along the second dimension
np.expand_dims(arr, 1) # shape = (4, 1)
```

## Removing Dimension

`np.squeeze(arr, axis=None)` is used to remove axes of length one from
`arr`.

```python
arr = np.array([[ [0], [1], [2] ]]) # shape (1, 3, 1)
np.squeeze(arr)                     # => [0, 1, 2] : shape (3,)
np.squeeze(arr, axis=0)             # => [ [0], [1], [2] ] : shape (3, 1)
np.squeeze(arr, axis=2)             # => [[0, 1, 2]] : shape (1, 3)
```

## Transpose Operations

### transpose

`np.transpose(a, axes=None)` reverses or permutes the axes of an array.

```python
arr = [[0, 1, 2],[3, 4, 5]] # shape = (2, 3)
np.tranpose(arr)            # => [ [0, 3], [1, 4], [2, 5] ] : shape (3, 2)
```

`np.tranpose(arr)` is the same as `arr.T`.

### swapaxes

`np.swapaxes(arr, axis1, axis2)` interchanges `axis1` with `axis2`.

```python
arr = [ [[0], [1]], [[2], [3]], [[4], [5]] ] # shape (3, 2, 1)
np.swapaxes(arr, 0, 2)                       # => [[ [0, 2, 4], [1, 3, 5] ]] : shape (1, 2, 3)
```

To understand the new location of the values, consider the number 3. Initially
it was at index `(1, 1, 0)`. After swapping axes 0 and 2, the new index of 3 is
`(0, 1, 1)`.

### rollaxis

`np.rollaxis(a, axis, start=0)` rolls the specified `axis` backwards, until
it lies in a given position.

```python
arr = [ [[0], [1]], [[2], [3]], [[4], [5]] ] # shape (3, 2, 1)
np.rollaxis(arr, 2)                          # => [[ [0, 1], [2, 3], [4, 5] ]] : shape (1, 3, 2)
```

To understand the new location of the values, consider the number 5. Initially
it was at index `(2, 1, 0)`. After the first roll backwards, it is at position
`(2, 0, 1)`, and after the second roll, it is at position `(0, 2, 1)`.


# Array Broadcasting

Arrays with different sizes cannot be added, subtracted, or generally be used
in arithmetic.

Broadcasting solves the problem of arithmetic between arrays of differing
shapes by in effect replicating the smaller array along the mismatched
dimensions, so that it matches the dimensionality and size as the larger array.
The idea is shown in the figure below.

![Broadcasting](./media/broadcasting.png)

NumPy does not actually duplicate the smaller array; instead, it makes memory
and computationally efficient use of existing structures in memory that in
effect achieve the same result.

- 2D array with a scalar

    ```python
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
    b = 10
    arr_2d + 10 # => [[11, 12, 13], [14, 15, 16]]
    ```

    Since the shape of `arr_2d` is `(2, 3)`, `b` is "stretched" 1 place along
    axis 0 and 2 places along axis 1 to produce an array with a shape of `(2, 3)`,
    which is then added to `arr_2d`.

- 2D array with 1D array

    ```python
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
    arr_1d = np.array([10, 20, 30])
    arr_2d + arr_1d # => [[11, 22, 33], [14, 25, 36]]
    ```

    `arr_1d` is "stretched" 1 place in axis 0 to create an array of shape `(2, 3)`.

- Arrays of unequal sizes

    ```python
    x1 = np.array([1, 2, 3, 4, 5])
    x2 = np.array([5, 4, 3])
    x1_new = x1[:, np.newaxis]
    x1_new + x2
    ```

    We first convert `x1` to an array of shape `(5, 1)`. Since the dimensions
    have to agree, `x2` is "stretched" to an array of shape `(5, 3)`. `x1` is
    then "stretched" to an array of shape `(5, 3)`.

# Universal Functions

These are functions that operate on an array in an **element-by-element**
fashion.

## Common Math Functions

Arithmetic:

- `add(x1, x2)`, `subtract(x1, x2)`, `multiply(x1, x2)`, `mod(x1, x2)`,
  `power(x1, x2)`, `true_divide(x1, x2)`, `floor_divide(x1, x2)`

- For the functions above, we can use **operator overloading** for simpler
  notation: `x1 + x2`, `x1 - x2`, `x1 * x2`, `x1 % x2`, `x1 ** x2`, `x1 / x2`,
  `x1 // x2`.

Other common functions:

- `reciprocal(x)`, `positive(x)`, `negative(x)`, `sign(x)`, `absolute(x)`,
  `square(x)`, `cbrt(x)`, `minimum(x)`, `maximum(x)`

Exponents and logarithm:

- `exp(x)`, `log(x)`, `log10(x)`, `log2(x)`

Trigonometric:

- `sin(x)`, `cos(x)`, `tan(x)`, `arcsin(x)`, `arccos(x)`, `arctan(x)`,
  `arctan(x1, x2)`, `degrees(x)`, `radians(x)`.

Rounding:

- `floor(x)`, `ceil(x)`, `trunc(x)`, `rint(x)`, `around(x, decimals)`

The full list of functions can be found
[here](https://numpy.org/doc/stable/reference/routines.math.html).

## Comparison Functions

These are:

- `greater(x1, x2)`, `greater_equal(x1, x2)`, `less(x1, x2)`, `less_equal(x1,
  x2)`, `not_equal(x1, x2)`, `equal(x1, x2)`

- We can use operator overloading for simpler notation: `x1 > x2`, `x1 >= x2`,
  `x1 < x2`, `x1 <= x2`, `x1 != x2`, `x1 == x2`.

For example:

```python
ary = np.array([1, 2, 3, 4])
mask = ary > 2 # => [False, False, True, True]
```

A related, useful function to assign values to specific elements in an array is
the `np.where` function. In the example below, we assign a 10 to all values in
the array that are greater than 2, and 0 otherwise:

```python
np.where(ary > 2, 10, 0)   # => [0, 0, 10, 10]
np.where(ary > 2, 10, ary) # => [1, 2, 10, 10]
```

## Bitwise Operations

Do not use the Python keywords `and` and `or` to combine logical array
expressions. These keywords will test the truth value of the entire array (not
element-by-element as you might expect). Use the bitwise operators instead:

- `bitwise_and(x1, x2)`, `bitwise_or(x1, x2)`, `bitwise_xor(x1, x2)`, `bitwise_not(x1)`

- We can use operator overloading for simpler notation: `&`, `|`, `^`, `~`.

For example:

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
a[(a > 3) & (a % 2 == 0)] # => [4, 6]
```

## The reduce function

This
[function](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html)
reduces an array’s dimension by one by applying a binary universal function
along one axis.

```python
a = np.array([[1, 2, 3], [4, 5, 6]])

# sum across rows (axis=0)
np.add.reduce(a)  # => [5, 7, 9]
np.sum(a, axis=0) # => [5, 7, 9]

# sum across columns
np.add.reduce(a, axis=1) # => [6, 15]
np.sum(a, axis=1)        # => [6, 15]
```

## Some other useful functions

Some useful unary functions are:

- `np.mean`: computes arithmetic average
- `np.std`: computes the standard deviation
- `np.var`: computes the variance
- `np.sort`: sorts an array
- `np.argsort`: returns indices showing how to sort array
- `np.min`: returns the minimum value of an array
- `np.max`: returns the maximum value of an array
- `np.argmin`: returns the index of the minimum value
- `np.argmax`: returns the index of the maximum value
- `np.array_equal`: checks if two arrays have the same shape and elements

For example:

```python
a = np.array([5, 8, 1, 3])
np.argsort(a)    # => [2, 3, 0, 1]
a[np.argsort(a)] # => [1, 3, 5, 8]
```

# Linear Algebra

## Array multiplication

`np.dot(A, B)` is defined as the sum product over the last axis of `A` and the
second-to-last of `A`.

- For 1D arrays, it is the same as the inner product of vectors (without
  complex conjugation).
- For 2D arrays, the dot product is equivalent to matrix multiplication.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.dot(a, b) # => 32
```

The function `np.matmul(A, B)` can also be used to compute the matrix product
of two arrays.

```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])
column = np.array([1, 2, 3]).reshape(-1, 1)
np.matmul(matrix, column) # => [[14], [32]]

# using operator overloading
matrix @ column # => [[14], [32]]
```

## linalg submodule

Most of the common linear algebra functions are defined inside the `linalg`
[module](https://numpy.org/doc/stable/reference/routines.linalg.html).

```python
from numpy import linalg
```

| function                | description                                                           |
| ---                     | ---                                                                   |
| `linalg.det(a)`         | Compute the determinant of an array.                                  |
| `linalg.matrix_rank(M)` | Return matrix rank of array using SVD method.                         |
| `linalg.norm(x[, ord])` | Matrix or vector norm.                                                |
| `linalg.cond(x[, p])`   | Compute the condition number of a matrix.                             |
| `trace(a)`              | Return the sum along diagonals of the array.                          |
| `linalg.eig(a)`         | Compute the eigenvalues and right eigenvectors of a square array.     |
| `linalg.eigvals(a)`     | Compute the eigenvalues of a general matrix.                          |
| `linalg.cholesky(a)`    | Cholesky decomposition.                                               |
| `linalg.qr(a)`          | Compute the qr factorization of a matrix.                             |
| `linalg.svd(a)`         | Singular Value Decomposition.                                         |
| `linalg.solve(a, b)`    | Solve a linear matrix equation, or system of linear scalar equations. |
| `linalg.lstsq(a, b)`    | Return the least-squares solution to a linear matrix equation.        |
| `linalg.inv(a)`         | Compute the (multiplicative) inverse of a matrix.                     |
| `linalg.pinv(a)`        | Compute the (Moore-Penrose) pseudo-inverse of a matrix.               |
