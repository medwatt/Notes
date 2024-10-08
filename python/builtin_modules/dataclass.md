In Python, the @dataclass decorator is a function that modifies the behavior of
a class. It is part of the dataclasses module, which was introduced in Python
3.7.

The @dataclass decorator automates the generation of certain methods for a
class, such as the __init__ method (which is used to initialize instances of
the class) and the __repr__ method (which is used to create a string
representation of an instance).

To use the @dataclass decorator, you need to define a class as you normally
would, but with the @dataclass decorator applied to it. Then, you can define
class variables as usual, and the decorator will automatically generate the
necessary methods for you.

Here is an example of a simple class that uses the @dataclass decorator:

```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int
    occupation: str
    hobbies: list = field(default_factory=list)

    def add_hobby(self, hobby: str):
        self.hobbies.append(hobby)

p = Person("John", 30, "Software Developer")
p.add_hobby("Programming")
p.add_hobby("Cooking")

print(p)  # Output: "Person(name='John', age=30, occupation='Software Developer', hobbies=['Programming', 'Cooking'])"
```

In this example, the `Person` class has four attributes: `name`, `age`,
`occupation`, and `hobbies`. The `hobbies` attribute is a list, and it has a
default value of an empty list, which is specified using the `field` function
and the `default_factory` parameter.

The `Person` class also has a method called `add_hobby`, which allows us to add
a hobby to the person's list of hobbies.

When we create an instance of the `Person` class and call the `add_hobby`
method on it, the `@dataclass` decorator automatically generates the necessary
methods for us, such as the `__init__` method and the `__repr__` method. This
makes it easy to create and manipulate instances of the `Person` class.
