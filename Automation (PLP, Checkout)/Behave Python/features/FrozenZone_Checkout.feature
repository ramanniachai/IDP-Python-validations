@checkout @frozenZone
Feature: Add all Frozen Zone products to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened_Fr

    Scenario Outline: Add a Frozen Zone product to the bag and proceed to checkout
        When I click on the "Frozen Zone" category
        And I click on the "<subcategory>" subcategory
        And I open the Frozen Zone product "<product_name>"
        And I add the Frozen Zone product to the bag
        And I proceed to checkout_Fr
        Then I should be on the checkout page_Fr
        And I click on the back button_Fr
        And I remove the Frozen Zone product from the bag
        And I close the bag_Fr

        Examples:
            | subcategory    | product_name                                       |
            | SONIC Blasts   | SONIC Blast® made with REESE’S® Peanut Butter Cups |
            | SONIC Blasts   | Chocolate Chip Cookie Dough Blast®                 |
            | SONIC Blasts   | SONIC Blast® made with M&M’S® Chocolate Candies    |
            | SONIC Blasts   | SONIC Blast® made with OREO® Cookie Pieces         |
            | SONIC Blasts   | SONIC Blast® made with HEATH®                      |
            | SONIC Blasts   | Chocolate Chunk Brownie Blast                      |
            | SONIC Blasts   | Turtle Truffle Nut Blast                           |
            | Classic Shakes | Strawberry Classic Shake                           |
            | Classic Shakes | Chocolate Classic Shake                            |
            | Classic Shakes | Banana Classic Shake                               |
            | Classic Shakes | Vanilla Classic Shake                              |
            | Classic Shakes | Peanut Butter Classic Shake                        |
            | Classic Shakes | Hot Fudge Classic Shake                            |
            | Classic Shakes | Caramel Classic Shake                              |
            | Master Shakes  | Strawberry Cheesecake Master Shake®                |
            | Master Shakes  | Cheesecake Master Shake®                           |
            | Master Shakes  | OREO® Cheesecake Master Shake®                     |
            | Master Shakes  | OREO® Chocolate Master Shake®                      |
            | Master Shakes  | OREO® Peanut Butter Master Shake                   |
            | Sundaes Cones  | Hot Fudge Sundae                                   |
            | Sundaes Cones  | Caramel Sundae                                     |
            | Sundaes Cones  | Strawberry Sundae                                  |
            | Sundaes Cones  | Vanilla Cup                                        |