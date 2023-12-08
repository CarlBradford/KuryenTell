from TopNavBar import *
from AddPage import *
from HomePage import *
from ExcelData import *


class Main(tk.Tk):
    """
        The main application class for Kuryentell.

        Attributes:
            navBar (TopNavBar): The top navigation bar instance.
            addPage (AddPage): The add page instance.
            energyPage (EnergyPage): The energy page instance.
            pricePage (ViewPage): The view page instance.
            current_frame (tk.Frame): The currently displayed frame.

        Methods:
            __init__: Initializes the main application.
            change_frame: Changes the currently displayed frame.

        """
    def __init__(self):
        """
                Initializes the main application.

                Configures the main window, creates navigation bar, add page, energy page,
                view page, and home page instances. Calls necessary methods to set up the
                initial state of the application.

                """
        # MAIN WINDOW CONFIG
        super().__init__()
        self.title('Kuryentell')
        self.geometry("1250x700+70+100")
        self.config(bg='black')
        self.resizable(FALSE, FALSE)

        # Navigation Bar
        self.navBar = TopNavBar(self)
        self.navBar.create_tabs()

        # ADD PAGE
        self.addPage = AddPage(self)
        self.addPage.create_date()
        self.addPage.create_labels()
        self.addPage.create_buttons()
        self.addPage.create_entry()

        # ENERGY PAGE
        self.energyPage = EnergyPage(self)

        # PRICE PAGE
        self.pricePage = ViewPage(self)
        self.pricePage.create_labels()
        self.pricePage.create_entry()
        self.pricePage.create_identity()

        # FUNCTIONS
        registered_no(self.addPage.registered_num)

        # HOME PAGE
        self.current_frame = tk.Frame(self)
        self.homePage = HomePage(self)
        self.change_frame(HomePage)

        # MAINLOOP
        self.mainloop()

    def change_frame(self, frame_class):
        """
                Changes the currently displayed frame.

                Args:
                    frame_class (class): The class of the frame to be displayed.

                """
        if hasattr(self, 'current_frame'):
            self.current_frame.pack_forget()

        if frame_class == HomePage:
            self.current_frame = self.homePage
        elif frame_class == AddPage:
            self.current_frame = self.addPage
        elif frame_class == EnergyPage:
            self.current_frame = self.energyPage
        elif frame_class == ViewPage:
            self.current_frame = self.pricePage

        self.current_frame.pack(expand=True, fill=tk.BOTH)


if __name__ == "__main__":
    app = Main()
