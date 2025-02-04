@checkout @featured
Feature: Add all featured items to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened__F

    Scenario: Add Bacon Deluxe Double SONIC® Smasher to the bag and proceed to checkout
        When I click on the "Featured" category
        And I open the featured item "Bacon Deluxe Double SONIC® Smasher"
        And I add the featured item to the bag
        And I proceed to checkout_F
        Then I should be on the checkout page_F
        And I click on the back button_F
        And I remove the featured item from the bag
        And I close the bag_F

    Scenario: Add Bacon Deluxe Triple SONIC® Smasher to the bag and proceed to checkout
        When I click on the "Featured" category
        And I open the featured item "Bacon Deluxe Triple SONIC® Smasher"
        And I add the featured item to the bag
        And I proceed to checkout_F
        Then I should be on the checkout page_F
        And I click on the back button_F
        And I remove the featured item from the bag
        And I close the bag_F

    Scenario: Add Strawberry Shortcake Snowball Slush Float to the bag and proceed to checkout
        When I click on the "Featured" category
        And I scroll down to "Flavorista Favorites"
        And I open the featured item "Strawberry Shortcake Snowball Slush Float"
        And I add the featured item to the bag
        And I proceed to checkout_F
        Then I should be on the checkout page_F
        And I click on the back button_F
        And I remove the featured item from the bag
        And I close the bag_F

    Scenario: Add Side of Queso to the bag and proceed to checkout
        When I click on the "Featured" category
        And I scroll down to "Side of Queso"
        And I open the featured item "Side of Queso"
        And I add the featured item to the bag
        And I proceed to checkout_F
        Then I should be on the checkout page_F
        And I click on the back button_F
        And I remove the featured item from the bag
        And I close the bag_F

    Scenario: Add Double SONIC® Smasher to the bag and proceed to checkout
        When I click on the "Featured" category
        And I scroll down to "SONIC® Smashers"
        And I open the featured item "Double SONIC® Smasher"
        And I add the featured item to the bag
        And I proceed to checkout_F
        Then I should be on the checkout page_F
        And I click on the back button_F
        And I remove the featured item from the bag
        And I close the bag_F

    Scenario: Add Triple SONIC® Smasher to the bag and proceed to checkout
        When I click on the "Featured" category
        And I scroll down to "SONIC® Smashers"
        And I open the featured item "Triple SONIC® Smasher"
        And I add the featured item to the bag
        And I proceed to checkout_F
        Then I should be on the checkout page_F
        And I click on the back button_F
        And I remove the featured item from the bag
        And I close the bag_F

    Scenario: Add Bacon Ranch Queso Wrap to the bag and proceed to checkout
        When I click on the "Featured" category
        And I scroll down to "$1.99 Queso Wraps"
        And I open the featured item "Bacon Ranch Queso Wrap"
        And I add the featured item to the bag
        And I proceed to checkout_F
        Then I should be on the checkout page_F
        And I click on the back button_F
        And I remove the featured item from the bag
        And I close the bag_F

    Scenario: Add Southwest Crunch Queso Wrap to the bag and proceed to checkout
        When I click on the "Featured" category
        And I scroll down to "$1.99 Queso Wraps"
        And I open the featured item "Southwest Crunch Queso Wrap"
        And I add the featured item to the bag
        And I proceed to checkout_F
        Then I should be on the checkout page_F
        And I click on the back button_F
        And I remove the featured item from the bag
        And I close the bag_F