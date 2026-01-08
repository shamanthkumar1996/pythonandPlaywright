# PlayWright Automation Project

## Overview
This is a Playwright-based test automation project that combines **API testing** and **Web UI automation** for the Rahul Shetty Academy e-commerce platform. The project uses pytest as the testing framework and demonstrates both browser automation and REST API testing.

## Project Structure

```
PlayWright_automation/
├── automate_AmazonSite.py          # Amazon site automation tests
├── playwright_apitest.py           # E-commerce API + UI test
├── TestPyTestValidation.py         # Pytest fixture examples and patterns
├── pytest_fixtures.md              # Fixture documentation
├── readme.txt                       # Quick setup instructions
└── utils/
    └── apiBase.py                  # Reusable API utility class
```

## Files Description

### 1. **playwright_apitest.py** (Main Test File)
**Purpose**: Combines API calls and web UI automation in a single integrated test.

**What it does**:
- Launches a Chromium browser in non-headless mode (visible window)
- Logs into the e-commerce platform using credentials
- Navigates to the Orders page
- Creates an order using the REST API
- Searches for the created order in the UI
- If the order isn't found immediately, it **refreshes the page and retries**
- Verifies the order details page displays the expected confirmation message

**Key Features**:
- Error handling with try-except for element not found scenarios
- `expect()` assertions for validating page content
- Combines `playwright.sync_api` for both browser and API operations

### 2. **utils/apiBase.py** (API Utilities)
**Purpose**: Reusable utility class for e-commerce API operations.

**Methods**:
- **`createToken(playwright)`**: 
  - Authenticates with the API using login credentials
  - Returns a JWT token for authorized requests
  
- **`createOrder(playwright)`**: 
  - Creates a new order using the authentication token
  - Sends order details (country, product ID) to the API
  - Returns the created order ID

**Base URL**: `https://rahulshettyacademy.com`

### 3. **automate_AmazonSite.py** (Amazon Automation Examples)
**Purpose**: Simple examples of Playwright automation on Amazon.

**Features**:
- Demonstrates two test approaches:
  1. **Manual browser setup**: Manually launching browser, context, and page
  2. **Fixture-based approach**: Using pytest's page fixture for cleaner code
- Tests include title verification and search functionality

### 4. **TestPyTestValidation.py** (Pytest Fixture Guide)
**Purpose**: Educational file demonstrating pytest fixture scopes and setup/teardown patterns.

**Fixture Scopes Covered**:
- **Function Scope** (default): Runs once per test function
- **Class Scope**: Runs once per test class
- **Module Scope**: Runs once per module/file
- **Session Scope**: Runs once for the entire test session
- **Package Scope**: Runs once per package

This file is useful for understanding how to structure test fixtures with proper initialization and cleanup.

## Key Technologies

| Technology | Purpose |
|-----------|---------|
| **Playwright** | Browser automation library for Chrome, Firefox, Safari |
| **pytest** | Testing framework for running and organizing tests |
| **pytest-playwright** | pytest plugin that provides automatic browser fixtures |
| **REST API** | Direct API calls for order creation and authentication |

## Setup & Installation

```bash
# Install required packages
pip install pytest
pip install pytest-playwright

# Install Playwright browsers
playwright install
```

## Running Tests

```bash
# Run the API + UI test with console output
pytest playwright_apitest.py -s

# Run Amazon site tests with output
pytest automate_AmazonSite.py -s

# Run pytest fixture examples
pytest TestPyTestValidation.py -s
```

The `-s` flag displays print statements and logs during test execution.

## Test Credentials

- **Email**: shamanthn8904@gmail.com
- **Password**: Awe@2528!
- **Base URL**: https://rahulshettyacademy.com/client

## Key Features & Patterns

### 1. **Integrated Testing**
- Single test combines API operations with UI verification
- API is used to create test data, UI validates the results

### 2. **Error Handling & Retry Logic**
- Gracefully handles missing elements with automatic page refresh
- Retries element lookup after page reload

### 3. **Assertions**
- Uses Playwright's `expect()` for modern assertion syntax
- Validates text content with `to_contain_text()`

### 4. **Page Navigation**
- Uses locators with `get_by_placeholder()`, `get_by_role()`, `locator()`
- Implements context-based filtering with `filter(has_text=...)`

## Example Test Flow

```
1. Launch browser (non-headless)
2. Navigate to login page
3. Fill email and password
4. Click Login button
5. Navigate to Orders page
6. Create order via API call
7. Search for order in UI using order ID
   └─ If not found: Refresh and retry
8. Click "View" button on order row
9. Assert confirmation message appears
10. Close browser and context
```

## Utility Class Usage

```python
from utils.apiBase import APIUtils

api_util = APIUtils()

# Get authentication token
token = api_util.createToken(playwright)

# Create order and get order ID
order_id = api_util.createOrder(playwright)
```

## Best Practices Demonstrated

✅ Reusable utility classes for API operations  
✅ Fixture-based test setup  
✅ Error handling with graceful retries  
✅ Clear separation of concerns (API utils vs UI tests)  
✅ Use of Playwright's modern locator strategies  
✅ Integration of multiple testing approaches  

## Notes

- Tests run in **non-headless mode** (browser window is visible)
- Uses **Chromium** browser by default
- Implements **synchronous API** (sync_api) rather than async
- All tests use the same e-commerce test environment
