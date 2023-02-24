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
            command=lambda:self.switchPersonal(),
            font=("Courier")
        )
        tab2Button = tk.Button(
            self.buttonFrame,
            text="Medical Information",
            command=lambda:self.switchMedical(),
            font=("Courier")
        )
        tab3Button = tk.Button(
            self.buttonFrame,
            text="Billing Information",
            command=lambda:self.switchBilling(),
            font=("Courier")
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
        super().__init__(parentWidget, bg="#E4E4E4")

        self.nameFrame = tk.LabelFrame(
            self,
            text="Name",
            font=("Courier")
        )
        self.nameFrame.grid(row=0, column=0, columnspan=10, sticky="w", padx=15)
        self.name = tk.Label(
            self.nameFrame,
            text=patient.firstName + " " + patient.middleName + " " + patient.lastName,
            font=("Courier", 18, "bold")
        )
        self.name.pack()

        self.addressFrame = tk.LabelFrame(
            self,
            text="Address",
            font=("Courier")
        )
        self.addressFrame.grid(row=1, column=0, sticky="w", padx=15, pady=15)
        self.address = tk.Label(
            self.addressFrame,
            text=patient.address[0] + "\n" + patient.address[1] + ", " + patient.address[2] + "\n" + patient.address[3],
            anchor="w",
            justify=tk.LEFT,
            font=("Courier")
        )
        self.address.pack()

        self.phoneFrame = tk.LabelFrame(
            self,
            text="Phone numbers",
            font=("Courier")
        )
        self.phoneFrame.grid(row=1, column=1, sticky="w", padx=15, pady=15)
        self.phone = tk.Label(
            self.phoneFrame,
            text="Mobile:" + patient.mobilePhone + "\nHome:  " + patient.homePhone + "\nWork:  " + patient.workPhone,
            anchor="w",
            justify=tk.LEFT,
            font=("Courier")
        )
        self.phone.pack()

        self.emergContactFrame = tk.LabelFrame(
            self,
            text="Emergency Contacts",
            font=("Courier")
        )
        self.emergContactFrame.grid(row=2, column=0, sticky="w", padx=15, pady=15)
        for i in range(len(patient.emergencyContactNames)):
            self.contact = tk.Label(
                self.emergContactFrame,
                relief=tk.RAISED,
                borderwidth=1,
                text=str(i+1) + ".)\n  Name:   " + patient.emergencyContactNames[i] + "\n  Number: " + patient.emergencyContactNumbers[i],
                anchor="w",
                justify=tk.LEFT,
                font=("Courier")
            )
            self.contact.grid(row=i, column=0, sticky="w", padx=3, pady=3)

        self.locationFrame = tk.LabelFrame(
            self,
            text="Location",
            font=("Courier")
        )
        self.locationFrame.grid(row=1, column=2, sticky="w", padx=15, pady=15)
        self.location = tk.Label(
            self.locationFrame,
            text="Facility: " + patient.location[0] + "\nFloor:    " + patient.location[1] + "\nRoom:     " + patient.location[2] + "\nBed:      " + patient.location[3],
            anchor="w",
            justify=tk.LEFT,
            font=("Courier")
        )
        self.location.pack()

        self.visitationFrame = tk.LabelFrame(
            self,
            text="Visitation",
            font=("Courier")
        )
        self.visitationFrame.grid(row=2, column=1, sticky="wn", padx=15, pady=15)
        self.numVisitors = tk.Label(
            self.visitationFrame,
            text="Max simultaneous visitors: " + patient.numAllowedVisitors,
            anchor="w",
            justify=tk.LEFT,
            font=("Courier")
        )
        self.numVisitors.grid(row=0, column=0, sticky="w")
        self.allowedVisitors = tk.Label(
            self.visitationFrame,
            text="List of approved visitors:",
            anchor="w",
            justify=tk.LEFT,
            font=("Courier")
        )
        self.allowedVisitors.grid(row=1, column=0, sticky="w")
        for i in range(len(patient.allowedVisitors)):
            self.visitor = tk.Label(
                self.visitationFrame,
                relief=tk.RAISED,
                borderwidth=1,
                text= str(i+1) + ".) " + patient.allowedVisitors[i],
                anchor="w",
                justify=tk.LEFT,
                font=("Courier")
            )
            self.visitor.grid(row=i+2, column=0, padx=3, pady=3, sticky="w")
        

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