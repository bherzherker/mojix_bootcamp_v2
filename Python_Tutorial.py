import streamlit as st 

# title
st.title("Python tutorial: Tricks to make your life easier.")
# header
st.header("Simple but effective tips for every python lovers")
# text
st.text("Here you have 10 tips to use in python to make easier your data science path")

#Tutorial
#subheader
# step 1 
st.header("1. Walrus operator")
st.text("The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.")
st.subheader("Example:")
st.code("Mylist = [1,2,3]")
st.code(if(l := len(Mylist) > 2):)
st.code(print(l)) 
st.code(print(a := Mylist)) 
st.code(print(a)) 


st.subheader("Output")
st.success("true")
st.success("[1,2,3]")
