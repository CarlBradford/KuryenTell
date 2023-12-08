import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk


def about_proj_viewer():
    """
        Displays a top-level window showing an image about the project.

        Creates a top-level window with a canvas, scrollbar, and an image.
        Allows scrolling using the mouse wheel.

        """
    # TOP LEVEL WINDOW
    top_level = tk.Toplevel()
    top_level.resizable(FALSE, FALSE)
    top_level.geometry('1250x700+70+100')

    frame = ttk.Frame(top_level, width=1250, height=630)
    frame.pack(expand=True, fill='both')

    canvas = tk.Canvas(frame, width=1200, height=630)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    image = Image.open("Other Images\\About Image.png")
    img_tk = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor="nw", image=img_tk)

    canvas.config(scrollregion=canvas.bbox("all"))
    try:
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * event.delta / 120), "units"))
    except:
        pass

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    top_level.mainloop()


class HomePage(tk.Frame):
    """
        The home page of the Kuryentell application.

        Attributes:
            home_frame (tk.Frame): The main frame for the home page.
            canvas (tk.Canvas): The canvas within the home frame.
            img (tk.PhotoImage): The image displayed on the home page.

        Methods:
            __init__: Initializes the home page.

        """
    def __init__(self, parent):
        """
                Initializes the home page.

                Creates the main frame, canvas, and displays an image on the canvas.

                Args:
                    parent: The parent widget.

                """
        super().__init__(parent)
        # MAIN FRAME AND BACKGROUND
        self.home_frame = Frame(self, bg='blue', height=630, width=1250, bd=0)
        self.canvas = tk.Canvas(self.home_frame, bg='black', height=630, width=1250, bd=0)
        self.canvas.pack(expand=True)
        self.canvas.create_rectangle(0, 5, 25, 5)
        self.img = PhotoImage(file='Other Images\\Home Image.png')
        self.canvas.create_image(625, 280, anchor='center', image=self.img)

        # ABOUT BUTTON
        Button(self.canvas, text='V  About Project', font=('Century Gothic', 20, 'bold'),
               bg='black', fg='white', bd=0, command=about_proj_viewer).place(x=200, y=490)

        self.home_frame.pack()
        self.pack()

