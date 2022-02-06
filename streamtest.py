import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from app import predict_wine
from PIL import Image

class StreamlitApp:


    def __init__(self):
        self.title = st.title('Wine Prediction Project')
        self.sidetitle = st.sidebar.text('Properties')
        self.tipo = st.sidebar.selectbox('Type',('White Wine','Red Wine'))
        self.df = pd.read_csv(r'winequalityN.csv')

        self.cols = list(self.df.columns)
        self.properties = {}
        for col in self.cols[1:-1]:
            self.properties[col]=st.sidebar.slider(col,float(self.df[col].min()),float(self.df[col].max()),float(self.df[col].mean()))

        self.prop = list(self.properties.values())
        mapper = {'White Wine':0,'Red Wine':1}


        if st.button('Wine Predict'):

            self.wine = predict_wine(mapper[self.tipo], self.prop[0], self.prop[1],self.prop[2],self.prop[3],self.prop[4],self.prop[5],self.prop[6],self.prop[7],self.prop[8],self.prop[9],self.prop[10])
            st.header(f"Wine Quality: {self.wine[0]}")
            st.markdown('Probability of Class')
            st.bar_chart(self.wine[1])
        else:
            st.write('')

        self.image = Image.open('WineTypes.jpg')
        st.image(self.image, caption='Wine Types', use_column_width='auto')





def main():
    app = StreamlitApp()
   
   

if __name__ == '__main__':
    main()
