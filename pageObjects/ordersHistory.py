from playwright.sync_api import Playwright, Page, expect
from pageObjects.orderSummary import OrderSummarypage
class OrdersHistorypage:
    def __init__(self, page):
        self.page = page

    def selectOrder(self, order_id):
        try:
         row = self.page.locator("tr").filter(has_text=order_id)
         row.wait_for(timeout=5000)
        except:
         print(
            f"Row with ID {order_id} not found. Refreshing page and trying again...")
        self.page.reload()
        row = self.page.locator("tr").filter(has_text=order_id)

        row.get_by_role("button", name="View").click()
        OrderSummaryPage = OrderSummarypage(self.page)
        return OrderSummaryPage
