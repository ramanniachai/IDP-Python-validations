@checkout @frozenZone @sundaes
Feature: Add Sundaes products to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened_SU

    Scenario Outline: Add <product_name> to the bag and proceed to checkout
        When I click on the "Frozen Zone" category_SU
        And I click on the "Sundaes" subcategory
        And I open the Sundaes product "<product_name>"
        And I add the Sundaes product to the bag
        And I proceed to checkout_SU
        Then I should be on the checkout page_SU
        And I click on the back button_SU
        And I remove the Sundaes product from the bag
        And I close the bag_SU

        Examples:
            | product_name      |
            | Hot Fudge Sundae  |
            | Caramel Sundae    |
            | Strawberry Sundae |
            | Vanilla Cup       |