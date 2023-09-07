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


st.set_page_config(
    page_title="Judgeabook",
    page_icon="🐉",
    layout="wide",
    initial_sidebar_state="collapsed")


emotions = {
    "angry": "angry",
    "disgust": "disgusted",
    "fear": "fearful",
    "happy": "happy",
    "surprise": "surprised",
    "neutral": "neutral",
    "sad": "sad"
}


background_image = "https://storage.googleapis.com/judgeabook-assets/assets/Model-Background-Final.png"

CSS = '''
h1 {{
    color: #d96059;
    }}
.stApp {{
    background-image: url({background_image});
    background-size: cover;
    background-color: #fff5ee;
    }}
'''
formatted_css = CSS.format(background_image=background_image)
st.write(f'<style>{formatted_css}</style>', unsafe_allow_html= True)


def project(tab):
    with tab:
        # col0, col1 = st.columns([0.1, 0.9], gap="small")
        # with col1:
        st.image(f"{params.ASSETS_PATH}/Project-Title.png")


def introduction(tab):
    with tab:
        st.subheader("Can you judge a book by its cover?")
        st.markdown("""
    - Humans are complex and we should not judge — **but we all do!**
    - Studies have shown that opinions about people are formed within **milliseconds**.""")

        col1, col2 = st.columns([0.45, 0.55], gap="large")
        with col1:
            st.subheader("Chinese Zodiac Signs")
        # left_co, center_co, last_co = st.columns([0.1,0.6,0.3])
        # left_co, center_co, last_co = st.columns([0.3,0.4,0.3])
        # with center_co:
        #     st.image(f"{params.ASSETS_PATH}/Zodiac-Wheel-2021-2022.jpg", width=500)
            st.markdown("""
    - Astrological **framework** that links the year of birth to specific character traits.
    - _Example:_ **Born:** 2023 => **Zodiac:** Rabbit => **Trait:** elegant, responsible and friendly.
    """)
            st.image(f"{params.ASSETS_PATH}/Zodiac-Wheel-2021-2022.jpg", width=500)

        with col2:
            st.subheader("Deep Learning Facial Recognition Model")
            st.markdown("""
    - A pretrained Model was used for Face Recognition (DeepFace).
    - **Predict character traits** and emotion based on age and facial features.
                        """)
            st.image(f"{params.ASSETS_PATH}/facial_recognition.png", width=500)

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


def prediction(tab):
    with tab:
        url = f'{params.SERVICE_URL}/files/'
        st.markdown("""# Judging a book by its cover""")
        st.markdown("**Who are you?**")
        st.markdown("By analyzing your facial features, your personal characteristic traits will be predicted based on Chinese Horoscopes.")
        # image = Image.open(f"{params.ASSETS_PATH}/example.png")
        # st.image(image, caption='You will see with our model',width=400)
        st.set_option('deprecation.showfileUploaderEncoding', False)
        uploaded_file = st.file_uploader("Please upload your picture.", type=['jpeg','jpg','png'])
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
                # st.subheader(f"You are a {emotion.capitalize()} {result['sign'].capitalize()}")
                col0, col1, col2 = st.columns([0.1,0.4,0.5], gap='small')
                with col1:
                    st.subheader(f"You are a {emotion.capitalize()} {result['sign'].capitalize()}")
                    st.image(data_bytes, width=450)
                    st.subheader("About you ...")
                    traits = result.get('traits')
                    st.subheader(f"You are {result['age']} years old and your traits are:")
                    st.subheader(f"{traits[0]}, {traits[1]} and {traits[2]}")
                with col2:
                    st.text("")
                    st.text("")
                    st.text("")
                    st.text("")
                    sign = result['sign']
                    emotion = result['emotion']
                    if not os.path.isfile(f"{params.ASSETS_PATH}/signs/{sign}_{result['emotion']}.png"):
                        sign = "unknown"
                        emotion = "neutral"
                    st.image(f"{params.ASSETS_PATH}/signs/{sign}_{emotion}.png", width=450)
            else:
                # print(response.json())
                st.error('Failed to upload image.')


def team_cards(user_names, user_info, image_path):
    for i, col in enumerate(st.columns([1, 1, 1, 1], gap="medium")):
        with col:
            st.image(image_path[i], width=250)
            st.subheader(f"{user_names[i]}")
            st.markdown(user_info[i].replace("\n",
            "<br>"), unsafe_allow_html=True)

def team(tab):
    with tab:
        st.subheader("Team", divider="rainbow")

        user_name = ["Thai",
                    "Maria",
                    "Yaren",
                    "Martin and Benji" ]
        user_info = ["Has a background in International\nBusiness and Business Intelligence.\nHe also worked in a start-up and a\nconsultancy. His interests lie in doing\nsports and meditating.",
                    "She is a Biologist and has broad experience\nin clinical and environmental research.\nShe would like to work on computer\nvision research in the automotive field.\nAnd she likes cats.",
                    "She has a background in Industrial\nEngineering. She has done Data\nAnalytics. Her next goal is studying\nArtificial Intelligence.",
                    "Studied politics and economics.\nBesides traveling he enjoys sports,\ncoffee and a good (or bad) book."]
        image_path = [f"{params.ASSETS_PATH}/Thai.png",
                    f"{params.ASSETS_PATH}/Maria.png",
                    f"{params.ASSETS_PATH}/Yaren.png",
                    f"{params.ASSETS_PATH}/Martin.png"
                    ]

        team_cards(user_name, user_info, image_path)

        if st.button('Thanks 🎈🎈🎈!'):
            st.balloons()

if __name__ == "__main__":
    tab1, tab2, tab3, tab4 = st.tabs(["Project", "Introduction", "Prediction", "About Us"])
    project(tab1)
    introduction(tab2)
    prediction(tab3)
    team(tab4)
