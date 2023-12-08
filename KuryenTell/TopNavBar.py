from HomePage import *
from AddPage import *
from ViewPage import *
from EnergyPage import *


class TopNavBar(tk.Frame):
    """
        Top navigation bar for the Kuryentell application.

        Attributes:
            options_frame (tk.Frame): Frame for holding navigation buttons and indicators.
            home_indicator (tk.Label): Indicator for the Home tab.
            add_indicator (tk.Label): Indicator for the Add Appliance tab.
            view_indicator (tk.Label): Indicator for the View Appliance Info tab.
            energy_indicator (tk.Label): Indicator for the Energy Efficiency Tips tab.

        Methods:
            __init__: Initializes the TopNavBar.
            create_tabs: Creates navigation buttons for Home, Add Appliance, View Appliance Info,
                         and Energy Efficiency Tips.
            tab_switching: Switches the tab indicators when a navigation button is clicked.

        """

    def __init__(self, parent):
        """
                Initializes the TopNavBar.

                Configures the frame and sets up indicators for different tabs.

                Args:
                    parent: The parent widget.

                """
        super().__init__(parent)
        self.options_frame = Frame(self, bg='black', height=70)
        self.options_frame.pack(side=TOP, fill=X)
        self.options_frame.pack_propagate(FALSE)
        self.pack(side=TOP, fill=X)

        # TAB INDICATORS
        self.home_indicator = Label(self.options_frame, bg='yellow')
        self.home_indicator.place(x=100, y=50, width=60, height=2)

        self.add_indicator = Label(self.options_frame, bg='black')
        self.add_indicator.place(x=350, y=50, width=140, height=2)

        self.view_indicator = Label(self.options_frame, bg='black')
        self.view_indicator.place(x=705, y=50, width=170, height=2)

        self.energy_indicator = Label(self.options_frame, bg='black')
        self.energy_indicator.place(x=1000, y=50, width=185, height=2)

    def create_tabs(self):
        """
                Creates navigation buttons for Home, Add Appliance, View Appliance Info,
                and Energy Efficiency Tips.

                Binds each button to switch the tab indicators and change the frame accordingly.

                """
        home_btn = tk.Button(self.options_frame, text="Home", font=('Century Gothic', 13, 'bold'),
                             bg='black', fg='white', bd=0,
                             command=lambda: [self.tab_switching(indicator_lbl=self.home_indicator), self.master.change_frame(HomePage)])
        home_btn.place(x=100, y=20)

        add_btn = tk.Button(self.options_frame, text="Add Appliance", font=('Century Gothic', 13, 'bold'),
                            bg='black', fg='white', bd=0,
                            command=lambda: [self.tab_switching(indicator_lbl=self.add_indicator), self.master.change_frame(AddPage)])
        add_btn.place(x=350, y=20)

        view_btn = tk.Button(self.options_frame, text="View Appliance Info", font=('Century Gothic', 13, 'bold'),
                             bg='black', fg='white', bd=0,
                             command=lambda: [self.tab_switching(indicator_lbl=self.view_indicator),
                                              self.master.change_frame(ViewPage)])
        view_btn.place(x=700, y=20)

        energy_btn = tk.Button(self.options_frame, text="Energy Efficiency Tips", font=('Century Gothic', 13, 'bold'),
                               bg='black', fg='white', bd=0,
                               command=lambda: [self.tab_switching(indicator_lbl=self.energy_indicator),
                                                self.master.change_frame(EnergyPage)])
        energy_btn.place(x=1000, y=20)

    def tab_switching(self, indicator_lbl):
        """
                Switches the tab indicators when a navigation button is clicked.

                Args:
                    indicator_lbl: The label representing the tab indicator.

                """
        for child in self.options_frame.winfo_children():
            if isinstance(child, Label):
                child['bg'] = 'black'
        indicator_lbl['bg'] = 'yellow'
