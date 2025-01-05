# IDP-Python-validations
The repository includes several scripts designed to validate the IDP menu.

This file provides explanations for each script added to this repository.


1. pdp_validation: This folder contains two files. First, you need to work with the pdp_validation.py file. The script in this 
file should be executed twice: once for the old menu in the API and once for the new menu. As a result, you will obtain two Excel files 
with detailed product structures. Next, execute the pdp_file_c.py script. This script compares the two Excel files and generates a log file 
where you can find any discrepancies in the menu, if there are any.


2. min_value_if_whatsOnIt.py: This script checks whether the number of single/obligatory modifiers corresponds to the ‘min’ value of the 
modifier group ‘What’s on It’. In cases of any discrepancies, it will cause an error before checkout. 

3. price_validation.py: This script allows you to retrieve prices for new products across all locations. The results will be mapped to a .txt file, 
which can be uploaded to Power BI for better visual representation of the results.


