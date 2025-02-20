@checkout @drinks @other
Feature: Add all sizes of Other drinks to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened__OT

    Scenario: Add Red Bull Energy Drink to the bag and proceed to checkout
        When I click on the "Drinks" category_OT
        And I click on the "Other" subcategory
        And I open the drink product "Red Bull Energy Drink"
        And I add the drink to the bag_OT
        And I proceed to checkout_OT
        Then I should be on the checkout page_OT
        And I click on the back button_OT
        And I remove the drink from the bag_OT
        And I close the bag_OT

    Scenario: Add Water to the bag and proceed to checkout
        When I click on the "Drinks" category_OT
        And I click on the "Other" subcategory
        And I open the drink product "Water"
        And I add all sizes of the drink to the bag_OT
        And I proceed to checkout_OT
        Then I should be on the checkout page_OT
        And I click on the back button_OT
        And I remove all sizes of the drink from the bag_OT
        And I close the bag_OT

    Scenario: Add Minute Maid® 100% Apple Juice Box to the bag and proceed to checkout
        When I click on the "Drinks" category_OT
        And I click on the "Other" subcategory
        And I open the drink product "Minute Maid® 100% Apple Juice Box"
        And I add the drink to the bag_OT
        And I proceed to checkout_OT
        Then I should be on the checkout page_OT
        And I click on the back button_OT
        And I remove the drink from the bag_OT
        And I close the bag_OT

    Scenario: Add Milk Jug (1%) - White to the bag and proceed to checkout
        When I click on the "Drinks" category_OT
        And I click on the "Other" subcategory
        And I open the drink product "Milk Jug (1%) - White"
        And I add the drink to the bag_OT
        And I proceed to checkout_OT
        Then I should be on the checkout page_OT
        And I click on the back button_OT
        And I remove the drink from the bag_OT
        And I close the bag_OT

    Scenario: Add Cup Of Ice to the bag and proceed to checkout
        When I click on the "Drinks" category_OT
        And I click on the "Other" subcategory
        And I open the drink product "Cup Of Ice"
        And I add all sizes of the drink to the bag_OT
        And I proceed to checkout_OT
        Then I should be on the checkout page_OT
        And I click on the back button_OT
        And I remove all sizes of the drink from the bag_OT
        And I close the bag_OT

    Scenario: Add Orange Juice to the bag and proceed to checkout
        When I click on the "Drinks" category_OT
        And I click on the "Other" subcategory
        And I open the drink product "Orange Juice"
        And I add all sizes of the drink to the bag_OT
        And I proceed to checkout_OT
        Then I should be on the checkout page_OT
        And I click on the back button_OT
        And I remove all sizes of the drink from the bag_OT
        And I close the bag_OT