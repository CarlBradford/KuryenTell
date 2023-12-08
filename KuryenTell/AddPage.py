import tkinter as tk
import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from datetime import date
from ExcelData import *


class AddPage(tk.Frame):
    """
        The Add Page of the Kuryentell application.

        Attributes:
            add_frame (tk.Frame): The main frame for the Add Page.
            image_path_var (StringVar): Variable to store the path of the selected image.
            large_frame (tk.Frame): The large center frame within the Add Page.
            ...

        Methods:
            __init__: Initializes the Add Page.
            create_date: Creates and displays the date entry on the Add Page.
            create_labels: Creates and displays labels on the Add Page.
            create_buttons: Creates and displays buttons on the Add Page.
            create_entry: Creates and displays entry boxes on the Add Page.
            to_upload: Opens a file dialog to upload an image and displays it on the Add Page.
            to_reset: Resets the entry fields and image on the Add Page.
            meralco: Computes various energy-related values on the Add Page.
            to_save: Saves the entered data to an Excel file and displays a success message.
            to_search: Searches for an appliance by ID and populates the fields on the Add Page.
            to_update: Updates the information of an existing appliance in the Excel file.

        """
    def __init__(self, parent):
        """
                Initializes the Add Page.

                Creates the main frame, large center frame, and initializes variables.

                Args:
                    parent: The parent widget.

                """
        super().__init__(parent)
        # MAIN FRAME AND BACKGROUND
        self.add_frame = Frame(self, bg='black', height=630, width=1250, bd=0)
        self.image_path_var = StringVar(value='')

        # LARGE CENTER FRAME
        self.large_frame = Frame(self.add_frame, bg='#A6A6A6', height=490, width=1000)
        self.large_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.black_line = Label(self.large_frame, bg='black')
        self.black_line.place(x=0, y=140, height=10, width=1000)

        self.top_label = Label(self.large_frame, text="\tAdd Appliance", font=('Century Gothic', 25, 'bold'),
                               bg='#A6A6A6', fg='yellow', height=3, width=83, anchor='w')
        self.top_label.place(x=-70, y=-20)

        self.add_logo = PhotoImage(file='Logos\\Add Logo.png')
        Button(self.large_frame, width=30, height=30, image=self.add_logo,
               bg='#A6A6A6', bd=0).place(x=20, y=25)

        # ID AND SEARCH
        self.the_ID = IntVar()
        self.theID_entry = Entry(self.large_frame, textvariable=self.the_ID, width=20, font=('Century Gothic', 15),
                                 borderwidth=1, relief='solid')
        self.theID_entry.place(x=370, y=30)

        Button(self.large_frame, text="SEARCH", font=('Century Gothic', 10, 'bold'),
               bg='white', fg='black', command=self.to_search).place(x=600, y=30)

        # APPLIANCE/DEVICE ID
        self.apd_label = Label(self.large_frame, text="Appliance/ Device No:", font=('Century Gothic', 15, 'bold'),
                               bg='#A6A6A6', fg='white')
        self.apd_label.place(x=50, y=90)

        global registered_num
        self.registered_num = IntVar()
        self.apd_box = Label(self.large_frame, textvariable=self.registered_num, font=('Century Gothic', 13),
                             bg='white', borderwidth=1, relief='solid')
        self.apd_box.place(x=280, y=90, height=30, width=100)

        # IMAGE FRAME
        self.img_frame = Frame(self.large_frame, bd=3, bg="black", width=200, height=200, relief=GROOVE)
        self.img_frame.place(x=750, y=180)

        self.user_avatar = PhotoImage(file="Other Images\\noImagelogo.png")
        self.img_frame_label = Label(self.img_frame, bg="black", image=self.user_avatar)
        self.img_frame_label.place(x=0, y=0)

        # VARIABLES FOR COMPUTATION
        self.kw_hourly_var = StringVar()
        self.kw_daily_var = StringVar()
        self.kw_weekly_var = StringVar()
        self.kw_monthly_var = StringVar()
        self.kw_yearly_var = StringVar()
        self.bill_perc_var = StringVar()

        # ENTRY BOXES
        self.the_name = StringVar()
        self.brand_var = StringVar()
        self.model_var = StringVar()
        self.wattage_var = DoubleVar()
        self.hrs_used_var = DoubleVar()
        self.total_bill_var = DoubleVar()

        # SAVE BUTTON
        self.save_button = Button(self.large_frame, text="SAVE", bg='yellow',
                                  font=('Century Gothic', 12, 'bold'), command=self.to_save)
        self.save_button.place(x=600, y=200, height=40, width=100)

        self.add_frame.pack()

    def create_date(self):
        """
               Creates and displays the date entry on the Add Page.

               """
        global the_date
        date_label = Label(self.large_frame, text="Date Today:", font=('Century Gothic', 15, 'bold'),
                           bg='#A6A6A6', fg='white')
        date_label.place(x=430, y=90)
        the_date = StringVar()
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        date_label = Label(self.large_frame, textvariable=the_date, font=('Century Gothic', 13),
                           bg="white", borderwidth=1, relief='solid')
        date_label.place(x=550, y=90, height=30, width=120)
        the_date.set(d1)

    def create_labels(self):
        """
                Creates and displays labels on the Add Page.

                """
        Label(self.large_frame, text="APPLIANCE/ DEVICE DETAILS", font=('Century Gothic', 20, 'bold'),
              bg='#A6A6A6', fg='white').place(x=30, y=170)

        Label(self.large_frame, text="NAME:", font=('Century Gothic', 15, 'bold'),
              bg='#A6A6A6', fg='white').place(x=30, y=220)
        Label(self.large_frame, text="BRAND:", font=('Century Gothic', 15, 'bold'),
              bg='#A6A6A6', fg='white').place(x=30, y=320)
        Label(self.large_frame, text="MODEL:", font=('Century Gothic', 15, 'bold'),
              bg='#A6A6A6', fg='white').place(x=30, y=420)

        Label(self.large_frame, text="WATTAGE:", font=('Century Gothic', 15, 'bold'),
              bg='#A6A6A6', fg='white').place(x=310, y=220)
        Label(self.large_frame, text="HOURS USED:", font=('Century Gothic', 15, 'bold'),
              bg='#A6A6A6', fg='white').place(x=280, y=320)
        Label(self.large_frame, text="(IN A DAY)", font=('Century Gothic', 15, 'bold'),
              bg='#A6A6A6', fg='white').place(x=280, y=345)
        Label(self.large_frame, text="TOTAL BILL:", font=('Century Gothic', 15, 'bold'),
              bg='#A6A6A6', fg='white').place(x=300, y=420)

    def create_buttons(self):
        """
                Creates and displays buttons on the Add Page.

                """
        reset_button = Button(self.large_frame, text="RESET", bg='yellow',
                              font=('Century Gothic', 12, 'bold'), command=self.to_reset)
        reset_button.place(x=600, y=290, height=40, width=100)

        update_button = Button(self.large_frame, text="UPDATE", bg='yellow',
                               font=('Century Gothic', 12, 'bold'), command=self.to_update)
        update_button.place(x=600, y=370, height=40, width=100)

        upload_button = Button(self.large_frame, text="UPLOAD", bg='yellow',
                               font=('Century Gothic', 12, 'bold'), command=self.to_upload)
        upload_button.place(x=800, y=400, height=40, width=100)

    def create_entry(self):
        """
                Creates and displays entry boxes on the Add Page.

                """
        the_name_entry = Entry(self.large_frame, textvariable=self.the_name,
                               font=('Century Gothic', 10), borderwidth=1, relief='solid')
        the_name_entry.insert(0, "Electric Fan")
        the_name_entry.place(x=120, y=220, height=30, width=140)

        brand_entry = Entry(self.large_frame, textvariable=self.brand_var,
                            font=('Century Gothic', 10), borderwidth=1, relief='solid')
        brand_entry.insert(0, "Hanabishi")
        brand_entry.place(x=120, y=320, height=30, width=140)

        model_entry = Entry(self.large_frame, textvariable=self.model_var,
                            font=('Century Gothic', 10), borderwidth=1, relief='solid')
        model_entry.place(x=120, y=420, height=30, width=140)

        wattage_entry = Entry(self.large_frame, textvariable=self.wattage_var,
                              font=('Century Gothic', 10), borderwidth=1, relief='solid')
        wattage_entry.place(x=420, y=220, height=30, width=140)

        hrs_used_entry = Entry(self.large_frame, textvariable=self.hrs_used_var,
                               font=('Century Gothic', 10), borderwidth=1, relief='solid')
        hrs_used_entry.place(x=420, y=320, height=30, width=140)

        total_entry = Entry(self.large_frame, textvariable=self.total_bill_var,
                            font=('Century Gothic', 10), borderwidth=1, relief='solid')
        total_entry.place(x=420, y=420, height=30, width=140)

    def to_upload(self):
        """
                Opens a file dialog to upload an image and displays it on the Add Page.

                """
        global image_path_var
        global user_avatar

        picture_name = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select image file",
            filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All Files", "*.txt"))
        )

        self.image_path_var.set(picture_name)  # Update the image file path
        user_avatar = Image.open(picture_name)
        resized_avatar = user_avatar.resize((190, 190))
        final_avatar = ImageTk.PhotoImage(resized_avatar)
        self.img_frame_label.config(image=final_avatar)
        self.img_frame_label.image = final_avatar

    def to_reset(self):
        """
               Resets the entry fields and image on the Add Page.

               """
        global user_avatar

        self.the_name.set('')
        self.brand_var.set('')
        self.model_var.set('')
        self.wattage_var.set(0.0)
        self.hrs_used_var.set(0)
        self.total_bill_var.set(0.0)

        registered_no(self.registered_num)
        # Load a default image or use your placeholder image
        default_image_path = "Other Images\\noImagelogo.png"
        temp_img = ImageTk.PhotoImage(file=default_image_path)
        self.img_frame_label.config(image=temp_img)
        self.img_frame_label.image = temp_img
        self.user_avatar = temp_img

        self.save_button.config(state='normal')

    def meralco(self):
        """
                Computes various energy-related values on the Add Page.

                """
        kwh = (float(self.wattage_var.get()) * float(self.hrs_used_var.get())) / 1000
        day_kwh = kwh * 12.0545
        hr_kwh = day_kwh / float(self.hrs_used_var.get())
        week_kwh = day_kwh * 7
        month_kwh = day_kwh * 30
        year_kwh = day_kwh * 365
        bill_perc = (float(month_kwh) / float(self.total_bill_var.get())) * 100

        self.kw_hourly_var.set('₱' + str(round(hr_kwh, 2)))
        self.kw_daily_var.set('₱' + str(round(day_kwh, 2)))
        self.kw_weekly_var.set('₱' + str(round(week_kwh, 2)))
        self.kw_monthly_var.set('₱' + str(round(month_kwh, 2)))
        self.kw_yearly_var.set('₱' + str(round(year_kwh, 2)))
        self.bill_perc_var.set(str(round(bill_perc, 2)) + '%')

    def to_save(self):
        """
                Saves the entered data to an Excel file and displays a success message.

                """
        reg1 = self.registered_num.get()
        date1 = the_date.get()
        name1 = self.the_name.get()
        brand1 = self.brand_var.get()
        model1 = self.model_var.get()
        wattage1 = self.wattage_var.get()
        hrs_used1 = self.hrs_used_var.get()
        tot_bill1 = self.total_bill_var.get()

        self.meralco()

        kw_h1 = self.kw_hourly_var.get()
        kw_d1 = self.kw_daily_var.get()
        kw_w1 = self.kw_weekly_var.get()
        kw_m1 = self.kw_monthly_var.get()
        kw_y1 = self.kw_yearly_var.get()
        bill_perc1 = self.bill_perc_var.get()

        if (reg1 == "" or date1 == "Select" or name1 == "" or brand1 == "" or model1 == ""
                or wattage1 == "" or hrs_used1 == "" or tot_bill1 == "" or kw_h1 == "" or kw_d1 == "" or kw_w1 == "" or
                kw_m1 == "" or kw_y1 == "" or bill_perc1 == ""):
            messagebox.showerror("Error", "Few data is missing")
            return

        else:
            a_file = openpyxl.load_workbook('Saved_Data.xlsx')
            a_sheet = a_file.active
            a_sheet.cell(column=1, row=a_sheet.max_row + 1, value=reg1)
            a_sheet.cell(column=2, row=a_sheet.max_row, value=date1)
            a_sheet.cell(column=3, row=a_sheet.max_row, value=name1)
            a_sheet.cell(column=4, row=a_sheet.max_row, value=brand1)
            a_sheet.cell(column=5, row=a_sheet.max_row, value=model1)
            a_sheet.cell(column=6, row=a_sheet.max_row, value=wattage1)
            a_sheet.cell(column=7, row=a_sheet.max_row, value=hrs_used1)
            a_sheet.cell(column=8, row=a_sheet.max_row, value=tot_bill1)
            a_sheet.cell(column=9, row=a_sheet.max_row, value=kw_h1)
            a_sheet.cell(column=10, row=a_sheet.max_row, value=kw_d1)
            a_sheet.cell(column=11, row=a_sheet.max_row, value=kw_w1)
            a_sheet.cell(column=12, row=a_sheet.max_row, value=kw_m1)
            a_sheet.cell(column=13, row=a_sheet.max_row, value=kw_y1)
            a_sheet.cell(column=14, row=a_sheet.max_row, value=bill_perc1)
            a_file.save('Saved_data.xlsx')

        try:
            if not os.path.exists("Registered Images"):
                os.makedirs("Registered Images")

            user_avatar.save("Registered Images/" + str(reg1) + ".jpg")
        except:
            messagebox.showinfo("Info", "Profile Picture is empty")

        messagebox.showinfo("Info", "Registration Successful")

        self.to_reset()
        registered_no(self.registered_num)

    def to_search(self):
        """
                Searches for an appliance by ID and populates the fields on the Add Page.

                """
        text = self.the_ID.get()

        self.to_reset()
        self.save_button.config(state='disabled')

        a_file = openpyxl.load_workbook("Saved_Data.xlsx")
        a_sheet = a_file.active
        name = None
        id_no = None
        id_found = False

        for row in a_sheet.rows:
            if row[0].value == int(text):
                name = row[0]
                id_no = str(name)[15:-1]
                id_found = True
                break  # Exit the loop if the ID is found

        if not id_found:
            messagebox.showerror("Invalid", "Invalid Appliance Number")
        else:
            try:
                print(str(name))
                # Rest of your code for setting variables and displaying image
            except Exception as e:
                print(f"Error: {e}")

        x1 = a_sheet.cell(row=int(id_no), column=1).value
        x2 = a_sheet.cell(row=int(id_no), column=2).value
        x3 = a_sheet.cell(row=int(id_no), column=3).value
        x4 = a_sheet.cell(row=int(id_no), column=4).value
        x5 = a_sheet.cell(row=int(id_no), column=5).value
        x6 = a_sheet.cell(row=int(id_no), column=6).value
        x7 = a_sheet.cell(row=int(id_no), column=7).value
        x8 = a_sheet.cell(row=int(id_no), column=8).value

        self.the_ID.set(x1)
        the_date.set(x2)
        self.the_name.set(x3)
        self.brand_var.set(x4)
        self.model_var.set(x5)
        self.wattage_var.set(x6)
        self.hrs_used_var.set(x7)
        self.total_bill_var.set(x8)

        try:
            user_avatar1 = (Image.open("Registered Images/" + str(x1) + ".jpg"))
            resized_avatar = user_avatar1.resize((190, 190))
            final_avatar = ImageTk.PhotoImage(resized_avatar)
            self.img_frame_label.config(image=final_avatar)
            self.img_frame_label.image = final_avatar
        except FileNotFoundError:
            pass

    def to_update(self):
        """
                Updates the information of an existing appliance in the Excel file.

                """
        reg1 = self.the_ID.get()
        date1 = the_date.get()
        name1 = self.the_name.get()
        brand1 = self.brand_var.get()
        model1 = self.model_var.get()
        wattage1 = self.wattage_var.get()
        hrs_used1 = self.hrs_used_var.get()
        tot_bill1 = self.total_bill_var.get()
        self.meralco()
        kw_h1 = self.kw_hourly_var.get()
        kw_d1 = self.kw_daily_var.get()
        kw_w1 = self.kw_weekly_var.get()
        kw_m1 = self.kw_monthly_var.get()
        kw_y1 = self.kw_yearly_var.get()
        bill_perc1 = self.bill_perc_var.get()

        a_file = openpyxl.load_workbook('Saved_Data.xlsx')
        a_sheet = a_file.active
        for row in a_sheet.rows:
            if row[0].value == reg1:
                name = row[0]
                id_number = str(name)[15:-1]

        a_sheet.cell(column=1, row=int(id_number), value=reg1)
        a_sheet.cell(column=2, row=int(id_number), value=date1)
        a_sheet.cell(column=3, row=int(id_number), value=name1)
        a_sheet.cell(column=4, row=int(id_number), value=brand1)
        a_sheet.cell(column=5, row=int(id_number), value=model1)
        a_sheet.cell(column=6, row=int(id_number), value=wattage1)
        a_sheet.cell(column=7, row=int(id_number), value=hrs_used1)
        a_sheet.cell(column=8, row=int(id_number), value=tot_bill1)
        a_sheet.cell(column=9, row=int(id_number), value=kw_h1)
        a_sheet.cell(column=10, row=int(id_number), value=kw_d1)
        a_sheet.cell(column=11, row=int(id_number), value=kw_w1)
        a_sheet.cell(column=12, row=int(id_number), value=kw_m1)
        a_sheet.cell(column=13, row=int(id_number), value=kw_y1)
        a_sheet.cell(column=14, row=int(id_number), value=bill_perc1)

        a_file.save('Saved_data.xlsx')

        try:
            user_avatar.save('Registered Images/' + str(reg1) + ".jpg")
        except:
            pass

        messagebox.showinfo("Update", "Update Successful")

        self.to_reset()
