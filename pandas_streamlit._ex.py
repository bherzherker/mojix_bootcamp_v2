import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

flag_soh= 0
flag_cc = 0

st.title('Stock/Inventory Discrepancy (Analytics)')
st.header('Importing data')

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

# show = st.button('show')

# if show:
#     st.dataframe(st.session_state.df_expected_updated)
#     dimension_soh = st.session_state.df_expected_updated.shape #table dimension 

#     delimiter = 'x'
#     dimension_soh_print = delimiter.join([str(value) for value in dimension_soh])
        
#     unique_soh = st.session_state.df_expected_updated["Retail_Product_SKU"].nunique() # unique values
#     unique_soh_print = ''.join([str(value) for value in dimension_soh])
        
#     col1_soh, col2_soh, col3_soh = st.columns(3)
#     col1_soh.metric("Dimension", dimension_soh_print)
#     col2_soh.metric("Unique values", unique_soh)
#     if dimension_soh[0] == unique_soh:
#         col3_soh.metric("Duplicates in this table", "False")
#     else:
#         col3_soh.metric("Duplicates in this table", "True")

#         ## Inventory CC
#     st.dataframe(st.session_state.df_counted_updated)
#     dimension_cc = st.session_state.df_counted_updated.shape #table dimension 

#     delimiter = 'x'
#     dimension_cc_print = delimiter.join([str(value) for value in dimension_cc])

#     unique_cc = st.session_state.df_counted_updated['RFID'].nunique() # unique values
#     unique_cc_print = ''.join([str(value) for value in dimension_cc])

#     col1_cc, col2_cc, col3_cc = st.columns(3)
#     col1_cc.metric("Dimension", dimension_cc_print)
#     col2_cc.metric("Unique values", unique_cc)
#     if dimension_cc[0] == unique_cc:
#         col3_cc.metric("Duplicates in this table", "False")
#     else:
#         col3_cc.metric("Duplicates in this table", "True")
