import io
import numpy as np
from PIL import Image, ImageDraw
import streamlit as st

st.set_page_config(
    page_title="Лабораторна -  Створення адаптивної системи розпізнавання з побудовою кластерів методом статистичної обробки навчальних послідовностей", layout="wide"
)
st.title("Завдання 1: Побудова абсолютного та нормованого векторів ознак")
# func generate testing data 4ex "2"
def gen_test_img():
    img = Image.new("L", (150, 150), color=255) # bg white
    draw = ImageDraw.Draw(img)
    # draw a "2"
    draw.arc([30, 20, 120, 80], start=180, end=0, fill=0, width=14)
    draw.line([(120, 50), (30, 130)], fill=0, width=14)
    draw.line([(30, 130), (120, 130)], fill=0, width=14)
    return img
# alg to calc px
def extract_features(imgage: Image.Image, row=5, col=5):
    binary = np.array(imgage) < 128  # Convert to binary (black/white)
    h, w = binary.shape

    abs_vector = []
    row_step = h // row
    col_step = w // col
    for r in range(row):
        for c in range(col):
            row_start = r * row_step
            row_end = (r + 1) * row_step
            col_start = c * col_step
            col_end = (c + 1) * col_step
            cell = binary[row_start:row_end, col_start:col_end]
            abs_vector.append(np.sum(cell))  # Count black pixels in the cell
    abs_vector = np.array(abs_vector, dtype=float)
    norm_vector = abs_vector / np.sum(abs_vector) if np.sum(abs_vector) > 0 else abs_vector
    return abs_vector, norm_vector
