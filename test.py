import pytkgif
import tkinter as tk


master = tk.Tk()
gif = pytkgif.Gif(master, pytkgif.Gif.load_images("C:/Python35/pyckage/arbok/image/gif/mirror/カビゴン.gif"))
gif.run_animation(50)
gif.image_label.pack()
master.mainloop()
