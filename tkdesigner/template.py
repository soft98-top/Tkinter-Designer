TEMPLATE = """
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"{{ assets_path }}")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("{{ window.width }}x{{ window.height }}")
window.configure(bg = "{{ window.bg_color }}")


canvas = Canvas(
    window,
    bg = "{{ window.bg_color }}",
    height = {{ window.height }},
    width = {{ window.width }},
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)


{%- for element in elements -%}
    {{ element.to_code() }}
{%- endfor -%}


window.resizable(False, False)
window.mainloop()

"""
