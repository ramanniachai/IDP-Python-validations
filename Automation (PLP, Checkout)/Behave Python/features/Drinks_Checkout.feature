Feature: Add all drinks to the bag and proceed to checkout

    Background:
        Given Sonic web page is opened__D

    Scenario Outline: Add a drink to the bag and proceed to checkout
        When I click on the "Drinks" category
        And I click on the "<subcategory>" subcategory
        And I open the drink product at index <index>
        And I add the drink to the bag
        And I proceed to checkout_D
        Then I should be on the checkout page_D
        And I click on the back button_D
        And I remove the drink from the bag
        And I close the bag_D

        Examples:
            | subcategory                    | index |
            | Flavorista Favorites           | 1     |
            | Flavorista Favorites           | 2     |
            | Flavorista Favorites           | 3     |
            | Flavorista Favorites           | 4     |
            | Flavorista Favorites           | 5     |
            | Flavorista Favorites           | 6     |
            | Flavorista Favorites           | 7     |
            | Flavorista Favorites           | 8     |
            | SONIC REchargers with Red Bull | 1     |
            | SONIC REchargers with Red Bull | 2     |
            | SONIC REchargers with Red Bull | 3     |
            | SONIC REchargers with Red Bull | 4     |
            | Slushes                        | 1     |
            | Slushes                        | 2     |
            | Slushes                        | 3     |
            | Slushes                        | 4     |
            | Slushes                        | 5     |
            | Slushes                        | 6     |
            | Slushes                        | 7     |
            | Slushes                        | 8     |
            | Slushes                        | 9     |
            | Slushes                        | 10    |
            | Slushes                        | 11    |
            | Slushes                        | 12    |
            | Lemonades & Limeades           | 1     |
            | Lemonades & Limeades           | 2     |
            | Lemonades & Limeades           | 3     |
            | Lemonades & Limeades           | 4     |
            | Lemonades & Limeades           | 5     |
            | Lemonades & Limeades           | 6     |
            | Lemonades & Limeades           | 7     |
            | Soft Drinks                    | 1     |
            | Soft Drinks                    | 2     |
            | Soft Drinks                    | 3     |
            | Soft Drinks                    | 4     |
            | Soft Drinks                    | 5     |
            | Soft Drinks                    | 6     |
            | Soft Drinks                    | 7     |
            | Soft Drinks                    | 8     |
            | Soft Drinks                    | 9     |
            | Soft Drinks                    | 10    |
            | Soft Drinks                    | 11    |
            | Soft Drinks                    | 12    |
            | Soft Drinks                    | 13    |
            | Iced Tea                       | 1     |
            | Iced Tea                       | 2     |
            | Iced Tea                       | 3     |
            | Iced Tea                       | 4     |
            | Iced Tea                       | 5     |
            | Coffee                         | 1     |
            | Coffee                         | 2     |
            | Coffee                         | 3     |
            | Other                          | 1     |
            | Other                          | 2     |
            | Other                          | 3     |
            | Other                          | 4     |
            | Other                          | 5     |
            | Other                          | 6     |