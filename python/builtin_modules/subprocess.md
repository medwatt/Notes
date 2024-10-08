# subprocess

The [`subprocess`](https://docs.python.org/3/library/subprocess.html) module
allows you to start new processes and interact with their stdin, stdout, and
stderr streams. It provides a high-level interface for running commands and
waiting for their completion, as well as a lower-level interface for more
fine-grained control over the process execution.

## Methods

Here is a list of some of the most commonly used functions in the `subprocess`
module:

- `subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None,
  shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None,
  universal_newlines=None, env=None)`: Run the specified command and wait for
  it to complete. Returns a `CompletedProcess` object containing the exit code,
  stdout, and stderr of the process.

- `subprocess.Popen(args, *, stdin=None, stdout=None, stderr=None, shell=False,
  cwd=None, env=None)`: Start a new process and return a `Popen` object that
  can be used to interact with the process's stdin, stdout, and stderr streams.

- `subprocess.Popen.communicate(input=None, timeout=None)`: Send data to the
  process's stdin and read from its stdout and stderr streams until the process
  completes. Returns a tuple containing the stdout and stderr of the process.

- `subprocess.Popen.wait(timeout=None)`: Wait for the process to complete and
  return the exit code.

- `subprocess.Popen.terminate()`: Terminate the process.

Here is a brief explanation of some of the arguments that are commonly used in
the `subprocess` module:

- `args`: A list or tuple containing the command and its arguments to be run.

- `stdin`, `stdout`, `stderr`: File-like objects or file descriptors to be used
  as the process's standard input, output, and error streams, respectively.

- `shell`: A boolean indicating whether the command should be run in a shell.

- `cwd`: The current working directory of the process.

- `timeout`: A timeout in seconds after which the process will be terminated.

- `check`: A boolean indicating whether a `CalledProcessError` should be raised
  if the process exits with a non-zero exit code.

- `encoding`, `errors`: The encoding and error handling used to decode the
  process's stdout and stderr.

- `universal_newlines`: A boolean indicating whether the process's stdout and
  stderr should be decoded as universal newlines.

- `env`: A dictionary of environment variables to be passed to the process.

## Example

```python
from subprocess import run, Popen, PIPE, STDOUT

# Run a command and store the output
p = run(['grep', 'f'],
        stdout=PIPE,
        input='one\ntwo\nthree\nfour\nfive\nsix\n',
        encoding='ascii'
        )
print(p.returncode)
print(p.stdout)

# Same but with Popen
p = Popen(['grep', 'f'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
out, err = p.communicate(input='one\ntwo\nthree\nfour\nfive\nsix\n'.encode())
print(out)
```

`PIPE` is a constant that represents a pipe to be used for streaming data
between processes. It is commonly used as the value for the `stdin`, `stdout`,
or `stderr` arguments of the `subprocess.Popen` constructor or the `run`
function to redirect the process's standard input, output, or error streams.
