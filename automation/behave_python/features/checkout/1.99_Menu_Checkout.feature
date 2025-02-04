@checkout @1.99Menu
Feature: Add all products to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened_M

    Scenario Outline: Add a $1.99 Menu to the bag and proceed to checkout
        When I click on the "$1.99 Menu" category
        And I open the product at index <index>
        And I add the product to the bag
        And I proceed to checkout_M
        Then I should be on the checkout page_M
        And I click on the back button_M
        And I remove the product from the bag
        And I close the bag_M

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