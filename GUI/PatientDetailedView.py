import tkinter as tk
import tkinter.ttk as ttk
from Data.dataClasses import *

BGCOLOR = "#E4E4E4"
BUTTONSELECTED = "#D9D9D9"
BUTTONUNSELECTED = "#F0F0F0"
FONTNAME = ("Courier", 18, "bold")
FONTINFO = ("Courier")

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
        self.personalButton = tk.Button(
            self.buttonFrame,
            text="Personal Information",
            command=lambda:self.switchPersonal(),
            font=FONTINFO,
            bg=BUTTONSELECTED
        )
        self.medicalButton = tk.Button(
            self.buttonFrame,
            text="Medical Information",
            command=lambda:self.switchMedical(),
            font=FONTINFO
        )
        self.billingButton = tk.Button(
            self.buttonFrame,
            text="Billing Information",
            command=lambda:self.switchBilling(),
            font=FONTINFO
        )
        self.personalButton.grid(row=0, column=0, padx=3, pady=3)
        self.medicalButton.grid(row=0, column=1, padx=3, pady=3)
        self.billingButton.grid(row=0, column=2, padx=3, pady=3)

        

        self.buttonFrame.grid(row=0, column=0, sticky="news")
        self.shownTab.grid(row=1, column=0, sticky="news")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)



        
    


    #Functions to switch between the tabs using the buttons
    def switchPersonal(self):
        self.personalButton.configure(bg=BUTTONSELECTED)
        self.medicalButton.configure(bg=BUTTONUNSELECTED)
        self.billingButton.configure(bg=BUTTONUNSELECTED)

        for i in self.shownTab.winfo_children():
            i.destroy()
        self.shownTab.destroy()
        self.shownTab = PersonalInfoTab(self, self.patient)
        self.shownTab.grid(row=1, column=0, sticky="news")
        #self.shownTab.pack()

    def switchMedical(self):
        self.personalButton.configure(bg=BUTTONUNSELECTED)
        self.medicalButton.configure(bg=BUTTONSELECTED)
        self.billingButton.configure(bg=BUTTONUNSELECTED)

        #prob need to iterate through children and destroy too
        self.shownTab.destroy()
        self.shownTab = MedicalInfoTab(self, self.patient)
        self.shownTab.grid(row=1, column=0, sticky="news")
        #self.shownTab.pack()

    def switchBilling(self):
        self.personalButton.configure(bg=BUTTONUNSELECTED)
        self.medicalButton.configure(bg=BUTTONUNSELECTED)
        self.billingButton.configure(bg=BUTTONSELECTED)

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
        super().__init__(parentWidget, bg=BGCOLOR)

        self.nameFrame = tk.LabelFrame(
            self,
            text="Name",
            font=FONTINFO
        )
        self.nameFrame.grid(row=0, column=0, columnspan=10, sticky="w", padx=15)
        self.name = tk.Label(
            self.nameFrame,
            text=patient.firstName + " " + patient.middleName + " " + patient.lastName,
            font=FONTNAME
        )
        self.name.pack()

        self.addressFrame = tk.LabelFrame(
            self,
            text="Address",
            font=FONTINFO
        )
        self.addressFrame.grid(row=1, column=0, sticky="w", padx=15, pady=15)
        self.address = tk.Label(
            self.addressFrame,
            text=patient.address[0] + "\n" + patient.address[1] + ", " + patient.address[2] + "\n" + patient.address[3],
            anchor="w",
            justify=tk.LEFT,
            font=FONTINFO
        )
        self.address.pack()

        self.phoneFrame = tk.LabelFrame(
            self,
            text="Phone numbers",
            font=FONTINFO
        )
        self.phoneFrame.grid(row=1, column=1, sticky="w", padx=15, pady=15)
        self.phone = tk.Label(
            self.phoneFrame,
            text="Mobile:" + patient.mobilePhone + "\nHome:  " + patient.homePhone + "\nWork:  " + patient.workPhone,
            anchor="w",
            justify=tk.LEFT,
            font=FONTINFO
        )
        self.phone.pack()

        self.emergContactFrame = tk.LabelFrame(
            self,
            text="Emergency Contacts",
            font=FONTINFO
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
                font=FONTINFO
            )
            self.contact.grid(row=i, column=0, sticky="w", padx=3, pady=3)

        self.locationFrame = tk.LabelFrame(
            self,
            text="Location",
            font=FONTINFO
        )
        self.locationFrame.grid(row=1, column=2, sticky="w", padx=15, pady=15)
        self.location = tk.Label(
            self.locationFrame,
            text="Facility: " + patient.location[0] + "\nFloor:    " + patient.location[1] + "\nRoom:     " + patient.location[2] + "\nBed:      " + patient.location[3],
            anchor="w",
            justify=tk.LEFT,
            font=FONTINFO
        )
        self.location.pack()

        self.visitationFrame = tk.LabelFrame(
            self,
            text="Visitation",
            font=FONTINFO
        )
        self.visitationFrame.grid(row=2, column=1, sticky="wn", padx=15, pady=15)
        self.numVisitors = tk.Label(
            self.visitationFrame,
            text="Max simultaneous visitors: " + patient.numAllowedVisitors,
            anchor="w",
            justify=tk.LEFT,
            font=FONTINFO
        )
        self.numVisitors.grid(row=0, column=0, sticky="w")
        self.allowedVisitors = tk.Label(
            self.visitationFrame,
            text="List of approved visitors:",
            anchor="w",
            justify=tk.LEFT,
            font=FONTINFO
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
                font=FONTINFO
            )
            self.visitor.grid(row=i+2, column=0, padx=3, pady=3, sticky="w")
        

