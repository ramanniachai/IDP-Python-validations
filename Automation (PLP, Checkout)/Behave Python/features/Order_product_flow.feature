 Feature: Add all burgers to the bag and proceed to checkout
 
     Scenario Outline: Add a burger to the bag and proceed to checkout
         Given Sonic web page is opened__
         When I reject non-essential cookies and accept the privacy policy
         And I click on the "Burgers" category
         And I open the burger product at index <index>
         And I add the burger to the bag
         And I proceed to checkout
         Then I should be on the checkout page
         And I remove the burger from the bag
 
     Examples:
         | index |
         | 1     |
         | 2     |
         | 3     |
         | 4     |
         | 5     |
         | 6     |
         | 7     |
         | 8     |
         | 9     |
         | 10    |
