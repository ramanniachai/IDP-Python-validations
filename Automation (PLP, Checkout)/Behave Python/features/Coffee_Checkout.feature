@checkout @drinks
Feature: Add all sizes of Coffee drinks to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened__CF

    Scenario: Add Original Cold Brew Iced Coffee to the bag and proceed to checkout
        When I click on the "Drinks" category_CF
        And I click on the "Coffee" subcategory
        And I open the drink product "Original Cold Brew Iced Coffee"
        And I add all sizes of the drink to the bag_CF
        And I proceed to checkout_CF
        Then I should be on the checkout page_CF
        And I click on the back button_CF
        And I remove all sizes of the drink from the bag_CF
        And I close the bag_CF

    Scenario: Add French Vanilla Cold Brew Iced Coffee to the bag and proceed to checkout
        When I click on the "Drinks" category_CF
        And I click on the "Coffee" subcategory
        And I open the drink product "French Vanilla Cold Brew Iced Coffee"
        And I add all sizes of the drink to the bag_CF
        And I proceed to checkout_CF
        Then I should be on the checkout page_CF
        And I click on the back button_CF
        And I remove all sizes of the drink from the bag_CF
        And I close the bag_CF

    Scenario: Add Coffee to the bag and proceed to checkout
        When I click on the "Drinks" category_CF
        And I click on the "Coffee" subcategory
        And I open the drink product "Coffee"
        And I add the drink to the bag_CF
        And I proceed to checkout_CF
        Then I should be on the checkout page_CF
        And I click on the back button_CF
        And I remove the drink from the bag_CF
        And I close the bag_CF