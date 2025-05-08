import pytest
from playwright.sync_api import sync_playwright
from pages.buy_tickets_page import BuyTicketPage


@pytest.fixture(scope="session")
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    yield page
    browser.close()
    playwright.stop()

@pytest.fixture()
def buy_tickets_page(page):
    return BuyTicketPage(page)
