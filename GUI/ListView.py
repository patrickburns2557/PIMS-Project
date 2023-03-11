import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk
import GUI.ScrollablePatientList as spl

class ListView(ctk.CTkFrame):
    def __init__(self, parentWidget, patientList):
        super().__init__(parentWidget)
        self.search = ctk.StringVar()

        self.searchText = ctk.CTkLabel(self, text="Name:", font=("Courier", 18, "bold"))
        self.searchText.grid(row=0, column=0, padx=10)

        self.textBox = ctk.CTkEntry(
            self,
            width=40,
            font=("Courier", 18, "bold"),
            textvariable=self.search
        )
        self.textBox.grid(row=0, column=1, sticky="ew", pady=6)

        self.searchButton = ctk.CTkButton(
            self,
            text="Search",
            font=("Courier", 18, "bold"),
            width=100,
            height=35
        )
        self.searchButton.grid(row=0, column=2, sticky="ew", padx=10, pady=6)
        
        self.top = spl.PatientListTopLabel(self)
        self.top.grid(row=1, column=0, columnspan=10, sticky="ew")


        self.scrollable = spl.ScrollablePatientList(self, patientList)
        self.scrollable.grid(row=2, column=0, sticky="news", columnspan=3)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(1, weight=1)