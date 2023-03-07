import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk
from Data.dataClasses import *
import GUI.MainWindow as MainWindow

BGCOLOR = "#E4E4E4"
BUTTONSELECTED = "#D9D9D9"
BUTTONUNSELECTED = "#F0F0F0"
FONTNAME = ("Courier", 32, "bold")
FONTINFO = ("Courier", 18)
FONTINFOOLD = ("Courier")
FONTBUTTON = ("Courier", 20)
PADSECTION = 15

#Class for showing all the information for a selected patient
class PatientDetailedView(ctk.CTkFrame):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget)
        self.patient = patient
        #first tab shown will be the personal info tab
        self.shownTab = PersonalInfoTab(self, patient)
        

        #Create frame and buttons for switching tabs
        #Will need to setup later to only show relavant tabs based on which user is logged in.
        self.buttonFrame = ctk.CTkFrame(self)
        self.personalButton = ctk.CTkButton(
            self.buttonFrame,
            text="Personal Information",
            command=lambda:self.switchPersonal(),
            font=FONTBUTTON,
            width=270,
            height=40,
            state="disabled",
        )
        self.medicalButton = ctk.CTkButton(
            self.buttonFrame,
            text="Medical Information",
            command=lambda:self.switchMedical(),
            font=FONTBUTTON,
            width=270,
            height=40,
        )
        self.billingButton = ctk.CTkButton(
            self.buttonFrame,
            text="Billing Information",
            command=lambda:self.switchBilling(),
            font=FONTBUTTON,
            width=270,
            height=40,
        )
        self.returnButton = ctk.CTkButton(
            self.buttonFrame,
            text="Back",
            font=FONTBUTTON,
            width=100,
            height=40,
            #command= BACK COMMAND HERE
        )
        self.returnButton.grid(row=0, column=0, padx=5, pady=5)
        self.personalButton.grid(row=0, column=1, padx=5, pady=5)
        self.medicalButton.grid(row=0, column=2, padx=5, pady=5)
        self.billingButton.grid(row=0, column=3, padx=5, pady=5)
        
        self.buttonFrame.grid(row=0, column=0, sticky="news", padx=8, pady=8)
        self.shownTab.grid(row=1, column=0, sticky="news")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)



    #Functions to switch between the tabs using the buttons
    def switchPersonal(self):
        self.personalButton.configure(state="disabled")
        self.medicalButton.configure(state="normal")
        self.billingButton.configure(state="normal")
        
        #Destroy the current tab before loading the new one
        for i in self.shownTab.winfo_children():
            i.destroy()
        self.shownTab.destroy()

        self.shownTab = PersonalInfoTab(self, self.patient)
        self.shownTab.grid(row=1, column=0, sticky="news")

    def switchMedical(self):
        self.personalButton.configure(state="normal")
        self.medicalButton.configure(state="disabled")
        self.billingButton.configure(state="normal")

        #Destroy the current tab before loading the new one
        for i in self.shownTab.winfo_children():
            i.destroy()
        self.shownTab.destroy()

        self.shownTab = MedicalInfoTab(self, self.patient)
        self.shownTab.grid(row=1, column=0, sticky="news")

    def switchBilling(self):
        self.personalButton.configure(state="normal")
        self.medicalButton.configure(state="normal")
        self.billingButton.configure(state="disabled")

        #Destroy the current tab before loading the new one
        for i in self.shownTab.winfo_children():
            i.destroy()
        self.shownTab.destroy()
        
        self.shownTab = BillingInfoTab(self, self.patient)
        self.shownTab.grid(row=1, column=0, sticky="news")








#############################################
# Tabs
#############################################


