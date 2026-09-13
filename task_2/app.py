import io
import numpy as np
from PIL import Image, ImageDraw
import streamlit as st

st.set_page_config(
    page_title="Лабораторна -  Створення адаптивної системи розпізнавання з побудовою кластерів методом статистичної обробки навчальних послідовностей", layout="wide"
)
st.title("Завдання 1: Побудова абсолютного та нормованого векторів ознак")
