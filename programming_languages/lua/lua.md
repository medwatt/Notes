# Introduction

## Comments

```lua
-- Single-line comment

--[[
   Multi-line comment
--]]
```

## Variable Scope

Variables in Lua are **global** by default, unless explicitly declared as
`local`. A local variable is limited to the **scope** of the
[chunk](https://www.lua.org/pil/1.1.html) where it is defined.

In **interactive mode**, each line is treated as a separate chunk. This means a
local variable declared on one line is out of scope in the next line. To
maintain scope across multiple lines, wrap code in a `do ... end` block.

```lua
var = 10 -- global
print("Global var:", var) --> 10

-- begin of local scope
do
    local var = 20 -- local
    print("Local var:", var) --> 20
end
-- end of local scope

-- use global var
print("Global var:", var) --> 10
```

## Variable Assignment

- Lua does not have augmented assignments: write `a = a + 1` instead of `a += 1`.

- Lua does not have chained assignments: write `a = 0; b = 0` instead of `a = b = 0`.

- Lua supports parallel assignment: `a, b, c = 0, 0, 0`.

## Variable Types

Lua has eight types: `nil`, `boolean`, `number`, `string`,
`userdata`, `function`, `thread`, and `table`.

```lua
print(type("Hello"))   --> string
print(type(10.4*3))    --> number
print(type({1, 2, 3})) --> table
print(type(print))     --> function
print(type(true))      --> boolean
print(type(nil))       --> nil
```

- `nil` represents no value. Accessing an undeclared variable returns
  `nil`. Assigning a variable to `nil` deletes it.

- When performing arithmetic on a string, Lua attempts to convert it to a
  number.

- When a number is used where a string is expected, it is automatically
  converted to a string.

- Use `tostring` and `tonumber` for explicit type conversion.

## Math Operators

```lua
local a, b = 0x14, 4

print(a + b) --> 24
print(a - b) --> 16
print(a * b) --> 80
print(a ^ b) --> 160000.0
print(a / b) --> 5.0
print(a % b) --> 0
print(-a)    --> -20
```

`/` does floating-point division. Lua 5.3 introduced `//` for integer
(floor) division.

## Relational Operators

```lua
local a, b = 20, 4

print(a == b) --> false
print(a ~= b) --> true
print(a > b)  --> true
print(a < b)  --> false
print(a >= b) --> true
print(a <= b) --> false
```

## Logical Operators

```lua
print(true and 10)   --> 10
print(10 and true)   --> true
print(false and 10)  --> false
print(false or 10)   --> 10
print(nil and 10)    --> nil
print(nil or 10)     --> 10
```

- Only `false` and `nil` are `false`; everything else is `true`.

- **`and`** returns its first argument if it is false, otherwise its second argument.

- **`or`** returns its first argument if it is not false, otherwise its
  second argument.

# Strings

```lua
local a = 'there is a "quote" inside this string'
local b = [[This is a
   multi-line string]]
local c = "this is a string with \t escape characters \\"
```

## Common String Methods

```lua
print(string.upper("The"))           --> THE
print(string.lower("ADT"))           --> adt
print(string.len("a b c"))           --> 5
print(#"a b c")                      --> 5 (`#`: length operator)
print(string.find("This is", "is"))  --> 3  4
print(string.sub("abcd", 2, 3))      --> bc
print(string.gsub("pen", "e", "i"))  --> pin
print(string.rep("ab", 2))           --> abab
print("a" .. ": " .. "b")            --> a: b (`..`: concatenation operator)
print(string.reverse("abcd"))        --> dcba
print(string.char(98))               --> b
print(string.byte("abc", 2))         --> 98
```

## String Formatting

Lua's `string.format` works like C's `printf` (excluding `* l L n p h`).

**Common Specifiers**:

- `%s`: string

- `%q`: quoted string

- `%c`: character

- `%d`: signed integer

- `%u`: unsigned integer

- `%x`: hexadecimal (lowercase)

- `%o`: octal

- `%e`: scientific notation

- `%f`: float (fixed-point)

```lua
print(string.format("%s", "hello"))        -- hello
print(string.format("%q", "hello"))        -- "hello"
print(string.format("%c", 65))             -- A
print(string.format("%d", -123))           -- -123
print(string.format("%u", -123))           -- 4294967173 (on 32-bit systems)
print(string.format("%x", 255))            -- ff
print(string.format("%o", 9))              -- 11
print(string.format("%e", 1234.56))        -- 1.234560e+03
print(string.format("%f", 3.14))           -- 3.140000
```

**Decimal Places**:

```lua
print(string.format("%.2f", 3.14159))      -- 3.14
print(string.format("%.3e", 1234.56))      -- 1.235e+03
```

**Flags**:

- `-`: left-justify

- `+`: always show sign

- `#`: add prefix (`0`, `0x`) for octal/hex

- `0`: pad with zeroes

```lua
print(string.format("%+d", 42))            -- +42
print(string.format("%05d", 42))           -- 00042
print(string.format("%-5d", 42))           -- 42
print(string.format("%#x", 255))           -- 0xff
print(string.format("%#o", 9))             -- 011
```

## Pattern Matching

Lua's patterns are simpler than full regex. They're useful for searching,
extracting, or replacing parts of strings.

### Character Classes


| Class | Matches |
| --- | --- |
| `%a` | letters |
| `%c` | control characters |
| `%d` | digits |
| `%l` | lowercase letters |
| `%p` | punctuation |
| `%s` | space characters |
| `%u` | uppercase letters |
| `%w` | alphanumeric |
| `%x` | hexadecimal digits |
| `%z` | null character |


Uppercase versions (e.g. `%D`, `%W`) match the **opposite**.

### Special Syntax

- `.`: any character

- `%`: escape magic characters

- `[...]`: custom class

- `[^...]`: negated class

- `*`: 0 or more (greedy)

- `+`: 1 or more (greedy)

- `-`: 0 or more (non-greedy)

- `?`: 0 or 1

- `( )`: capture

### Examples

```lua
-- 1. Extract digits from a string
print(string.match("User ID: 3487", "%d+"))        -- 3487

-- 2. Capture two words separated by space
local first, last = string.match("Jane Doe", "(%a+)%s+(%a+)")
print(first, last)                                 -- Jane Doe

-- 3. Match shortest tag using non-greedy '-'
print(string.match("<div>text</div><p>hi</p>", "<.->"))  -- <div>
```

```lua
local str  = 'color:#@(fg)'
local pat  = '@%(([^()]+)%)'
local repl = 'FF00FF'
print(string.gsub(str, pat, repl)) --> color:#FF00FF
```

# Control Structures

## Conditional Statements

```lua
local num = math.random(1, 100)

if num < 25 then
    print(num .. " < 25")
elseif num < 50 then
    print(num .. " < 50")
else
    print(num .. " >= 50")
end
```

## Loops

### While

```lua
local i = 1

while i <= 5 do
    io.write(i, " ")
    i = i + 1
end
```

### Repeat

```lua
local i = 1

repeat
    io.write(i, " ")
    i = i + 1
until i > 5
```

### For

```lua
for i = 1, 5 do
    io.write(i, " ")
end
```

### Break

`break` exits a loop early.

```lua
for i = 1, 10 do
    if i > 5 then break end
    io.write(i, " ")
end
```

### Continue (simulated)

Lua doesn't have a built-in `continue`, but in Lua versions above 5.1,
it can be simulated using `goto`.

```lua
for i = 1, 5 do
    if i == 3 then
        goto skip
    end
    io.write(i, " ")
    ::skip::
end
```

For version 5.1 and earlier, reverse the condition:

```{lua}
for i = 1, 5 do
    if i ~= 3 then
        io.write(i, " ")
    end
end
```

# Tables

Tables are Lua's only container type. They are associative arrays, meaning they
store key/value pairs.

The `#` operator can be used to retrieve the length of a string or the number
of elements in a table. However, when used with tables, it returns only the
**last integer key**. As a result, it should not be used for tables where the
integer keys are not consecutive.

## Indexing

- Indexing in Lua starts at 1.

- `vec = {"a", "b", "c"}` is the same as `vec = {[1]="a", [2]="b", [3]="c"}`.

```lua
local T =  {
    4, 8, "x",         -- indexed with T[1], T[2], T[3]
    ["title"] = "Lua", -- indexed with T["title"] or T.title
    x = 3,             -- indexed with T["x"] or T.x
    ["the page"] = 5,  -- indexed with T["the page"]
    [123] = 456,       -- indexed with T[123]
    {4, 5, 6}          -- indexed with T[4][1], T[4][2], T[4][3]
}

-- # returns only the last consecutive integer key !!
print( #T ) --> 4
```

## Basic Table Operations

Lua provides `ipairs` and `pairs` as iterator functions that provide
successive elements from a table. Both of these functions return two
variables: key/index and value. Generally, `ipairs` should be used to
iterate over arrays since the `ipairs` iterator will stop at the first
non-initialized index (the index at which the value is `nil`).

```lua
local T = {"b", "c", "d"} --> {[1]="b", [2]="c", [3]="d"}

-- update an entry
T[1] = "a" --> {[1]="a", [2]="c", [3]="d"}

-- add a new item at a specific unoccupied index
T[10] = "j" --> {[1]="a", [2]="c", [3]="d", [10]="j"}

-- add a new item to the end of the last consecutive integer key
table.insert(T, "e") --> {[1]="a", [2]="c", [3]="d", [4],"e", [10]="j"}

-- insert a new item at a specific occupied index
table.insert(T, 2, "b") --> {[1]="a", [2]="b", [3]="c", [4]="d", [5],"e", [10]="j"}

-- T[6] = nil, so the loop stops at T[5]
for index, value in ipairs(T) do
    print(index, value)
end

-- delete a key/value pair by setting the key to nil
T[3] = nil --> {[1]="a", [2]="b", [3]=nil, [4]="d", [5],"e", [10]="j"}

-- remove item from a specific location
table.remove(T, 3) --> {[1]="a", [2]="b", [4]="d", [5],"e", [10]="j"}
```

## Other Table Functions


- `table.concat(t[, sep[, i[, j]])`

    - Concatenates values in the table into a string.

    - `sep` is the separator (default is empty string), `i` and `j` are the start and end indices.

        ```lua
        local T = {"a", "b", "c", [10] = "j"}
        print(table.concat(T, ", ", 2, 3))  -- b, c
        ```

- `table.move(a, f, e, t[, dest])` *(Lua 5.3+)*

    - Moves elements from table `a`, from index `f` to `e`, into
      position `t`.

    - If `dest` is given, it is the destination table; otherwise, `a` is used.

        ```lua
        local T = {2, 3, 4, 5}
        table.move(T, 1, #T, 2)
        T[1] = 1
        -- T is now {1, 2, 3, 4, 5}
        ```

- `table.sort(t[, comp])`

    - Sorts elements in a given order, *in-place*.

    - If `comp` is given, then it must be a function that receives
      two list elements and returns `true` when the first element must come
      before the second in the final order. If `comp` is not given, then the
      standard Lua operator `<` is used instead.

        ```lua
        local T = {"John", "Mary", "Thomas"}

        local function comp(a, b)
            return string.sub(a, 2, 2) > string.sub(b, 2, 2)
        end

        table.sort(T, comp)
        -- T is now {John, Thomas, Mary}
        ```

# Functions

## Basic Expression

Functions are first class in Lua:

```lua
local function add(a, b)
    return a + b
end
```

Equivalent:

```lua
local add
add = function(a, b)
    return a + b
end
```

When calling a function with one string or table argument, parentheses are
optional (`print "Hello"`).

## Function Parameters

```lua
function add(a, b) return a + b end
add(3, 4)   -- a=3, b=4
add(3, 4, 5)-- extra discarded
add(3)      -- a=3, b=nil
```

## Default Arguments

```lua
function add(a, b)
    b = b or 10
    return a + b
end

print(add(3)) --> 13
```

## Returning Multiple Values

```lua
function arith(a, b)
    return a+b, a-b, a*b
end

local r1, r2, r3, r4 = arith(5,4)
print(r1, r2, r3, r4) --> 9 1 20 nil
```

If a function call is not the last item in a list, it returns only its first
value.

```lua
local a, b, c, d = arith(5,4), 10
print(a, b, c, d) --> 9 10 nil nil
```

Use a table to return multiple values and `table.unpack` to expand them:

```lua
local function arith(a, b)
    return {a+b, a-b, a*b}
end

local k, l, m = table.unpack(arith(5,4))
print(k, l, m) --> 9 1 20
```

## Variable Number of Arguments

```lua
local function average(...)
    local sum = 0
    local arg = {...}
    for _, value in ipairs(arg) do
        sum = sum + value
    end
    return sum / #arg
end

print(string.format("The average is %.f.", average(10,5,3,4,5,6)))
```

## Non-Global Functions

Store functions in tables:

```lua
local M = {}

function M.gcd(a, b)
    if b ~= 0 then
        return M.gcd(b, a % b)
    else
        return math.abs(a)
    end
end

print(M.gcd(8, 12)) --> 4
```

## Closures

We have a **closure** when:

-   a nested function references a value (called an *upvalue* in Lua
    lingo) of its enclosing function, and then

-   the enclosing function returns the nested function

### Simple Class

Closures can be used to mimic a simple class (in object-oriented languages)
with instance variables and methods.

``` lua
local function f()
    -- this variable will be captured by the closure
    -- it acts like an instance variable
    local v = 0
    -- nested function
    -- it acts like an instance method
    local function get()
        return v
    end
    -- another nested function
    local function set(new_v)
        v = new_v
    end
    -- enclosing function returns nested functions
    return {get=get, set=set}
end

local t = f() -- create an instance of the closure
print(t.get()) --> 0
t.set(5)
print(t.get()) --> 5
```

### Iterator Functions

Another common use of closures is to create custom iterator functions. In the
example below, we build a custom iterator that returns the next number of a
power series of a given length.

``` lua
function power_iter(exp, len) -- exp = exponent, len = length of the series
    local iter = 1 -- variable to keep track of where we are in the series

    return function ()
        -- the closure captures variables: exp, len, iter
        if iter <= len then
            local res = math.pow(iter, exp)
            iter = iter + 1
            return res
        else
            return nil
        end
    end

end
```

We can use the iterator in two ways:

``` lua
local square = power_iter(2, 5) -- square series of length 5

while true do
    local num = square() -- call iterator to return the next value
    if num == nil then break end
    io.write(num, " ") --> 1  4  9  16  25
end
```

A downside to using the iterator as we did above is that once that
iterator reaches the end, it becomes exhausted and can no longer be
used.

The second way to use the iterator is given below.

``` lua
for num in power_iter(3, 4) do
    io.write(num, " ") --> 1  8  27  64
end
```

# Metatables

## Tables as Unordered Sets

A set is a data structure in which all the items are unique. An easy way
to implement sets in Lua is to store items in the keys of a table and
setting the values to a dummy value (like `true`). Doing this will help
you use a table like an unordered set with fast insertion and removal
since there is no need to shift the items in the table when an item is
added or removed. Also, when checking whether an item is in the set,
instead of searching the table for a given element, you just index the
table and test whether the returned value is `nil` or not.

``` lua
-- a function that makes a table behave like a set
local function Set (list)
    local set = {}
    for _, v in ipairs(list) do
        set[v] = true
    end
    return set
end

local s1 = Set {1, 2, 3, 2, 4} --> s1 = {1, 2, 3, 4}
```

Now that we\'ve found a way to use tables to represent sets, how can we use
operators such as `+` and `-` to find the union and difference of two sets?
This is where [**metatables**](https://www.lua.org/pil/13.html) and
**metamethods** come to the rescue.

Suppose we want the addition operator (`+`) to compute the union of two sets.
Clearly, Lua does not know the mathematical definition of the union of two
sets. We can tell it by creating a function that implements the union operation
and then associate this function with the `+` operator.

Let us call the union function associated with the `+` operator a
**metamethod**. This is nothing new. This is known as operator overloading in
other programming languages. What is new is that we need to inform all `Set`
objects of the existence of this metamethod so that the expression `s1 + s2`
calls our union function on the two sets.

The way this is done is to define all our functions in a separate table, called
a **metatable**, and then inform our objects to inherit from this table using
the `setmetatable` function.

When you create a new table, Lua does not give it a metatable. That is, by
default a table will have a `nil` value for its metatable. The steps required
to assign a metatable to our `Set` object are listed below:

-   Create a regular table that we will use as the metatable for our
    sets. For example, `Set.mt = {}`.

-   To use the `+` operator, we redefine the reserved function `__add`
    of the metatable `Set.mt` to implement the union operation.

-   Finally, we associate each of our `Set` objects (which are tables)
    with the metatable.

Complementary to the `setmetatable` method, you can retrieve the
metatable of a table using the `getmetatable` method.

``` lua
Set = {}

-- create a metatable for Set
Set.mt = {}

-- method to make a table behave like a set object
function Set.new (list)
    local set = {}
    setmetatable(set, Set.mt) -- associate each set object with the metatable
    for _, v in ipairs(list) do set[v] = true end
    return set
end

-- metamethod that allows us to use + to compute the union of two sets
function Set.mt.__add (a, b)
    local res = Set.new {}
    for k in pairs(a) do res[k] = true end
    for k in pairs(b) do res[k] = true end
    return res
end

-- metamethod that allows us to use tostring(obj)
function Set.mt.__tostring (set)
    local s = "{"
    local sep = ""
    for e in pairs(set) do
        s = s .. sep .. e
        sep = ", "
    end
    return s .. "}"
end

local s1 = Set.new {1, 2, 3}
local s2 = Set.new {3, 4, 5}
local s3 = s1 + s2

print( s1 + s2 ) --> {1, 2, 3, 4, 5}
```

For each arithmetic operator there is a corresponding field name in a
metatable. Besides `__add`, there are:

-   `__sub` (for subtraction)
-   `__mul` (for multiplication)
-   `__div` (for division)
-   `__unm` (for negation)
-   `__pow` (for exponentiation)
-   `__mod` (for modulo)
-   `__concat` (for the concatenation operator `..`).

For relational operators, there are:

-   `__eq` (*equality*)
-   `__lt` (*less than*)
-   `__le` (*less or equal*)

There are no separate metamethods for the other three relational
operators, as Lua translates `a ~= b` to `not (a == b)`, `a > b` to
`b < a`, and `a >= b` to `b <= a`.

Other useful metamethods include:

-   `__tostring`, which is used for string representation.
-   `__call`, which makes the object callable.
-   `__index`, which specifies how we retrieve values from missing keys
    in a table.
-   `__newindex`, which specifies how we assign values to missing keys.

We make use of the simple example below to demonstrate how `__index` and
`__newindex` work.

``` lua
local P = { x=10 } -- P has only one field

-- let's put some default values in the metatable
local meta = { x=0, y=0 }

-- let's add the __index metamethod to the metatable
meta.__index = function(table, key)
    return meta[key]
end

-- let's add the __newindex metamethod to the metatable
meta.__newindex = function(table, key, value)
    meta[key] = value
end

-- Now, let's associate P with the metatable
setmetatable(P, meta)

print( P.x, P.y, P.z ) --> 10  0  nil

P.z = 20

print( P.x, P.y, P.z ) --> 10  0  20
```

In the above snippet, when we call `P.x`, since `P` has a `x` field, the
value of `x` is returned. When we call `P.y`, Lua sees that `P` does not
have a `y` field, but is associated a metatable that has an `__index`
metamethod. Lua then calls the `__index` method with `P` and `y`. In the
example here, the metamethod indexes itself. This is because the
metatable is `meta` and we are searching for `y` inside `meta`. In cases
where the `__index` metamethod is just indexing the metatable, we can
replace the entire function with just `meta.__index = meta`. If `y` is
found inside the metatable, the value of `y` is returned, otherwise
`nil` is returned.

Finally, when we execute `P.z = 20`, Lua sees that `P` does not have a
`z` field but has a metatable with a `__newindex` metamethod. Lua then
calls the `__newindex` metamethod and assigns a new key/value pair to
`meta`.

## Object Oriented Programming

In many OO languages, **classes** can be thought of as the templates
from which **objects** can be created. The class definition typically
specifies **instance variables**, also known as data members or data
attributes, that the object contains, as well as the **methods**, also
known as member functions, that the object can execute.

Lua does not have the concept of a class. However, we can use tables to
emulate its functionality. We already know enough to build a simple
class. The steps are outlined below:

-   We create a namespace for the class. For example, `MyClass = {}`.
-   We then create a class prototype table that contains the data
    attributes and methods that all object will share.
-   Next, we create a class metatable in which we can define our
    metamethods and also use to index the prototype table so that
    objects can inherit from the prototype.
-   Finally, we create a constructor function where we set the metatable
    of all newly created objects to that of the class metatable.

``` lua
local Vector = {} -- our class

-- class data members and methods go in the prototype
Vector.prototype = { x=0, y=0, z=0 }

-- metamethods go in the metatable
-- metatable also indexes the prototype table
Vector.mt = { __index = Vector.prototype }

-- constructor
function Vector.new (obj)
    obj = obj or {}   -- create object if user does not provide one
    setmetatable(obj, Vector.mt)
    return obj
end

-- metamethod
Vector.mt.__add = function(v1, v2)
    local vec = Vector.new()
    vec.x = v1.x + v2.x
    vec.y = v1.y + v2.y
    vec.z = v1.z + v2.z
    return vec
end

-- prototype method
Vector.prototype.translate = function (vec, dy, dx, dz)
    vec.x = vec.x + dx
    vec.y = vec.y + dy
    vec.z = vec.z + dz
end

local v1 = Vector.new {x=10,y=10,z=10}
local v2 = Vector.new {x=15, y=15}
local v3 = Vector.new()

v3 = v1 + v2
v1.translate(v1, 10, 10, 10)

print( v1.x, v1.y, v1.z ) --> 20  20  20
print( v2.x, v2.y, v2.z ) --> 15  15  0
print( v3.x, v3.y, v3.z ) --> 25  25  10
```

The above code works as expected but it\'s a little bit verbose:

- we have to explicitly create a metatable.

- the notation used to apply the `translate` method on the object is a
little bit inconvenient.

Fortunately, there is a solution to these two issues:

For the first issue, we arrange for all new objects to inherit their
operations directly from `Vector`. We can reference `Vector` with the
`self` keyword. All we then need to do is set the metatable of new
objects to `self` and set the `__index` metamethod of `self` to point to
`self`.

As for the second issue, we can also use the `self` keyword to point to
the object that called the method. So,
`Vector.translate (vec, dy, dx, dz)` becomes
`Vector.translate (self, dy, dx, dz)`. While this doesn\'t seem to have
solved the issue of the inconvenient notation, Lua offers the `:`
operator to allow us to hide `self` from the parameter list (even though
it is there) and get instead `Vector:translate (dy, dx, dz)`.

``` lua
Vector = {  x=0, y=0, z=0 } -- our class

-- constructor
function Vector:new (obj)
    obj = obj or {}   -- create object if user does not provide one
    setmetatable(obj, self)
    self.__index = self
    return obj
end

-- metamethod
Vector.__add = function(v1, v2)
    local vec = Vector:new()
    vec.x = v1.x + v2.x
    vec.y = v1.y + v2.y
    vec.z = v1.z + v2.z
    return vec
end

-- prototype method
function Vector:translate (dy, dx, dz)
    self.x = self.x + dx
    self.y = self.y + dy
    self.z = self.z + dz
end

local v1 = Vector:new {x=10,y=10,z=10}
local v2 = Vector:new {x=15, y=15}
local v3 = Vector:new()

v3 = v1 + v2
v1:translate(10, 10, 10)

print( v1.x, v1.y, v1.z ) --> 20  20  20
print( v2.x, v2.y, v2.z ) --> 15  15  0
print( v3.x, v3.y, v3.z ) --> 25  25  10
```

# Packages

Lua does not provide any explicit mechanism for organizing code in
packages. However, we can implement them easily by a table, as the basic
libraries do.

All the functions defined inside the package can be called from outside
the package. If we do not want a function to be accessible from outside
the package, we can declare it `local`.

When using tables for packages, we must explicitly put the package name
in every function definition and a function that calls another function
inside the same package must prefix the function name with the package
name. We can ameliorate these problems by using a fixed local name for
the package (`M`, for instance).

``` lua
local M = {} -- all definitions go inside this table

local function fib_r (n)
    if n <= 1 then return n else return fib1(n-1) + fib1(n-2) end
end

function M.fib_m (n)
    local memo = {1, 1}
    local function inner (n)
        if memo[n] == nil then
            memo[n] = inner(n - 1) + inner(n - 2)
        end
        return memo[n]
    end
    return inner(n)
end

function M.fib_t (n)
    local T = {}
    T[1], T[2] = 0, 1
    for i=1,n-1 do
        T[i+1] = T[i+1] + T[i]
        T[i+2] = T[i]
    end
    T[#T] = T[#T] + T[#T-1]
    return T[#T]
end

return M
```

A drawback of this approach is its verbosity when accessing other public
entities inside the same package, as every access still needs the prefix
`M`. A bigger problem is that we have to change the calls whenever we
change the status of a function from private to public (or from public
to private).

A solution to this problem is to declare all functions in our package as
`local` and later put them in the final table to be exported.

``` lua
local function fib_r (n)
    if n <= 1 then return n else return fib1(n-1) + fib1(n-2) end
end

local function fib_m (n)
    local memo = {1, 1}
    local function inner (n)
        if memo[n] == nil then
            memo[n] = inner(n - 1) + inner(n - 2)
        end
        return memo[n]
    end
    return inner(n)
end

local function fib_t (n)
    local T = {}
    T[1], T[2] = 0, 1
    for i=1,n-1 do
        T[i+1] = T[i+1] + T[i]
        T[i+2] = T[i]
    end
    T[#T] = T[#T] + T[#T-1]
    return T[#T]
end

-- MyPackage is global, so no need for `return MyPackage`
MyPackage = {
    fib_r = fib_r,
    fib_t = fib_t
}
```

Finally, to make the functions in the package accessible in another
file, we simply do:

`local some_name = require "MyPackage"`

To call a function from the package, we use `some_name.func_name`.

# The Environment

Lua keeps all its global variables in a regular table, called the
**environment**, and the the environment itself in a global variable `_G`.

Because the environment is a regular table, you can simply index it with
the desired key (the variable name): `value = _G[varname]`. This makes
it possible to retrieve the value of a global variable when a local
variable of the same name exists.

``` lua
x = 10 -- global
do
    local x = 20
    print(_G["x"], x) --> 10  20
end
```

In a similar way, you can assign to a global variable whose name is
computed dynamically, writing `_G[varname] = value`.
