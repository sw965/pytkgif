import tkinter as tk
import pytkgif
import os

BASE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
images = pytkgif.Gif.load_images(BASE_DIRECTORY + "/python.gif")

root = tk.Tk()
gif = pytkgif.Gif(root, images[:])
gif.run_animation(interval=60)
gif.image_label.pack()

root.mainloop()
