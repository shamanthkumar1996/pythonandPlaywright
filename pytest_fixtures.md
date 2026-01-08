Here are **clean, copy-paste–ready notes** on the pytest fixture code 👇

---

## Pytest Fixture – Function Scope (Notes)

### Code

```python
@pytest.fixture(scope="function")
def fixture_function_scope():
    print("\n[SETUP] Function scope - running ONCE per test function")
    yield "function_data"
    print("[TEARDOWN] Function scope cleanup")
```

---

### What is a fixture?

* A **pytest fixture** is used to provide setup and teardown logic for tests.
* Fixtures supply data or state to test functions.
* Tests request fixtures by name as parameters.

---

### `@pytest.fixture(scope="function")`

* Declares the function as a pytest fixture.
* `scope="function"` means:

  * Fixture runs **once for each test function**
  * Each test gets a **fresh instance**
* This is the **default scope** in pytest.

---

### Fixture function name

```python
def fixture_function_scope():
```

* The function name is how tests access the fixture.
* Example:

```python
def test_example(fixture_function_scope):
    ...
```

---

### Setup phase

```python
print("\n[SETUP] Function scope - running ONCE per test function")
```

* Runs **before the test starts**
* Used to initialize resources or data.

---

### `yield "function_data"`

* Separates **setup** and **teardown**
* Everything **before `yield`** → setup
* Everything **after `yield`** → teardown
* `"function_data"` is the value passed into the test.

Inside the test:

```python
fixture_function_scope == "function_data"
```

---

### Teardown phase

```python
print("[TEARDOWN] Function scope cleanup")
```

* Runs **after the test finishes**
* Executes even if the test fails
* Used for cleanup (closing files, DB connections, etc.)

---

### Execution order (per test)

1. Setup code runs
2. Test function runs
3. Teardown code runs

---

### Key points

* Runs **once per test function**
* Uses `yield` instead of `return`
* Supports automatic cleanup
* Ensures test isolation

---

If you want, I can also prepare:

* **One-page fixture comparison table**
* **Example with multiple tests**
* **Notes for class/module/session scope**

Just tell me 👍
