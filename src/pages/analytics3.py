import pathlib
import utils.display as udisp
import pandas as pd
import calendar
import streamlit as st
import plotly.express as px
from PIL import Image

def write():
    udisp.title_awesome("Data Analytics")
    
    
    keys = {
    "Homeownership Rate for the United States: Black or African American Alone" :'./data/homeownership rate for the united states black or african american.csv',
    }
    st.header("Dataset")
    pick = st.selectbox("Select Dataset: ", list(keys.keys()))
        
    if pick == "Homeownership Rate for the United States: Black or African American Alone":
        picks = keys[pick]   
        df = pd.read_csv(picks, encoding='utf8')  
        df.rename(columns = {'BOAAAHORUSQ156N':'Percent'}, inplace = True)
        df['year'] = pd.DatetimeIndex(df['DATE']).year
        df['month'] = pd.DatetimeIndex(df['DATE']).month
        st.dataframe(df)  
    
        st.header("")
        st.header("")
        st.header("")
        st.subheader("Line Graph")
        fig2 = px.line(df, x="DATE", y="Percent", title=str(pick))
        st.plotly_chart(fig2)