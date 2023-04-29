import customtkinter as ctk
from Data.dataClasses import *
import GUI.MainWindow
import Data.System
from PIL import Image

class LoginView(ctk.CTkFrame):
    def __init__(self, parentWidget, user):
        super().__init__(parentWidget)
        self.username = ctk.StringVar()
        self.password = ctk.StringVar()
        self.user = user
        
        try:
            self.logo = ctk.CTkImage(
                light_image=Image.open("logo.png"),
                size=(300, 300)
            )
            self.logoLabel = ctk.CTkLabel(
                self,
                text="",
                image=self.logo,
                anchor="center",
                justify="center"
            )
            self.logoLabel.grid(row=0, column=0, padx=10, pady=30, columnspan=10, sticky="ew")
        except:
            # Ignore if the image fails to load (usually happens when running on linux)
            pass

        self.usernameLabel = ctk.CTkLabel(self, text="Username:", font=("Courier", 18, "bold"))
        self.usernameLabel.grid(row=1, column=1, padx=10)

        self.usernameEntry = ctk.CTkEntry(
            self,
            width=200,
            font=("Courier", 18, "bold"),
            textvariable=self.username
        )
        self.usernameEntry.grid(row=1, column=2, sticky="ew", pady=6)

        self.passwordLabel = ctk.CTkLabel(self, text="Password:", font=("Courier", 18, "bold"))
        self.passwordLabel.grid(row=2, column=1, padx=10)

        self.passwordEntry = ctk.CTkEntry(
            self,
            width=40,
            font=("Courier", 18, "bold"),
            show="*",
            textvariable=self.password
        )
        self.passwordEntry.grid(row=2, column=2, sticky="ew", pady=6)

        self.personalButton = ctk.CTkButton(
            self,
            text="Login",
            command=lambda:self.processLogin(),
            font=("Courier", 20),
            width=270,
            height=40,
        )
        self.personalButton.grid(row=3, column=1, padx=5, pady=5, columnspan=2)

        self.usernameEntry.bind('<Return>', self.processLogin)
        self.passwordEntry.bind('<Return>', self.processLogin)

        self.leftSpacer = ctk.CTkFrame(self, fg_color="transparent")
        self.rightSpacer = ctk.CTkFrame(self, fg_color="transparent")
        self.leftSpacer.grid(row=0, column=0, rowspan=10)
        self.rightSpacer.grid(row=0, column=3, rowspan=10)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.master.after(100, lambda:self.usernameEntry.focus_set())

    def processLogin(self, event=None):
        username = self.username.get()
        password = self.password.get()
        if loginSystem.login(self.user, username, password):
            Data.System.loadDatabase()
            GUI.MainWindow.switchPatientList(Data.System.getPatientList())
            GUI.MainWindow.updateTopBar() #update user type in TopBar
        else:
            self.incorrectLabel = ctk.CTkLabel(self, text="Incorrect username or password", font=("Courier", 18, "bold"))
            self.incorrectLabel.grid(row=4, column=1, padx=5, pady=5, columnspan=2)