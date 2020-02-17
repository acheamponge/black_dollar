import pathlib
import utils.display as udisp
import pandas as pd
import calendar
import streamlit as st
import plotly.express as px


def write():
    udisp.title_awesome("Employment Data Analytics")
    
    
    keys = {
    "Unemployment Level: 20 years and over, Black or African American Women":'./data/unemployment level 20 years and over, black or african american women.csv',
    "Unemployment Rate: 16 to 19 years, Black or African American":'./data/unemployment rate 16 to 19 years, black or African American.csv',
    "Unemployment Rate: 20 years and over, Black or African American Men":'./data/unemployment rate 20 years and over Black or African American men.csv',
    "Unemployment Rate: 20 years and over, Black or African American Women" : './data/unemployment rate 20 years and over, Black or African American Women.csv',
    "Unemployment Rate: Black or African American":'./data/unemployment rate Black or African American.csv',
    }
    st.header("Dataset")
    pick = st.selectbox("Select Dataset: ", list(keys.keys()))
        
    if pick == "Unemployment Level: 20 years and over, Black or African American Women":
        picks = keys[pick]   
        df = pd.read_csv(picks, encoding='utf8')  
        df.rename(columns = {'LNS13000032':'Thousands of Persons'}, inplace = True)
        df['year'] = pd.DatetimeIndex(df['DATE']).year
        df['month'] = pd.DatetimeIndex(df['DATE']).month
        st.dataframe(df)  
    
        st.header("")
        st.header("")
        st.header("")
        st.subheader("Line Graph")
        fig2 = px.line(df, x="DATE", y="Thousands of Persons", title=str(pick))
        st.plotly_chart(fig2)
        
    elif pick == "Unemployment Rate: 16 to 19 years, Black or African American":
        picks = keys[pick]   
        df = pd.read_csv(picks, encoding='utf8')  
        df.rename(columns = {'LNS14000018':'Percent'}, inplace = True)
        df['year'] = pd.DatetimeIndex(df['DATE']).year
        df['month'] = pd.DatetimeIndex(df['DATE']).month
        st.dataframe(df)  
    
        st.header("")
        st.header("")
        st.header("")
        st.subheader("Line Graph")
        fig2 = px.line(df, x="DATE", y="Percent", title=str(pick))
        st.plotly_chart(fig2)
        
    elif pick == "Unemployment Rate: 20 years and over, Black or African American Men":
        picks = keys[pick]   
        df = pd.read_csv(picks, encoding='utf8')  
        df.rename(columns = {'LNS14000031':'Percent'}, inplace = True)
        df['year'] = pd.DatetimeIndex(df['DATE']).year
        df['month'] = pd.DatetimeIndex(df['DATE']).month
        st.dataframe(df)  
    
        st.header("")
        st.header("")
        st.header("")
        st.subheader("Line Graph")
        fig2 = px.line(df, x="DATE", y="Percent", title=str(pick))
        st.plotly_chart(fig2)
        
    elif pick == "Unemployment Rate: 20 years and over, Black or African American Women":
        picks = keys[pick]   
        df = pd.read_csv(picks, encoding='utf8')  
        df.rename(columns = {'LNU04000032':'Percent'}, inplace = True)
        df['year'] = pd.DatetimeIndex(df['DATE']).year
        df['month'] = pd.DatetimeIndex(df['DATE']).month
        st.dataframe(df)  
    
        st.header("")
        st.header("")
        st.header("")
        st.subheader("Line Graph")
        fig2 = px.line(df, x="DATE", y="Percent", title=str(pick))
        st.plotly_chart(fig2)
        
    elif pick == "Unemployment Rate: Black or African American":
        picks = keys[pick]   
        df = pd.read_csv(picks, encoding='utf8')  
        df.rename(columns = {'LNS14000006':'Percent'}, inplace = True)
        df['year'] = pd.DatetimeIndex(df['DATE']).year
        df['month'] = pd.DatetimeIndex(df['DATE']).month
        st.dataframe(df)  
    
        st.header("")
        st.header("")
        st.header("")
        st.subheader("Line Graph")
        fig2 = px.line(df, x="DATE", y="Percent", title=str(pick))
        st.plotly_chart(fig2)