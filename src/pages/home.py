import pathlib
import utils.display as udisp
from PIL import Image
import streamlit as st


def write():
    udisp.title_awesome("Home")
    image = Image.open('./img/1.jpg')

    st.image(image, use_column_width=False)
    
    st.write(
            """
The $Black project is data analytics and visualization project that seeks to bring more insights into the economical data of African Americans.

In this project, we're looking at:
- **Employment**.
- **Salaries**. 
- **Population**.
- **Home Ownership**.
    """
        
    )
    
    image = Image.open('./img/2.jpg')

    st.image(image, use_column_width=False)
