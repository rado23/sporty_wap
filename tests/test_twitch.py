from pytest_bdd import scenario, given, when, then, parsers
from pages.twitch_page import TwitchPage
import pytest

@scenario("../features/twitch_search.feature", "Search for a streamer")
def test_twitch_search():
    pass

@pytest.fixture
def twitch_page(driver):
    return TwitchPage(driver)

@given("I open Twitch on a mobile browser")
def open_twitch(twitch_page):
    twitch_page.open()

@when("I accept the consent banner if it exists")
def accept_consent_banner(twitch_page):
    twitch_page.accept_consent_banner()

@when("I open the Browse page")
def open_browse_page(twitch_page):
    twitch_page.open_browse_page()

@when("I click on the search field")
def click_search(twitch_page):
    twitch_page.click_search_field()

@when(parsers.parse('I input "{search_text}"'))
def search_game(twitch_page, search_text):
    twitch_page.search_game(search_text)

@when(parsers.parse("I scroll down {scroll_count:d} times"))
def scroll(twitch_page, scroll_count):
    twitch_page.scroll_down(scroll_count)

@when("I select a visible streamer")
def select_streamer(twitch_page):
    twitch_page.select_streamer()

@then("I wait for the streamer page to load and take a screenshot")
def screenshot(twitch_page):
    twitch_page.handle_modals_and_screenshot()
