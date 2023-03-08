import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Header Text
st.header('st.write')

# Example 1 - Display Markdown-formatted text
st.write('hello, *World!* :sunglasses')

# Example 2 - Diaplay Numeric Data
st.write(1234)

# Example 3 - Display Data in tabular form
df = pd.DataFrame({
    'first column' : [1, 2, 3, 4],
    'second column' : [10, 20, 30, 40]
})

st.write(df)

#Exanple 4 - Pass multiple arguments
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5 - Display plots by passing variable
df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns = ['a', 'b', 'c']
)

c = alt.Chart(df2).mark_circle().encode(
    x = 'a', y = 'b', size = 'c', color = 'c', tooltip = ['a', 'b', 'c']
)

st.write(c)