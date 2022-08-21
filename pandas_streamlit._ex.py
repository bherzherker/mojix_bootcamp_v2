import streamlit as st 
import pandas as pd
#import matplotlib.pyplot as plt

flag_soh= 0
flag_cc = 0

st.title('Stock/Inventory Discrepancy (Analytics)')
st.header('Importing data')

txt = '''
    If you have the link to the updated data files you can add them, below is the default link.
'''
st.write(txt)
if 'data' not in st.session_state:
    #default dataframe
    st.session_state.df_expected = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Expected.csv", encoding="latin-1", dtype=str)
    st.session_state.df_counted = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Counted.csv", encoding="latin-1", dtype=str)

    st.session_state.df_expected_updated = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Expected.csv", encoding="latin-1", dtype=str)
    st.session_state.df_counted_updated = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Counted.csv", encoding="latin-1", dtype=str)

txt = '''
    Copy the link of your CSV file, to import from a webpage.
    '''
st.write(txt)
file_website_soh = st.text_input('SOH CSV file', "https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Expected.csv")
file_website_cc = st.text_input('Inventory CycleCount CSV file', "https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Counted.csv")

txt = '''
    It is recommended to import the data in order to have the most updated data.
'''
st.write(txt)

import_from_web = st.button("Import data")
if import_from_web:
    st.session_state.df_expected = pd.read_csv(file_website_soh, encoding="latin-1", dtype=str)
    st.session_state.df_counted = pd.read_csv(file_website_cc, encoding="latin-1", dtype=str)
    
    #st.dataframe(st.session_state.df_expected)
    


#SOH
st.dataframe(st.session_state.df_expected)
dimension_soh = st.session_state.df_expected.shape #table dimension 

delimiter = 'x'
dimension_soh_print = delimiter.join([str(value) for value in dimension_soh])
    
unique_soh = st.session_state.df_expected["Retail_Product_SKU"].nunique() # unique values
unique_soh_print = ''.join([str(value) for value in dimension_soh])
    
col1_soh, col2_soh, col3_soh = st.columns(3)
col1_soh.metric("Dimension", dimension_soh_print)
col2_soh.metric("Unique values", unique_soh)
if dimension_soh[0] == unique_soh:
    col3_soh.metric("Duplicates in this table", "False")
else:
    col3_soh.metric("Duplicates in this table", "True")

    ## Inventory CC
st.dataframe(st.session_state.df_counted)
dimension_cc = st.session_state.df_counted.shape #table dimension 

delimiter = 'x'
dimension_cc_print = delimiter.join([str(value) for value in dimension_cc])

unique_cc = st.session_state.df_counted['RFID'].nunique() # unique values
unique_cc_print = ''.join([str(value) for value in dimension_cc])

col1_cc, col2_cc, col3_cc = st.columns(3)
col1_cc.metric("Dimension", dimension_cc_print)
col2_cc.metric("Unique values", unique_cc)
if dimension_cc[0] == unique_cc:
    col3_cc.metric("Duplicates in this table", "False")
else:
    col3_cc.metric("Duplicates in this table", "True")


#fix and update
txt = '''
Press the update button without duplicates before starting the comparison.
'''
st.write(txt)

update_df = st.button('Without duplicates')
if update_df:
    st.session_state.df_expected_updated = st.session_state.df_expected.drop_duplicates("Retail_Product_SKU")
    st.session_state.df_counted_updated = st.session_state.df_counted.drop_duplicates('RFID')

#### Show update
st.dataframe(st.session_state.df_expected_updated)
dimension_soh = st.session_state.df_expected_updated.shape #table dimension 

delimiter = 'x'
dimension_soh_print = delimiter.join([str(value) for value in dimension_soh])
    
unique_soh = st.session_state.df_expected_updated["Retail_Product_SKU"].nunique() # unique values
unique_soh_print = ''.join([str(value) for value in dimension_soh])
    
