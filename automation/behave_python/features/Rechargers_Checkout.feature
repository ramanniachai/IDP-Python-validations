@checkout @drinks @rechargers
Feature: Add all sizes of SONIC Rechargers with Red Bull drinks to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened__RRB

    Scenario: Add Sour Dragon Fruit Recharger with Red Bull® to the bag and proceed to checkout
        When I click on the "Drinks" category_RRB
        And I click on the "SONIC Rechargers with Red Bull" subcategory
        And I open the drink product "Sour Dragon Fruit Recharger with Red Bull®"_R
        And I add all sizes of the drink to the bag_RRB
        And I proceed to checkout_RRB
        Then I should be on the checkout page_RRB
        And I click on the back button_RRB
        And I remove the drink from the bag_RRB
        And I close the bag_RRB

    Scenario: Add Twisted Lime Recharger with Red Bull® with Red Bull® to the bag and proceed to checkout
        When I click on the "Drinks" category_RRB
        And I click on the "SONIC Rechargers with Red Bull" subcategory
        And I open the drink product "Twisted Lime Recharger with Red Bull®"
        And I add all sizes of the drink to the bag_RRB
        And I proceed to checkout_RRB
        Then I should be on the checkout page_RRB
        And I click on the back button_RRB
        And I remove all sizes of the drink from the bag_RRB
        And I close the bag_RRB

    Scenario: Add Blood Orange Recharger with Red Bull® to the bag and proceed to checkout
        When I click on the "Drinks" category_RRB
        And I click on the "SONIC Rechargers with Red Bull" subcategory
        And I open the drink product "Blood Orange Recharger with Red Bull®"
        And I add all sizes of the drink to the bag_RRB
        And I proceed to checkout_RRB
        Then I should be on the checkout page_RRB
        And I click on the back button_RRB
        And I remove all sizes of the drink from the bag_RRB
        And I close the bag_RRB

    Scenario: Add Dragon Fruit Recharger with Red Bull® to the bag and proceed to checkout
        When I click on the "Drinks" category_RRB
        And I click on the "SONIC Rechargers with Red Bull" subcategory
        And I open the drink product "Dragon Fruit Recharger with Red Bull®"
        And I add all sizes of the drink to the bag_RRB
        And I proceed to checkout_RRB
        Then I should be on the checkout page_RRB
        And I click on the back button_RRB
        And I remove all sizes of the drink from the bag_RRB
        And I close the bag_RRB