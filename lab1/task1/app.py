import io
import streamlit as st
import numpy as np
from PIL import Image, ImageDraw

st.set_page_config(page_title="Лаб.1 - Завдання 1", layout="wide")
st.title("Побудова абсолютних та нормованих векторів ознак розпізнавання стандартизованих графічних зображень")

# func gen numb "2"
def get_test_img():
    img = Image.new("L", (150, 150), color=255) # white bg
    draw = ImageDraw.Draw(img)
    # draw numb "2"
    draw.arc([30, 20, 130, 80], start=0, end=180, fill=0, width=14)
    draw.line([120, 50], [30, 130] fill=0, width=14)
    draw.line([30, 130], [120, 130], fill=0, width=14)
    return img
# func calc px
def calc_px(image: Image.Image, rows=5, cols=5):
    binary = np.array(image) < 128 # black & white
    h, w = binary.shape

    abs_vector = []
    row_step = h // rows
    col_step = w // cols
    for r in range(rows):
        for c in range(cols):
            row_start = r * row_step
            row_end = (r+1) * row_step
            col_start = c * col_step
            col_end = (c+1) * col_step
            cell = binary[row_start:row_end, col_start:col_end]
            abs_vector.append(np.sum(cell)) # count black px in cell
    abs_vector = np.array(abs_vector, dtype=float)
    

    

# grid
def draw_grid(image: Image.Image, rows=5, cols=5):
    grid_img = image.convert("RGB")
    draw = ImageDraw.Draw(grid_img)
    w, h = grid_img.size
    for r in range(1, rows):
        y = int(r * (h / rows))
        draw.line([0, y], [w, y], fill="red", width=3)
    for c in range(1, cols):
        x = int(c * (w / cols))
        draw.line([x, 0], [x, h], fill="red", width=3)
    return grid_img

# interface
