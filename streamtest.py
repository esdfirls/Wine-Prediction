from turtle import width
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from app import predict_wine
from PIL import Image
import plotly.express as px
import time

class StreamlitApp:


    def __init__(self):
        st.set_page_config(page_title='Wine Prediction', layout='wide', initial_sidebar_state='expanded')
        self.df = self.import_df()
        self.title = st.title('Wine Prediction Project')
        with st.expander("See explanation"):
            st.write("""
         The objective of this project is to predict the quality of a wine from its physicochemical properties. 
         Data were extracted from kaggle for study purposes. 
         There are several possibilities of application in development and quality control in the wine making process from this solution.
         
         Based on the properties of the wine, a prediction is made whether the wine is good or bad. 
         The database has the properties and an evaluation score, which goes from 0 to 10. 
         These groups were separated where 0 to 5 is bad and 6 to 10 is good.

         Original Dataset Example:
     """)
            st.dataframe(self.df)   
            st.write(f'Model Accuracy: 83%  \n  Model F1-Score: 83%')

        self.sidetitle = st.sidebar.text('Properties')
        self.tipo = st.sidebar.radio('Type',('White Wine','Red Wine'))

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
            st.plotly_chart(fig, width=400)
        else:
            st.write('')

        self.image = Image.open('WineTypes.jpg')
        st.image(self.image, caption='Wine Types', use_column_width='auto')

    @st.cache(allow_output_mutation=True)
    def import_df(self):
        self.df = pd.read_csv(r'winequalityN.csv')
        self.df.dropna(inplace=True)
        return self.df





def main():
    app = StreamlitApp()
   
   

if __name__ == '__main__':
    main()
