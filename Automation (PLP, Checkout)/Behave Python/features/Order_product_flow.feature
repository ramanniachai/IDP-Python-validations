Feature: Add a burger to the bag and proceed to checkout

    Scenario: Add a burger to the bag and proceed to checkout
        Given Sonic web page is opened__
        When I reject non-essential cookies and accept the privacy policy
        And I click on the "Burgers" category
        And I open the first burger product
        And I add the burger to the bag
        And I proceed to checkout
        Then I should be on the checkout page