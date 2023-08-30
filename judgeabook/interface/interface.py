import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

st.markdown("""# Judging a book by its cover.
''Who are you?'''

By analyzing your facial features, your personal characteristic traits will be predicted based on Chinese Horoscopes.""")




image = Image.open('/Users/yaren/Desktop/Zodiac-Wheel-2021-2022.jpg')

st.image(image, caption='Chinese Zodiac Signs based on years')


st.set_option('deprecation.showfileUploaderEncoding', False)

uploaded_file = st.file_uploader("Please upload your picture", type="jpg")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)

if st.button('Upload'):
    print('button clicked!')
    st.write('Please wait 🎉')
    st.write('Your character traits are being predicted!')
else:
    st.write('Please try again 😞')



def add_bg_from_url():   ######NOT WORKING
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image:("/Users/yaren/Desktop/Chinese-zodiac-signs-Graphics-7010501-1.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

    return add_bg_from_url()



#HOW TO CALL API
#import requests
#import streamlit as st
#data = requests.get("'https://jsonplaceholder.typicode.com/todos/1'").json()
#st.write(data)


#E9967A
#E9E9E80






# Loading Image using PIL
im = Image.open('/Users/yaren/Desktop/Chinese-zodiac-signs-Graphics-7010501-1.jpg')

st.set_page_config(page_title="Surge Price Prediction App", page_icon = im)
