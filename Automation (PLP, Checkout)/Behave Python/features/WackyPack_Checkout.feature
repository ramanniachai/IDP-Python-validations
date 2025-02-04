@checkout @wackyPack
Feature: Add all Wacky Pack Kids Meals products to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened_W

    Scenario Outline: Add a Wacky Pack Kids Meals product to the bag and proceed to checkout
        When I click on the "Wacky Pack Kids Meals" category
        And I open the Wacky Pack Kids Meals product "<product_name>"
        And I click on the "Next" button_W
        And I select the side item "<side_item>"_W
        And I click on the "Next" button_W
        And I select the drink "<drink>"_W
        And I click on the "Next" button_W
        And I add the Wacky Pack Kids Meals product to the bag
        And I proceed to checkout_W
        Then I should be on the checkout page_W
        And I click on the back button_W
        And I remove the Wacky Pack Kids Meals product from the bag
        And I close the bag_W

        Examples:
            | product_name               | side_item            | drink                             |
            | Hamburger Wacky Pack®      | Groovy Fries         | Milk Jug (1%) - White             |
            | Crispy Tenders Wacky Pack® | Tots                 | Minute Maid® 100% Apple Juice Box |
            | Hot Dog Wacky Pack®        | Tree Top® Applesauce | Milk Jug (1%) - White             |
            | Corn Dog Wacky Pack®       | Tots                 | Minute Maid® 100% Apple Juice Box |
            | Grilled Cheese Wacky Pack® | Groovy Fries         | Milk Jug (1%) - White             |
