import allure
from playwright.sync_api import expect


class BasePage:
    __BASE_URL = 'https://www.cp.pt/passageiros/en'

    def __init__(self, page):
        self.page = page
        self._endpoint = ''

    def _get_full_url(self):
        return f"{self.__BASE_URL}/{self._endpoint}"

    @allure.step("Navigate to endpoint")
    def navigate_to(self):
        full_url = self._get_full_url()
        self.page.goto(full_url)
        self.page.wait_for_load_state('load')
        expect(self.page).to_have_url(full_url)

    @allure.step("Click element with selector")
    def wait_for_selector_and_click(self, selector):
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    @allure.step("Fill into input with selector")
    def wait_for_selector_and_fill(self, selector, value):
        self.page.wait_for_selector(selector)
        self.page.fill(selector, value)

    @allure.step("Type into input with selector")
    def wait_for_selector_and_type(self, selector, value, delay):
        self.page.wait_for_selector(selector)
        self.page.type(selector, value, delay=delay)

    @allure.step("Save input data")
    def get_input_value(self, selector):
        return self.page.locator(selector).input_value()

    @allure.step("Verify that element is visible")
    def assert_element_is_visible(self, selector):
        expect(self.page.locator(selector)).to_be_visible()

    @allure.step("Verify text on page")
    def assert_text_present_on_page(self, text):
        expect(self.page.locator("body")).to_contain_text(text)

    @allure.step("Verify element in text")
    def assert_text_in_element(self, selector, text):
        expect(self.page.locator(selector)).to_have_text(text)

    @allure.step("Verify input value")
    def assert_input_value(self, selector, expected_value):
        expect(self.page.locator(selector)).to_have_value(expected_value)
