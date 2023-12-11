import streamlit as st
import pandas as pd

def find_largest_num(n1,n2,n3):
    return max(n1,n2,n3)
st.title("Find Largest Number")
 
n1=st.number_input("Enter first number ", value=0.0)
n2=st.number_input("Enter second number ", value=0.0)
n3=st.number_input("Enter third number ", value=0.0)

if st.button("Find largest"):
    l=find_largest_num(n1,n2,n3)
    st.success(f"The largest number is {l}")
    