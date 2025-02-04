@checkout
Feature: Add all burgers to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened__
        And I reject non-essential cookies and accept the privacy policy

    Scenario Outline: Add a burger to the bag and proceed to checkout
        When I click on the "Burgers" category
        And I open the burger product at index <index>
        And I add the burger to the bag
        And I proceed to checkout
        Then I should be on the checkout page
        And I click on the back button
        And I remove the burger from the bag
        And I close the bag

        Examples:
            | index |
            | 1     |
            | 2     |
            | 3     |
            | 4     |
            | 5     |
            | 6     |
            | 7     |
            | 8     |
            | 9     |
            | 10    |
            | 11    |
            | 12    |