@checkout @drinks @flavorista
Feature: Add all sizes of Flavorista Favorites drinks to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened__FF

    Scenario: Add Strawberry Mangonada Slush to the bag and proceed to checkout
        When I click on the "Drinks" category
        And I click on the "Flavorista Favorites" subcategory
        And I open the drink product "Strawberry Mangonada Slush"
        And I add the drink to the bag
        And I proceed to checkout_FF
        Then I should be on the checkout page_FF
        And I click on the back button_FF
        And I remove the drink from the bag
        And I close the bag_FF

    Scenario: Add Strawberry Shortcake Snowball Slush Float to the bag and proceed to checkout
        When I click on the "Drinks" category
        And I click on the "Flavorista Favorites" subcategory
        And I open the drink product "Strawberry Shortcake Snowball Slush Float"
        And I add the drink to the bag
        And I proceed to checkout_FF
        Then I should be on the checkout page_FF
        And I click on the back button_FF
        And I remove the drink from the bag
        And I close the bag_FF

    Scenario: Add Strawberry Fusion Fizz to the bag and proceed to checkout
        When I click on the "Drinks" category
        And I click on the "Flavorista Favorites" subcategory
        And I open the drink product "Strawberry Fusion Fizz"
        And I add all sizes of the drink to the bag
        And I proceed to checkout_FF
        Then I should be on the checkout page_FF
        And I click on the back button_FF
        And I remove all sizes of the drink from the bag
        And I close the bag_FF

    Scenario: Add Sour Dragon Fruit Recharger with Red Bull® to the bag and proceed to checkout
        When I click on the "Drinks" category
        And I click on the "Flavorista Favorites" subcategory
        And I open the drink product "Sour Dragon Fruit Recharger with Red Bull®"
        And I add all sizes of the drink to the bag
        And I proceed to checkout_FF
        Then I should be on the checkout page_FF
        And I click on the back button_FF
        And I remove all sizes of the drink from the bag
        And I close the bag_FF

    Scenario: Add Sparkling Sugar Cookie Dr Pepper® to the bag and proceed to checkout
        When I click on the "Drinks" category
        And I click on the "Flavorista Favorites" subcategory
        And I open the drink product "Sparkling Sugar Cookie Dr Pepper®"
        And I add all sizes of the drink to the bag
        And I proceed to checkout_FF
        Then I should be on the checkout page_FF
        And I click on the back button_FF
        And I remove all sizes of the drink from the bag
        And I close the bag_FF

    Scenario: Add Lemonade Cream Cooler to the bag and proceed to checkout
        When I click on the "Drinks" category
        And I click on the "Flavorista Favorites" subcategory
        And I open the drink product "Lemonade Cream Cooler"
        And I add all sizes of the drink to the bag
        And I proceed to checkout_FF
        Then I should be on the checkout page_FF
        And I click on the back button_FF
        And I remove all sizes of the drink from the bag
        And I close the bag_FF

    Scenario: Add Rainbow Slush to the bag and proceed to checkout
        When I click on the "Drinks" category
        And I click on the "Flavorista Favorites" subcategory
        And I open the drink product "Rainbow Slush"
        And I add the drink to the bag
        And I proceed to checkout_FF
        Then I should be on the checkout page_FF
        And I click on the back button_FF
        And I remove the drink from the bag
        And I close the bag_FF

    Scenario: Add Twisted Flamingo to the bag and proceed to checkout
        When I click on the "Drinks" category
        And I click on the "Flavorista Favorites" subcategory
        And I open the drink product "Twisted Flamingo"
        And I add all sizes of the drink to the bag
        And I proceed to checkout_FF
        Then I should be on the checkout page_FF
        And I click on the back button_FF
        And I remove all sizes of the drink from the bag
        And I close the bag_FF

    Scenario: Add Dirty Dr Pepper® to the bag and proceed to checkout
        When I click on the "Drinks" category
        And I click on the "Flavorista Favorites" subcategory
        And I open the drink product "Dirty Dr Pepper®"
        And I add all sizes of the drink to the bag
        And I proceed to checkout_FF
        Then I should be on the checkout page_FF
        And I click on the back button_FF
        And I remove all sizes of the drink from the bag
        And I close the bag_FF