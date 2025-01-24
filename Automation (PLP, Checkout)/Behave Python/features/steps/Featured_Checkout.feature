Feature: Add all featured items to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened__F

    Scenario Outline: Add a featured item to the bag and proceed to checkout
        When I click on the "Featured" category
        And I open the featured item at index <index>
        And I add the featured item to the bag
        And I proceed to checkout_F
        Then I should be on the checkout page_F
        And I click on the back button_F
        And I remove the featured item from the bag
        And I close the bag_F

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