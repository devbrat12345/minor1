# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 22:07:30 2022

@author: 91831
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('C:\work/heart_disease_model.sav' ,'rb'))

# creating a function for Prediction

def heart_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction == 0):
      return 'The Person does not have a heart disease'
    else:
      return 'The Person has a heart disease'
  
    
  
def main():
    
    
    # giving a title
    st.title('Heart Disease Prediction Web App')
    
    
    # getting the input data from the user
    
    
    age= st.number_input('Age of the person')
    sex = st.number_input('Gender')
    cp = st.number_input('CP value')
    trestbps = st.number_input('Trestbps value')
    chol = st.number_input('Chol Level')
    fbs = st.number_input('Fbsvalue')
    restecg = st.number_input('Restecg value')
    thalach = st.number_input('Thalach value')
    exang = st.number_input('Exang value')
    oldpeak = st.number_input('Oldpeak value')
    slope = st.number_input('Slope Value')
    ca = st.number_input('Ca value')
    thal = st.number_input('Thal value')
    
    
    
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        diagnosis = heart_prediction([age, sex, cp, trestbps, chol, fbs, restecg, thalach ,exang ,oldpeak ,slope ,ca ,thal])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    