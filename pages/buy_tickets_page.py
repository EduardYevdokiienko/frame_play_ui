from datetime import datetime, timedelta

import allure
from playwright.sync_api import expect
from pages.base_page import BasePage


class BuyTicketPage(BasePage):
    INPUT_FROM = '//input[@title="From "]'
    INPUT_TO = '//input[@title="To "]'
    DEPARTURE_INPUT = '//input[@name="departDate"]'
    RETURN_INPUT = '//input[@name="returnDate"]'
    SUBMIT_BUTTON = '//input[@type="submit"]'
    CANCEL_BUTTON = '#exitButton'
    MONTH_SELECTOR = '(//div[@class="picker__month"])[1]'
    YEAR_SELECTOR = '(//div[@class="picker__year"])[1]'
    DEPARTURE_DATE_SELECTOR = 'table#datepicker-first_table td:not(.is-disabled)'
    RETURN_DATE_SELECTOR = 'table#datepicker-second_table td:not(.is-disabled)'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/buy-tickets'

    @allure.step("Open page")
    def open(self):
        return self.navigate_to()

    @allure.step("Fill route: from_city - to_city")
    def fill_from_to_route(self, from_city, to_city):
        self.wait_for_selector_and_fill(self.INPUT_FROM, from_city)
        self.wait_for_selector_and_fill(self.INPUT_TO, to_city)

    @allure.step("Select departure date: days_from_now")
    def select_departure_days_from_now(self, days_from_now):
        self.wait_for_selector_and_click(self.DEPARTURE_INPUT)
        target_day = (datetime.today() + timedelta(days=days_from_now)).day
        self.wait_for_selector_and_click(f'{self.DEPARTURE_DATE_SELECTOR} >> text="{target_day}"')
        return self.get_input_value(self.DEPARTURE_INPUT)

    @allure.step("Select return date: days_from_now")
    def select_return_days_from_now(self, days_from_now):
        self.wait_for_selector_and_click(self.RETURN_INPUT)
        target_day = (datetime.today() + timedelta(days=days_from_now)).day
        self.wait_for_selector_and_click(f'{self.RETURN_DATE_SELECTOR} >> text="{target_day}"')
        return self.get_input_value(self.RETURN_INPUT)

    @allure.step("Submit the form")
    def submit_form(self):
        with self.page.expect_navigation():
            self.wait_for_selector_and_click(self.SUBMIT_BUTTON)

    @allure.step("Cancel the booking")
    def cancel_booking(self):
        self.page.locator(self.CANCEL_BUTTON).wait_for(state="visible")
        self.wait_for_selector_and_click(self.CANCEL_BUTTON)

    @allure.step("Assert calendar shows month and year")
    def assert_month_year(self, expected_month, expected_year):
        expect(self.page.locator(self.MONTH_SELECTOR)).to_contain_text(expected_month)
        expect(self.page.locator(self.YEAR_SELECTOR)).to_contain_text(str(expected_year))

    @allure.step("Assert tickets form is ready")
    def assert_tickets_form_is_ready(self):
        self.assert_element_is_visible(self.INPUT_FROM)

    @allure.step("Assert city FROM")
    def assert_city_from_value(self, city):
        self.assert_input_value(self.INPUT_FROM, city)

    @allure.step("Assert city TO")
    def assert_city_to_value(self, city):
        self.assert_input_value(self.INPUT_TO, city)

    @allure.step("Assert DEPARTURE date saved")
    def assert_departure_date_is_saved(self):
        self.assert_input_value(self.DEPARTURE_INPUT, self.get_input_value(self.DEPARTURE_INPUT))

    @allure.step("Assert RETURN date saved")
    def assert_return_date_is_saved(self):
        self.assert_input_value(self.RETURN_INPUT, self.get_input_value(self.RETURN_INPUT))
