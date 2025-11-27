import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.header("This is a header")
st.subheader("This is a subheader")

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
st.pyplot(plt)

#streamlit run streamlit_test.py