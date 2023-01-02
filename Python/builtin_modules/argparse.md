# argparse

The [`argparse`](https://docs.python.org/3/library/argparse.html) module
provides functions for parsing command-line arguments. It allows you to define
the arguments that your program accepts, and provides a convenient interface
for parsing those arguments from the command line.

## Methods

Here are some of the most commonly used functions in the `argparse` module:

- `ArgumentParser`: The main class for parsing command-line arguments. It
  provides methods for defining the arguments that your program accepts and for
  parsing the command-line arguments.

- `add_argument(...)`: A method of the `ArgumentParser` class that is used to
  define an argument that your program accepts. You can specify the name or
  flags of the argument, as well as other options such as the argument's type
  and whether it is required.

- `parse_args(...)`: A method of the `ArgumentParser` class that is used to
  parse the command-line arguments. It returns an `Namespace` object that
  contains the values of the arguments as attributes.

## Example

```python
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Define an argument
parser.add_argument("-n", "--name", required=True, help="Your name")

# Define an optional argument with a default value
parser.add_argument("-o", "--output_file", default="output.txt", help="Output file (default: output.txt)")

# Define an optional argument that takes an integer value
parser.add_argument("-l", "--lines", type=int, help="Number of lines to process")

# Define a mutually exclusive group of arguments
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true", help="Verbose mode")
group.add_argument("-q", "--quiet", action="store_true", help="Quiet mode")

# Parse the command-line arguments
args = parser.parse_args()
```

Here is an example program that uses the `argparse` module to parse
command-line arguments:

```python
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="Example program")

# Define an argument
parser.add_argument("-n", "--name", required=True, help="Your name")

# Define a mutually exclusive group of arguments
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true", help="Verbose mode")
group.add_argument("-q", "--quiet", action="store_true", help="Quiet mode")

# Parse the command-line arguments
args = parser.parse_args()

# Print a message based on the arguments
if args.verbose:
    print("Hello, {}! How are you today?".format(args.name))
elif args.quiet:
    print("Hello, {}!".format(args.name))
else:
    print("Hi, {}!".format(args.name))
```

To run this program, you can use the following command:

```python
python program.py -n John -v
```
