from playwright.sync_api import Playwright, Page, expect
class OrderSummarypage:
    def __init__(self, page: Page):
        self.page = page

    def verifyOrderPlaced(self):
        expect(self.page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")