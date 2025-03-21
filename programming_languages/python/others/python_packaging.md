# Python Packaging

## Project Structure

A well-organized project structure makes the code more maintainable and easier
to navigate. Here is a standard structure for a Python project:

```{python}
project/
├── src/
│   ├── __init__.py
│   ├── package1/
│   │   ├── __init__.py
│   │   ├── module1.py
│   │   └── package1_1/
│   │       ├── __init__.py
│   │       └── module1_1.py
│   └── package2/
│       ├── __init__.py
│       ├── module2.py
│       └── package2_1/
│           ├── __init__.py
│           └── module2_1.py
├── tests/
│   └── test_module1.py
├── main.py
├── pyproject.toml
├── README.md
└── LICENSE
```

### Key Components:

- **`src/`**: Houses the main Python packages and modules.
- **`tests/`**: Contains test scripts for the code.
- **`pyproject.toml`**: Configuration file for build systems like setuptools.
- **`README.md`**: Documentation.
- **`LICENSE`**: License information.

## Defining a Package

In Python, a package is a way to organize related modules. To define a package:

1. **Create a directory**: This directory's name will be your package name.
2. **Add an `__init__.py` file**: This file tells Python that the directory is a package.

### The Role of `__init__.py`

The `__init__.py` file can be empty, but it can also serve several important functions:

- **Package Initialization**: Execute initialization code for the package.
- **Control Imports**: Define what symbols the package exports by setting
  the `__all__` list. This simplifies the import statements for users.

### Example of __init__.py

```{python}
# src/package1/__init__.py

# Re-exporting modules and functions
from .module1 import func1
from .package1_1.module1_1 import func1_1

__all__ = ['func1', 'func1_1']
```

By doing this, users can import functions directly from `package1`:

```{python}
from package1 import func1, func1_1
```

# Understanding Imports

## Absolute and Relative Imports

### Absolute Imports

Absolute imports specify the full path to the module from the project's root
directory. They are clear and unambiguous.

```{python}
from src.package1.package1_1.module1_1 import func1_1
```

### Relative Imports

Relative imports specify the module's location relative to the current module
using dot notation.

- **Single dot (`.`)**: Refers to the current package of the module.
- **Double dot (`..`)**: Refers to the parent package of the module.
- **Triple dot (`...`)**: Refers to the grandparent package of the module, and so on.

## Import Examples

- **Importing Inside `main.py`**: Located in the root, so absolute imports can
access modules in `src/`.

```{python}
# project/main.py

from src.package1.package1_1.module1_1 import func1_1

# Using the function
func1_1()
```

- **Importing Inside `module1.py`**: Relative imports provide simplicity
  and flexibility within a package.

```{python}
# project/src/package1/module1.py

# Importing from the sibling package module:
# project/src/package1/package1_1/module1_1.py
from .package1_1.module1_1 import func1_1

# Importing from a parent package module module:
# project/src/package2/module2.py
from ..package2.module2 import func2

# Using the imported functions
func1_1()
func2()
```

 - **Importing Inside `test_module1.py`**: Since `src` is not in
   the path of `test_module1.py`, modify `sys.path` to include `src`.

```{python}
# root/tests/test_module1.py

import sys
import os

# Let python know the path of the project (using absolute path)
# sys.path.append("/path/to/project/src")

# Let python know the path of the project (using relative path)
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from package1.module1 import func1

func1()
```

# Packaging The Project

Effective packaging includes setting up metadata, specifying dependencies, and
preparing the project for distribution.

## Creating `pyproject.toml`

The `pyproject.toml` file configures the build system and project metadata.

```{toml}

[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "your_project_name"
version = "0.1.0"
description = "A brief description of your project."
authors = [{ name = "Your Name", email = "your.email@example.com" }]
license = { file = "LICENSE" }
readme = "README.md"
requires-python = ">=3.7"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.urls]
"Documentation" = "https://github.com/yourusername/your_project_name#readme"
"Issue Tracker" = "https://github.com/yourusername/your_project_name/issues"

[project.dependencies]
requests = ">=2.25.1"
numpy = ">=1.19.2"
```

## Building the Package

Use the `build` module to create distribution files.

```{bash}
pip install build
python -m build
```

This command generates distribution files in the `dist/` directory:

- **Source Distribution (`.tar.gz`)**
- **Wheel Distribution (`.whl`)**

### Installing the Package Locally

For development purposes, install the package in editable mode:

```{bash}
pip install -e .
```

This allows you to modify your code and have the changes reflected without
reinstalling.

### Distributing the Package

#### Publishing to PyPI

1. **Create an account on [PyPI](https://pypi.org/).**

2. **Install Twine for uploading packages:**

    ```{bash}
    pip install twine
    ```

3. **Upload your package:**

    ```{bash}
    twine upload dist/*
    ```

4. **Install your package from PyPI:**

    ```{bash}
    pip install your_project_name
    ```
