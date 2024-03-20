
    
import streamlit as st

import pickle 
import pandas as pd
from sklearn import datasets

import plotly.graph_objects as go
from sklearn.preprocessing import MinMaxScaler

import numpy as np

def get_clean_data():
    features=datasets.load_breast_cancer().feature_names

    df=pd.DataFrame(datasets.load_breast_cancer().data, columns=features)
    df["diagnosis"]=datasets.load_breast_cancer().target
    return df

def main():
    st.set_page_config(
        page_title="Breast Cancer Predictor",
        page_icon=":female-Doctor",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    
    df=get_clean_data()
    st.sidebar.header("Cell Nuclei Measurements")
    slider_labels=[[x,x.replace(" ","_").capitalize()] for x in df.columns if x !="diagnosis"]
    
    
    inp_dict={}
    for i in slider_labels:
        inp_dict[i[0]]=st.sidebar.slider(
            i[1],
         
            min_value=float(0),
            max_value=float(df[i[0]].max()),
            value=float(df[i[0]].mean()),
            
            
        )
    
    def get_scaled_value(inp_dict):
        scaled={}
        for key,value in inp_dict.items():
            mx=df[key].max()
            mn=df[key].min()
            scaled_value=(value-mn)/(mx-mn)
            scaled[key]=scaled_value
        
        return scaled
            
    
    def get_radar_plot(inp_dic):
      
        col=[" ".join(x.split()[1:]).capitalize() for x in  [x for x in df.columns if "mean" in x]]
        
        sacled_dic=get_scaled_value(inp_dic)
        mean_measure=[sacled_dic[x] for x in df.columns if "mean" in x]
        error_measure=[sacled_dic[x] for x in df.columns if "error" in x]
        worst_measure=[sacled_dic[x] for x in df.columns if "worst" in x]
        fig=go.Figure()
     
        fig.add_trace(go.Scatterpolar(r=mean_measure,theta=col,fill="toself", name="mean"))
        fig.add_trace(go.Scatterpolar(r=error_measure,theta=col,fill="toself", name="error"))
        fig.add_trace(go.Scatterpolar(r=worst_measure,theta=col,fill="toself", name="worst"))
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True)),
            showlegend=True,
        
        )
        return fig
     
        
    def add_prediction(inp_dic):
        
        x_values=np.array(list(inp_dic.values())).reshape(1,-1)
        
        scaler=pickle.load(open("scaler.pkl","rb"))
        model=pickle.load(open("model.pkl","rb"))
        
        trans_values=scaler.transform(x_values)
        
        st.subheader("Cell Cluster Prediction")
        st.write("The Cell Cluster Is :\n")
        if model.predict(trans_values)==0:
            st.write("Benign")
        else :
            st.write("Malignant")
            
        st.write("The probablity of being benign :",model.predict_proba(trans_values)[0][0])
        st.write("The probablity of being Malignant :",model.predict_proba(trans_values)[0][1])
        st.write("This app is used for assiting medical professionals but ,however it is not substitue for any proffesional diagnosis ")   
        
        
        
        
        
        
        
         
    # st.markdown(
    #     <style>          </style>
        
    # )
    
    
    with st.container():
        st.title("Breast Cancer Prediction")
        st.write("Please connect this app to your cytology lab to help diagnose breast cancer from your tissue sample . This app predicts using a machine learning model whether your breast is benign or malignant based on the measurements received from the cytosis lab .You can update the measurement by hand using the slider in the sidebar")
        
        col1,col3,col2=st.columns([4,0.5,1],gap='medium')
        st.write("Hello world")
    
        with col1:
          
           fig=get_radar_plot(inp_dict)
           st.plotly_chart(fig)
           
        with col2:
         
           add_prediction(inp_dict)

       
    
if __name__=="__main__":
    main()