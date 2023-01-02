# shutil

The [`shutil`](https://docs.python.org/3/library/shutil.html) (shell utilities)
module  provides functions for high-level file operations such as copying and
deleting files and directories.

## Methods

Here is a list of some of the most commonly used functions in the shutil
module:

- `shutil.copy(src, dst)`: This function copies the file at the path specified
  by `src` to the location specified by `dst`. If `dst` is a directory, the
  file is copied into that directory with the same name as the original file.
  If `dst` is a file, the file is copied to that location with the new name.

- `shutil.copy2(src, dst)`: This function is similar to `shutil.copy()`, but it
  also attempts to preserve as much metadata as possible from the original
  file, including file permissions, modification times, and flags.

- `shutil.copytree(src, dst)`: This function copies the directory at the path
  specified by `src` and all its contents to the location specified by `dst`.
  If `dst` does not exist, it is created.

- `shutil.move(src, dst)`: This function moves the file or directory at the
  path specified by `src` to the location specified by `dst`. If `dst` is a
  directory, the file is moved into that directory with the same name as the
  original file. If `dst` is a file, the file is moved to that location with
  the new name.

- `shutil.rmtree(path)`: This function removes the directory at the specified
  path, as well as all its contents.

- `shutil.make_archive(base_name, format, root_dir)`: This function creates an
  archive of the directory at the path specified by `root_dir` and saves it to
  the file specified by `base_name`. The `format` argument specifies the format
  of the archive to be created (e.g. 'zip', 'tar', etc.).
