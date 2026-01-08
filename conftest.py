import pytest
pytest_plugins = ['pytest_bdd']

@pytest.fixture(scope="session")
# request is a built-in pytest fixture that is used globally
# Read this later important
def user_credentials(request):
    return request.param

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", 
        help="Browser name: chrome, chromium, firefox, or webkit"
    )
# If i have scope as session then the fixture runs once and the cookie is saved, 
# we don't get new browser session hence script fails
@pytest.fixture()
def browserInstance(playwright, request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(channel="chrome", headless=True)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=False)
    else:
        browser = playwright.chromium.launch(headless=False)
    # context is a new session within the browser
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()