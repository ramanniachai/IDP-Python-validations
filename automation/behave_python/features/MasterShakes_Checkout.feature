@checkout @frozenZone @masterShakes
Feature: Master Shakes Checkout

    Scenario: Add OREO® Peanut Butter Master Shake to the bag and proceed to checkout
        Given Sonic web page is opened_MS
        When I click on the "Frozen Zone" category_MS
        And I click on the "Master Shakes" subcategory
        And I open the Master Shakes product "OREO® Peanut Butter Master Shake"
        And I add all sizes of the Master Shakes product to the bag
        And I proceed to checkout_MS
        Then I should be on the checkout page_MS
        And I click on the back button_MS
        And I remove all sizes of the Master Shakes product from the bag
        And I close the bag_MS

    Scenario: Add Strawberry Cheesecake Master Shake® to the bag and proceed to checkout
        Given Sonic web page is opened_MS
        When I click on the "Frozen Zone" category_MS
        And I click on the "Master Shakes" subcategory
        And I open the Master Shakes product "Strawberry Cheesecake Master Shake®"
        And I add all sizes of the Master Shakes product to the bag
        And I proceed to checkout_MS
        Then I should be on the checkout page_MS
        And I click on the back button_MS
        And I remove all sizes of the Master Shakes product from the bag
        And I close the bag_MS

    Scenario: Add Cheesecake Master Shake® to the bag and proceed to checkout
        Given Sonic web page is opened_MS
        When I click on the "Frozen Zone" category_MS
        And I click on the "Master Shakes" subcategory
        And I open the Master Shakes product "Cheesecake Master Shake®"
        And I add all sizes of the Master Shakes product to the bag
        And I proceed to checkout_MS
        Then I should be on the checkout page_MS
        And I click on the back button_MS
        And I remove all sizes of the Master Shakes product from the bag
        And I close the bag_MS

    Scenario: Add OREO® Chocolate Master Shake® to the bag and proceed to checkout
        Given Sonic web page is opened_MS
        When I click on the "Frozen Zone" category_MS
        And I click on the "Master Shakes" subcategory
        And I open the Master Shakes product "OREO® Chocolate Master Shake®"
        And I add all sizes of the Master Shakes product to the bag
        And I proceed to checkout_MS
        Then I should be on the checkout page_MS
        And I click on the back button_MS
        And I remove all sizes of the Master Shakes product from the bag
        And I close the bag_MS

    Scenario: Add OREO® Cheesecake Master Shake® to the bag and proceed to checkout
        Given Sonic web page is opened_MS
        When I click on the "Frozen Zone" category_MS
        And I click on the "Master Shakes" subcategory
        And I open the Master Shakes product "OREO® Cheesecake Master Shake®"
        And I add all sizes of the Master Shakes product to the bag
        And I proceed to checkout_MS
        Then I should be on the checkout page_MS
        And I click on the back button_MS
        And I remove all sizes of the Master Shakes product from the bag
        And I close the bag_MS