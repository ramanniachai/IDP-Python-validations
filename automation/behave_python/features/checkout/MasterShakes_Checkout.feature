@checkout @frozenZone @masterShakes
Feature: Add all sizes of Master Shakes products to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened_MS

    Scenario Outline: Add a Master Shakes product to the bag and proceed to checkout
        When I click on the "Frozen Zone" category_MS
        And I click on the "Master Shakes" subcategory
        And I open the Master Shakes product "<product_name>"
        And I add all sizes of the Master Shakes product to the bag
        And I proceed to checkout_MS
        Then I should be on the checkout page_MS
        And I click on the back button_MS
        And I remove all sizes of the Master Shakes product from the bag
        And I close the bag_MS

        Examples:
            | product_name                        |
            | OREO® Peanut Butter Master Shake    |
            | Strawberry Cheesecake Master Shake® |
            | Cheesecake Master Shake®            |
            | OREO® Chocolate Master Shake®       |
            | OREO® Cheesecake Master Shake®      |