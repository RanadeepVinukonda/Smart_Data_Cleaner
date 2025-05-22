
import streamlit as st
import pandas as pd
st.title('Streamlit App with CSV Upload ,cleaning , and download')
st.write('Upload a CSV file to clean and download it.')
# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
# If a file is selected, it will be displayed
if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    st.write("Original DataFrame:")
    st.dataframe(df)

    # Clean the DataFrame
    # Remove rows with any missing values
    cleaned_df = df.dropna()
    st.write("Cleaned DataFrame (missing values removed):")
    st.dataframe(cleaned_df)

    # Download button for cleaned DataFrame
    csv = cleaned_df.to_csv(index=False)
    st.download_button(
        label="Download Cleaned CSV",
        data=csv,
        file_name='cleaned_data.csv',
        mime='text/csv'
    )