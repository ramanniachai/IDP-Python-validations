Feature: Add all Sandwiches products to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened_Ss

    Scenario Outline: Add a Sandwiches product to the bag and proceed to checkout
        When I click on the "Sandwiches" category
        And I open the Sandwiches product "<product_name>"
        And I add the Sandwiches product to the bag
        And I proceed to checkout_Ss
        Then I should be on the checkout page_Ss
        And I click on the back button_Ss
        And I remove the Sandwiches product from the bag
        And I close the bag_Ss

        Examples:
            | product_name            |
            | Grilled Cheese Sandwich |
            | Crispy Chicken Sandwich |
