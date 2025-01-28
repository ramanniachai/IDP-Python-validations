Feature: Add all Combos products to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened_Co

    Scenario Outline: Add a Combos product to the bag and proceed to checkout
        When I click on the "Combos" category
        And I open the Combos product "<product_name>"
        And I click on the "Next" button
        And I select the side item "<side_item>"
        And I click on the "Next" button
        And I select the drink "<drink>"
        And I click on the "Next" button
        And I add the Combos product to the bag
        And I proceed to checkout_Co
        Then I should be on the checkout page_Co
        And I click on the back button_Co
        And I remove the Combos product from the bag
        And I close the bag_Co

        Examples:
            | product_name                                    | side_item    | drink                  |
            | Bacon Deluxe Triple SONIC® Smasher Combo        | Groovy Fries | Strawberry Fusion Fizz |
            | Bacon Deluxe Double SONIC® Smasher Combo        | Tots         | Classic Cruiser        |
            | Triple SONIC® Smasher Combo                     | Groovy Fries | Twisted Flamingo       |
            | Double SONIC® Smasher Combo                     | Groovy Fries | Strawberry Fusion Fizz |
            | Cheesy Bacon SONIC® Stack Combo                 | Tots         | Classic Cruiser        |
            | Cheesy Bacon SuperSONIC® Stack Combo            | Groovy Fries | Twisted Flamingo       |
            | Garlic Butter Bacon Cheeseburger Combo          | Groovy Fries | Twisted Flamingo       |
            | Plain SONIC® Cheeseburger Combo                 | Tots         | Classic Cruiser        |
            | SONIC® Cheeseburger Combo                       | Groovy Fries | Classic Cruiser        |
            | SuperSONIC® Double Cheeseburger Combo           | Groovy Fries | Strawberry Fusion Fizz |
            | SuperSONIC® Bacon Double Cheeseburger Combo     | Tots         | Classic Cruiser        |
            | Chili Cheese Coney Combo                        | Groovy Fries | Twisted Flamingo       |
            | All-American Hot Dog Combo                      | Groovy Fries | Strawberry Fusion Fizz |
            | Footlong Quarter Pound Coney Combo              | Tots         | Classic Cruiser        |
            | Premium Chicken Bites Combo                     | Groovy Fries | Twisted Flamingo       |
            | 3 Piece Crispy Tenders Combo                    | Groovy Fries | Strawberry Fusion Fizz |
            | 5 Piece Crispy Tenders Combo                    | Tots         | Classic Cruiser        |
            | Crispy Chicken Sandwich Combo                   | Groovy Fries | Twisted Flamingo       |
            | Ultimate Meat & Cheese Breakfast Burrito™ Combo | Groovy Fries | Strawberry Fusion Fizz |
            | SuperSONIC® Breakfast Burrito Combo             | Tots         | Classic Cruiser        |
            | Bacon Breakfast Burrito Combo                   | Groovy Fries | Twisted Flamingo       |
            | Sausage Breakfast Burrito Combo                 | Groovy Fries | Strawberry Fusion Fizz |
            | Bacon Breakfast TOASTER® Combo                  | Tots         | Classic Cruiser        |
            | Sausage Breakfast TOASTER® Combo                | Groovy Fries | Twisted Flamingo       |
            | French Toast Sticks Combo                       | Groovy Fries | Strawberry Fusion Fizz |
            | Bacon Deluxe Triple SONIC® Smasher Combo        | Tots         | Classic Cruiser        |
            | Bacon Deluxe Double SONIC® Smasher Combo        | Groovy Fries | Twisted Flamingo       |
            | Classic Chicken Sandwich Combo                  | Groovy Fries | Strawberry Fusion Fizz |
            | Crispy Chicken Tenders Combo                    | Tots         | Classic Cruiser        |
            | product_name                                    | Groovy Fries | Twisted Flamingo       |
            | Bacon Deluxe Triple SONIC® Smasher Combo        | Groovy Fries | Strawberry Fusion Fizz |
            | Bacon Deluxe Double SONIC® Smasher Combo        | Tots         | Classic Cruiser        |
            | Classic Chicken Sandwich Combo                  | Groovy Fries | Twisted Flamingo       |
            | Crispy Chicken Tenders Combo                    | Groovy Fries | Strawberry Fusion Fizz |