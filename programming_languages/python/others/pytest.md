# Introduction to pytest

`pytest` is a powerful and flexible testing framework for Python that
simplifies the process of writing and running tests.

## Why Use pytest?

- **Simplicity**: Write tests using plain Python functions without the need for classes or boilerplate code.
- **Powerful Assertions**: Enhanced assertion introspection provides detailed information on test failures.
- **Parameterization**: Run the same test with different inputs efficiently.
- **Fixtures**: Manage test setup and teardown efficiently using fixtures.
- **Plugins**: Extend functionality with a rich set of plugins.

## Installation

Install `pytest`:

```{bash}
pip install pytest
```

# Writing Tests with pytest

- **Test Files**: Should be named starting with `test_` or ending with `_test.py`.
- **Test Functions**: Should be named starting with `test_`.
- Use classes prefixed with `Test` to group tests.
- Use standard Python `assert` statements.

```{python}
# test_sample.py
class TestMathOperations:
    def test_multiplication(self):
        assert 2 * 3 == 6
    def test_division(self):
        assert 10 / 2 == 5
```

- Run all tests in a specific file: `pytest <filename>`.
- Run a specific test function: `pytest test_sample.py::test_function_name`
- Use `pytest -v` for verbose output.
- Use `pytest -x` to stop the test run after the first failure.

## Parameterizing Tests

Run the same test with different input values using `@pytest.mark.parametrize`.

```{python}
import pytest

@pytest.mark.parametrize('input, expected', [
    ('3+5', 8),
    ('2+4', 6),
    ('6*9', 54),
])
def test_eval(input, expected):
    assert eval(input) == expected
```

- The test `test_eval` runs three times with different inputs.

## Marking Tests

Use markers to categorize or modify test behavior.

- **`@pytest.mark.skip`**: Skip a test.
- **`@pytest.mark.skipif(condition)`**: Skip a test if a condition is true.
- **`@pytest.mark.xfail`**: Mark a test as expected to fail.

### Skipping Tests

```{python}
import sys
import pytest

@pytest.mark.skip(reason="Not implemented yet")
def test_unimplemented_feature():
    pass

@pytest.mark.skipif(sys.platform != 'win32', reason="Windows-specific test")
def test_windows_feature():
    assert perform_windows_operation() is True
```

### Expected Failures

```{python}
@pytest.mark.xfail(reason="Bug #123 not fixed")
def test_buggy_function():
    assert buggy_function() == 'expected result'
```

- If `test_buggy_function` fails, it is reported as `xfail`.
- If it unexpectedly passes, it is reported as `xpass`.

## Fixtures

Fixtures are functions that run before (and optionally after) test functions to
set up test conditions.

```{python}
import pytest

@pytest.fixture
def sample_list():
    # Setup: create a sample list
    return [1, 2, 3, 4, 5]

def test_sum(sample_list):
    assert sum(sample_list) == 15

def test_length(sample_list):
    assert len(sample_list) == 5
```

- Here, `sample_list` is a fixture that provides a list. It is passed as
  an argument to any test needing it.

- Each test that receives `sample_list` as an argument will automatically
  use the fixture, allowing for consistent setup across tests.

### Fixture Scope

Fixtures have a `scope` parameter that controls how often the fixture is executed:

- **Function (default)**: Executed once per test.
- **Class**: Executed once per test class.
- **Module**: Executed once per module.
- **Session**: Executed once per test session.

```{python}
@pytest.fixture(scope="module")
def db_connection():
    # Setup: Connect to database
    conn = create_connection()
    yield conn
    # Teardown: Close connection
    conn.close()

def test_query1(db_connection):
    assert db_connection.query("SELECT 1") == 1

def test_query2(db_connection):
    assert db_connection.query("SELECT 2") == 2
```

- Here, `db_connection` is only set up once for the entire module, saving
  time when multiple tests need the same setup.

- The `yield` statement divides setup and teardown; code after `yield`
  runs after each test using the fixture completes.

### Using autouse Fixtures

```{python}
@pytest.fixture(autouse=True)
def setup_env():
    os.environ['TEST_ENV'] = 'True'
    yield
    del os.environ['TEST_ENV']

def test_environment():
    assert os.getenv('TEST_ENV') == 'True'
```

- `setup_env` runs automatically before and after each test, setting and
  removing an environment variable. This is helpful for shared configurations
  across tests.

### Fixture Dependencies

Fixtures can depend on other fixtures by accepting them as arguments.

```{python}
@pytest.fixture
def base_number():
    return 10

@pytest.fixture
def multiplied_number(base_number):
    return base_number * 2

def test_multiplication(multiplied_number):
    assert multiplied_number == 20
```

- Here, `multiplied_number` depends on `base_number`. `pytest` resolves
  dependencies and ensures each fixture runs in the correct order.

### Fixture Parameters

You can parameterize fixtures to provide different values to the same fixture,
making it easier to test variations.

```{python}
@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

def test_square(number):
    assert number * number in [1, 4, 9]
```

- `params` allows `number` to take values `1`, `2`, and `3`, running
  `test_square` three times—once for each value of `number`.

# Plugins

`pytest` plugins extend the framework's functionality, providing additional
tools and features to enhance testing. Here, we'll cover two essential plugins:
`pytest-cov` for coverage and `pytest-mock`.

## pytest-cov: Code Coverage

`pytest-cov` measures code coverage, showing which parts of the code were
executed during tests. This is useful for identifying untested sections and
improving overall test quality.

### Installation

Install `pytest-cov` with pip: `pip install pytest-cov`.

### Usage

Run tests with `pytest --cov=<module_name>` to generate a coverage report. You
can specify multiple options for customizing the output:

- `--cov=<module_name>`: Specifies the module or package to measure.

- `--cov-report=term-missing`: Shows missing lines in the terminal output
  for easier identification of uncovered code.

- `--cov-report=html`: Generates an HTML report for a visual overview of
  code coverage, accessible in the `htmlcov` directory.

## pytest-mock: Mocking

`pytest-mock` provides a `mocker` fixture, which is a wrapper around the
`unittest.mock` module, simplifying the process of replacing parts of the code
during testing. This is helpful when testing isolated functionality without
relying on external dependencies.

### Installation

Install `pytest-mock` with pip: `pip install pytest-mock`.

### Usage

Use the `mocker` fixture to mock functions, classes, or methods in your tests.
It provides tools like `mocker.patch()` to temporarily replace objects for the
duration of a test.

```{python}
def test_api_call(mocker):
    # Mock an API call function
    mock_api = mocker.patch("my_module.api_call")
    mock_api.return_value = {"status": "success"}

    result = my_module.api_call()
    assert result["status"] == "success"
    mock_api.assert_called_once()
```

- `mocker.patch("<module.function>")`: Replaces the specified function or
  method with a mock object.

- `assert_called_once()`: Verifies that the mock was called exactly once.
