# IDP-Python-validations
The repository includes several scripts designed to validate the IDP menu.

This file provides explanations for each script added to this repository.


1. pdp_validation : This folder contains two files. First, you need to work with the pdp_validation.py file. The script in this 
file should be executed twice: once for the old menu in the API and once for the new menu. As a result, you will obtain two Excel files 
with detailed product structures. Next, execute the pdp_file_c.py script. This script compares the two Excel files and generates a log file 
where you can find any discrepancies in the menu, if there are any.


2. min_value_if_whatsOnIt.py : This script checks whether the number of single/obligatory modifiers corresponds to the ‘min’ value of the 
modifier group ‘What’s on It’. In cases of any discrepancies, it will cause an error before checkout. 

3. price_validation.py : This script allows you to retrieve prices for new products across all locations. The results will be mapped to a .txt file, 
which can be uploaded to Power BI for better visual representation of the results.

4. price_validation_ALL_PRODUCTS.py : This script retrieves prices for all products across all locations and maps the results into an Excel file.

5. automation-> behave_python directory :
The "behave_python" folder contains all necessary components for automated testing of web and mobile applications using the Behave framework and Gherkin language. Here's a brief overview of its structure and the purpose of each component:

features/ Directory: Contains Gherkin .feature files specifying the test scenarios in a human-readable format. It's where the test cases are defined:
1. plp_web_validation.feature: Test scenarios for web application validation.
2. Plp_app_validation.feature: Test scenarios for mobile application validation.
3. '_Checkout' files: This script simulates the user behavior of opening a product, adding all items to the bag, and navigating to the checkout page.

features/steps/ Directory: Contains Python scripts with step definitions for the scenarios described in the .feature files. These scripts translate Gherkin steps into actions:
1. plp_web_validation.py: Step definitions for web testing scenarios.
2. Plp_app_validations.py: Step definitions for mobile app testing scenarios.
3.'_Checkout' files: Step definitions to simulate product checkout.

environment.py: A configuration file that sets up and tears down the testing environment before and after the test runs. It initializes web or mobile drivers based on the TEST_ENV environment variable.

venv/ Directory: A virtual environment directory containing Python and all necessary packages isolated from the rest of the system. It ensures consistent, reproducible testing environments.

requirements.txt: Lists all Python packages required to run the tests. Use pip install -r requirements.txt to install these dependencies in your virtual environment.
test

