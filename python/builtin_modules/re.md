# Regular Expressions

The [`re`](https://docs.python.org/3/library/re.html) module provides regular
expression matching operations similar to those found in Perl.

## Methods

Here are some of the most commonly used methods in the `re` module:

- `re.match(pattern, string)`: This method searches for a pattern at the
  beginning of the string. If the pattern is found, it returns a match object.
  If the pattern is not found, it returns `None`.

- `re.search(pattern, string)`: This method searches for the first occurrence
  of the pattern in the string. If the pattern is found, it returns a match
  object. If the pattern is not found, it returns `None`.

- `re.findall(pattern, string)`: This method returns a list of all
  non-overlapping occurrences of the pattern in the string.

- `re.compile(pattern, flags=0)`: This method compiles a regular expression
  pattern into a regular expression object, which can be used for matching
  using its `match()`, `search()`, and `findall()` methods. Using
  `re.compile()` can be more efficient if you need to use the same regular
  expression pattern multiple times in your code, because it allows you to
  compile the pattern once and reuse the regular expression object.

  ```python
  pattern = re.compile("world")
  result = pattern.search("Hello, world!")
  ```

- `re.sub(pattern, repl, string)`: This method replaces all occurrences of the
  pattern in the string with the specified replacement string.

## Match Object

A match object is an object that represents the search result of a successful
call to the functions `re.match()` and `re.search()`.

A match object has several methods that you can use to retrieve information
about the search. Here are some of the most commonly used methods:

- `match.group([group1, …])`: This method returns the string matched by the
  regular expression. If the `group()` method is called with one or more group
  numbers, it returns the string matched by the corresponding group.

  ```python
  string = "My name is John Smith"
  result = re.search(r"My name is (\w+) (\w+)", string)
  first_name = result.group(1)
  last_name = result.group(2)
  ```

- `match.start([group])`: This method returns the start position of the match.
  If the `start()` method is called with a group number, it returns the start
  position of the corresponding group.

- `match.end([group])`: This method returns the end position of the match. If
  the `end()` method is called with a group number, it returns the end position
  of the corresponding group.

## Flags

There are several flags that you can use in the `re` module to modify the
behavior of regular expression matching. You can specify flags using the
`flags` parameter in the `re.compile()` function or as inline options in the
pattern string.

Here is a list of the commly-used flags that you can use in the `re` module,
along with how they can be used inline and some examples:

- `re.IGNORECASE`: This flag specifies that the regular expression should be
  case-insensitive. Inline: `(?i)`

- `re.MULTILINE`: This flag specifies that the `^` and `$` anchor characters
  should match the beginning and end of each line (in addition to the beginning
  and end of the string), rather than the beginning and end of the entire
  string. Inline: `(?m)`

- `re.DOTALL`: This flag specifies that the `.` wildcard should match any
  character, including newline characters. Inline: `(?s)`

## Example

```python
import re

# Find all occurrences of a pattern in a string
pattern = r"\d+"  # This is a regular expression that matches one or more digits
string = "There are 12 apples and 45 oranges"

# Use the findall function to find all occurrences of the pattern in the string
result = re.findall(pattern, string)
print(result)  # Output: ['12', '45']
```

```python
import re

# Define a regular expression with two groups
pattern = r"(\d+)\s+(\w+)"
string = "I have 12 apples and 45 oranges"

# Use the match function to match the string against the regular expression
match = re.match(pattern, string)

# Check if a match was found
if match:
    # Access the groups using the group method of the Match object
    count = match.group(1)  # This is the first group, which matches one or more digits
    fruit = match.group(2)  # This is the second group, which matches one or more word characters
    print(f"I have {count} {fruit}")
else:
    print("No match found")

# Output: "I have 12 apples"
```

```python
import re

# Define a regular expression with two groups
pattern = r".*?(\d+)\s+apples.*?(\d+)\s+oranges"
string = "I have 12 apples and 45 oranges"

# Define a replacement string that includes the groups from the pattern
replacement = r"Number of apples: \1, Number of oranges: \2"

# Use the sub function to replace all occurrences of the pattern with the replacement string
result = re.sub(pattern, replacement, string)
print(result)  # Output: Number of apples: 12, Number of oranges: 45
```

```python
import re

# Split a string by a pattern
pattern = r"\W+"  # This is a regular expression that matches one or more non-word characters
string = "Hello, World!"

# Use the split function to split the string by the pattern
result = re.split(pattern, string)
print(result)  # Output: ['Hello', 'World', '']

```
