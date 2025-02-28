@fishSand
Feature: Order Fish Sandwich with selected modifiers and proceed to checkout

    Background:
        Given Sonic web page is opened_FS

    Scenario: Add Fish Sandwich to the bag and proceed to checkout with Easy Pickles, Extra Tartar Sauce, Regular Cheese Slice
        When I click on the "Sandwiches" category_FS
        And I open the Sandwiches product "Fish Sandwich"
        And I select Pickles intensity as "Easy"
        And I select Tartar Sauce intensity as "Extra"
        And I select Cheese Slice intensity as "Regular"
        And I add the Sandwiches product to the bag_FS
        And I proceed to checkout_FS
        Then I should be on the checkout page_FS

    Scenario: Add Fish Sandwich to the bag and proceed to checkout with Easy Lettuce, None Tartar Sauce, Extra Cheese Slice
        When I click on the "Sandwiches" category_FS
        And I open the Sandwiches product "Fish Sandwich"
        And I select Lettuce intensity as "Easy"
        And I select Tartar Sauce intensity as "None"
        And I select Cheese Slice intensity as "Extra"
        And I add the Sandwiches product to the bag_FS
        And I proceed to checkout_FS
        Then I should be on the checkout page_FS

    Scenario: Add Fish Sandwich to the bag and proceed to checkout with Extra Lettuce, None Pickles, Extra Cheese Slice
        When I click on the "Sandwiches" category_FS
        And I open the Sandwiches product "Fish Sandwich"
        And I select Lettuce intensity as "Extra"
        And I select Pickles intensity as "None"
        And I select Cheese Slice intensity as "Extra"
        And I add the Sandwiches product to the bag_FS
        And I proceed to checkout_FS
        Then I should be on the checkout page_FS

    Scenario: Add Fish Sandwich to the bag and proceed to checkout with None Lettuce, Easy Pickles, Extra Tartar Sauce
        When I click on the "Sandwiches" category_FS
        And I open the Sandwiches product "Fish Sandwich"
        And I select Lettuce intensity as "None"
        And I select Pickles intensity as "Easy"
        And I select Tartar Sauce intensity as "Extra"
        And I add the Sandwiches product to the bag_FS
        And I proceed to checkout_FS
        Then I should be on the checkout page_FS

    Scenario: Add Fish Sandwich to the bag and proceed to checkout with Extra Pickles, None Tartar Sauce, Extra Cheese Slice
        When I click on the "Sandwiches" category_FS
        And I open the Sandwiches product "Fish Sandwich"
        And I select Pickles intensity as "Extra"
        And I select Tartar Sauce intensity as "None"
        And I select Cheese Slice intensity as "Extra"
        And I add the Sandwiches product to the bag_FS
        And I proceed to checkout_FS
        Then I should be on the checkout page_FS

    Scenario: Add Fish Sandwich to the bag and proceed to checkout with Easy Lettuce, None Pickles, Extra Tartar Sauce
        When I click on the "Sandwiches" category_FS
        And I open the Sandwiches product "Fish Sandwich"
        And I select Lettuce intensity as "Easy"
        And I select Pickles intensity as "None"
        And I select Tartar Sauce intensity as "Extra"
        And I add the Sandwiches product to the bag_FS
        And I proceed to checkout_FS
        Then I should be on the checkout page_FS

    Scenario: Add Fish Sandwich to the bag and proceed to checkout with Extra Lettuce, Easy Pickles
        When I click on the "Sandwiches" category_FS
        And I open the Sandwiches product "Fish Sandwich"
        And I select Lettuce intensity as "Extra"
        And I select Pickles intensity as "Easy"
        And I add the Sandwiches product to the bag_FS
        And I proceed to checkout_FS
        Then I should be on the checkout page_FS

    Scenario: Add Fish Sandwich to the bag and proceed to checkout with None Lettuce, Extra Tartar Sauce, Extra Cheese Slice
        When I click on the "Sandwiches" category_FS
        And I open the Sandwiches product "Fish Sandwich"
        And I select Lettuce intensity as "None"
        And I select Tartar Sauce intensity as "Extra"
        And I select Cheese Slice intensity as "Extra"
        And I add the Sandwiches product to the bag_FS
        And I proceed to checkout_FS
        Then I should be on the checkout page_FS

    Scenario: Add Fish Sandwich to the bag and proceed to checkout with None Pickles, Easy Tartar Sauce
        When I click on the "Sandwiches" category_FS
        And I open the Sandwiches product "Fish Sandwich"
        And I select Pickles intensity as "None"
        And I select Tartar Sauce intensity as "Easy"
        And I add the Sandwiches product to the bag_FS
        And I proceed to checkout_FS
        Then I should be on the checkout page_FS

    Scenario: Add Fish Sandwich to the bag and proceed to checkout with Easy Lettuce, Extra Pickles, Extra Cheese Slice
        When I click on the "Sandwiches" category_FS
        And I open the Sandwiches product "Fish Sandwich"
        And I select Lettuce intensity as "Easy"
        And I select Pickles intensity as "Extra"
        And I select Cheese Slice intensity as "Extra"
        And I add the Sandwiches product to the bag_FS
        And I proceed to checkout_FS
        Then I should be on the checkout page_FS

    Scenario: Add Fish Sandwich to the bag and proceed to checkout with Extra Lettuce, Easy Tartar Sauce, Extra Cheese Slice
        When I click on the "Sandwiches" category_FS
        And I open the Sandwiches product "Fish Sandwich"
        And I select Lettuce intensity as "Extra"
        And I select Tartar Sauce intensity as "Easy"
        And I select Cheese Slice intensity as "Extra"
        And I add the Sandwiches product to the bag_FS
        And I proceed to checkout_FS
        Then I should be on the checkout page_FS

    Scenario: Add Fish Sandwich to the bag and proceed to checkout with None Lettuce, None Pickles
        When I click on the "Sandwiches" category_FS
        And I open the Sandwiches product "Fish Sandwich"
        And I select Lettuce intensity as "None"
        And I select Pickles intensity as "None"
        And I add the Sandwiches product to the bag_FS
        And I proceed to checkout_FS
        Then I should be on the checkout page_FS