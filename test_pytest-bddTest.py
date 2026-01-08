from pytest_bdd import given, scenarios, when, then, parsers
import pytest
from conftest import user_credentials
from pageObjects.login import LoginPage
from utils.apiBase import APIUtils

scenarios('features/orderTransaction.feature')

@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse('place the item order with {username} and {password}'))
def place_order(playwright,username, password,shared_data):
    user_credentials={
        "username": username,
        "password": password
    }
    api_util = APIUtils()
    response = api_util.createOrder(playwright,user_credentials)
    shared_data['order_response'] = response

@given('the user is on landing page')
def landing_page(browserInstance,shared_data):
   loginPage = LoginPage(browserInstance)
   loginPage.navigate()
   shared_data['loginPage'] = loginPage

@when(parsers.parse('I Login to portal with {username} and {password}'))
def user_login(browserInstance, username, password, shared_data):
    dashboard = shared_data['loginPage'].login(username, password)
    shared_data['dashboard_page'] = dashboard

@when('navigate to orders page')
def navigate_orders_page(shared_data):
    OrderHistory = shared_data['dashboard_page'].goToOrders()
    shared_data['OrderHistory_page'] = OrderHistory

@when('select the orderId')
def select_orderID(shared_data):
    OrderHistory = shared_data['OrderHistory_page']
    order_response = shared_data['order_response']
    OrderHistory.selectOrder(order_response)

