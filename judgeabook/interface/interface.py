import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import requests
from io import BytesIO
import cv2
from judgeabook import params


url = f'{params.SERVICE_URL}/files/'  #ERROR HERE
st.markdown("""# Judging a book by its cover.
''Who are you?'''
By analyzing your facial features, your personal characteristic traits will be predicted based on Chinese Horoscopes.""")
image = Image.open(f'{params.ASSETS_PATH}/Zodiac-Wheel-2021-2022.jpg')
st.image(image, caption='Chinese Zodiac Signs based on years')
if st.button('Upload'):
    st.write('Your character traits are being predicted!')
else:
     print('')
st.set_option('deprecation.showfileUploaderEncoding', False)
uploaded_file = st.file_uploader("Please upload your picture", type=['jpeg','jpg','png'])
if uploaded_file is not None:
    data_bytes = uploaded_file.getvalue()
    uploaded_file.close()

    # st.write(data_bytes)
    response = requests.post(url, data=data_bytes)
    st.image(data_bytes)
    if response.status_code ==200 :
        result = response.json()
        # st.succes('Image uploaded!')
        st.write('API response : ', result)
    else:
        # print(response.json())
        st.error('Failed to upload image.')



#HOW TO CALL API
#import requests
#import streamlit as st
#data = requests.get("'https://jsonplaceholder.typicode.com/todos/1'").json()
#st.write(data)


#E9967A
#E9E9E80






# # Loading Image using PIL
# im = Image.open('/Users/yaren/Desktop/Chinese-zodiac-signs-Graphics-7010501-1.jpg')

# st.set_page_config(page_title="Surge Price Prediction App", page_icon = im)
# from deepface import DeepFace


# if __name__ == "__main__":
#     objs = DeepFace.analyze(img_path = "/Users/maria/Downloads/img3.jpeg",
#         actions = ['age', 'gender', 'race', 'emotion'])
#     print(objs)
