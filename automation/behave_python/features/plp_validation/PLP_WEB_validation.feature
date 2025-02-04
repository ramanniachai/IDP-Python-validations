Feature: PLP validation

    Scenario: Validate the list of products under Combos category
        Given Sonic web page is opened_
        When User clicks on Combos category
        Then The list of all combos products is displayed on the page

    Scenario: Validate the list of products under Flavorista Favorites category
        When User clicks on Drinks category
        And User clicks on Flavorista Favorites subcategory
        Then The list of all Flavorista Favorites products is displayed on the page

    Scenario: Validate the list of products under Sonic Rechargers category
        When User clicks on Drinks category
        And User clicks on Sonic Rechargers subcategory
        Then The list of all Sonic Rechargers products is displayed on the page

    Scenario: Validate the list of products under Slushes category
        When User clicks on Drinks category
        And User clicks on Slushes subcategory
        Then The list of all Slushes products is displayed on the page

    Scenario: Validate the list of products under Lemonades & Limeades category
        When User clicks on Drinks category
        And User clicks on Lemonades & Limeades subcategory
        Then The list of all Lemonades & Limeades products is displayed on the page

    Scenario: Validate the list of products under Soft Drinks category
        When User clicks on Drinks category
        And User clicks on Soft Drinks subcategory
        Then The list of all Soft Drinks products is displayed on the page

    Scenario: Validate the list of products under Iced Tea category
        When User clicks on Drinks category
        And User clicks on Iced Tea subcategory
        Then The list of all Iced Tea products is displayed on the page

    Scenario: Validate the list of products under Coffee category
        When User clicks on Drinks category
        And User clicks on Coffee subcategory
        Then The list of all Coffee products is displayed on the page

    Scenario: Validate the list of products under Other category
        When User clicks on Drinks category
        And User clicks on Other subcategory
        Then The list of all Other products is displayed on the page

    Scenario: Validate the list of products under Burgers category
        When User clicks on Burgers category
        Then The list of all Burgers products is displayed on the page

    Scenario: Validate the list of products under Featured category
        When User clicks on Featured category
        Then The list of all Featured products is displayed on the page

    Scenario: Validate the list of products under $1.99 category
        When User clicks on $1.99 category
        Then The list of all $1.99 products is displayed on the page

    Scenario: Validate the list of products under Snacks & Sides category
        When User clicks on Snacks & Sides category
        Then The list of all Snacks & Sides products is displayed on the page

    Scenario: Validate the list of products under Carhop Classics category
        When User clicks on Carhop Classics category
        Then The list of all Carhop Classics products is displayed on the page

    Scenario: Validate the list of products under Sonic Blasts category
        When User clicks on Frozen Zone category
        And User clicks on Sonic Blasts subcategory
        Then The list of all Sonic Blasts products is displayed on the page

    Scenario: Validate the list of products under Classic Shakes category
        When User clicks on Frozen Zone category
        And User clicks on Classic Shakes subcategory
        Then The list of all Classic Shakes products is displayed on the page

    Scenario: Validate the list of products under Master Shakes category
        When User clicks on Frozen Zone category
        And User clicks on Master Shakes subcategory
        Then The list of all Master Shakes products is displayed on the page

    Scenario: Validate the list of products under Sundaes category
        When User clicks on Frozen Zone category
        And User clicks on Sundaes subcategory
        Then The list of all Sundaes products is displayed on the page

    Scenario: Validate the list of products under Hot Dogs category
        When User clicks on Hot Dogs category
        Then The list of all Hot Dogs products is displayed on the page

    Scenario: Validate the list of products under Chicken category
        When User clicks on Chicken category
        Then The list of all Chicken products is displayed on the page

    Scenario: Validate the list of products under Breakfast category
        When User clicks on Breakfast category
        Then The list of all Breakfast products is displayed on the page

    Scenario: Validate the list of products under Wacky Pack Kids Meals category
        When User clicks on Wacky Pack category
        Then The list of all Wacky Pack products is displayed on the page

    Scenario: Validate the list of products under Sandwiches Kids Meals category
        When User clicks on Sandwiches category
        Then The list of all Sandwiches products is displayed on the page

