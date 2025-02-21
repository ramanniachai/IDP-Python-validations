@checkout @1.99Menu
Feature: Add all products to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened_M

    Scenario Outline: Add <product_name> to the bag and proceed to checkout
        When I click on the "$1.99 Menu" category
        And I open the product "<product_name>" at index <index>
        And I add the product to the bag
        And I proceed to checkout_M
        Then I should be on the checkout page_M
        And I click on the back button_M
        And I remove the product from the bag
        And I close the bag_M

        Examples:
            | product_name            | index |
            | Jr. Deluxe Cheeseburger | 1     |
            | Bacon Ranch Queso Wrap  | 2     |
            | Chicken Strip Sandwich  | 3     |
            | Jr. Breakfast Burrito   | 4     |
            | Jr. Double Cheeseburger | 5     |
            | Grilled Cheese          | 6     |
            | Corn Dog                | 7     |
            | Vanilla Cone            | 8     |
            | Small Tots              | 9     |