class PersonalInfoTab(ctk.CTkFrame):
    def __init__(self, parentWidget, patient):
        #super().__init__(parentWidget, bg=BGCOLOR)
        super().__init__(parentWidget)

        self.nameFrame = ctk.CTkFrame(
            self
        )
        self.nameFrame.grid(row=0, column=0, columnspan=10, sticky="w", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.nameFrame, "Name").grid(row=0, column=0, sticky="w", padx=2, pady=2)
        self.name = ctk.CTkLabel(
            self.nameFrame,
            text=patient.firstName + " " + patient.middleName + " " + patient.lastName,
            font=FONTNAME
        )
        self.name.grid(row=1, column=0, sticky="w", padx=3, pady=3)


        self.addressFrame = ctk.CTkFrame(
            self
        )
        self.addressFrame.grid(row=1, column=0, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.addressFrame, "Address").grid(row=0, column=0, sticky="w", padx=2, pady=2)
        self.address = ctk.CTkLabel(
            self.addressFrame,
            text=patient.address[0] + "\n" + patient.address[1] + ", " + patient.address[2] + "\n" + patient.address[3],
            anchor="w",
            justify=tk.LEFT,
            font=FONTINFO
        )
        self.address.grid(row=1, column=0, sticky="w", padx=3, pady=3)


        self.phoneFrame = ctk.CTkFrame(
            self
        )
        self.phoneFrame.grid(row=1, column=1, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.phoneFrame, "Phone Numbers").grid(row=0, column=0, sticky="w", padx=2, pady=2)
        self.phone = ctk.CTkLabel(
            self.phoneFrame,
            text="Mobile:" + patient.mobilePhone + "\nHome:  " + patient.homePhone + "\nWork:  " + patient.workPhone,
            anchor="w",
            justify=tk.LEFT,
            font=FONTINFO
        )
        self.phone.grid(row=1, column=0, sticky="w", padx=3, pady=3)


        self.emergContactFrame = ctk.CTkFrame(
            self
        )
        self.emergContactFrame.grid(row=2, column=0, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.emergContactFrame, "Emergency Contacts").grid(row=0, column=0, sticky="w", padx=2, pady=2)
        for i in range(len(patient.emergencyContactNames)):
            self.contact = LabelBorder(self.emergContactFrame, str(i+1) + ".)\n  Name:   " + patient.emergencyContactNames[i] + "\n  Number: " + patient.emergencyContactNumbers[i], isList=True)
            self.contact.grid(row=i+1, column=0, sticky="w", padx=3, pady=3)


        self.locationFrame = ctk.CTkFrame(
            self
        )
        self.locationFrame.grid(row=1, column=2, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.locationFrame, "Location").grid(row=0, column=0, sticky="w", padx=2, pady=2)
        self.location = ctk.CTkLabel(
            self.locationFrame,
            text="Facility: " + patient.location[0] + "\nFloor:    " + patient.location[1] + "\nRoom:     " + patient.location[2] + "\nBed:      " + patient.location[3],
            anchor="w",
            justify=tk.LEFT,
            font=FONTINFO
        )
        self.location.grid(row=1, column=0, sticky="w", padx=3, pady=3)


        self.visitationFrame = ctk.CTkFrame(
            self
        )
        self.visitationFrame.grid(row=2, column=1, sticky="wn", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.visitationFrame, "Visitation").grid(row=0, column=0, sticky="w", padx=2, pady=2)
        self.numVisitors = ctk.CTkLabel(
            self.visitationFrame,
            text="Max simultaneous visitors: " + patient.numAllowedVisitors,
            anchor="w",
            justify=tk.LEFT,
            font=FONTINFO
        )
        self.numVisitors.grid(row=1, column=0, sticky="w", padx=3, pady=3)
        self.allowedVisitors = ctk.CTkLabel(
            self.visitationFrame,
            text="List of approved visitors:",
            anchor="w",
            justify=tk.LEFT,
            font=FONTINFO
        )
        self.allowedVisitors.grid(row=2, column=0, sticky="w", padx=3, pady=3)
        for i in range(len(patient.allowedVisitors)):
            self.visitor = LabelBorder(self.visitationFrame, str(i+1) + ".) " + patient.allowedVisitors[i], isList=True)
            self.visitor.grid(row=i+3, column=0, padx=3, pady=3, sticky="w")
        