class MedicalInfoTab(tk.Frame):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget, bg=BGCOLOR)

        self.nameFrame = tk.LabelFrame(
            self,
            text="Name",
            font=FONTINFO
        )
        self.nameFrame.grid(row=0, column=0, columnspan=10, sticky="w", padx=15)
        self.name = tk.Label(
            self.nameFrame,
            text=patient.firstName + " " + patient.middleName + " " + patient.lastName,
            font=FONTNAME
        )
        self.name.pack()

        self.famDoctorFrame = tk.LabelFrame(
            self,
            text="Family Doctor",
            font=FONTINFO
        )
        self.famDoctorFrame.grid(row=1, column=0, sticky="w", padx=15, pady=15)
        self.famDoctor = tk.Label(
            self.famDoctorFrame,
            text=patient.familyDoctor,
            anchor="w",
            justify=tk.LEFT,
            font=FONTINFO
        )
        self.famDoctor.pack()

        self.admittanceFrame = tk.LabelFrame(
            self,
            text="Admittance",
            font=FONTINFO
        )
        self.admittanceFrame.grid(row=2, column=0, sticky="w", padx=15, pady=15)
        self.admittance = tk.Label(
            self.admittanceFrame,
            text="Date:   " + patient.dateAdmittance + "\nTime:   " + patient.timeAdmittance + "\nReason: " + patient.reasonAdmission,
            anchor="w",
            justify=tk.LEFT,
            font=FONTINFO
        )
        self.admittance.pack()

        self.dischargeFrame = tk.LabelFrame(
            self,
            text="Discharge",
            font=FONTINFO
        )
        self.dischargeFrame.grid(row=3, column=0, sticky="w", padx=15, pady=15)
        self.discharge = tk.Label(
            self.dischargeFrame,
            text="Date: " + patient.dateDischarge + "\nTime: " + patient.timeDischarge,
            anchor="w",
            justify=tk.LEFT,
            font=FONTINFO
        )
        self.discharge.pack()

        self.prescriptionFrame = tk.LabelFrame(
            self,
            text="Prescriptions",
            font=FONTINFO
        )
        self.prescriptionFrame.grid(row=4, column=0, sticky="w", padx=15, pady=15)
        for i in range(len(patient.prescriptionNames)):
            self.prescription = tk.Label(
                self.prescriptionFrame,
                relief=tk.RAISED,
                border=1,
                text=str(i+1) + ".)\n  Name:     " + patient.prescriptionNames[i] + "\n  Amount:   " + patient.prescriptionAmount[i] + "\n  Schedule: " + patient.prescriptionSchedule[i],
                anchor="w",
                justify=tk.LEFT,
                font=FONTINFO
            )
            self.prescription.grid(row=i, column=0, sticky="w", padx=3, pady=3)


class BillingInfoTab(tk.Frame):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget, bg="blue")

        self.testLabel = tk.Label(
            self,
            text="I am the Billing Information Tab",
            font=("Segoe UI", 25)
        )

        self.testLabel.pack()