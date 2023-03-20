import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk
from Data.dataClasses import *
import GUI.MainWindow as MainWindow
import Data.System

BGCOLOR = "#E4E4E4"
BUTTONSELECTED = "#D9D9D9"
BUTTONUNSELECTED = "#F0F0F0"
FONTNAME = ("Courier", 32, "bold")
FONTINFO = ("Courier", 18)
FONTINFOOLD = ("Courier")
FONTBUTTON = ("Courier", 20)
PADSECTION = 15
PADLABEL = 2
PADCOMP = 3 #Component padding

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
            command=lambda:MainWindow.switchPatientList(Data.System.getPatientList())
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
        LabelBorder(self.nameFrame, "Name").grid(row=0, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.name = ctk.CTkLabel(
            self.nameFrame,
            text=patient.firstName + " " + patient.middleName + " " + patient.lastName,
            font=FONTNAME
        )
        self.name.grid(row=1, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)


        self.addressFrame = ctk.CTkFrame(
            self
        )
        self.addressFrame.grid(row=1, column=0, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.addressFrame, "Address").grid(row=0, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.address = ctk.CTkLabel(
            self.addressFrame,
            text=patient.address[0] + "\n" + patient.address[1] + ", " + patient.address[2] + "\n" + patient.address[3],
            anchor="w",
            justify=ctk.LEFT,
            font=FONTINFO
        )
        self.address.grid(row=1, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)


        self.phoneFrame = ctk.CTkFrame(
            self
        )
        self.phoneFrame.grid(row=1, column=1, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.phoneFrame, "Phone Numbers").grid(row=0, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.phone = ctk.CTkLabel(
            self.phoneFrame,
            text="Mobile:" + patient.mobilePhone + "\nHome:  " + patient.homePhone + "\nWork:  " + patient.workPhone,
            anchor="w",
            justify=ctk.LEFT,
            font=FONTINFO
        )
        self.phone.grid(row=1, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)


        self.emergContactFrame = ctk.CTkFrame(
            self
        )
        self.emergContactFrame.grid(row=2, column=0, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.emergContactFrame, "Emergency Contacts").grid(row=0, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        for i in range(len(patient.emergencyContactNames)):
            self.contact = LabelBorder(
                self.emergContactFrame,
                label=str(i+1) + ".)\n  Name:   " + patient.emergencyContactNames[i] + "\n  Number: " + patient.emergencyContactNumbers[i],
                isList=True
            )
            self.contact.grid(row=i+1, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)


        self.locationFrame = ctk.CTkFrame(
            self
        )
        self.locationFrame.grid(row=1, column=2, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.locationFrame, "Location").grid(row=0, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.location = ctk.CTkLabel(
            self.locationFrame,
            text="Facility: " + patient.location[0] + "\nFloor:    " + patient.location[1] + "\nRoom:     " + patient.location[2] + "\nBed:      " + patient.location[3],
            anchor="w",
            justify=ctk.LEFT,
            font=FONTINFO
        )
        self.location.grid(row=1, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)


        self.visitationFrame = ctk.CTkFrame(
            self
        )
        self.visitationFrame.grid(row=2, column=1, sticky="wn", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.visitationFrame, "Visitation").grid(row=0, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.numVisitors = ctk.CTkLabel(
            self.visitationFrame,
            text="Max simultaneous visitors: " + patient.numAllowedVisitors,
            anchor="w",
            justify=ctk.LEFT,
            font=FONTINFO
        )
        self.numVisitors.grid(row=1, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.allowedVisitors = ctk.CTkLabel(
            self.visitationFrame,
            text="List of approved visitors:",
            anchor="w",
            justify=ctk.LEFT,
            font=FONTINFO
        )
        self.allowedVisitors.grid(row=2, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        for i in range(len(patient.allowedVisitors)):
            self.visitor = LabelBorder(
                self.visitationFrame,
                label=str(i+1) + ".) " + patient.allowedVisitors[i],
                isList=True
            )
            self.visitor.grid(row=i+3, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        


class MedicalInfoTab(ctk.CTkFrame):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget)

        self.nameFrame = ctk.CTkFrame(
            self
        )
        self.nameFrame.grid(row=0, column=0, columnspan=10, sticky="nw", padx=PADSECTION, pady= PADSECTION)
        LabelBorder(self.nameFrame, "Name").grid(row=0, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.name = ctk.CTkLabel(
            self.nameFrame,
            text=patient.firstName + " " + patient.middleName + " " + patient.lastName,
            font=FONTNAME
        )
        self.name.grid(row=1, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)


        self.famDoctorFrame = ctk.CTkFrame(
            self
        )
        self.famDoctorFrame.grid(row=1, column=0, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.famDoctorFrame, "Family Doctor").grid(row=0, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.famDoctor = ctk.CTkLabel(
            self.famDoctorFrame,
            text=patient.familyDoctor,
            anchor="w",
            justify=ctk.LEFT,
            font=FONTINFO
        )
        self.famDoctor.grid(row=1, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)


        self.admittanceFrame = ctk.CTkFrame(
            self
        )
        self.admittanceFrame.grid(row=2, column=0, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.admittanceFrame, "Admittance").grid(row=0, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.admittance = ctk.CTkLabel(
            self.admittanceFrame,
            text="Date:   " + patient.dateAdmittance + "\nTime:   " + patient.timeAdmittance + "\nReason: " + patient.reasonAdmission,
            anchor="w",
            justify=ctk.LEFT,
            font=FONTINFO
        )
        self.admittance.grid(row=1, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)


        self.dischargeFrame = ctk.CTkFrame(
            self
        )
        self.dischargeFrame.grid(row=3, column=0, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.dischargeFrame, "Discharge").grid(row=0, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.discharge = ctk.CTkLabel(
            self.dischargeFrame,
            text="Date: " + patient.dateDischarge + "\nTime: " + patient.timeDischarge,
            anchor="w",
            justify=ctk.LEFT,
            font=FONTINFO
        )
        self.discharge.grid(row=1, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)


        self.prescriptionFrame = ctk.CTkFrame(
            self
        )
        self.prescriptionFrame.grid(row=1, column=1, sticky="nw", padx=PADSECTION, pady=PADSECTION, rowspan=2)
        LabelBorder(self.prescriptionFrame, "Prescriptions").grid(row=0, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        for i in range(len(patient.prescriptionNames)):
            self.prescription = LabelBorder(
                self.prescriptionFrame,
                label=str(i+1) + ".)\n  Name:     " + patient.prescriptionNames[i] + "\n  Amount:   " + patient.prescriptionAmount[i] + "\n  Schedule: " + patient.prescriptionSchedule[i],
                isList=True
            )
            self.prescription.grid(row=i+1, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        

        self.proceduresFrame = ctk.CTkFrame(
            self
        )
        self.proceduresFrame.grid(row=3, column=1, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.proceduresFrame, "Scheduled Procedures").grid(row=0, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        for i in range(len(patient.scheduledProcedures)):
            self.procedure = LabelBorder(
                self.proceduresFrame,
                label=str(i+1) + ".) " + patient.scheduledProcedures[i],
                isList=True
            )
            self.procedure.grid(row=i+1, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)


        self.doctorNoteFrame = ctk.CTkFrame(
            self
        )
        self.doctorNoteFrame.grid(row=1, column=2, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.doctorNoteFrame, "Doctor Notes").grid(row=0, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        for i in range(len(patient.doctorNotes)):
            self.doctorNote = LabelBorder(
                self.doctorNoteFrame,
                label=str(i+1) + ".) " + patient.doctorNotes[i],
                isList=True
            )
            self.doctorNote.grid(row=i+1, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)


        self.nurseNoteFrame =ctk.CTkFrame(
            self
        )
        self.nurseNoteFrame.grid(row=2, column=2, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.nurseNoteFrame, "Nurse Notes").grid(row=0, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        for i in range(len(patient.nurseNotes)):
            self.nurseNote = LabelBorder(
                self.nurseNoteFrame,
                label=str(i+1) + ".) " + patient.nurseNotes[i],
                isList=True
            )
            self.nurseNote.grid(row=i+1, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)


        self.addNoteFrame = ctk.CTkFrame(
            self
        )
        self.addNoteFrame.grid(row=3, column=2, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.addNoteFrame, "Add New Note").grid(row=0, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=1, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )
        #Create if statement to change between adding doctor note or nurse note
        #depending on the type of user logged in
        self.addNoteButton.configure(command=lambda: self.addDoctorNote(patient, self.note.get()))
        self.addNoteButton.grid(row=1, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)


    def addNurseNote(self, patient, nurseNote):
        patient.addNurseNote(nurseNote)
        self.master.switchMedical()
    def addDoctorNote(self, patient, doctorNote):
        patient.addDoctorNote(doctorNote)
        self.master.switchMedical()


        



class BillingInfoTab(ctk.CTkFrame):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget)

        self.nameFrame = ctk.CTkFrame(
            self
        )
        self.nameFrame.grid(row=0, column=0, columnspan=10, sticky="w", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.nameFrame, "Name").grid(row=0, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.name = ctk.CTkLabel(
            self.nameFrame,
            text=patient.firstName + " " + patient.middleName + " " + patient.lastName,
            font=FONTNAME
        )
        self.name.grid(row=1, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)


        self.insuranceFrame = ctk.CTkFrame(
            self
        )
        self.insuranceFrame.grid(row=1, column=0, sticky="w", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.insuranceFrame, "Insurance Carrier").grid(row=0, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.insuranceName = ctk.CTkLabel(
            self.insuranceFrame,
            text=patient.insuranceCarrier,
            anchor="w",
            justify=ctk.LEFT,
            font=FONTINFO
        )
        self.insuranceName.grid(row=1, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)


        self.policyInfoFrame = ctk.CTkFrame(
            self
        )
        self.policyInfoFrame.grid(row=2, column=0, sticky="w", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.policyInfoFrame, "Insurance Policy Info").grid(row=0, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.policyInfo = ctk.CTkLabel(
            self.policyInfoFrame,
            text="Account Number: " + patient.insuranceAccountNumber + "\nGroup Number:   " + patient.insuranceGroupNumber,
            anchor="w",
            justify=ctk.LEFT,
            font=FONTINFO
        )
        self.policyInfo.grid(row=1, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)


        self.amountPaidFrame = ctk.CTkFrame(
            self
        )
        self.amountPaidFrame.grid(row=3, column=0, sticky="w", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.amountPaidFrame, "Amount Paid").grid(row=0, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.amountPaid = ctk.CTkLabel(
            self.amountPaidFrame,
            text="${:.2f}".format(patient.amountPaid),
            anchor="w",
            justify=ctk.LEFT,
            font=FONTINFO
        )
        self.amountPaid.grid(row=1, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)


        self.amountPaidInsuranceFrame = ctk.CTkFrame(
            self
        )
        self.amountPaidInsuranceFrame.grid(row=4, column=0, sticky="w", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.amountPaidInsuranceFrame, "Amount Paid By Insurance").grid(row=0, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.amountPaidInsurance = ctk.CTkLabel(
            self.amountPaidInsuranceFrame,
            text="${:.2f}".format(patient.amountPaidByInsurance),
            anchor="w",
            justify=ctk.LEFT,
            font=FONTINFO
        )
        self.amountPaidInsurance.grid(row=1, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)

        try:
            patient.updateAmountOwed() #Update amount owed before printing it in GUI
        except:
            pass
        self.amountOwedFrame = ctk.CTkFrame(
            self
        )
        self.amountOwedFrame.grid(row=5, column=0, sticky="w", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.amountOwedFrame, "Amount Owed").grid(row=0, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.amountOwed = ctk.CTkLabel(
            self.amountOwedFrame,
            text="${:.2f}".format(patient.amountOwed),
            anchor="w",
            justify=ctk.LEFT,
            font=FONTINFO
        )
        self.amountOwed.grid(row=1, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)

        
        self.listChargesFrame = ctk.CTkFrame(
            self
        )
        self.listChargesFrame.grid(row=1, column=1, sticky="nw", padx=PADSECTION, pady=PADSECTION, rowspan=10)
        LabelBorder(self.listChargesFrame, "List of Charges").grid(row=0, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL, columnspan=2)
        for i in range(len(patient.listCharges)):
            self.singleChargeFrame = ctk.CTkFrame(self.listChargesFrame)
            self.chargeName = ctk.CTkLabel(
                self.singleChargeFrame,
                text=patient.listCharges[i],
                anchor="w",
                justify=ctk.LEFT,
                wraplength=500,
                font=FONTINFO
            )
            self.chargeName.grid(row=0, column=0, sticky="w", padx=PADCOMP)
            self.chargeAmount = ctk.CTkLabel(
                self.singleChargeFrame,
                text="${:.2f}".format(patient.listChargesAmount[i]),
                anchor="e",
                justify=ctk.RIGHT,
                font=FONTINFO
            )
            self.chargeAmount.grid(row=0, column=1, sticky="e", padx=10)
            self.singleChargeFrame.grid(row=i+1, column=0, sticky="ew", padx=PADCOMP, pady=PADCOMP)
            self.singleChargeFrame.grid_columnconfigure(0, weight=1)



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
            justify=ctk.LEFT,
            font=("Courier", 15),
            height=1
        )
        if isList:
            self.label.configure(font=FONTINFO)
            self.label.configure(wraplength=550)
        self.label.pack(padx=3)