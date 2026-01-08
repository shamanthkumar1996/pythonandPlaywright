import pytest

# FIXTURE EXPLANATION:
# A fixture is a reusable function that provides setup/teardown for tests.
# It can return data, configure state, or perform cleanup operations.
# Tests request fixtures as parameters, and pytest injects them automatically.

# ============= FUNCTION SCOPE (default) =============
# Runs ONCE per test function that uses it
@pytest.fixture(scope="function")
def fixture_function_scope():
    print("\n[SETUP] Function scope - running ONCE per test function")
    yield "function_data"
    print("[TEARDOWN] Function scope cleanup")

# ============= CLASS SCOPE =============
# Runs ONCE per test class
@pytest.fixture(scope="class")
def fixture_class_scope():
    print("\n[SETUP] Class scope - running ONCE per test class")
    yield "class_data"
    print("[TEARDOWN] Class scope cleanup")

# ============= MODULE SCOPE =============
# Runs ONCE per module (file)
@pytest.fixture(scope="module")
def fixture_module_scope():
    print("\n[SETUP] Module scope - running ONCE for entire module")
    yield "module_data"
    print("[TEARDOWN] Module scope cleanup")

# ============= SESSION SCOPE =============
# Runs ONCE for the entire test session (all tests)
@pytest.fixture(scope="session")
def fixture_session_scope():
    print("\n[SETUP] Session scope - running ONCE for all tests")
    yield "session_data"
    print("[TEARDOWN] Session scope cleanup")

# ============= PACKAGE SCOPE =============
# Runs ONCE per package
@pytest.fixture(scope="package")
def fixture_package_scope():
    print("\n[SETUP] Package scope - running ONCE per package")
    yield "package_data"
    print("[TEARDOWN] Package scope cleanup")


# ============= TEST EXAMPLES =============
@pytest.mark.smoke
def test_function_scope_1(fixture_function_scope):
    print(f"Test 1 with: {fixture_function_scope}")
    assert fixture_function_scope == "function_data"

@pytest.mark.skip(reason="This test is under development")
def test_function_scope_2(fixture_function_scope):
    print(f"Test 2 with: {fixture_function_scope}")
    assert fixture_function_scope == "function_data"

@pytest.mark.smoke
def test_module_scope_1(fixture_module_scope):
    print(f"Test 3 with: {fixture_module_scope}")
    assert fixture_module_scope == "module_data"

@pytest.mark.skip(reason="Waiting for API fix")
def test_module_scope_2(fixture_module_scope):
    print(f"Test 4 with: {fixture_module_scope}")
    assert fixture_module_scope == "module_data"

@pytest.mark.smoke
def test_session_scope(fixture_session_scope):
    print(f"Test 5 with: {fixture_session_scope}")
    assert fixture_session_scope == "session_data"
