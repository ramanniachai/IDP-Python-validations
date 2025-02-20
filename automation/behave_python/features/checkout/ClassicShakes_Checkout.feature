@checkout @frozenZone @classicShakes
Feature: Add all sizes of Classic Shakes products to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened_CS

    Scenario Outline: Add <product_name> to the bag and proceed to checkout
        When I click on the "Frozen Zone" category_CS
        And I click on the "Classic Shakes" subcategory
        And I open the Classic Shakes product "<product_name>"
        And I add all sizes of the Classic Shakes product to the bag
        And I proceed to checkout_CS
        Then I should be on the checkout page_CS
        And I click on the back button_CS
        And I remove all sizes of the Classic Shakes product from the bag
        And I close the bag_CS

        Examples:
            | product_name                |
            | Vanilla Classic Shake       |
            | Banana Classic Shake        |
            | Chocolate Classic Shake     |
            | Caramel Classic Shake       |
            | Strawberry Classic Shake    |
            | Hot Fudge Classic Shake     |
            | Peanut Butter Classic Shake |