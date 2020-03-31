"""reading and writing excel files"""
import pandas as pd
def read_excel():#reading Excel files
    '''read excel'''
    r_data = pd.read_excel("cricket.xlsx")
    df_data = pd.DataFrame(r_data)
    print(df_data)
    return df_data
def writeto_excel(df_data):#writing excel files
    '''read'''
    df_data.to_excel('output1.xlsx')
    