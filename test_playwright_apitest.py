import json
from playwright.sync_api import Playwright, Page
import pytest

from pageObjects.login import LoginPage
from utils.apiBase import APIUtils
from playwright.sync_api import Playwright, Page, expect
from utils.apiBase import APIUtils

with open('data/credentials.json') as f:
        test_data = json.load(f)
        credentials = test_data["user_credentials"]

@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials',credentials)   
def test_api_and_web_site(playwright:Playwright,browserInstance,user_credentials):
# Json file load and read
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    dashboard = loginPage.login(user_credentials["username"], user_credentials["password"])
    api_util = APIUtils()
    response = api_util.createOrder(playwright,user_credentials)
    print(f"Order created with ID: {response}")
    OrderHistory = dashboard.goToOrders()
    OrderHistory.selectOrder(response)

@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials',credentials)   
def test_api_and_web_site_two(playwright:Playwright,browserInstance,user_credentials):
# Json file load and read
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    dashboard = loginPage.login(user_credentials["username"], user_credentials["password"])
    api_util = APIUtils()
    response = api_util.createOrder(playwright,user_credentials)
    print(f"Order created with ID: {response}")
    OrderHistory = dashboard.goToOrders()
    OrderHistory.selectOrder(response)