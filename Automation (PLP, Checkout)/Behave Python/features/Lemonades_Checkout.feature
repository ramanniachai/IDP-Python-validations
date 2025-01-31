Feature: Add all sizes of Lemonades & Limeades drinks to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened__LL

    Scenario: Add Cherry Limeade to the bag and proceed to checkout
        When I click on the "Drinks" category_LL
        And I click on the "Lemonades & Limeades" subcategory
        And I open the drink product "Cherry Limeade"
        And I add all sizes of the drink to the bag_LL
        And I proceed to checkout_LL
        Then I should be on the checkout page_LL
        And I click on the back button_LL
        And I remove all sizes of the drink from the bag_LL
        And I close the bag_LL

    Scenario: Add Diet Cherry Limeade to the bag and proceed to checkout
        When I click on the "Drinks" category_LL
        And I click on the "Lemonades & Limeades" subcategory
        And I open the drink product "Diet Cherry Limeade"
        And I add all sizes of the drink to the bag_LL
        And I proceed to checkout_LL
        Then I should be on the checkout page_LL
        And I click on the back button_LL
        And I remove all sizes of the drink from the bag_LL
        And I close the bag_LL

    Scenario: Add Strawberry Limeade to the bag and proceed to checkout
        When I click on the "Drinks" category_LL
        And I click on the "Lemonades & Limeades" subcategory
        And I open the drink product "Strawberry Limeade"
        And I add all sizes of the drink to the bag_LL
        And I proceed to checkout_LL
        Then I should be on the checkout page_LL
        And I click on the back button_LL
        And I remove all sizes of the drink from the bag_LL
        And I close the bag_LL

    Scenario: Add Cranberry Limeade to the bag and proceed to checkout
        When I click on the "Drinks" category_LL
        And I click on the "Lemonades & Limeades" subcategory
        And I open the drink product "Cranberry Limeade"
        And I add all sizes of the drink to the bag_LL
        And I proceed to checkout_LL
        Then I should be on the checkout page_LL
        And I click on the back button_LL
        And I remove all sizes of the drink from the bag_LL
        And I close the bag_LL

    Scenario: Add Limeade to the bag and proceed to checkout
        When I click on the "Drinks" category_LL
        And I click on the "Lemonades & Limeades" subcategory
        And I open the drink product "Limeade"
        And I add all sizes of the drink to the bag_LL
        And I proceed to checkout_LL
        Then I should be on the checkout page_LL
        And I click on the back button_LL
        And I remove all sizes of the drink from the bag_LL
        And I close the bag_LL

    Scenario: Add Diet Limeade to the bag and proceed to checkout
        When I click on the "Drinks" category_LL
        And I click on the "Lemonades & Limeades" subcategory
        And I open the drink product "Diet Limeade"
        And I add all sizes of the drink to the bag_LL
        And I proceed to checkout_LL
        Then I should be on the checkout page_LL
        And I click on the back button_LL
        And I remove all sizes of the drink from the bag_LL
        And I close the bag_LL

    Scenario: Add All Natural Lemonade to the bag and proceed to checkout
        When I click on the "Drinks" category_LL
        And I click on the "Lemonades & Limeades" subcategory
        And I open the drink product "All Natural Lemonade"
        And I add all sizes of the drink to the bag_LL
        And I proceed to checkout_LL
        Then I should be on the checkout page_LL
        And I click on the back button_LL
        And I remove all sizes of the drink from the bag_LL
        And I close the bag_LL