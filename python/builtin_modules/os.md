# os

The [`os`](https://docs.python.org/3/library/os.html) module provides functions
for interacting with the operating system. It allows you to perform a wide
range of tasks, such as reading and writing files, creating and deleting
directories, and starting processes.

## Methods

Here is a list of some of the most commonly used functions in the `os` module:

- `os.getcwd()`: Returns the current working directory.

- `os.chdir(path)`: Changes the current working directory to the specified `path`.

- `os.listdir(path)`: Returns a list of the files and directories in the specified `path`.

- `os.mkdir(path)`: Creates a new directory at the specified `path`.

- `os.rmdir(path)`: Deletes the specified directory.

- `os.rename(src, dst)`: Renames the file or directory at `src` to `dst`.

- `os.remove(path)`: Deletes the specified file.

- `os.environ`: A dictionary containing the current environment variables.

- `os.system(command)`: Executes the specified command in the operating system's shell.

## os.path

The `os.path` module is a submodule of the `os` module that provides functions
for working with file and directory paths. It allows you to perform tasks such
as checking whether a file or directory exists, getting the file size, and
extracting the file name and extension.

Here are some of the most commonly used functions in the `os.path` module:

- `os.path.exists(path)`: Returns `True` if the specified `path` exists, and
  `False` otherwise.

- `os.path.isfile(path)`: Returns `True` if the specified `path` is a file, and
  `False` otherwise.

- `os.path.isdir(path)`: Returns `True` if the specified `path` is a directory,
  and `False` otherwise.

- `os.path.getsize(path)`: Returns the size of the file at the specified `path`
  in bytes.

- `os.path.splitext(path)`: Returns a tuple containing the root and extension
  of the file at the specified `path`.

- `os.path.split(path)`: This function splits the specified `path` into a tuple
  containing the head (i.e. the directory component) and the tail (i.e. the
  base name).

- `os.path.join(path, *paths)`: Joins the specified `path` and `paths` into a
  single path.

- `os.path.abspath(path)`: Returns the absolute path of the specified `path`.

- `os.path.dirname(path)`: Returns the directory name (i.e. the portion of the
  path up to the last slash) for the specified `path`.

- `os.path.basename(path)`: Returns the base name (i.e. the last component of
  the path) for the specified `path`.

- `os.path.realpath(path)`: Returns the real path of the specified `path`
  (i.e., follows symbolic links).

- `os.path.expanduser(path)`: Expands the `~` character to the user's home
  directory.

- `os.path.expandvars(path)`: Expands any environment variables in the
  specified `path`.
