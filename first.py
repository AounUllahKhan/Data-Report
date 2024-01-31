import numpy as np
import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Web App Title
st.markdown('''
# **The EDA App**

This is the **EDA App** created in Streamlit using the **pandas-profiling** library.
---
''')

# Upload CSV data
with st.sidebar.header('1. Upload your Excel data'):
    header = st.sidebar.number_input('Enter Header', min_value=1, max_value=10, value=1, step=1)
    uploaded_file = st.sidebar.file_uploader("Upload your input Excel file", type=["xlsx"])
    


# Pandas Profiling Report
if uploaded_file is not None:
    # @st.cache_data
    def load_excel():
        excel_file = pd.ExcelFile(uploaded_file)
        sheet_names = excel_file.sheet_names
        selected_sheet_name = st.selectbox('Select the Sheet Name',sheet_names)
    
        csv = pd.read_excel(uploaded_file,sheet_name=selected_sheet_name,header=header-1)
        return csv
    df = load_excel()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for Excel file to be uploaded.')
