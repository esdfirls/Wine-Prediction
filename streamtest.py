import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from app import predict_wine

class StreamlitApp:


    def __init__(self):
        self.title = st.title('Wine Prediction Project')

        df = pd.read_csv(r'C:\Users\aheng\OneDrive\Data Science Knowledge\Projetinhos\Wine-Prediction\winequalityN.csv')
        cols = list(df.columns)
        self.sidetitle = st.sidebar.text('Properties')
        self.tipo = st.sidebar.selectbox('Type',('White Wine','Red Wine'))
        objects = {}
        for col in cols[1:-1]:
            objects[col]=st.sidebar.slider(col,float(df[col].min()),float(df[col].max()),float(df[col].mean()))

        listobjs = list(objects.values())
        mapper = {'White Wine':0,'Red Wine':1}
        
        if st.button('Wine Predict'):

            Wine = predict_wine(mapper[self.tipo], listobjs[0], listobjs[1],listobjs[2],listobjs[3],listobjs[4],listobjs[5],listobjs[6],listobjs[7],listobjs[8],listobjs[9],listobjs[10])
            st.write(f"Wine Quality: {Wine[0]}")
            st.markdown('Probability of Class')
            st.bar_chart(Wine[1])
        else:
            st.write('')






def main():
    app = StreamlitApp()
   
   

if __name__ == '__main__':
    main()
