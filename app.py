import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Description
st.write("""
This is a simple calculator that can perform basic arithmetic operations:
**Addition**, **Subtraction**, **Multiplication**, and **Division**.
""")

# Input fields for numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Operation selection
operation = st.selectbox("Select Operation", ("Add", "Subtract", "Multiply", "Divide"))

# Function definitions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Perform calculation when button is clicked
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
        st.success(f"{num1} + {num2} = {result}")
    elif operation == "Subtract":
        result = subtract(num1, num2)
        st.success(f"{num1} - {num2} = {result}")
    elif operation == "Multiply":
        result = multiply(num1, num2)
        st.success(f"{num1} * {num2} = {result}")
    elif operation == "Divide":
        result = divide(num1, num2)
        if isinstance(result, str):
            st.error(result)
        else:
            st.success(f"{num1} / {num2} = {result}")
