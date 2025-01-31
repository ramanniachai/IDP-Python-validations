Feature: Add all sizes of Iced Tea drinks to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened__IT

    Scenario: Add Sweet Iced Tea to the bag and proceed to checkout
        When I click on the "Drinks" category_IT
        And I click on the "Iced Tea" subcategory
        And I open the drink product "Sweet Iced Tea"
        And I add all sizes of the drink to the bag_IT
        And I proceed to checkout_IT
        Then I should be on the checkout page_IT
        And I click on the back button_IT
        And I remove all sizes of the drink from the bag_IT
        And I close the bag_IT

    Scenario: Add Unsweet Iced Tea to the bag and proceed to checkout
        When I click on the "Drinks" category_IT
        And I click on the "Iced Tea" subcategory
        And I open the drink product "Unsweet Iced Tea"
        And I add all sizes of the drink to the bag_IT
        And I proceed to checkout_IT
        Then I should be on the checkout page_IT
        And I click on the back button_IT
        And I remove all sizes of the drink from the bag_IT
        And I close the bag_IT

    Scenario: Add Half Sweet Tea / Half Lemonade to the bag and proceed to checkout
        When I click on the "Drinks" category_IT
        And I click on the "Iced Tea" subcategory
        And I open the drink product "Half Sweet Tea / Half Lemonade"
        And I add all sizes of the drink to the bag_IT
        And I proceed to checkout_IT
        Then I should be on the checkout page_IT
        And I click on the back button_IT
        And I remove all sizes of the drink from the bag_IT
        And I close the bag_IT

    Scenario: Add Half Sweet Tea / Half Unsweet Tea to the bag and proceed to checkout
        When I click on the "Drinks" category_IT
        And I click on the "Iced Tea" subcategory
        And I open the drink product "Half Sweet Tea / Half Unsweet Tea"
        And I add all sizes of the drink to the bag_IT
        And I proceed to checkout_IT
        Then I should be on the checkout page_IT
        And I click on the back button_IT
        And I remove all sizes of the drink from the bag_IT
        And I close the bag_IT

    Scenario: Add Half Unsweet Tea / Half Lemonade to the bag and proceed to checkout
        When I click on the "Drinks" category_IT
        And I click on the "Iced Tea" subcategory
        And I open the drink product "Half Unsweet Tea / Half Lemonade"
        And I add all sizes of the drink to the bag_IT
        And I proceed to checkout_IT
        Then I should be on the checkout page_IT
        And I click on the back button_IT
        And I remove all sizes of the drink from the bag_IT
        And I close the bag_IT