import customtkinter as ctk
from Data.dataClasses import *
import GUI.MainWindow
import Data.System

class LoginView(ctk.CTkFrame):
    def __init__(self, parentWidget, user):
        super().__init__(parentWidget)
        self.username = ctk.StringVar()
        self.password = ctk.StringVar()
        self.user = user
        
        self.usernameLabel = ctk.CTkLabel(self, text="Username:", font=("Courier", 18, "bold"))
        self.usernameLabel.grid(row=0, column=0, padx=10)

        self.usernameEntry = ctk.CTkEntry(
            self,
            width=200,
            font=("Courier", 18, "bold"),
            textvariable=self.username
        )
        self.usernameEntry.grid(row=0, column=1, sticky="ew", pady=6)

        self.passwordLabel = ctk.CTkLabel(self, text="Password:", font=("Courier", 18, "bold"))
        self.passwordLabel.grid(row=1, column=0, padx=10)

        self.passwordEntry = ctk.CTkEntry(
            self,
            width=40,
            font=("Courier", 18, "bold"),
            show="*",
            textvariable=self.password
        )
        self.passwordEntry.grid(row=1, column=1, sticky="ew", pady=6)

        self.personalButton = ctk.CTkButton(
            self,
            text="Login",
            command=lambda:self.processLogin(self.username.get(), self.password.get()),
            font=("Courier", 20),
            width=270,
            height=40,
        )
        self.personalButton.grid(row=2, column=0, padx=5, pady=5)

    def processLogin(self, username, password):
        if loginSystem.login(self.user, username, password):
            GUI.MainWindow.switchPatientList(Data.System.getPatientList())
        else:
            self.incorrectLabel = ctk.CTkLabel(self, text="Incorrect username or password", font=("Courier", 18, "bold"))
            self.incorrectLabel.grid(row=3, columnspan=2, padx=10)





        

        