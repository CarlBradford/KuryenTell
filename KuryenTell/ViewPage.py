import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from ExcelData import *


class ViewPage(tk.Frame):
    """
        The View Page of the Kuryentell application.

        Attributes:
            price_frame (tk.Frame): The main frame for the View Page.
            large_frame (tk.Frame): The large center frame within the View Page.
            ...

        Methods:
            __init__: Initializes the View Page.
            create_labels: Creates and displays labels on the View Page.
            create_entry: Creates and displays entry boxes on the View Page.
            create_identity: Creates and displays identity labels on the View Page.
            to_reset: Resets the entry fields and image on the View Page.
            to_search: Searches for an appliance by ID and populates the fields on the View Page.

        """
    def __init__(self, parent):
        """
                Initializes the View Page.

                Creates the main frame, large center frame, and initializes variables.

                Args:
                    parent: The parent widget.

                """
        super().__init__(parent)
        # MAIN FRAME AND BACKGROUND
        self.price_frame = Frame(self, bg='black', height=630, width=1250, bd=0)

        # LARGE CENTER FRAME
        self.large_frame = Frame(self.price_frame, bg='#A6A6A6', height=490, width=1000)
        self.large_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.black_line = Label(self.large_frame, bg='black')
        self.black_line.place(x=0, y=140, height=10, width=1000)

        Label(self.large_frame, text="View Appliance Information", font=('Century Gothic', 25, 'bold'),
              bg='#A6A6A6', fg='yellow').place(x=70, y=10)

        Label(self.large_frame, text="Nov 2023 Meralco Rate: ₱ 12.0545", font=('Century Gothic', 15),
              bg='#A6A6A6', fg='yellow').place(x=660, y=10)

        Label(self.large_frame, text="ENTER APPLIANCE/DEVICE ID", font=('Century Gothic', 15, 'bold'),
              bg='#A6A6A6', fg='white').place(x=70, y=70)

        self.view_logo = PhotoImage(file='Logos\\View Logo.png')
        Button(self.large_frame, width=30, height=30, image=self.view_logo,
               bg='#A6A6A6', bd=0).place(x=25, y=20)

        # ID AND SEARCH BUTTON
        self.the_ID = IntVar()
        self.theID_entry = Entry(self.large_frame, textvariable=self.the_ID, width=20,
                                 font="arial 15", borderwidth=1, relief='solid')
        self.theID_entry.insert(0, '')
        self.theID_entry.place(x=370, y=70)

        Button(self.large_frame, text="SEARCH", font=('Century Gothic', 10, 'bold'),
               bg='white', fg='black', command=self.to_search).place(x=600, y=70)

        # ENTRY BOXES
        self.kw_hourly_var = StringVar()
        self.kw_daily_var = StringVar()
        self.kw_weekly_var = StringVar()
        self.kw_monthly_var = StringVar()
        self.kw_yearly_var = StringVar()
        self.bill_perc_var = StringVar()

        # IDENTITY LABELS
        self.the_name = StringVar()
        self.brand_var = StringVar()
        self.model_var = StringVar()

        # IMAGE FRAME
        self.img_frame = Frame(self.price_frame, bd=3, bg="black", width=200, height=200, relief=GROOVE)
        self.img_frame.place(x=850, y=250)

        self.user_avatar = PhotoImage(file="Other Images\\noImagelogo.png")
        self.img_frame_label = Label(self.img_frame, bg="black", image=self.user_avatar)
        self.img_frame_label.place(x=0, y=0)

        self.price_frame.pack()

    def create_labels(self):
        """
                Creates and displays labels on the View Page.

                """
        Label(self.large_frame, text="APPLIANCE/DEVICE DETAILS", font=('Century Gothic', 15, 'bold'),
              bg='#A6A6A6', fg='white').place(x=90, y=180)

        Label(self.large_frame, text="kW Hourly:", font=('Century Gothic', 15, 'bold'),
              bg='#A6A6A6', fg='white').place(x=100, y=240)

        Label(self.large_frame, text="kW Daily:", font=('Century Gothic', 15, 'bold'),
              bg='#A6A6A6', fg='white').place(x=100, y=320)

        Label(self.large_frame, text="kW Weekly:", font=('Century Gothic', 15, 'bold'),
              bg='#A6A6A6', fg='white').place(x=100, y=400)

        Label(self.large_frame, text="kW Monthly:", font=('Century Gothic', 15, 'bold'),
              bg='#A6A6A6', fg='white').place(x=360, y=240)

        Label(self.large_frame, text="kW Yearly:", font=('Century Gothic', 15, 'bold'),
              bg='#A6A6A6', fg='white').place(x=360, y=320)

        Label(self.large_frame, text="Bill Percentage:", font=('Century Gothic', 15, 'bold'),
              bg='#A6A6A6', fg='white').place(x=360, y=400)

    def create_entry(self):
        """
                Creates and displays entry boxes on the View Page.

                """

        kw_hourly_entry = Entry(self.large_frame, textvariable=self.kw_hourly_var, width=10,
                                font=('Century Gothic', 15), borderwidth=1, relief='solid', state=DISABLED)
        kw_hourly_entry.place(x=220, y=240)

        kw_daily_entry = Entry(self.large_frame, textvariable=self.kw_daily_var, width=10,
                               font=('Century Gothic', 15), borderwidth=1, relief='solid', state=DISABLED)
        kw_daily_entry.place(x=220, y=320)

        kw_weekly_entry = Entry(self.large_frame, textvariable=self.kw_weekly_var, width=10,
                                font=('Century Gothic', 15), borderwidth=1, relief='solid', state=DISABLED)
        kw_weekly_entry.place(x=220, y=400)

        kw_monthly_entry = Entry(self.large_frame, textvariable=self.kw_monthly_var, width=10,
                                 font=('Century Gothic', 15), borderwidth=1, relief='solid', state=DISABLED)
        kw_monthly_entry.place(x=520, y=240)

        kw_yearly_entry = Entry(self.large_frame, textvariable=self.kw_yearly_var, width=10,
                                font=('Century Gothic', 15), borderwidth=1, relief='solid', state=DISABLED)
        kw_yearly_entry.place(x=520, y=320)

        bill_perc_entry = Entry(self.large_frame, textvariable=self.bill_perc_var, width=10,
                                font=('Century Gothic', 15), borderwidth=1, relief='solid', state=DISABLED)
        bill_perc_entry.place(x=520, y=400)

    def create_identity(self):
        """
                Creates and displays identity labels on the View Page.

                """
        the_name_label = Label(self.large_frame, textvariable=self.the_name, width=20,
                               font=('Century Gothic', 10), borderwidth=1, relief='solid')
        the_name_label.place(x=745, y=390)

        brand_label = Label(self.large_frame, textvariable=self.brand_var, width=20,
                            font=('Century Gothic', 10), borderwidth=1, relief='solid')
        brand_label.place(x=745, y=420)

        model_label = Label(self.large_frame, textvariable=self.model_var, width=20,
                            font=('Century Gothic', 10), borderwidth=1, relief='solid')
        model_label.place(x=745, y=450)

    def to_reset(self):
        """
                Resets the entry fields and image on the View Page.

                """
        global user_avatar

        self.kw_hourly_var.set('')
        self.kw_daily_var.set('')
        self.kw_weekly_var.set('')
        self.kw_monthly_var.set('')
        self.kw_yearly_var.set('')
        self.bill_perc_var.set('')
        self.the_name.set('')
        self.brand_var.set('')
        self.model_var.set('')

        registered_no(self.the_ID)
        # Load a default image or use your placeholder image
        default_image_path = "Other Images\\noImagelogo.png"
        temp_img = ImageTk.PhotoImage(file=default_image_path)
        self.img_frame_label.config(image=temp_img)
        self.img_frame_label.image = temp_img
        self.user_avatar = temp_img

    def to_search(self):
        """
                Searches for an appliance by ID and populates the fields on the View Page.

                """
        text = self.the_ID.get()

        self.to_reset()

        a_file = openpyxl.load_workbook("Saved_Data.xlsx")
        a_sheet = a_file.active

        for row in a_sheet.rows:
            if row[0].value == int(text):
                name = row[0]
                id_no = str(name)[15:-1]

        try:
            print(str(name))
        except:
            messagebox.showerror("Invalid", "Invalid Appliance Number")

        x1 = a_sheet.cell(row=int(id_no), column=1).value
        x3 = a_sheet.cell(row=int(id_no), column=3).value
        x4 = a_sheet.cell(row=int(id_no), column=4).value
        x5 = a_sheet.cell(row=int(id_no), column=5).value
        x9 = a_sheet.cell(row=int(id_no), column=9).value
        x10 = a_sheet.cell(row=int(id_no), column=10).value
        x11 = a_sheet.cell(row=int(id_no), column=11).value
        x12 = a_sheet.cell(row=int(id_no), column=12).value
        x13 = a_sheet.cell(row=int(id_no), column=13).value
        x14 = a_sheet.cell(row=int(id_no), column=14).value

        self.kw_hourly_var.set(x9)
        self.kw_daily_var.set(x10)
        self.kw_weekly_var.set(x11)
        self.kw_monthly_var.set(x12)
        self.kw_yearly_var.set(x13)
        self.bill_perc_var.set(x14)
        self.the_name.set(x3)
        self.brand_var.set(x4)
        self.model_var.set(x5)
        self.the_ID.set(0)
        try:
            user_avatar1 = (Image.open("Registered Images/" + str(x1) + ".jpg"))
            resized_avatar = user_avatar1.resize((190, 190))
            final_avatar = ImageTk.PhotoImage(resized_avatar)
            self.img_frame_label.config(image=final_avatar)
            self.img_frame_label.image = final_avatar
        except FileNotFoundError:
            pass
