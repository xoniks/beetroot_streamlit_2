import streamlit as st

st.title('Calculate Wage App :sunglasses:')


hours = st.number_input('Please enter hours: ',step=1)

rate = st.number_input('Please enter rate: ')

# result = hours * float(rate)

def calculate_wage(hours, rate):
    return hours * rate


if st.button('Calculate wage '):
    result = calculate_wage(hours, rate)
    st.write(f'Your wage is {result}')