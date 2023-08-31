import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import requests

url = 'http://localhost:8502/'  #ERROR HERE


st.markdown("""# Judging a book by its cover.
''Who are you?'''

By analyzing your facial features, your personal characteristic traits will be predicted based on Chinese Horoscopes.""")

image = Image.open('/Users/yaren/Desktop/Zodiac-Wheel-2021-2022.jpg')

st.image(image, caption='Chinese Zodiac Signs based on years')

if st.button('Upload'):
    st.write('Your character traits are being predicted!')
else:
     print('')


st.set_option('deprecation.showfileUploaderEncoding', False)

uploaded_file = st.file_uploader("Please upload your picture", type=['jpeg','jpg','png'])

if uploaded_file is not None:
    data_bytes = uploaded_file.getvalue()
    st.image(data_bytes)
    st.write(data_bytes)

    files = {"file" : (data_bytes)}
    response = requests.post(url, files=files)

    if response.status_code ==200 :
        result = response.json()
        st.succes('Image uploaded!')
        st.write('API response : ', result)
    else:
        st.error('Failed to upload image.')









# def add_bg_from_url():   ######NOT WORKING
#     st.markdown(
#          f"""
#          <style>
#          .stApp {{
#              background-image:("/Users/yaren/Desktop/Chinese-zodiac-signs-Graphics-7010501-1.jpg");
#              background-attachment: fixed;
#              background-size: cover
#          }}
#          </style>
#          """,
#          unsafe_allow_html=True
#      )

#     return add_bg_from_url()



#HOW TO CALL API
#import requests
#import streamlit as st
#data = requests.get("'https://jsonplaceholder.typicode.com/todos/1'").json()
#st.write(data)

# Loading Image using PIL
# im = Image.open('/Users/yaren/Desktop/Chinese-zodiac-signs-Graphics-7010501-1.jpg')

# st.set_page_config(page_title="Surge Price Prediction App", page_icon = im)
