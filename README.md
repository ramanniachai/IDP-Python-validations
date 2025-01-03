# IDP-Python-validations
The repository contains a number of scripts to validate IDP menu.

This file contans some explanation for each script added to this repository.

1. pdp_validation: There're 2 files in this folder. At first you need to work with 'pdp_validation.py' file. The script in this file
should be executed for the old menu in API and for the new one. So the script should be executed twice. As a result, you'll get 2 excel
file with detailed products' structure. 
Then we need to execute 'pdp_file_c.py' script. This script compares 2 excel file and generated log file when you can find discrepancies 
in the menu if there're any.

