@checkout @frozenZone @blasts
Feature: Add all sizes of SONIC Blasts products to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened_SB

    Scenario Outline: Add <product_name> to the bag and proceed to checkout
        When I click on the "Frozen Zone" category_SB
        And I click on the "SONIC Blasts" subcategory
        And I open the SONIC Blasts product "<product_name>"
        And I add all sizes of the SONIC Blasts product to the bag
        And I proceed to checkout_SB
        Then I should be on the checkout page_SB
        And I click on the back button_SB
        And I remove all sizes of the SONIC Blasts product from the bag
        And I close the bag_SB

        Examples:
            | product_name                                       |
            | Turtle Truffle Nut Blast                           |
            | Chocolate Chunk Brownie Blast                      |
            | SONIC Blast® made with HEATH®                      |
            | SONIC Blast® made with OREO® Cookie Pieces         |
            | SONIC Blast® made with REESE’S® Peanut Butter Cups |
            | SONIC Blast® made with M&M’S® Chocolate Candies    |
            | Chocolate Chip Cookie Dough Blast®                 |