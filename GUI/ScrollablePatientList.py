import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk
import GUI.MainWindow

backColor = "#1f6aa5"
#individual patient list entry to be used in ScrollablePatientList
class SinglePatientListWidget(ctk.CTkFrame):
    numInstances = 0
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget)
        self.patient = patient

        #frame to hold the label
        self.firstNameFrame = ctk.CTkFrame(
            self,
        )
        self.firstNameFrame.grid(row=0,column=0, padx=3, pady=3)
        try:
            self.firstNameButton = ctk.CTkButton(
                self.firstNameFrame,
                text=self.patient.firstName,
                width=200,
                anchor="w",
                command=lambda: GUI.MainWindow.switchDetailedView(self.patient)
            )
            self.firstNameButton.pack(padx=2, pady=2)
        except:#placeholder text if the first name fails to load
            self.firstNameLabel = ctk.CTkLabel(
                self.firstNameFrame,
                text="FIRST NAME",
                width=200,
                font=("Courier", 18, "bold")
            )
            self.firstNameLabel.pack(padx=2, pady=2)
        

        #frame to hold the label
        self.lastNameFrame = ctk.CTkFrame(
            self,
        )
        self.lastNameFrame.grid(row=0,column=1, padx=3, pady=3)
        try:
            self.lastNameLabel = ctk.CTkButton(
                self.lastNameFrame,
                text=self.patient.lastName,
                width=200,
                anchor="w",
                command=lambda: GUI.MainWindow.switchDetailedView(self.patient)
            )
            self.lastNameLabel.pack(padx=2, pady=2)
        except: #placeholder text if the last name fails to load
            self.lastNameLabel = ctk.CTkLabel(
                self.lastNameFrame,
                text="LAST NAME",
                width=200,
                font=("Courier", 18, "bold")
                #anchor="w",
                #justify=tk.LEFT
            )
            self.lastNameLabel.pack(padx=2, pady=2)


        #space in between last name and location
        self.spacer = ctk.CTkFrame(
            self,
            width=300,
            height=10,
            fg_color="transparent"
        )
        self.spacer.grid(row=0,column=2, padx=0, pady=3, sticky="news")

        #frame to hold the label
        self.locationFrame = ctk.CTkFrame(
            self,
        )
        self.locationFrame.grid(row=0,column=3, padx=3, pady=3)
        try:
            self.locationLabel = ctk.CTkLabel(
                self.locationFrame,
                text=(self.patient.location[0] + "\n" + self.patient.location[1] + "\n" + self.patient.location[2] + "\n" + self.patient.location[3]),
                width=150,
                anchor="w",
                justify=ctk.LEFT
            )
            self.locationLabel.pack(padx=2, pady=2)
        except:#placeholder text if the location fails to load
            self.locationLabel = ctk.CTkLabel(
            self.locationFrame,
            text="LOCATION",
            width=150,
            font=("Courier", 18, "bold")
            #anchor="w",
            )
            self.locationLabel.pack(padx=2, pady=2)
        
        #Resize the spacer to fill any extra window size
        self.grid_columnconfigure(2, weight=1)

#reuse the SinglePatientListWidget to be the label at the top of the list
class PatientListTopLabel(SinglePatientListWidget):
    def __init__(self, parentWidget):
        super().__init__(parentWidget, "")
        self.endSpacer = ctk.CTkFrame(self, width=18, height=10, fg_color="transparent")
        self.endSpacer.grid(row=0, column=4)
        self.configure(fg_color=backColor)



#Class to create a scrollable list of patient names given a list of Patient objects
class ScrollablePatientList(ctk.CTkScrollableFrame):
    def __init__(self, parent, patientList):
        super().__init__(parent)
        
        for p in patientList:
            patient = SinglePatientListWidget(self, p)
            patient.pack(fill="both", expand=True, padx=3, pady=3)