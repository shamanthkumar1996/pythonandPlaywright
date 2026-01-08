from playwright.sync_api import Playwright, Page, expect
from pageObjects.ordersHistory import OrdersHistorypage
class DashBoardPage:
    def __init__(self, page):
        self.page = page

    def goToOrders(self):
        self.page.get_by_role("button", name="ORDERS").click()
        ordersPage = OrdersHistorypage(self.page)
        return ordersPage
        