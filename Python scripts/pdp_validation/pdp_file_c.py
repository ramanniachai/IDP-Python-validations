import json
import pandas as pd
import requests
import openpyxl
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)




def file_comparison_detailed():
    with open('Products_API_regression3_5575.txt', 'w') as f:
        df1 = pd.read_excel('PDP_PROD_5575_before_3.xlsx')
        df2 = pd.read_excel('PDP_PROD_5575_after_3.xlsx')

        diff_df = df1.eq(df2)  
        not_matching = diff_df[~diff_df]
    
        for column in not_matching.columns:
            for row in not_matching[column].index:
                cell1 = df1.at[row, column]
                if row in df2.index: 
                    cell2 = df2.at[row, column]  
                else: 
                    continue  
                if pd.isnull(cell1) and pd.isnull(cell2):
                    continue
                if cell1 != cell2:
                    #print(f"Cell at ({row},{column}) do not match. {cell1} != {cell2}")
                    #f.write(f"Cell at ({row},{column}) do not match. {cell1} != {cell2}\n")
                    f.write(f"Cell at ({row+2},{column}) ----- {cell1} != {cell2}\n")
    
        f.write(str(diff_df))

#file_comparison_detailed()

def file_comparison_detailed2():
    with open('Log_file.txt', 'w') as f:
        df1 = pd.read_excel('Regresison_UAT11.xlsx')
        df2 = pd.read_excel('Regresison_UAT2.xlsx')

        diff_df = df1.eq(df2)  
        not_matching = diff_df[~diff_df]

        for column in not_matching.columns:
            for row in not_matching[column].index:
                cell1 = str(df1.at[row, column]).replace("\n"," ")
                if row in df2.index: 
                    cell2 = str(df2.at[row, column]).replace("\n"," ")
                else: 
                    continue  
                if pd.isnull(cell1) and pd.isnull(cell2):
                    continue
                #if cell1.strip() != cell2.strip():
                if cell1 != cell2:
                    f.write(f"Cell at ({row+2},{column}) ----- {cell1} != {cell2}\n")
        f.write(str(diff_df))

file_comparison_detailed2()


def file_comparison_detailed3():
    with open('Log_file.txt', 'w') as f:
        df1 = pd.read_excel('Regression_test1.xlsx')
        df2 = pd.read_excel('Regression_test2.xlsx')

        diff_df = df1.eq(df2)  
        not_matching = diff_df[~diff_df]

        for column in not_matching.columns:
            for row in not_matching[column].index:
                #print(row, column) # добавленна строка с print
                cell1 = str(df1.at[row, column]).replace("\n"," ")
                if row in df2.index: 
                    cell2 = str(df2.iloc[row, column]).replace("\n"," ")
                else: 
                    continue  
                if pd.isnull(cell1) and pd.isnull(cell2):
                    continue
                #if cell1.strip() != cell2.strip():
                if cell1 != cell2:
                    f.write(f"Cell at ({row+2},{column}) ----- {cell1} != {cell2}\n")
        f.write(str(diff_df))

#file_comparison_detailed3()