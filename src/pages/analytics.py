import pathlib
import utils.display as udisp
import pandas as pd
import calendar
import streamlit as st
import plotly.express as px


def write():
    udisp.title_awesome("Employment Data Analytics")
    
    image = Image.open('./img/3.jpg')

    st.image(image, use_column_width=True)
    
    keys = {
    
    "Employed Full Time: Median Usual Weekly Nominal Earnings (second quartile): Wage and Salary Workers 25 to 54: Black or African American" :'./data/employed full time median usual weekly nominal earnings wage and salary workers 25 to 54 black or african american.csv',
    "Employed full time: Median usual weekly real earnings: Wage and salary workers: 16 years and over: Black or African American" : './data/employed full time Median usual weekly real earnings wage and salary workers 16 years and over Black or African America.csv',
    "Employed full time: Median usual weekly real earnings: Wage and salary workers: 16 years and over: Black or African American: Men":'./data/employed full time median usual weekly real earnings wage and salary workers 16 years and over black or african american men.csv',
    "Employed full time: Median usual weekly real earnings: Wage and salary workers: 16 years and over: Black or African American: Women" : './data/employed full time median usual weekly real earnings wage and salary workers 16 years and over black or african american women.csv',
    "Employed full time: Wage and salary workers: 25 to 54 years: Black or African American":'./data/employed full time wage and salary workers 25 to 54 years black or african american.csv',
    "Employment Level: Black or African American":'./data/employment level black or african american.csv',
    "Employment-Population Ratio: 16 to 19 years, Black or African American":'./data/employment population ratio 16 to 19 years black or african american.csv',
    "Employment-Population Ratio: 20 years and over, Black or African American Men":'./data/employment population ratio 20 years and over, Black or African American Men.csv',
    "Employment-Population Ratio: Black or African American":'./data/employment-population ratio black or african american.csv',
    }
    
    
    st.header("Dataset")
    pick = st.selectbox("Select Dataset: ", list(keys.keys()))
       
    if pick == "Employed Full Time: Median Usual Weekly Nominal Earnings (second quartile): Wage and Salary Workers 25 to 54: Black or African American":
        picks = keys[pick]   
        df = pd.read_csv(picks, encoding='utf8')  
        df.rename(columns = {'LEU0253204900Q':'Dollars'}, inplace = True)
        df['year'] = pd.DatetimeIndex(df['DATE']).year
        df['month'] = pd.DatetimeIndex(df['DATE']).month
        st.dataframe(df)  
    
        st.header("")
        st.header("")
        st.header("")
        st.subheader("Line Graph")
        fig2 = px.line(df, x="DATE", y="Dollars", title="")
        st.plotly_chart(fig2)    
 
 
    elif pick == "Employed full time: Median usual weekly real earnings: Wage and salary workers: 16 years and over: Black or African American":
        picks = keys[pick]   
        df = pd.read_csv(picks, encoding='utf8')  
        df.rename(columns = {'LEU0252884600Q':'1982-84 CPI Adjusted Dollars'}, inplace = True)
        df['year'] = pd.DatetimeIndex(df['DATE']).year
        df['month'] = pd.DatetimeIndex(df['DATE']).month
        st.dataframe(df)  
    
        st.header("")
        st.header("")
        st.header("")
        st.subheader("Line Graph")
        fig2 = px.line(df, x="DATE", y="1982-84 CPI Adjusted Dollars", title=str(pick))
        st.plotly_chart(fig2) 
        
    elif pick == "Employed full time: Median usual weekly real earnings: Wage and salary workers: 16 years and over: Black or African American: Men":
        picks = keys[pick]   
        df = pd.read_csv(picks, encoding='utf8')  
        df.rename(columns = {'LEU0252884900Q':'1982-84 CPI Adjusted Dollars'}, inplace = True)
        df['year'] = pd.DatetimeIndex(df['DATE']).year
        df['month'] = pd.DatetimeIndex(df['DATE']).month
        st.dataframe(df)  
    
        st.header("")
        st.header("")
        st.header("")
        st.subheader("Line Graph")
        fig2 = px.line(df, x="DATE", y="1982-84 CPI Adjusted Dollars", title=str(pick))
        st.plotly_chart(fig2)       
        
        
    elif pick == "Employed full time: Median usual weekly real earnings: Wage and salary workers: 16 years and over: Black or African American: Women":
        picks = keys[pick]   
        df = pd.read_csv(picks, encoding='utf8')  
        df.rename(columns = {'LEU0252885200Q':'1982-84 CPI Adjusted Dollars'}, inplace = True)
        df['year'] = pd.DatetimeIndex(df['DATE']).year
        df['month'] = pd.DatetimeIndex(df['DATE']).month
        st.dataframe(df)  
    
        st.header("")
        st.header("")
        st.header("")
        st.subheader("Line Graph")
        fig2 = px.line(df, x="DATE", y="1982-84 CPI Adjusted Dollars", title=str(pick))
        st.plotly_chart(fig2)
        
    elif pick == "Employed full time: Wage and salary workers: 25 to 54 years: Black or African American":
        picks = keys[pick]   
        df = pd.read_csv(picks, encoding='utf8')  
        df.rename(columns = {'LEU0253204800A':'Thousands of Persons'}, inplace = True)
        df['year'] = pd.DatetimeIndex(df['DATE']).year
        df['month'] = pd.DatetimeIndex(df['DATE']).month
        st.dataframe(df)  
    
        st.header("")
        st.header("")
        st.header("")
        st.subheader("Line Graph")
        fig2 = px.line(df, x="DATE", y="Thousands of Persons", title=str(pick))
        st.plotly_chart(fig2)
        
        
    elif pick == "Employment Level: Black or African American":
        picks = keys[pick]   
        df = pd.read_csv(picks, encoding='utf8')  
        df.rename(columns = {'LNS12000006':'Thousands of Persons'}, inplace = True)
        df['year'] = pd.DatetimeIndex(df['DATE']).year
        df['month'] = pd.DatetimeIndex(df['DATE']).month
        st.dataframe(df)  
    
        st.header("")
        st.header("")
        st.header("")
        st.subheader("Line Graph")
        fig2 = px.line(df, x="DATE", y="Thousands of Persons", title=str(pick))
        st.plotly_chart(fig2)
        
    elif pick == "Employment-Population Ratio: 16 to 19 years, Black or African American":
        picks = keys[pick]   
        df = pd.read_csv(picks, encoding='utf8')  
        df.rename(columns = {'LNS12300018':'Percent'}, inplace = True)
        df['year'] = pd.DatetimeIndex(df['DATE']).year
        df['month'] = pd.DatetimeIndex(df['DATE']).month
        st.dataframe(df)  
    
        st.header("")
        st.header("")
        st.header("")
        st.subheader("Line Graph")
        fig2 = px.line(df, x="DATE", y="Percent", title=str(pick))
        st.plotly_chart(fig2)
        
    elif pick == "Employment-Population Ratio: 20 years and over, Black or African American Men":
        picks = keys[pick]   
        df = pd.read_csv(picks, encoding='utf8')  
        df.rename(columns = {'LNU02300031':'Percent'}, inplace = True)
        df['year'] = pd.DatetimeIndex(df['DATE']).year
        df['month'] = pd.DatetimeIndex(df['DATE']).month
        st.dataframe(df)  
    
        st.header("")
        st.header("")
        st.header("")
        st.subheader("Line Graph")
        fig2 = px.line(df, x="DATE", y="Percent", title=str(pick))
        st.plotly_chart(fig2)
        
    elif pick == "Employment-Population Ratio: Black or African American":
        picks = keys[pick]   
        df = pd.read_csv(picks, encoding='utf8')  
        df.rename(columns = {'LNS12300006':'Percent'}, inplace = True)
        df['year'] = pd.DatetimeIndex(df['DATE']).year
        df['month'] = pd.DatetimeIndex(df['DATE']).month
        st.dataframe(df)  
    
        st.header("")
        st.header("")
        st.header("")
        st.subheader("Line Graph")
        fig2 = px.line(df, x="DATE", y="Percent", title=str(pick))
        st.plotly_chart(fig2)
        
  