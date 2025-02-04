@checkout @carhopClassic
Feature: Add all Carhop Classics products to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened_C

    Scenario: Add Quarter Pound Double Cheeseburger to the bag and proceed to checkout
        When I click on the "Carhop Classics" category
        And I open the Carhop Classics item "Quarter Pound Double Cheeseburger"
        And I add Carhop Classics to the bag
        And I proceed to checkout_C
        Then I should be on the checkout page_C
        And I click on the back button_C
        And I remove Carhop Classics from the bag
        And I close the bag_C

    Scenario: Add FRITOS® Chili Cheese Wrap to the bag and proceed to checkout
        When I click on the "Carhop Classics" category
        And I open the Carhop Classics item "FRITOS® Chili Cheese Wrap"
        And I add Carhop Classics to the bag
        And I proceed to checkout_C
        Then I should be on the checkout page_C
        And I click on the back button_C
        And I remove Carhop Classics from the bag
        And I close the bag_C

    Scenario: Add Grilled Cheese Sandwich to the bag and proceed to checkout
        When I click on the "Carhop Classics" category
        And I open the Carhop Classics item "Grilled Cheese Sandwich"
        And I add Carhop Classics to the bag
        And I proceed to checkout_C
        Then I should be on the checkout page_C
        And I click on the back button_C
        And I remove Carhop Classics from the bag
        And I close the bag_C

    Scenario: Add Premium Chicken Bites to the bag and proceed to checkout
        When I click on the "Carhop Classics" category
        And I open the Carhop Classics item "Premium Chicken Bites"
        And I add Carhop Classics to the bag
        And I proceed to checkout_C
        Then I should be on the checkout page_C
        And I click on the back button_C
        And I remove Carhop Classics from the bag
        And I close the bag_C