class MedicalInfoTab(ctk.CTkFrame):
    def __init__(self, parentWidget, patient):
        #super().__init__(parentWidget, bg=BGCOLOR)
        super().__init__(parentWidget)

        self.nameFrame = tk.LabelFrame(
            self,
            text="Name",
            font=FONTINFOOLD
        )
        self.nameFrame.grid(row=0, column=0, columnspan=10, sticky="w", padx=PADSECTION, pady= PADSECTION)
        self.name = tk.Label(
            self.nameFrame,
            text=patient.firstName + " " + patient.middleName + " " + patient.lastName,
            font=FONTNAME
        )
        self.name.pack()

        self.famDoctorFrame = tk.LabelFrame(
            self,
            text="Family Doctor",
            font=FONTINFOOLD
        )
        self.famDoctorFrame.grid(row=1, column=0, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        self.famDoctor = tk.Label(
            self.famDoctorFrame,
            text=patient.familyDoctor,
            anchor="w",
            justify=tk.LEFT,
            font=FONTINFOOLD
        )
        self.famDoctor.pack()

        self.admittanceFrame = tk.LabelFrame(
            self,
            text="Admittance",
            font=FONTINFOOLD
        )
        self.admittanceFrame.grid(row=2, column=0, sticky="w", padx=PADSECTION, pady=PADSECTION)
        self.admittance = tk.Label(
            self.admittanceFrame,
            text="Date:   " + patient.dateAdmittance + "\nTime:   " + patient.timeAdmittance + "\nReason: " + patient.reasonAdmission,
            anchor="w",
            justify=tk.LEFT,
            font=FONTINFOOLD
        )
        self.admittance.pack()

        self.dischargeFrame = tk.LabelFrame(
            self,
            text="Discharge",
            font=FONTINFOOLD
        )
        self.dischargeFrame.grid(row=3, column=0, sticky="w", padx=PADSECTION, pady=PADSECTION)
        self.discharge = tk.Label(
            self.dischargeFrame,
            text="Date: " + patient.dateDischarge + "\nTime: " + patient.timeDischarge,
            anchor="w",
            justify=tk.LEFT,
            font=FONTINFOOLD
        )
        self.discharge.pack()

        #maybe make scrollable at some point
        self.prescriptionFrame = tk.LabelFrame(
            self,
            text="Prescriptions",
            font=FONTINFOOLD
        )
        self.prescriptionFrame.grid(row=1, column=1, sticky="w", padx=PADSECTION, pady=PADSECTION, rowspan=2)
        for i in range(len(patient.prescriptionNames)):
            self.prescription = tk.Label(
                self.prescriptionFrame,
                relief=tk.RAISED,
                borderwidth=1,
                text=str(i+1) + ".)\n  Name:     " + patient.prescriptionNames[i] + "\n  Amount:   " + patient.prescriptionAmount[i] + "\n  Schedule: " + patient.prescriptionSchedule[i],
                anchor="w",
                justify=tk.LEFT,
                font=FONTINFOOLD
            )
            self.prescription.grid(row=i, column=0, sticky="w", padx=3, pady=3)
        
        self.proceduresFrame = tk.LabelFrame(
            self,
            text="Scheduled Procedures",
            font=FONTINFOOLD
        )
        self.proceduresFrame.grid(row=3, column=1, sticky="w", padx=PADSECTION, pady=PADSECTION)
        for i in range(len(patient.scheduledProcedures)):
            self.procedure = tk.Label(
                self.proceduresFrame,
                relief=tk.RAISED,
                borderwidth=1,
                text=str(i+1) + ".) " + patient.scheduledProcedures[i],
                anchor="w",
                justify=tk.LEFT,
                font=FONTINFOOLD
            )
            self.procedure.grid(row=i, column=0, sticky="w", padx=3, pady=3)

        self.doctorNoteFrame = tk.LabelFrame(
            self,
            text="Doctor Notes",
            font=FONTINFOOLD
        )
        self.doctorNoteFrame.grid(row=1, column=2, sticky="w", padx=PADSECTION, pady=PADSECTION)
        for i in range(len(patient.doctorNotes)):
            self.doctorNote = tk.Label(
                self.doctorNoteFrame,
                relief=tk.RAISED,
                borderwidth=1,
                text=str(i+1) + ".) " + patient.doctorNotes[i],
                anchor="w",
                justify=tk.LEFT,
                font=FONTINFOOLD
            )
            self.doctorNote.grid(row=i, column=0, sticky="w", padx=3, pady=3)

        self.nurseNoteFrame = tk.LabelFrame(
            self,
            text="Nurse Notes",
            font=FONTINFOOLD
        )
        self.nurseNoteFrame.grid(row=2, column=2, sticky="w", padx=PADSECTION, pady=PADSECTION)
        for i in range(len(patient.nurseNotes)):
            self.nurseNote = tk.Label(
                self.nurseNoteFrame,
                relief=tk.RAISED,
                borderwidth=1,
                text=str(i+1) + ".) " + patient.nurseNotes[i],
                anchor="w",
                justify=tk.LEFT,
                font=FONTINFOOLD
            )
            self.nurseNote.grid(row=i, column=0, sticky="w", padx=3, pady=3)

        self.addNoteFrame = tk.LabelFrame(
            self,
            text="Add New Note",
            font=FONTINFOOLD
        )
        self.note = tk.StringVar()
        self.addNoteFrame.grid(row=3, column=2, sticky="w", padx=PADSECTION, pady=PADSECTION)
        self.addNoteEntry = tk.Entry(
            self.addNoteFrame,
            font=FONTINFOOLD,
            width=40,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=0, column=0)
        self.addNoteButton = tk.Button(
            self.addNoteFrame,
            text="Add",
            font=FONTINFOOLD,
            padx=5,
            pady=5
        )
        #Create if statement to change between adding doctor note or nurse note
        #depending on the type of user logged in
        self.addNoteButton.configure(command=lambda: self.addDoctorNote(patient, self.note.get()))
        self.addNoteButton.grid(row=0, column=1)


    def addNurseNote(self, patient, nurseNote):
        patient.addNurseNote(nurseNote)
        self.master.switchMedical()
    def addDoctorNote(self, patient, doctorNote):
        patient.addDoctorNote(doctorNote)
        self.master.switchMedical()


        



class BillingInfoTab(ctk.CTkFrame):
    def __init__(self, parentWidget, patient):
        #super().__init__(parentWidget, bg=BGCOLOR)
        super().__init__(parentWidget)

        self.nameFrame = tk.LabelFrame(
            self,
            text="Name",
            font=FONTINFOOLD
        )
        self.nameFrame.grid(row=0, column=0, columnspan=10, sticky="w", padx=PADSECTION, pady=PADSECTION)
        self.name = tk.Label(
            self.nameFrame,
            text=patient.firstName + " " + patient.middleName + " " + patient.lastName,
            font=FONTNAME
        )
        self.name.pack()

        self.insuranceFrame = tk.LabelFrame(
            self,
            text="Insurance Carrier",
            font=FONTINFOOLD
        )
        self.insuranceFrame.grid(row=1, column=0, sticky="w", padx=PADSECTION, pady=PADSECTION)
        self.insuranceName = tk.Label(
            self.insuranceFrame,
            text=patient.insuranceCarrier,
            anchor="w",
            justify=tk.LEFT,
            font=FONTINFOOLD
        )
        self.insuranceName.pack()

        self.policyInfoFrame = tk.LabelFrame(
            self,
            text="Insurance Policy Info",
            font=FONTINFOOLD
        )
        self.policyInfoFrame.grid(row=2, column=0, sticky="w", padx=PADSECTION, pady=PADSECTION)
        self.policyInfo = tk.Label(
            self.policyInfoFrame,
            text="Account Number: " + patient.insuranceAccountNumber + "\nGroup Number:   " + patient.insuranceGroupNumber,
            anchor="w",
            justify=tk.LEFT,
            font=FONTINFOOLD
        )
        self.policyInfo.pack(fill=tk.BOTH)

        self.amountPaidFrame = tk.LabelFrame(
            self,
            text="Amount Paid",
            font=FONTINFOOLD
        )
        self.amountPaidFrame.grid(row=3, column=0, sticky="w", padx=PADSECTION, pady=PADSECTION)
        self.amountPaid = tk.Label(
            self.amountPaidFrame,
            text="${:.2f}".format(patient.amountPaid),
            anchor="w",
            justify=tk.LEFT,
            font=FONTINFOOLD
        )
        self.amountPaid.pack(fill=tk.BOTH)

        self.amountPaidInsuranceFrame = tk.LabelFrame(
            self,
            text="Amount Paid By Insurance",
            font=FONTINFOOLD
        )
        self.amountPaidInsuranceFrame.grid(row=4, column=0, sticky="w", padx=PADSECTION, pady=PADSECTION)
        self.amountPaidInsurance = tk.Label(
            self.amountPaidInsuranceFrame,
            text="${:.2f}".format(patient.amountPaidByInsurance),
            anchor="w",
            justify=tk.LEFT,
            font=FONTINFOOLD
        )
        self.amountPaidInsurance.pack(fill=tk.BOTH)

        patient.updateAmountOwed() #UPDATE AMOUNT OWED BEFORE PRINTING IT IN GUI
        self.amountOwedFrame = tk.LabelFrame(
            self,
            text="Amount Owed",
            font=FONTINFOOLD
        )
        self.amountOwedFrame.grid(row=5, column=0, sticky="w", padx=PADSECTION, pady=PADSECTION)
        self.amountOwed = tk.Label(
            self.amountOwedFrame,
            text="${:.2f}".format(patient.amountOwed),
            anchor="w",
            justify=tk.LEFT,
            font=FONTINFOOLD
        )
        self.amountOwed.pack(fill=tk.BOTH)

        self.chargesList = tk.StringVar(value=patient.listCharges)
        self.chargesAmountList = tk.StringVar(value=patient.listChargesAmount)
        self.listChargesFrame = tk.LabelFrame(
            self,
            text="List of Charges",
            font=FONTINFOOLD
        )
        self.listChargesFrame.grid(row=1, column=1, sticky="nw", padx=PADSECTION, pady=PADSECTION, rowspan=10)
        self.chargesListBox = tk.Listbox(
            self.listChargesFrame,
            listvariable=self.chargesList,
            width=30,
            font=FONTINFOOLD
        )
        self.chargesListBox.grid(row=0, column=0, sticky="w", padx=3, pady=3)
        self.chargesAmountListBox = tk.Listbox(
            self.listChargesFrame,
            listvariable=self.chargesAmountList,
            width=12,
            font=FONTINFOOLD
        )
        self.chargesAmountListBox.grid(row=0, column=1, sticky="w", padx=3, pady=3)


#Class to create a label with a border around it
#isList is a boolean flag to mark if the border is a list item, in which it should use the default INFO font
#   Assumes false as the default
class LabelBorder(ctk.CTkFrame):
    def __init__(self, parentWidget, label, isList=False):
        super().__init__(parentWidget)
        self.configure(height=1)
        self.label = ctk.CTkLabel(
            self,
            text=label,
            anchor="w",
            justify=tk.LEFT,
            font=("Courier", 15),
            height=1
        )
        if isList:
            self.label.configure(font=FONTINFO)
        self.label.pack(padx=3)