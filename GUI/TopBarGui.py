import customtkinter as ctk
import Data.System
import Data.Printer
import GUI.MainWindow
TOPBARFONT = ("Arial", 20)
class TopBar(ctk.CTkFrame):
    def __init__(self, parentWidget):
        super().__init__(parentWidget)
        
        #Show the user type that's currently logged in
        self.userType = "Not Logged In"
        if Data.System.getUserType() == 0:
            self.userType = "Doctor"
        elif Data.System.getUserType() == 1:
            self.userType = "Nurse"
        elif Data.System.getUserType() == 2:
            self.userType = "Office Staff"
        elif Data.System.getUserType() == 3:
            self.userType = "Volunteer"
        
        self.userTypeLabel = ctk.CTkLabel(
            self,
            text="Logged in as: " + str(self.userType),
            anchor = "w",
            justify=ctk.LEFT,
            font=TOPBARFONT
        )
        self.userTypeLabel.grid(row=0, column=0, padx=3, pady=3, sticky="news")

        
        self.spacer = ctk.CTkFrame(
            self,
            width=300,
            height=10,
            fg_color="transparent"
        )
        self.spacer.grid(row=0,column=1, padx=3, pady=3, sticky="news")
        
        #Create a switch and accompanying function to change between light and dark mode
        self.switchAppearanceVar = ctk.StringVar(value="off")
        def switchAppearance():
            if self.switchAppearanceVar.get() == "on":
                ctk.set_appearance_mode("dark")
            else:
                ctk.set_appearance_mode("light")
        self.switch = ctk.CTkSwitch(
            self,
            text="Dark Mode",
            command=switchAppearance,
            variable=self.switchAppearanceVar,
            onvalue="on",
            offvalue="off",
            font=TOPBARFONT
        )
        self.switch.grid(row=0, column=2, padx=3, pady=3, sticky="news")

        #Create a switch and accompanying function to change between normal and large scaling
        self.switchScaleVar = ctk.StringVar(value="off")
        def switchScaling():
            if self.switchScaleVar.get() == "on":
                ctk.set_widget_scaling(1.2)
            else:
                ctk.set_widget_scaling(1.0)
        self.switchScale = ctk.CTkSwitch(
            self,
            text="Increase Scaling",
            command=switchScaling,
            variable=self.switchScaleVar,
            onvalue="on",
            offvalue="off",
            font=TOPBARFONT
        )
        self.switchScale.grid(row=0,column=3, padx=3, pady=3, sticky="news")

        #Only show the print button when logged in
        if Data.System.getUserType() in range(0,5):
            self.printButton = ctk.CTkButton(
                self,
                text="Print",
                font=TOPBARFONT,
                command=lambda:Data.Printer.initPrint(0)
            )
            self.printButton.grid(row=0, column=4, padx=3, pady=3, sticky="news")


        self.logoutButton = ctk.CTkButton(
            self,
            text="Logout",
            font=TOPBARFONT,
            command=lambda:[Data.System.logoutUser(), GUI.MainWindow.switchLoginView(Data.System.getUser())]
        )
        self.logoutButton.grid(row=0,column=5, padx=3, pady=3, sticky="news")






        self.grid_columnconfigure(1, weight=1)