col1_soh, col2_soh, col3_soh = st.columns(3)
col1_soh.metric("Dimension", dimension_soh_print)
col2_soh.metric("Unique values", unique_soh)
if dimension_soh[0] == unique_soh:
    col3_soh.metric("Duplicates in this table", "False")
else:
    col3_soh.metric("Duplicates in this table", "True")

    ## Inventory CC
st.dataframe(st.session_state.df_counted_updated)
dimension_cc = st.session_state.df_counted_updated.shape #table dimension 

delimiter = 'x'
dimension_cc_print = delimiter.join([str(value) for value in dimension_cc])

unique_cc = st.session_state.df_counted_updated['RFID'].nunique() # unique values
unique_cc_print = ''.join([str(value) for value in dimension_cc])

col1_cc, col2_cc, col3_cc = st.columns(3)
col1_cc.metric("Dimension", dimension_cc_print)
col2_cc.metric("Unique values", unique_cc)
if dimension_cc[0] == unique_cc:
    col3_cc.metric("Duplicates in this table", "False")
else:
    col3_cc.metric("Duplicates in this table", "True")


#prepare for merge
st.session_state.df_expected_updated = st.session_state.df_expected.drop_duplicates("Retail_Product_SKU")
st.session_state.df_counted_updated = st.session_state.df_counted.drop_duplicates('RFID')
df_B = st.session_state.df_counted_updated.groupby("Retail_Product_SKU").count()[["RFID"]] # count and subset RFID
df_B = df_B.reset_index() #prepare to merge
df_B = df_B.rename(columns={"RFID":"Retail_CyCQTY"}) #changing RFID name to Retail_CyCQTY

interest_columns = ["Retail_Product_Color",
                    "Retail_Product_Level1Name",
                    "Retail_Product_Level2Name",
                    "Retail_Product_Level3Name",
                    "Retail_Product_Level4Name",
                    "Retail_Product_Level5Name",
                    "Retail_Product_Name",
                    "Retail_Product_Size",
                    "serial",
                    "Retail_Product_SKU",
                    "Retail_SOHQTY"]

# prepare from SOH
df_A = st.session_state.df_expected_updated[interest_columns]

#merging
st.header('Discrepancy')
txt = '''
In this section the merging of data is performed, be sure not to have duplicate data. The differential or unders will be found.
'''
st.write(txt)
merge = st.button('Merge')
if merge:
    df_discrepancy = pd.merge(df_A, df_B, how="outer", left_on="Retail_Product_SKU", right_on="Retail_Product_SKU", indicator=True) #merging
    df_dyscrepancy = df_discrepancy[['Retail_CyCQTY', 'Retail_Product_Size']] = df_discrepancy[['Retail_CyCQTY', 'Retail_Product_Size']].fillna(0)
    st.dataframe(df_discrepancy)
    # differential
    df_dyscrepancy = df_discrepancy['Retail_CyCQTY'] = df_discrepancy['Retail_CyCQTY'].astype(int)
    df_dyscrepancy = df_discrepancy["Retail_SOHQTY"] = df_discrepancy["Retail_SOHQTY"].fillna(0).astype(int) #converting NAN to 0 and to interger type
    df_dyscrepancy = df_discrepancy["Diff"] = df_discrepancy["Retail_CyCQTY"] - df_discrepancy["Retail_SOHQTY"] #dataframe  by dataframe
    st.dataframe(df_discrepancy)
    st.dataframe(df_discrepancy[["Retail_Product_Name", "Diff"]])
    #st.dataframe(df_diff)
    #unders
    df_discrepancy.loc[df_discrepancy["Diff"]<0, "Unders"] = df_discrepancy["Diff"] * (-1)
    df_discrepancy["Unders"] = df_discrepancy["Unders"].fillna(0).astype(int)
    st.dataframe(df_discrepancy)
    st.dataframe(df_discrepancy[["Retail_Product_Name", "Diff","Unders"]])

