import customtkinter as ctk

import Data.System
import Data.AddNewInfo
import GUI.MainWindow as MainWindow

BG_COLOR = "#E4E4E4"
BUTTON_SELECTED = "#D9D9D9"
BUTTON_UNSELECTED = "#F0F0F0"
FONTNAME = ("Courier", 32, "bold")
FONT_INFO = ("Courier", 18)
FONT_BUTTON = ("Courier", 20)
PAD_SECTION = 15
PAD_LABEL = 2
PAD_COMP = 3  # Component padding


# Class for showing all the information for a selected patient
class PatientDetailedView(ctk.CTkFrame):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget)
        self.patient = patient
        # first tab shown will be the personal info tab
        self.shownTab = PersonalInfoTab(self, patient)

        # Create frame and buttons for switching tabs
        # Will need to set up later to only show relevant tabs based on which user is logged in.
        self.buttonFrame = ctk.CTkFrame(self)
        self.personalButton = ctk.CTkButton(
            self.buttonFrame,
            text="Personal Information",
            command=lambda: self.switchPersonal(),
            font=FONT_BUTTON,
            width=270,
            height=40,
            state="disabled",
        )
        self.personalButton.grid(row=0, column=1, padx=5, pady=5)

        # Only show the medical tab to Doctor and Nurse user types
        if Data.System.getUserType() == 0 or Data.System.getUserType() == 1:
            self.medicalButton = ctk.CTkButton(
                self.buttonFrame,
                text="Medical Information",
                command=lambda: self.switchMedical(),
                font=FONT_BUTTON,
                width=270,
                height=40,
            )
            self.medicalButton.grid(row=0, column=2, padx=5, pady=5)

        # Only show billing tab for Doctor, Nurse, and Office Staff user types
        if Data.System.getUserType() == 0 or Data.System.getUserType() == 1 or Data.System.getUserType() == 2:
            self.billingButton = ctk.CTkButton(
                self.buttonFrame,
                text="Billing Information",
                command=lambda: self.switchBilling(),
                font=FONT_BUTTON,
                width=270,
                height=40,
            )
            self.billingButton.grid(row=0, column=3, padx=5, pady=5)

        self.returnButton = ctk.CTkButton(
            self.buttonFrame,
            text="Back",
            font=FONT_BUTTON,
            width=100,
            height=40,
            command=lambda: MainWindow.switchPatientList(Data.System.getPatientList())
        )
        self.returnButton.grid(row=0, column=0, padx=5, pady=5)

        # Only show the edit patient button for Office Staff user type
        if Data.System.getUserType() == 2:
            self.EditPatientButton = ctk.CTkButton(
                self.buttonFrame,
                text="Edit Patient",
                font=FONT_BUTTON,
                width=100,
                height=40,
                command=lambda: MainWindow.switchEditPatientView(Data.System.getUser())
            )
            self.EditPatientButton.grid(row=0, column=4, padx=5, pady=5)

        self.buttonFrame.grid(row=0, column=0, sticky="news", padx=8, pady=8)
        self.shownTab.grid(row=1, column=0, sticky="news")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

    # Functions to switch between the tabs using the buttons
    def switchPersonal(self):
        # Some tab buttons may not exist depending on the type of user logged in
        try:
            self.personalButton.configure(state="disabled")
        except (AttributeError, NameError):
            pass
        try:
            self.medicalButton.configure(state="normal")
        except (AttributeError, NameError):
            pass
        try:
            self.billingButton.configure(state="normal")
        except (AttributeError, NameError):
            pass

        # Destroy the current tab before loading the new one
        for i in self.shownTab.winfo_children():
            i.destroy()
        self.shownTab.destroy()

        self.shownTab = PersonalInfoTab(self, self.patient)
        self.shownTab.grid(row=1, column=0, sticky="news")

    def switchMedical(self):
        # Some tab buttons may not exist depending on the type of user logged in
        try:
            self.personalButton.configure(state="normal")
        except (AttributeError, NameError):
            pass
        try:
            self.medicalButton.configure(state="disabled")
        except (AttributeError, NameError):
            pass
        try:
            self.billingButton.configure(state="normal")
        except (AttributeError, NameError):
            pass

        # Destroy the current tab before loading the new one
        for i in self.shownTab.winfo_children():
            i.destroy()
        self.shownTab.destroy()

        self.shownTab = MedicalInfoTab(self, self.patient)
        self.shownTab.grid(row=1, column=0, sticky="news")

    def switchBilling(self):
        # Some tab buttons may not exist depending on the type of user logged in
        try:
            self.personalButton.configure(state="normal")
        except (AttributeError, NameError):
            pass
        try:
            self.medicalButton.configure(state="normal")
        except (AttributeError, NameError):
            pass
        try:
            self.billingButton.configure(state="disabled")
        except (AttributeError, NameError):
            pass

        # Destroy the current tab before loading the new one
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
        super().__init__(parentWidget)

        self.nameFrame = ctk.CTkFrame(
            self
        )
        self.nameFrame.grid(row=0, column=0, columnspan=10, sticky="w", padx=PAD_SECTION, pady=PAD_SECTION)
        LabelBorder(self.nameFrame, "Name").grid(row=0, column=0, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)
        self.name = ctk.CTkLabel(
            self.nameFrame,
            text=patient.firstName + " " + patient.middleName + " " + patient.lastName,
            font=FONTNAME
        )
        self.name.grid(row=1, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        ctk.CTkButton(self.nameFrame, text="Print", font=("Arial", 20), command=lambda: Data.Printer.initPrint(1)).grid(
            row=0, column=1, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)

        # Don't show address of patient if volunteer is logged in
        if Data.System.getUserType() != 3:
            self.addressFrame = ctk.CTkFrame(
                self
            )
            self.addressFrame.grid(row=1, column=0, sticky="nw", padx=PAD_SECTION, pady=PAD_SECTION)
            LabelBorder(self.addressFrame, "Address").grid(row=0, column=0, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)
            self.address = ctk.CTkLabel(
                self.addressFrame,
                text=patient.address[0] + "\n" + patient.address[1] + ", " + patient.address[2] + "\n" +
                     patient.address[3],
                anchor="w",
                justify=ctk.LEFT,
                font=FONT_INFO
            )
            self.address.grid(row=1, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        # Don't show phone numbers of patient if volunteer is logged in
        if Data.System.getUserType() != 3:
            self.phoneFrame = ctk.CTkFrame(
                self
            )
            self.phoneFrame.grid(row=1, column=1, sticky="nw", padx=PAD_SECTION, pady=PAD_SECTION)
            LabelBorder(self.phoneFrame, "Phone Numbers").grid(row=0, column=0, sticky="w", padx=PAD_LABEL,
                                                               pady=PAD_LABEL)
            self.phone = ctk.CTkLabel(
                self.phoneFrame,
                text="Mobile:" + patient.mobilePhone + "\nHome:  " + patient.homePhone + "\nWork:  " + patient.workPhone,
                anchor="w",
                justify=ctk.LEFT,
                font=FONT_INFO
            )
            self.phone.grid(row=1, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        self.emergencyContactFrame = ctk.CTkFrame(
            self
        )
        # Change location of emergency contacts in grid if volunteer is logged in
        if Data.System.getUserType() == 3:
            self.emergencyContactFrame.grid(row=1, column=0, sticky="nw", padx=PAD_SECTION, pady=PAD_SECTION)
        else:
            self.emergencyContactFrame.grid(row=2, column=0, sticky="nw", padx=PAD_SECTION, pady=PAD_SECTION)
        LabelBorder(self.emergencyContactFrame, "Emergency Contacts").grid(row=0, column=0, sticky="w", padx=PAD_LABEL,
                                                                           pady=PAD_LABEL)
        for i in range(len(patient.emergencyContactNames)):
            self.contact = LabelBorder(
                self.emergencyContactFrame,
                label=str(i + 1) + ".)\n  Name:   " + patient.emergencyContactNames[i] + "\n  Number: " +
                      patient.emergencyContactNumbers[i],
                isList=True
            )
            self.contact.grid(row=i + 1, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        self.locationFrame = ctk.CTkFrame(
            self
        )
        self.locationFrame.grid(row=1, column=2, sticky="nw", padx=PAD_SECTION, pady=PAD_SECTION)
        LabelBorder(self.locationFrame, "Location").grid(row=0, column=0, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)
        self.location = ctk.CTkLabel(
            self.locationFrame,
            text="Facility: " + patient.location[0] + "\nFloor:    " + patient.location[1] + "\nRoom:     " +
                 patient.location[2] + "\nBed:      " + patient.location[3],
            anchor="w",
            justify=ctk.LEFT,
            font=FONT_INFO
        )
        self.location.grid(row=1, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        self.visitationFrame = ctk.CTkFrame(
            self
        )
        # Change location of visitation frame if volunteer is logged in
        if Data.System.getUserType() == 3:
            self.visitationFrame.grid(row=1, column=1, sticky="wn", padx=PAD_SECTION, pady=PAD_SECTION)
        else:
            self.visitationFrame.grid(row=2, column=1, sticky="wn", padx=PAD_SECTION, pady=PAD_SECTION)
        LabelBorder(self.visitationFrame, "Visitation").grid(row=0, column=0, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)
        self.numVisitors = ctk.CTkLabel(
            self.visitationFrame,
            text="Max simultaneous visitors: " + patient.numAllowedVisitors,
            anchor="w",
            justify=ctk.LEFT,
            font=FONT_INFO
        )
        self.numVisitors.grid(row=1, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)
        self.allowedVisitors = ctk.CTkLabel(
            self.visitationFrame,
            text="List of approved visitors:",
            anchor="w",
            justify=ctk.LEFT,
            font=FONT_INFO
        )
        self.allowedVisitors.grid(row=2, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)
        for i in range(len(patient.allowedVisitors)):
            self.visitor = LabelBorder(
                self.visitationFrame,
                label=str(i + 1) + ".) " + patient.allowedVisitors[i],
                isList=True
            )
            self.visitor.grid(row=i + 3, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)


class MedicalInfoTab(ctk.CTkFrame):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget)

        self.nameFrame = ctk.CTkFrame(
            self
        )
        self.nameFrame.grid(row=0, column=0, columnspan=10, sticky="nw", padx=PAD_SECTION, pady=PAD_SECTION)
        LabelBorder(self.nameFrame, "Name").grid(row=0, column=0, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)
        self.name = ctk.CTkLabel(
            self.nameFrame,
            text=patient.firstName + " " + patient.middleName + " " + patient.lastName,
            font=FONTNAME
        )
        self.name.grid(row=1, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        ctk.CTkButton(self.nameFrame, text="Print", font=("Arial", 20), command=lambda: Data.Printer.initPrint(2)).grid(
            row=0, column=1, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)

        self.famDoctorFrame = ctk.CTkFrame(
            self
        )
        self.famDoctorFrame.grid(row=1, column=0, sticky="nw", padx=PAD_SECTION, pady=PAD_SECTION)
        LabelBorder(self.famDoctorFrame, "Family Doctor").grid(row=0, column=0, sticky="w", padx=PAD_LABEL,
                                                               pady=PAD_LABEL)
        self.famDoctor = ctk.CTkLabel(
            self.famDoctorFrame,
            text=patient.familyDoctor,
            anchor="w",
            justify=ctk.LEFT,
            font=FONT_INFO
        )
        self.famDoctor.grid(row=1, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        self.admittanceFrame = ctk.CTkFrame(
            self
        )
        self.admittanceFrame.grid(row=2, column=0, sticky="nw", padx=PAD_SECTION, pady=PAD_SECTION)
        LabelBorder(self.admittanceFrame, "Admittance").grid(row=0, column=0, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)
        self.admittance = ctk.CTkLabel(
            self.admittanceFrame,
            text="Date:   " + patient.dateAdmittance + "\nTime:   " + patient.timeAdmittance + "\nReason: " + patient.reasonAdmission,
            anchor="w",
            justify=ctk.LEFT,
            font=FONT_INFO
        )
        self.admittance.grid(row=1, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        self.dischargeFrame = ctk.CTkFrame(
            self
        )
        self.dischargeFrame.grid(row=3, column=0, sticky="nw", padx=PAD_SECTION, pady=PAD_SECTION)
        LabelBorder(self.dischargeFrame, "Discharge").grid(row=0, column=0, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)
        self.discharge = ctk.CTkLabel(
            self.dischargeFrame,
            text="Date: " + patient.dateDischarge + "\nTime: " + patient.timeDischarge,
            anchor="w",
            justify=ctk.LEFT,
            font=FONT_INFO
        )
        self.discharge.grid(row=1, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        self.prescriptionFrame = ctk.CTkFrame(
            self
        )
        self.prescriptionFrame.grid(row=1, column=1, sticky="nw", padx=PAD_SECTION, pady=PAD_SECTION, rowspan=2)
        LabelBorder(self.prescriptionFrame, "Prescriptions").grid(row=0, column=0, sticky="w", padx=PAD_LABEL,
                                                                  pady=PAD_LABEL)
        for i in range(len(patient.prescriptionNames)):
            self.prescription = LabelBorder(
                self.prescriptionFrame,
                label=str(i + 1) + ".)\n  Name:     " + patient.prescriptionNames[i] + "\n  Amount:   " +
                      patient.prescriptionAmount[i] + "\n  Schedule: " + patient.prescriptionSchedule[i],
                isList=True
            )
            self.prescription.grid(row=i + 1, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        self.proceduresFrame = ctk.CTkFrame(
            self
        )
        self.proceduresFrame.grid(row=3, column=1, sticky="nw", padx=PAD_SECTION, pady=PAD_SECTION)
        LabelBorder(self.proceduresFrame, "Scheduled Procedures").grid(row=0, column=0, sticky="w", padx=PAD_LABEL,
                                                                       pady=PAD_LABEL)
        for i in range(len(patient.scheduledProcedures)):
            self.procedure = LabelBorder(
                self.proceduresFrame,
                label=str(i + 1) + ".) " + patient.scheduledProcedures[i],
                isList=True
            )
            self.procedure.grid(row=i + 1, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        self.doctorNoteFrame = ctk.CTkFrame(
            self
        )
        self.doctorNoteFrame.grid(row=1, column=2, sticky="nw", padx=PAD_SECTION, pady=PAD_SECTION)
        LabelBorder(self.doctorNoteFrame, "Doctor Notes").grid(row=0, column=0, sticky="w", padx=PAD_LABEL,
                                                               pady=PAD_LABEL)
        for i in range(len(patient.doctorNotes)):
            self.doctorNote = LabelBorder(
                self.doctorNoteFrame,
                label=str(i + 1) + ".) " + patient.doctorNotes[i],
                isList=True
            )
            self.doctorNote.grid(row=i + 1, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        self.nurseNoteFrame = ctk.CTkFrame(
            self
        )
        self.nurseNoteFrame.grid(row=2, column=2, sticky="nw", padx=PAD_SECTION, pady=PAD_SECTION)
        LabelBorder(self.nurseNoteFrame, "Nurse Notes").grid(row=0, column=0, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)
        for i in range(len(patient.nurseNotes)):
            self.nurseNote = LabelBorder(
                self.nurseNoteFrame,
                label=str(i + 1) + ".) " + patient.nurseNotes[i],
                isList=True
            )
            self.nurseNote.grid(row=i + 1, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        self.addNoteFrame = ctk.CTkFrame(
            self
        )
        self.addNoteFrame.grid(row=3, column=2, sticky="nw", padx=PAD_SECTION, pady=PAD_SECTION)
        LabelBorder(self.addNoteFrame, "Add New Note").grid(row=0, column=0, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)
        self.note = ctk.StringVar()
        self.addNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=1, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)
        self.addNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONT_INFO,
            width=80
        )

        # The added note will be assigned to either Doctor's Notes or Nurse's notes depending on the type of user logged in
        if Data.System.getUserType() == 0:
            self.addNoteButton.configure(command=lambda: self.addDoctorNote(patient, self.note.get()))
        elif Data.System.getUserType() == 1:
            self.addNoteButton.configure(command=lambda: self.addNurseNote(patient, self.note.get()))
        self.addNoteButton.grid(row=1, column=1, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

    def addNurseNote(self, patient, nurseNote):
        patient.addNurseNote(nurseNote)
        try:
            Data.AddNewInfo.addNewInfo().updatePatient(patient, False)
        except:
            # don't add if not connected to db
            pass
        self.master.switchMedical()

    def addDoctorNote(self, patient, doctorNote):
        patient.addDoctorNote(doctorNote)
        try:
            Data.AddNewInfo.addNewInfo().updatePatient(patient, False)
        except:
            # don't add if not connected to db
            pass
        self.master.switchMedical()


class BillingInfoTab(ctk.CTkFrame):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget)

        self.nameFrame = ctk.CTkFrame(
            self
        )
        self.nameFrame.grid(row=0, column=0, columnspan=10, sticky="w", padx=PAD_SECTION, pady=PAD_SECTION)
        LabelBorder(self.nameFrame, "Name").grid(row=0, column=0, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)
        self.name = ctk.CTkLabel(
            self.nameFrame,
            text=patient.firstName + " " + patient.middleName + " " + patient.lastName,
            font=FONTNAME
        )
        self.name.grid(row=1, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        ctk.CTkButton(self.nameFrame, text="Print", font=("Arial", 20), command=lambda: Data.Printer.initPrint(3)).grid(
            row=0, column=1, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)

        self.insuranceFrame = ctk.CTkFrame(
            self
        )
        self.insuranceFrame.grid(row=1, column=0, sticky="w", padx=PAD_SECTION, pady=PAD_SECTION)
        LabelBorder(self.insuranceFrame, "Insurance Carrier").grid(row=0, column=0, sticky="w", padx=PAD_LABEL,
                                                                   pady=PAD_LABEL)
        self.insuranceName = ctk.CTkLabel(
            self.insuranceFrame,
            text=patient.insuranceCarrier,
            anchor="w",
            justify=ctk.LEFT,
            font=FONT_INFO
        )
        self.insuranceName.grid(row=1, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        self.policyInfoFrame = ctk.CTkFrame(
            self
        )
        self.policyInfoFrame.grid(row=2, column=0, sticky="w", padx=PAD_SECTION, pady=PAD_SECTION)
        LabelBorder(self.policyInfoFrame, "Insurance Policy Info").grid(row=0, column=0, sticky="w", padx=PAD_LABEL,
                                                                        pady=PAD_LABEL)
        self.policyInfo = ctk.CTkLabel(
            self.policyInfoFrame,
            text="Account Number: " + patient.insuranceAccountNumber + "\nGroup Number:   " + patient.insuranceGroupNumber,
            anchor="w",
            justify=ctk.LEFT,
            font=FONT_INFO
        )
        self.policyInfo.grid(row=1, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        self.amountPaidFrame = ctk.CTkFrame(
            self
        )
        self.amountPaidFrame.grid(row=3, column=0, sticky="w", padx=PAD_SECTION, pady=PAD_SECTION)
        LabelBorder(self.amountPaidFrame, "Amount Paid").grid(row=0, column=0, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)
        self.amountPaid = ctk.CTkLabel(
            self.amountPaidFrame,
            text="${:.2f}".format(patient.amountPaid),
            anchor="w",
            justify=ctk.LEFT,
            font=FONT_INFO
        )
        self.amountPaid.grid(row=1, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        self.amountPaidInsuranceFrame = ctk.CTkFrame(
            self
        )
        self.amountPaidInsuranceFrame.grid(row=4, column=0, sticky="w", padx=PAD_SECTION, pady=PAD_SECTION)
        LabelBorder(self.amountPaidInsuranceFrame, "Amount Paid By Insurance").grid(row=0, column=0, sticky="w",
                                                                                    padx=PAD_LABEL, pady=PAD_LABEL)
        self.amountPaidInsurance = ctk.CTkLabel(
            self.amountPaidInsuranceFrame,
            text="${:.2f}".format(patient.amountPaidByInsurance),
            anchor="w",
            justify=ctk.LEFT,
            font=FONT_INFO
        )
        self.amountPaidInsurance.grid(row=1, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        try:
            patient.updateAmountOwed()  # Update amount owed before printing it in GUI
        except:
            pass
        self.amountOwedFrame = ctk.CTkFrame(
            self
        )
        self.amountOwedFrame.grid(row=5, column=0, sticky="w", padx=PAD_SECTION, pady=PAD_SECTION)
        LabelBorder(self.amountOwedFrame, "Amount Owed").grid(row=0, column=0, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)
        self.amountOwed = ctk.CTkLabel(
            self.amountOwedFrame,
            text="${:.2f}".format(patient.amountOwed),
            anchor="w",
            justify=ctk.LEFT,
            font=FONT_INFO
        )
        self.amountOwed.grid(row=1, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        self.listChargesFrame = ctk.CTkFrame(
            self
        )
        self.listChargesFrame.grid(row=1, column=1, sticky="nw", padx=PAD_SECTION, pady=PAD_SECTION, rowspan=10)
        LabelBorder(self.listChargesFrame, "List of Charges").grid(row=0, column=0, sticky="w", padx=PAD_LABEL,
                                                                   pady=PAD_LABEL, columnspan=2)
        for i in range(len(patient.listCharges)):
            self.singleChargeFrame = ctk.CTkFrame(self.listChargesFrame)
            self.chargeName = ctk.CTkLabel(
                self.singleChargeFrame,
                text=patient.listCharges[i],
                anchor="w",
                justify=ctk.LEFT,
                wraplength=500,
                font=FONT_INFO
            )
            self.chargeName.grid(row=0, column=0, sticky="w", padx=PAD_COMP)
            self.chargeAmount = ctk.CTkLabel(
                self.singleChargeFrame,
                text="${:.2f}".format(patient.listChargesAmount[i]),
                anchor="e",
                justify=ctk.RIGHT,
                font=FONT_INFO
            )
            self.chargeAmount.grid(row=0, column=1, sticky="e", padx=10)
            self.singleChargeFrame.grid(row=i + 1, column=0, sticky="ew", padx=PAD_COMP, pady=PAD_COMP)
            self.singleChargeFrame.grid_columnconfigure(0, weight=1)


# Class to create a label with a border around it
# isList is a boolean flag to mark if the border is a list item, in which it should use the default INFO font
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
            self.label.configure(font=FONT_INFO)
            self.label.configure(wraplength=550)
        self.label.pack(padx=3)
