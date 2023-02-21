import tkinter as tk
import tkinter.ttk as ttk
import GUI.ScrollablePatientList as spl

class ListView(tk.Frame):
    def __init__(self, parentWidget, patientList):
        super().__init__(parentWidget)
        self.search = tk.StringVar()

        self.searchText = tk.Label(self, text="Name: ", font=("Segoe UI", 20))
        self.searchText.grid(row=0, column=0)

        self.textBox = tk.Entry(
            self,
            width=40,
            font=("Segoe UI", 20),
            textvariable=self.search
        )
        self.textBox.grid(row=0, column=1, sticky="ew", pady=6)

        self.searchButton = tk.Button(
            self,
            text="Search",
            font=("Segoe UI", 15)
        )
        self.searchButton.grid(row=0, column=2, sticky="ew", pady=6)
        
        self.scrollable = spl.ScrollablePatientList(self, patientList)
        self.scrollable.grid(row=1, column=0, sticky="news", columnspan=3)