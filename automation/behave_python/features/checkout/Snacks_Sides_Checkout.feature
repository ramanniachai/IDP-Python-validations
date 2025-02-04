@checkout @snacksSides
Feature: Add all products to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened_S

    Scenario: Add Mozzarella Sticks to the bag and proceed to checkout
        When I click on the "Snacks & Sides" category
        And I open the Snacks & Sides item "Mozzarella Sticks"
        And I add all sizes of Snacks & Sides to the bag
        And I proceed to checkout_S
        Then I should be on the checkout page_S
        And I click on the back button_S
        And I remove all sizes of Snacks & Sides from the bag
        And I close the bag_S

    Scenario: Add Groovy Fries to the bag and proceed to checkout
        When I click on the "Snacks & Sides" category
        And I open the Snacks & Sides item "Groovy Fries"
        And I add all sizes of Snacks & Sides to the bag
        And I proceed to checkout_S
        Then I should be on the checkout page_S
        And I click on the back button_S
        And I remove all sizes of Snacks & Sides from the bag
        And I close the bag_S

    Scenario: Add Tots to the bag and proceed to checkout
        When I click on the "Snacks & Sides" category
        And I open the Snacks & Sides item "Tots"
        And I add all sizes of Snacks & Sides to the bag
        And I proceed to checkout_S
        Then I should be on the checkout page_S
        And I click on the back button_S
        And I remove all sizes of Snacks & Sides from the bag
        And I close the bag_S

    Scenario: Add Chili Cheese Tots to the bag and proceed to checkout
        When I click on the "Snacks & Sides" category
        And I open the Snacks & Sides item "Chili Cheese Tots"
        And I add all sizes of Snacks & Sides to the bag
        And I proceed to checkout_S
        Then I should be on the checkout page_S
        And I click on the back button_S
        And I remove all sizes of Snacks & Sides from the bag
        And I close the bag_S

    Scenario: Add Ched 'R' Peppers to the bag and proceed to checkout
        When I click on the "Snacks & Sides" category
        And I open the Snacks & Sides item "Ched 'R' Peppers"
        And I add all sizes of Snacks & Sides to the bag
        And I proceed to checkout_S
        Then I should be on the checkout page_S
        And I click on the back button_S
        And I remove all sizes of Snacks & Sides from the bag
        And I close the bag_S

    Scenario: Add Onion Rings to the bag and proceed to checkout
        When I click on the "Snacks & Sides" category
        And I open the Snacks & Sides item "Onion Rings"
        And I add all sizes of Snacks & Sides to the bag
        And I proceed to checkout_S
        Then I should be on the checkout page_S
        And I click on the back button_S
        And I remove all sizes of Snacks & Sides from the bag
        And I close the bag_S

    Scenario: Add Pickle Fries to the bag and proceed to checkout
        When I click on the "Snacks & Sides" category
        And I open the Snacks & Sides item "Pickle Fries"
        And I add all sizes of Snacks & Sides to the bag
        And I proceed to checkout_S
        Then I should be on the checkout page_S
        And I click on the back button_S
        And I remove all sizes of Snacks & Sides from the bag
        And I close the bag_S

    Scenario: Add Cheese Tots to the bag and proceed to checkout
        When I click on the "Snacks & Sides" category
        And I open the Snacks & Sides item "Cheese Tots"
        And I add all sizes of Snacks & Sides to the bag
        And I proceed to checkout_S
        Then I should be on the checkout page_S
        And I click on the back button_S
        And I remove all sizes of Snacks & Sides from the bag
        And I close the bag_S

    Scenario: Add Chili Cheese Groovy Fries to the bag and proceed to checkout
        When I click on the "Snacks & Sides" category
        And I open the Snacks & Sides item "Chili Cheese Groovy Fries"
        And I add all sizes of Snacks & Sides to the bag
        And I proceed to checkout_S
        Then I should be on the checkout page_S
        And I click on the back button_S
        And I remove all sizes of Snacks & Sides from the bag
        And I close the bag_S

    Scenario: Add Cheese Groovy Fries to the bag and proceed to checkout
        When I click on the "Snacks & Sides" category
        And I open the Snacks & Sides item "Cheese Groovy Fries"
        And I add all sizes of Snacks & Sides to the bag
        And I proceed to checkout_S
        Then I should be on the checkout page_S
        And I click on the back button_S
        And I remove all sizes of Snacks & Sides from the bag
        And I close the bag_S

    Scenario: Add Side of Queso to the bag and proceed to checkout
        When I click on the "Snacks & Sides" category
        And I open the Snacks & Sides item "Side of Queso"
        And I add Snacks & Sides to the bag
        And I proceed to checkout_S
        Then I should be on the checkout page_S
        And I click on the back button_S
        And I remove Snacks & Sides from the bag
        And I close the bag_S

    Scenario: Add Soft Pretzel Twist to the bag and proceed to checkout
        When I click on the "Snacks & Sides" category
        And I scroll down to Snacks and open the Snacks & Sides item "Soft Pretzel Twist"
        And I add Snacks & Sides to the bag
        And I proceed to checkout_S
        Then I should be on the checkout page_S
        And I click on the back button_S
        And I remove Snacks & Sides from the bag
        And I close the bag_S

    Scenario: Add Premium Chicken Bites to the bag and proceed to checkout
        When I click on the "Snacks & Sides" category
        And I scroll down to Snacks and open the Snacks & Sides item "Premium Chicken Bites"
        And I add all sizes of Snacks & Sides to the bag
        And I proceed to checkout_S
        Then I should be on the checkout page_S
        And I click on the back button_S
        And I remove all sizes of Snacks & Sides from the bag
        And I close the bag_S

    Scenario: Add Bacon Ranch Queso Wrap to the bag and proceed to checkout
        When I click on the "Snacks & Sides" category
        And I scroll down to Snacks and open the Snacks & Sides item "Bacon Ranch Queso Wrap"
        And I add Snacks & Sides to the bag
        And I proceed to checkout_S
        Then I should be on the checkout page_S
        And I click on the back button_S
        And I remove Snacks & Sides from the bag
        And I close the bag_S

    Scenario: Add Southwest Crunch Queso Wrap to the bag and proceed to checkout
        When I click on the "Snacks & Sides" category
        And I scroll down to Snacks and open the Snacks & Sides item "Southwest Crunch Queso Wrap"
        And I add Snacks & Sides to the bag
        And I proceed to checkout_S
        Then I should be on the checkout page_S
        And I click on the back button_S
        And I remove Snacks & Sides from the bag
        And I close the bag_S

    Scenario: Add FRITOS® Chili Cheese Jr. Wrap to the bag and proceed to checkout
        When I click on the "Snacks & Sides" category
        And I scroll down to Snacks and open the Snacks & Sides item "FRITOS® Chili Cheese Jr. Wrap"
        And I add Snacks & Sides to the bag
        And I proceed to checkout_S
        Then I should be on the checkout page_S
        And I click on the back button_S
        And I remove Snacks & Sides from the bag
        And I close the bag_S

    Scenario: Add FRITOS® Chili Cheese Wrap to the bag and proceed to checkout
        When I click on the "Snacks & Sides" category
        And I scroll down to Snacks and open the Snacks & Sides item "FRITOS® Chili Cheese Wrap"
        And I add Snacks & Sides to the bag
        And I proceed to checkout_S
        Then I should be on the checkout page_S
        And I click on the back button_S
        And I remove Snacks & Sides from the bag
        And I close the bag_S

    Scenario: Add FRITOS® Chili Pie to the bag and proceed to checkout
        When I click on the "Snacks & Sides" category
        And I scroll down to Snacks and open the Snacks & Sides item "FRITOS® Chili Pie"
        And I add all sizes of Snacks & Sides to the bag
        And I proceed to checkout_S
        Then I should be on the checkout page_S
        And I click on the back button_S
        And I remove all sizes of Snacks & Sides from the bag
        And I close the bag_S

    Scenario: Add Ched 'R' Bites to the bag and proceed to checkout
        When I click on the "Snacks & Sides" category
        And I scroll down to Snacks and open the Snacks & Sides item "Ched 'R' Bites"
        And I add all sizes of Snacks & Sides to the bag
        And I proceed to checkout_S
        Then I should be on the checkout page_S
        And I click on the back button_S
        And I remove all sizes of Snacks & Sides from the bag
        And I close the bag_S