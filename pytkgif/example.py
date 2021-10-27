import tkinter as tk
import pytkgif

root = tk.Tk()
gif = pytkgif.Gif(root, "gif_path")
gif.run_animation(interval=30)
gif.image_label.pack()
root.mainloop()
