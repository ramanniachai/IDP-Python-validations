Feature: Add all Chicken products to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened_Cc

    Scenario Outline: Add a Chicken product to the bag and proceed to checkout
        When I click on the "Chicken" category
        And I open the Chicken product "<product_name>"
        And I add the Chicken product to the bag
        And I proceed to checkout_Cc
        Then I should be on the checkout page_Cc
        And I click on the back button_Cc
        And I remove the Chicken product from the bag
        And I close the bag_Cc

        Examples:
            | product_name                |
            | Bacon Ranch Queso Wrap      |
            | Southwest Crunch Queso Wrap |
            | Premium Chicken Bites       |
            | Crispy Tenders - 3 Piece    |
            | Crispy Tenders - 5 Piece    |
            | Crispy Chicken Sandwich     |