import tkinter as tk
import pytkgif
import os

BASE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

root = tk.Tk()
#images is list
images = pytkgif.Gif.load_images(BASE_DIRECTORY + "/python.gif")
gif = pytkgif.Gif(root, images[:])
#gif = pytkgif.Gif(root, images[:-1])
gif.run_animation(interval=60)
gif.image_label.pack()

root.mainloop()
