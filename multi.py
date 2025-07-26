import streamlit as st
import numpy as np
import pickle
from streamlit_option_menu import option_menu
load=pickle.load(open('trained_model.sav','rb'))
with st.sidebar:
    selected=option_menu('Multiple Disease Pred',
                         ['Diabetes Prediction',
                          'Heart','Parkin'],default_index=0)