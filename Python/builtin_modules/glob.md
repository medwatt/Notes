# glob

The [`glob`](https://docs.python.org/3/library/glob.html) module provides
functions for matching files and directories using glob patterns. Glob
patterns are similar to regular expressions, but simpler.

Here are some common glob patterns and examples of how they can be used to
match files and directories.

- `*`: Matches any number of characters, except for path separators (e.g. `/`
  on Unix-like systems). For example, the glob pattern `*.txt` would match the
  files `file1.txt`, `file2.txt`, `my_file.txt`, etc.

- `?`: Matches any single character, except for path separators. For example,
  the glob pattern `file?.txt` would match the files `file1.txt` and
  `file2.txt`, but not `file12.txt` or `file.txt`.

- `[...]`: Matches any single character within the brackets. For example, the
  glob pattern `file[0-3].txt` would match the files `file0.txt`, `file1.txt`,
  `file2.txt`, and `file3.txt`, but not `file4.txt` or `file12.txt`.

- `[!...]`: Matches any single character that is not within the brackets. For
  example, the glob pattern `file[!0123].txt` would match the files
  `file4.txt`, `file5.txt`, etc., but not `file0.txt`, `file1.txt`,
  `file2.txt`, or `file3.txt`.

- `{a,b,...}`: Matches any of the comma-separated patterns. For example, the
  glob pattern `file{1,2,3}.txt` would match the files `file1.txt`,
  `file2.txt`, and `file3.txt`, but not `file4.txt` or `file12.txt`.

Note: This module doesn't expand tilde `(~)` and shell variables.

## Methods

There are several methods available in the `glob` module:

- `glob.glob(pattern)`: This function returns a list of file paths that match
  the given pattern.

- `glob.iglob(pattern)`: This function is similar to `glob.glob()`, but it
  returns an iterator instead of a list. This can be useful if you want to
  process the files one at a time, rather than reading them all into memory at
  once.

- `glob.escape(pattern)`: This function escapes all special characters in a
  pattern, so that it can be used as a literal string in a filesystem
  operation.

```python
import glob

# Find all files ending in '.txt' in the current directory files =
glob.glob('*.txt')

# Find all files ending in '.txt' in the '/tmp' directory files =
glob.glob('/tmp/*.txt')

# Iterate over all files ending in '.txt' in the current directory for file in
glob.iglob('*.txt'): print(file)

# Escape a pattern to use it as a literal string pattern = r'[abc]'
escaped_pattern = glob.escape(pattern)
```
