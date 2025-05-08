import allure
import pytest


@pytest.mark.e2e
@allure.epic("Train Ticket Booking")
@allure.feature("Buy and Cancel Ticket")
@allure.title("Buy and cancel ticket with correct input and dates")
@allure.description("Fills route, selects dates, submits and cancels booking, verifies inputs remain unchanged.")
@allure.severity(allure.severity_level.CRITICAL)
def test_buy_and_cancel_ticket(page, buy_tickets_page):
    buy_tickets_page.open()
    buy_tickets_page.fill_from_to_route("Lagos", "Porto Campanha")
    buy_tickets_page.assert_month_year('May', '2025')
    buy_tickets_page.select_departure_days_from_now(3)
    buy_tickets_page.select_return_days_from_now(5)
    buy_tickets_page.submit_form()
    buy_tickets_page.assert_text_present_on_page("Online Ticket Office")
    buy_tickets_page.cancel_booking()
# Validate that all that parameters are saved
    buy_tickets_page.assert_tickets_form_is_ready()
    buy_tickets_page.assert_city_from_value("Lagos")
    buy_tickets_page.assert_city_to_value("Porto Campanha")
    buy_tickets_page.assert_departure_date_is_saved()
    buy_tickets_page.assert_return_date_is_saved()
