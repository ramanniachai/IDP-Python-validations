@checkout @burgers
Feature: Add all burgers to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened__
        And I reject non-essential cookies and accept the privacy policy

    Scenario Outline: Add <product_name> to the bag and proceed to checkout
        When I click on the "Burgers" category
        And I open the burger product "<product_name>"
        And I add the burger to the bag
        And I proceed to checkout
        Then I should be on the checkout page
        And I click on the back button
        And I remove the burger from the bag
        And I close the bag

        Examples:
            | product_name                          |
            | Bacon Deluxe Triple SONIC® Smasher    |
            | Bacon Deluxe Double SONIC® Smasher    |
            | Triple SONIC® Smasher                 |
            | Double SONIC® Smasher                 |
            | Cheesy Bacon SONIC® Stack             |
            | Cheesy Bacon SuperSONIC® Stack        |
            | Garlic Butter Bacon Cheeseburger      |
            | SONIC® Cheeseburger                   |
            | Plain SONIC® Cheeseburger             |
            | Quarter Pound Double Cheeseburger     |
            | SuperSONIC® Double Cheeseburger       |
            | SuperSONIC® Bacon Double Cheeseburger |