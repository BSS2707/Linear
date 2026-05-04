import streamlit as st
import joblib 

m=joblib.load('model.joblib')

st.title('Medical Charges Prediction using Linear Regression And Streamlit')

age = st.number_input('Enter Age', min_value=0, max_value=120, value=30)
bmi = st.number_input('Enter BMI', min_value=0.0, max_value
=100.0, value=25.0)
children = st.number_input('Enter Number of Children', min_value=0, max_value=
10, value=0)    
if st.button('Predict Charges'):
    input_data = [[age, bmi, children]]
    prediction = m.predict(input_data)
    st.error(f'Predicted Medical Charges: ₹ {prediction[0]}')
