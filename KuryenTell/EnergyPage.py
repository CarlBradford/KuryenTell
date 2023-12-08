import tkinter as tk
from tkinter import ttk


class EnergyPage(tk.Frame):
    """
        The Energy Page of the Kuryentell application.

        Attributes:
            canvas (tk.Canvas): The canvas widget for displaying energy-related content.
            _drag_data (dict): A dictionary to store data related to dragging.

        Methods:
            __init__: Initializes the Energy Page.
            on_mousewheel: Handles mouse wheel scrolling on the canvas.
            on_drag_start: Records the starting position of a drag event.
            on_drag_end: Resets drag data when the drag event ends.
            on_drag: Updates the scroll region during a drag event.

        """
    def __init__(self, parent):
        """
                Initializes the Energy Page.

                Creates a canvas for displaying energy-related content with scrollbars.

                Args:
                    parent: The parent widget.

                """
        super().__init__(parent)
        outer_frame = ttk.Frame(self, width=1250, height=630)
        outer_frame.pack()

        style = ttk.Style()
        style.configure("Black.TFrame", background="black")

        inner_frame = ttk.Frame(outer_frame, width=630, height=1250, style="Black.TFrame")
        inner_frame.pack(side='left')

        frame = ttk.Frame(inner_frame, width=630, height=1250, style="Black.TFrame")
        frame.pack(expand=True, fill='both')

        self.canvas = tk.Canvas(frame, width=1230, height=630, scrollregion=(0, 0, 1250, 3500), bg='black')
        self.canvas.pack(side='left', expand=True, fill='both')

        v_scrollbar = ttk.Scrollbar(frame, orient='vertical', command=self.canvas.yview)
        v_scrollbar.pack(side='right', fill='y')

        self.canvas.configure(yscrollcommand=v_scrollbar.set)

        self.canvas.bind("<MouseWheel>", self.on_mousewheel)

        self.canvas.bind('<B1-Motion>', self.on_drag_start)
        self.canvas.bind('<ButtonRelease-1>', self.on_drag_end)

        image = tk.PhotoImage(file="Other Images\\Energy Image.png")
        self.canvas.create_image(0, 0, anchor='nw', image=image)
        self.canvas.image = image

        self._drag_data = {'x': 0, 'y': 0}

    def on_mousewheel(self, event):
        """
                Handles mouse wheel scrolling on the canvas.

                Args:
                    event: The mouse wheel event.

                """
        delta = -event.delta // 120
        self.canvas.yview_scroll(delta, 'units')

    def on_drag_start(self, event):
        """
                Records the starting position of a drag event.

                Args:
                    event: The drag start event.

                """
        self._drag_data['x'] = event.x
        self._drag_data['y'] = event.y

    def on_drag_end(self, event):
        """
                Resets drag data when the drag event ends.

                Args:
                    event: The drag end event.

                """
        self._drag_data['x'] = 0
        self._drag_data['y'] = 0

    def on_drag(self, event):
        """
                Updates the scroll region during a drag event.

                Args:
                    event: The drag event.

                """
        delta_x = event.x - self._drag_data['x']
        delta_y = event.y - self._drag_data['y']

        bbox = self.canvas.bbox("all")
        new_scroll_region = (
            max(0, bbox[0] - delta_x),
            max(0, bbox[1] - delta_y),
            bbox[2] - delta_x,
            bbox[3] - delta_y
        )

        self.canvas.configure(scrollregion=new_scroll_region)

        self._drag_data['x'] = event.x
        self._drag_data['y'] = event.y
