import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
import boa

class Gif:
    def load_images(file_path):
        assert os.path.exists(file_path), file_path
        result = []
        i = 0
        while True:
            try:
                result.append(tk.PhotoImage(file=file_path, format="gif -index " + str(i)))
            except tk.TclError:
                break
            i += 1
        if len(result) == 1:
            return result
        return result[:]

    def __init__(self, master, images):
        self.master = master
        self.images = images
        self.image_label = tk.Label(master=master)
        self.__run_animation_method_call_count = 0

    def run_animation(self, interval):
        assert self.__run_animation_method_call_count == 0
        self.__run_animation_method_call_count += 1

        def run_next_frame_animation(image_index, interval):
            try:
                gif_image = self.images[image_index]
            except Exception:
                image_index = 0
                gif_image = self.images[image_index]

            image_index += 1

            self.image_label.configure(image=gif_image)
            self.master.after(interval, lambda image_index:run_next_frame_animation(image_index, interval),
                              image_index)

        self.master.after(interval, lambda image_index:run_next_frame_animation(image_index, interval), 0)
