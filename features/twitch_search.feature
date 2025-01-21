Feature: Twitch Search

    Scenario Outline: Search for a streamer
        Given I open Twitch on a mobile browser
        When I accept the consent banner if it exists
        And I open the Browse page
        And  I click on the search field
        And I input "<search_text>"
        And I scroll down <scroll_count> times
        And I select a visible streamer
        Then I wait for the streamer page to load and take a screenshot

        Examples:
        | search_text  | scroll_count |
        | StarCraft II | 2           |
