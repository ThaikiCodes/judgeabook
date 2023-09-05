import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import requests
from io import BytesIO
import cv2
from judgeabook import params
import json
import os

emotions = {
    "angry": "angry",
    "disgust": "disgusted",
    "fear": "fearful",
    "happy": "happy",
    "surprise": "surprised",
    "neutral": "neutral",
    "sad": "sad"
}

background_image = f"{params.ASSETS_PATH}/Page1.png"
background_image_url = "https://storage.cloud.google.com/judgebook/pag2.png"

CSS = '''
h1 {{
    color: #d96059;
    }}
.stApp {{
    background-image: url({background_image_url});
    background-size: cover;
    background-color: #fff5ee;
}}
'''
formatted_css = CSS.format(background_image_url=background_image_url)
st.write(f'<style>{formatted_css}</style>', unsafe_allow_html= True)

def prediction(tab):
    with tab:
        url = f'{params.SERVICE_URL}/files/'  #ERROR HERE
        st.markdown("""# Judging a book by its cover""")
        st.markdown("**Who are you?**")
        st.markdown("By analyzing your facial features, your personal characteristic traits will be predicted based on Chinese Horoscopes.")
        # image = Image.open(f'{params.ASSETS_PATH}/Zodiac-Wheel-2021-2022.jpg')
        # st.image(image, caption='Chinese Zodiac Signs based on years')
        # if st.button('Upload'):
        #     st.write('Your character traits are being predicted!')
        # else:
        #     print('')
        st.set_option('deprecation.showfileUploaderEncoding', False)
        uploaded_file = st.file_uploader("Please upload your picture", type=['jpeg','jpg','png'])
        if uploaded_file is not None:
            data_bytes = uploaded_file.getvalue()
            uploaded_file.close()

            # st.write(data_bytes)
            response = requests.post(url, data=data_bytes)

            if response.status_code ==200 :
                result = response.json()
                # st.write('API response : ', result)
                result = json.loads(result)
                emotion = emotions.get(result.get('emotion', 'neutral'), 'neutral')
                st.subheader(f"You are a {emotion.capitalize()} {result['sign'].capitalize()}")
                col1, col2 = st.columns([1,1], gap='small')
                with col1:
                    st.image(data_bytes, width=300)
                with col2:
                    sign = result['sign']
                    emotion = result['emotion']
                    if not os.path.isfile(f"{params.ASSETS_PATH}/signs/{sign}_{result['emotion']}.png"):
                        sign = "unknown"
                        emotion = "neutral"
                    st.image(f"{params.ASSETS_PATH}/signs/{sign}_{emotion}.png", width=300)
                st.subheader("About you")
                traits = result.get('traits')
                st.markdown(f"You are {result['age']} years old and your traits are:")
                st.markdown(f"{traits[0]}, {traits[1]} and {traits[2]}")
            else:
                # print(response.json())
                st.error('Failed to upload image.')


def about():
    st.header(""":orange[What are Chinese Zodiac Signs? :dragon:]""")
    col1, col2 =st.columns(2)
    with col1:
        st.markdown("""- The 12 animal signs that make up the Chinese zodiac, also known as Sheng Xiao or Shu Xiang, are as follows: Rat, Ox, Tiger, Rabbit, Dragon, Snake, Horse, Sheep, Monkey, Rooster, Dog, and Pig.""")
        st.markdown(""" - It has a more than 2,000-year history and is fundamental to Chinese culture. Its roots are in ancient zoolatry.""")
        st.markdown(""" - In addition to being used to represent years in China, the 12 Chinese zodiac animals are also said to have an impact on people's personalities, careers, compatibility, marriages, and fortune.""")
        st.markdown(""" - Chinese zodiac signs, symbolized by animals, are determined by a person's birth year in accordance with the Chinese lunar calendar.""")
    with col2:
        image = Image.open(f"{params.ASSETS_PATH}/5741_Horoscope-wheel-removebg-preview.jpg")
        st.image(image, caption='Chinese Zodiac Signs based on years' , width=450)

def team_cards(user_names, user_info, image_path):
    for i, col in enumerate(st.columns([1, 1, 1, 1], gap="large")):
        with col:
            st.image(image_path[i], width=100)
            st.subheader(f"{user_names[i]}")
            st.markdown(user_info[i].replace("\n",
            "<br>"), unsafe_allow_html=True)

def introduction(tab):
    with tab:
        st.image(f"{params.ASSETS_PATH}/Pink Modern Lunar New Year Party Invitation.png")

def history(tab):
    with tab:
        st.subheader("Can you judge a book by its cover?")

        st.markdown("""
    - People are complex and it's not easy to judge people solely based on appearance
    - **However, first impressions** can have significant psychological effects on individuals
    - Studies showed: **people can make judgments** about a person's trustworthiness and competence based on
    **very brief exposures to their facial expressions**""")

        st.subheader("Chinese Zodiac Signs")

        left_co, center_co, last_co = st.columns([0.1,0.6,0.3])
        with center_co:
            st.image(f"{params.ASSETS_PATH}/Zodiac-Wheel-2021-2022.jpg", width=500)



        st.markdown("""
    - Chinese astrological **framework** for **understanding personality traits**
    - People's zodiac signs are determined by their **birth year**, and each year is **associated** with
    one of the **twelve animal** signs
    - Each **sign is associated** with **specific personality traits and characteristics**""")
        st.subheader("Using Deep Learning to map a face to positive character traits")
        st.markdown("""
    - Use of **convolutional neural network** to analyse faces
    - **Predict character traits** based on facial characteristics
                        """)

def team(tab):
    with tab:
        st.subheader("Team", divider="rainbow")

        user_name = ["Thai Dao",
                    "Maria Escalante-Rojas",
                    "Yaren Merve Akin",
                    "Martin" ]
        user_info = ["I studied Business Intelligence and Smart Services in my Masters. Then became a Strategy Consultant.",
                    "I'm a biologist, master's degree in science.",
                    "I studied Industrial Engineering. I want to improve myself on artificial intelligence.",
                    "Political Scientist and Economist by education. Into books, sports, coffee, concerts."]
        image_path = [f"{params.ASSETS_PATH}/Thai.png",
                    f"{params.ASSETS_PATH}/Maria.png",
                    f"{params.ASSETS_PATH}/Yaren.png",
                    f"{params.ASSETS_PATH}/Martin.png"
                    ]

        team_cards(user_name, user_info, image_path)


if __name__ == "__main__":
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Introduction", "History", "Process", "Prediction", "About Us"])
    # about()
    # application()
    introduction(tab1)
    history(tab2)
    prediction(tab4)
    team(tab5)
