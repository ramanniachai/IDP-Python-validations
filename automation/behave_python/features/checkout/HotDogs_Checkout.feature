@checkout @hotDogs
Feature: Add all Hot Dogs products to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened_H

    Scenario Outline: Add <product_name> to the bag and proceed to checkout
        When I click on the "Hot Dogs" category
        And I open the Hot Dogs product "<product_name>"
        And I add the Hot Dogs product to the bag
        And I proceed to checkout_H
        Then I should be on the checkout page_H
        And I click on the back button_H
        And I remove the Hot Dogs product from the bag
        And I close the bag_H

        Examples:
            | product_name                 |
            | All-American Dog             |
            | Chili Cheese Coney           |
            | Footlong Quarter Pound Coney |
            | Corn Dog                     |