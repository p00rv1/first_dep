import streamlit as st
import numpy as np
import pickle
from streamlit_option_menu import option_menu
load=pickle.load(open('trained_model.sav','rb'))
with st.sidebar:
    selected=option_menu('Multiple Disease Pred',
                         ['Diabetes Pred',
                          ''])
def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    pred = load.predict(input_data_reshaped)
    print(pred)
    if(pred[0]==0):
        return 'Has Diabetes'
    else:
        return 'No Diabetes'
def main():
    st.title('Diabetes prediction web app')
    P=st.text_input("No. of pregnancies")
    G = st.text_input("Glucose Level")
    BP= st.text_input("Blood Pressure")
    I = st.text_input("Insulin Level")
    Skin = st.text_input("Skin Thickness")
    BMI = st.text_input("BMI value")
    ped = st.text_input("Diabetes Pedigree function VAl")
    age= st.text_input("AGE")
    diagnosis=''
    if st.button('Diabetes Test Result'):
        inp=(P,G,BP,Skin,I,BMI,ped,age)
        diagnosis=diabetes_prediction(inp)
    st.success(diagnosis)

if __name__=='__main__':
    main()