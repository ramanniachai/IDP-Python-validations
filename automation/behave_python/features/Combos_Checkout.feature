@checkout @combos
Feature: Combos Checkout

    Scenario: Add Bacon Deluxe Triple SONIC® Smasher Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "Bacon Deluxe Triple SONIC® Smasher Combo"
        And I click on the "Next" button
        And I select the side item "Groovy Fries"
        And I click on the "Next" button
        And I select the drink "Strawberry Fusion Fizz"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add Bacon Deluxe Double SONIC® Smasher Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "Bacon Deluxe Double SONIC® Smasher Combo "
        And I click on the "Next" button
        And I select the side item "Tots"
        And I click on the "Next" button
        And I select the drink "Lemonade Cream Cooler"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add Triple SONIC® Smasher Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "Triple SONIC® Smasher Combo"
        And I click on the "Next" button
        And I select the side item "Groovy Fries"
        And I click on the "Next" button
        And I select the drink "Twisted Flamingo"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add Double SONIC® Smasher Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "Double SONIC® Smasher Combo"
        And I click on the "Next" button
        And I select the side item "Groovy Fries"
        And I click on the "Next" button
        And I select the drink "Strawberry Fusion Fizz"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add Cheesy Bacon SONIC® Stack Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "Cheesy Bacon SONIC® Stack Combo"
        And I click on the "Next" button
        And I select the side item "Tots"
        And I click on the "Next" button
        And I select the drink "Lemonade Cream Cooler"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add Cheesy Bacon SuperSONIC® Stack Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "Cheesy Bacon SuperSONIC® Stack Combo"
        And I click on the "Next" button
        And I select the side item "Groovy Fries"
        And I click on the "Next" button
        And I select the drink "Twisted Flamingo"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add Garlic Butter Bacon Cheeseburger Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "Garlic Butter Bacon Cheeseburger Combo"
        And I click on the "Next" button
        And I select the side item "Groovy Fries"
        And I click on the "Next" button
        And I select the drink "Twisted Flamingo"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add Plain SONIC® Cheeseburger Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "Plain SONIC® Cheeseburger Combo"
        And I click on the "Next" button
        And I select the side item "Tots"
        And I click on the "Next" button
        And I select the drink "Lemonade Cream Cooler"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add SONIC® Cheeseburger Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "SONIC® Cheeseburger Combo"
        And I click on the "Next" button
        And I select the side item "Groovy Fries"
        And I click on the "Next" button
        And I select the drink "Lemonade Cream Cooler"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add SuperSONIC® Double Cheeseburger Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "SuperSONIC® Double Cheeseburger Combo"
        And I click on the "Next" button
        And I select the side item "Groovy Fries"
        And I click on the "Next" button
        And I select the drink "Strawberry Fusion Fizz"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add SuperSONIC® Bacon Double Cheeseburger Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "SuperSONIC® Bacon Double Cheeseburger Combo"
        And I click on the "Next" button
        And I select the side item "Tots"
        And I click on the "Next" button
        And I select the drink "Lemonade Cream Cooler"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add Chili Cheese Coney Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "Chili Cheese Coney Combo"
        And I click on the "Next" button
        And I select the side item "Groovy Fries"
        And I click on the "Next" button
        And I select the drink "Twisted Flamingo"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add All-American Hot Dog Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "All-American Hot Dog Combo"
        And I click on the "Next" button
        And I select the side item "Groovy Fries"
        And I click on the "Next" button
        And I select the drink "Strawberry Fusion Fizz"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add Footlong Quarter Pound Coney Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "Footlong Quarter Pound Coney Combo"
        And I click on the "Next" button
        And I select the side item "Tots"
        And I click on the "Next" button
        And I select the drink "Lemonade Cream Cooler"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add Premium Chicken Bites Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "Premium Chicken Bites Combo"
        And I click on the "Next" button
        And I select the side item "Groovy Fries"
        And I click on the "Next" button
        And I select the drink "Twisted Flamingo"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add 3 Piece Crispy Tenders Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "3 Piece Crispy Tenders Combo"
        And I click on the "Next" button
        And I select the side item "Groovy Fries"
        And I click on the "Next" button
        And I select the drink "Strawberry Fusion Fizz"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add 5 Piece Crispy Tenders Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "5 Piece Crispy Tenders Combo"
        And I click on the "Next" button
        And I select the side item "Tots"
        And I click on the "Next" button
        And I select the drink "Lemonade Cream Cooler"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add Crispy Chicken Sandwich Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "Crispy Chicken Sandwich Combo"
        And I click on the "Next" button
        And I select the side item "Groovy Fries"
        And I click on the "Next" button
        And I select the drink "Twisted Flamingo"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add Ultimate Meat & Cheese Breakfast Burrito™ Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "Ultimate Meat & Cheese Breakfast Burrito™ Combo"
        And I click on the "Next" button
        And I select the side item "Groovy Fries"
        And I click on the "Next" button
        And I select the drink "Strawberry Fusion Fizz"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add SuperSONIC® Breakfast Burrito Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "SuperSONIC® Breakfast Burrito Combo"
        And I click on the "Next" button
        And I select the side item "Tots"
        And I click on the "Next" button
        And I select the drink "Lemonade Cream Cooler"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add Bacon Breakfast Burrito Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "Bacon Breakfast Burrito Combo"
        And I click on the "Next" button
        And I select the side item "Groovy Fries"
        And I click on the "Next" button
        And I select the drink "Twisted Flamingo"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add Sausage Breakfast Burrito Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "Sausage Breakfast Burrito Combo"
        And I click on the "Next" button
        And I select the side item "Groovy Fries"
        And I click on the "Next" button
        And I select the drink "Strawberry Fusion Fizz"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add Bacon Breakfast TOASTER® Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "Bacon Breakfast TOASTER® Combo"
        And I click on the "Next" button
        And I select the side item "Tots"
        And I click on the "Next" button
        And I select the drink "Lemonade Cream Cooler"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add Sausage Breakfast TOASTER® Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "Sausage Breakfast TOASTER® Combo"
        And I click on the "Next" button
        And I select the side item "Groovy Fries"
        And I click on the "Next" button
        And I select the drink "Twisted Flamingo"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add French Toast Sticks Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "French Toast Sticks Combo"
        And I click on the "Next" button
        And I select the drink "Strawberry Fusion Fizz"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

    Scenario: Add Fish Sandwich Combo to the bag and proceed to checkout
        Given Sonic web page is opened_Co
        When I click on the "Combos" category
        And I open the Combos product "Fish Sandwich Combo"
        And I click on the "Next" button
        And I select the side item "Groovy Fries"
        And I click on the "Next" button
        And I select the drink "Twisted Flamingo"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co