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
    "Civilian Labor Force Participation Rate: 20 years and over, Black or African American Men" : './data/civilian labor force participation rate 20 years and over black or african american.csv',
    "Civilian Labor Force Population Rate: Black or African American": './data/civilian labor force population rate black or african american.csv',
    "Labor Force Participation Rate: 20 years and over, Black or African American Women":'./data/labor force participation rate 20 years and over, black or african american women.csv',
    "Labor Force Participation Rate: Black or African American":'./data/labor force participation rate Black or African American.csv',
    "Not in Labor Force: Black or African American":'./data/not in labor force black or african american.csv',
    }
    st.header("Dataset")
    pick = st.selectbox("Select Dataset: ", list(keys.keys()))
    if pick == "Civilian Labor Force Participation Rate: 20 years and over, Black or African American Men":
        picks = keys[pick]
        df = pd.read_csv(picks, encoding='utf8')  
        df.rename(columns = {'LNS11300031':'Percent'}, inplace = True)
        df['year'] = pd.DatetimeIndex(df['DATE']).year
        df['month'] = pd.DatetimeIndex(df['DATE']).month
        st.dataframe(df)  
    
        st.header("")
        st.header("")
        st.header("")
        st.subheader("Line Graph")
        fig2 = px.line(df, x="DATE", y="Percent", title="")
        st.plotly_chart(fig2)

    elif pick == "Civilian Labor Force Population Rate: Black or African American":
        picks = keys[pick]   
        df = pd.read_csv(picks, encoding='utf8')  
        df.rename(columns = {'LNU01300006':'Percent'}, inplace = True)
        df['year'] = pd.DatetimeIndex(df['DATE']).year
        df['month'] = pd.DatetimeIndex(df['DATE']).month
        st.dataframe(df)  
    
        st.header("")
        st.header("")
        st.header("")
        st.subheader("Line Graph")
        fig2 = px.line(df, x="DATE", y="Percent", title="")
        st.plotly_chart(fig2)
        
    elif pick == "Labor Force Participation Rate: 20 years and over, Black or African American Women":
        picks = keys[pick]   
        df = pd.read_csv(picks, encoding='utf8')  
        df.rename(columns = {'LNS11300032':'Percent'}, inplace = True)
        df['year'] = pd.DatetimeIndex(df['DATE']).year
        df['month'] = pd.DatetimeIndex(df['DATE']).month
        st.dataframe(df)  
    
        st.header("")
        st.header("")
        st.header("")
        st.subheader("Line Graph")
        fig2 = px.line(df, x="DATE", y="Percent", title=str(pick))
        st.plotly_chart(fig2)
        
    elif pick == "Labor Force Participation Rate: Black or African American":
        picks = keys[pick]   
        df = pd.read_csv(picks, encoding='utf8')  
        df.rename(columns = {'LNS11300006':'Percent'}, inplace = True)
        df['year'] = pd.DatetimeIndex(df['DATE']).year
        df['month'] = pd.DatetimeIndex(df['DATE']).month
        st.dataframe(df)  
    
        st.header("")
        st.header("")
        st.header("")
        st.subheader("Line Graph")
        fig2 = px.line(df, x="DATE", y="Percent", title=str(pick))
        st.plotly_chart(fig2)
        
    elif pick == "Not in Labor Force: Black or African American":
        picks = keys[pick]   
        df = pd.read_csv(picks, encoding='utf8')  
        df.rename(columns = {'LNS15000006':'Thousands of Persons'}, inplace = True)
        df['year'] = pd.DatetimeIndex(df['DATE']).year
        df['month'] = pd.DatetimeIndex(df['DATE']).month
        st.dataframe(df)  
    
        st.header("")
        st.header("")
        st.header("")
        st.subheader("Line Graph")
        fig2 = px.line(df, x="DATE", y="Thousands of Persons", title=str(pick))
        st.plotly_chart(fig2)
        
    