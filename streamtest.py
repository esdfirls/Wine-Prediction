from tracemalloc import start
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from app import predict_wine
from PIL import Image
import plotly.express as px
import time

class StreamlitApp:


    def __init__(self):
        self.title = st.title('Wine Prediction Project')
        with st.expander("See explanation"):
            st.write("""
         The objective of this project is to predict the quality of a wine from its physicochemical properties. 
         Data were extracted from kaggle for study purposes. 
         There are several possibilities of application in development and quality control in the wine making process from this solution.
     """)
        self.sidetitle = st.sidebar.text('Properties')
        self.tipo = st.sidebar.radio('Type',('White Wine','Red Wine'))
        self.df = pd.read_csv(r'winequalityN.csv')

        self.cols = list(self.df.columns)
        self.properties = {}
        for col in self.cols[1:-1]:
            self.properties[col]=st.sidebar.slider(col,float(self.df[col].min()),float(self.df[col].max()),float(self.df[col].mean()))

        self.prop = list(self.properties.values())
        mapper = {'White Wine':0,'Red Wine':1}


        # Predict Button
        if st.button('Wine Predict'):
            starttime = time.time()
            self.wine = predict_wine(mapper[self.tipo], self.prop[0], self.prop[1],self.prop[2],self.prop[3],self.prop[4],self.prop[5],self.prop[6],self.prop[7],self.prop[8],self.prop[9],self.prop[10])
            st.markdown('Time execution: {:.2f} seconds'.format((time.time() - starttime)))
            # self.progress = st.pr
            if self.wine[0] == 'Good Wine':
                st.success(f"Wine Quality: {self.wine[0]}")
            else:
                st.error(f"Wine Quality: {self.wine[0]}")
            st.markdown(f"Wine Type: {self.tipo}")

            st.markdown('Probability of Class')
            fig = px.pie(self.wine[1], values=self.wine[1][0], names=['Bad Wine','Good Wine'], color_discrete_sequence=px.colors.sequential.Burgyl)
            st.plotly_chart(fig)
        else:
            st.write('')

        self.image = Image.open('WineTypes.jpg')
        st.image(self.image, caption='Wine Types', use_column_width='auto')





def main():
    app = StreamlitApp()
   
   

if __name__ == '__main__':
    main()
