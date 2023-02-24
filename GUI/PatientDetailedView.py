import tkinter as tk
import tkinter.ttk as ttk
from Data.dataClasses import *


#Class for showing all the information for a selected patient
class PatientDetailedView(tk.Frame):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget)
        self.patient = patient
        #first tab shown will be the personal info tab
        self.shownTab = PersonalInfoTab(self, patient)
        

        #Create frame and buttons for switching tabs
        #Will need to setup later to only show relavant tabs based on
        # which user is logged in.
        self.buttonFrame = tk.LabelFrame(self, relief=tk.RAISED, borderwidth=2)
        tab1Button = tk.Button(
            self.buttonFrame,
            text="Personal Information",
            command=lambda:self.switchPersonal()
        )
        tab2Button = tk.Button(
            self.buttonFrame,
            text="Medical Information",
            command=lambda:self.switchMedical()
        )
        tab3Button = tk.Button(
            self.buttonFrame,
            text="Billing Information",
            command=lambda:self.switchBilling()
        )
        tab1Button.grid(row=0, column=0, padx=3, pady=3)
        tab2Button.grid(row=0, column=1, padx=3, pady=3)
        tab3Button.grid(row=0, column=2, padx=3, pady=3)

        

        self.buttonFrame.grid(row=0, column=0, sticky="news")
        self.shownTab.grid(row=1, column=0, sticky="news")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)



        
    


    #Functions to switch between the tabs using the buttons
    def switchPersonal(self):
        #prob need to iterate through children and destroy too
        self.shownTab.destroy()
        self.shownTab = PersonalInfoTab(self, self.patient)
        self.shownTab.grid(row=1, column=0, sticky="news")
        #self.shownTab.pack()

    def switchMedical(self):
        #prob need to iterate through children and destroy too
        self.shownTab.destroy()
        self.shownTab = MedicalInfoTab(self, self.patient)
        self.shownTab.grid(row=1, column=0, sticky="news")
        #self.shownTab.pack()

    def switchBilling(self):
        #prob need to iterate through children and destroy too
        self.shownTab.destroy()
        self.shownTab = BillingInfoTab(self, self.patient)
        self.shownTab.grid(row=1, column=0, sticky="news")
        #self.shownTab.pack()








#############################################
# Tabs
#############################################


class PersonalInfoTab(tk.Frame):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget, bg="orange")



        self.testLabel = tk.Label(
            self,
            text="I am the Personal Information Tab",
            font=("Segoe UI", 25)
        )

        self.testLabel.pack()

class MedicalInfoTab(tk.Frame):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget, bg="green")



        self.testLabel = tk.Label(
            self,
            text="I am the Medical Information Tab",
            font=("Segoe UI", 25)
        )

        self.testLabel.pack()

class BillingInfoTab(tk.Frame):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget, bg="blue")

        self.testLabel = tk.Label(
            self,
            text="I am the Billing Information Tab",
            font=("Segoe UI", 25)
        )

        self.testLabel.pack()