import streamlit as st
import pickle

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Create input fields for three features
feature1 = st.number_input('Feature 1')
feature2 = st.number_input('Feature 2')
feature3 = st.number_input('Feature 3')

# Create a button for prediction
if st.button('Predict'):
    prediction = model.predict([[feature1, feature2, feature3]])
    st.write('Prediction:', prediction)