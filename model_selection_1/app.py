import numpy as np
import pickle
import pandas as pd
import streamlit as st

pickle_in = open("C:/Users/ASUS/Desktop/All/Moldel_Selection/model_selection_1/Final_model.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_Disease_Detection(MDVP_Fo,MDVP_Fhi,MDVP_Flo,MDVP_jitter,MDVP_Jitter_Abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE):
    prediction=classifier.predict([[MDVP_Fo,MDVP_Fhi,MDVP_Flo,MDVP_jitter,MDVP_Jitter_Abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
    print(prediction)
    return prediction


def main():
    st.title("Parkinson’s Disease Detection App")
    html_temp = """
    <div style="background-color:green;padding:10px">
    <h2 style="color:white;text-align:center;">Parkinson’s Disease Detection </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    MDVP_Fo = st.text_input("MDVP_Fo")
    MDVP_Fhi = st.text_input("MDVP_Fhi")
    MDVP_Flo = st.text_input("MDVP_Flo")
    MDVP_jitter = st.text_input("MDVP_jitter")
    MDVP_Jitter_Abs = st.text_input("MDVP_Jitter_Abs")
    MDVP_RAP = st.text_input("MDVP_RAP")
    MDVP_PPQ = st.text_input("MDVP_PPQ")
    Jitter_DDP = st.text_input("Jitter_DDP")
    MDVP_Shimmer = st.text_input("MDVP_Shimmer")
    MDVP_Shimmer_dB = st.text_input("MDVP_Shimmer_dB")
    Shimmer_APQ3 = st.text_input("Shimmer_APQ3")
    Shimmer_APQ5 = st.text_input("Shimmer_APQ5")
    MDVP_APQ = st.text_input("MDVP_APQ")
    Shimmer_DDA = st.text_input("Shimmer_DDA")
    NHR = st.text_input("NHR")
    HNR = st.text_input("HNR")
    RPDE = st.text_input("RPDE")
    DFA = st.text_input("DFA")
    spread1 = st.text_input("spread1")
    spread2 = st.text_input("spread2")
    D2 = st.text_input("D2")
    PPE = st.text_input("PPE")
    result=""
    if st.button("Predict"):
        result=predict_Disease_Detection(MDVP_Fo,MDVP_Fhi,MDVP_Flo,MDVP_jitter,MDVP_Jitter_Abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE)
        if result==0:
            st.success("The patient is not effected and healthy.")
        else:
            st.warning("The patient is effected with Parkinson’s Disease !!!")

main()











