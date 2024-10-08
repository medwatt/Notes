# Collections

The [`collections`](https://docs.python.org/3/library/collections.html) module
provides specialized container data types. These data types are designed to be
more efficient and flexible than the built-in Python containers (such as lists,
dictionaries, and tuples).

The `collections` module provides the following container data types:

- `namedtuple`: A subclass of tuple that allows you to access the elements of
  the tuple using named fields.

  ```python
  from collections import namedtuple

  # Define a named tuple type with two fields: 'x' and 'y'
  Point = namedtuple('Point', ['x', 'y'])

  # Create a new point object
  p = Point(1, 2)

  print(p.x)  # Output: 1
  print(p.y)  # Output: 2
  ```

- `deque`: A double-ended queue that supports efficient insertion and deletion
  from both ends.

  ```python
  from collections import deque

  # Create a new deque object
  queue = deque()

  # Enqueue elements to the right of the deque
  queue.append('a')
  queue.append('b')
  queue.append('c')

  print(queue)  # Output: deque(['a', 'b', 'c'])

  # Dequeue elements from the left of the deque
  print(queue.popleft())  # Output: 'a'
  print(queue.popleft())  # Output: 'b'

  # You can also enqueue elements to the left of the deque
  queue.appendleft('d')

  print(queue)  # Output: deque(['d', 'c'])
  ```

- `Counter`: A dictionary-like object that counts the number of occurrences of
  each element.

  ```python
  from collections import Counter

  # Create a list of elements
  elements = ['a', 'b', 'c', 'a', 'b', 'b']

  # Create a Counter object and count the number of occurrences of each element
  counter = Counter(elements)

  print(counter)  # Output: Counter({'b': 3, 'a': 2, 'c': 1})

  # You can access the count of an element using the [] operator
  print(counter['a'])  # Output: 2
  print(counter['b'])  # Output: 3
  print(counter['c'])  # Output: 1

  # You can also use the most_common method to get
  # the n most common elements and their counts
  print(counter.most_common(2))  # Output: [('b', 3), ('a', 2)]
  ```

- `defaultdict`: A dictionary-like object that returns a default value for keys
  that are not present in the dictionary.

  ```python
  from collections import defaultdict

  # Create a defaultdict with a default value of 0
  dd = defaultdict(lambda: 0)

  # You can access elements of the defaultdict using the [] operator
  print(dd['a'])  # Output: 0
  print(dd['b'])  # Output: 0

  # You can also set the value of an element using the [] operator
  dd['a'] = 1
  dd['b'] = 2

  print(dd['a'])  # Output: 1
  print(dd['b'])  # Output: 2
  ```

- `ChainMap`: A mapping that allows you to create a single view of multiple
  mappings.

  ```python
  from collections import ChainMap

  # Create two dictionaries
  d1 = {'a': 1, 'b': 2}
  d2 = {'b': 3, 'c': 4}

  # Create a ChainMap object from the dictionaries
  cm = ChainMap(d1, d2)

  # You can access the elements of the ChainMap using the [] operator
  # The `ChainMap` object searches for the key in the underlying dictionaries
  # in the order they were passed to the constructor.
  print(cm['a'])  # Output: 1
  print(cm['b'])  # Output: 2
  print(cm['c'])  # Output: 4

  # You can also use the keys, values, and items methods to get
  # the keys, values, and key-value pairs, respectively
  print(cm.keys())   # Output: ['a', 'b', 'c']
  print(cm.values()) # Output: [1, 2, 4]
  print(cm.items())  # Output: [('a', 1), ('b', 2), ('c', 4)]

  # You can update the values of the elements in the ChainMap
  # by updating the underlying dictionaries
  d1['a'] = 5
  d2['c'] = 6

  print(cm['a'])  # Output: 5
  print(cm['b'])  # Output: 2
  print(cm['c'])  # Output: 6
  ```

- `OrderedDict`: A dictionary-like object that preserves the order of the keys
  as they are added. In Python 3.7 and later, dictionaries are ordered by
  default, so you might not need to use `OrderedDict` as often as you did in
  earlier versions of Python.
