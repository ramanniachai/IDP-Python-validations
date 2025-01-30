Feature: Add all Breakfast products to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened_Br

    Scenario Outline: Add a Breakfast product to the bag and proceed to checkout
        When I click on the "Breakfast" category
        And I open the Breakfast product "<product_name>"
        And I add the Breakfast product to the bag
        And I proceed to checkout_Br
        Then I should be on the checkout page_Br
        And I click on the back button_Br
        And I remove the Breakfast product from the bag
        And I close the bag_Br


        Examples:
            | product_name                                  |
            | French Toast Sticks                           |
            | Bacon BREAKFAST TOASTER®                      |
            | Sausage BREAKFAST TOASTER®                    |
            | Bacon Breakfast Burrito                       |
            | Sausage Breakfast Burrito                     |
            | SuperSONIC® Breakfast Burrito                 |
            | Ultimate Meat & Cheese Breakfast Burrito™     |
            | Jr. Bacon, Egg and Cheese Breakfast Burrito   |
            | Jr. Sausage, Egg and Cheese Breakfast Burrito |
