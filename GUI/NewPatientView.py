import re
import tkinter as tk
import tkinter.ttk as ttk

import customtkinter as ctk

import Data.System
import Data.ValidateInfo
import GUI.MainWindow as MainWindow
from Data.DataClasses import Patient

FONT_INFO = ("Courier", 18)
FONT_BUTTON = ("Courier", 20)
PAD_SECTION = 15
PAD_LABEL = 2
PAD_COMP = 3


class NewPatientView(ctk.CTkFrame):
    def __init__(self, parentWidget, user):
        super().__init__(parentWidget)

        self.NewPatient = Patient()

        # button to call the save function patient
        self.buttonFrame = ctk.CTkFrame(self)
        self.SaveButton = ctk.CTkButton(
            self.buttonFrame,
            text="Save Patient",
            font=FONT_BUTTON,
            width=100,
            height=40,
            command=lambda: finalizePatient(self, )
        )
        self.SaveButton.grid(row=0, column=4, padx=5, pady=5)

        # initialize all tabs to switch between them
        self.PersonalTab = PersonalInfoTab(self, self.NewPatient)
        self.MedicalTab = MedicalInfoTab(self, self.NewPatient)
        self.BillingTab = BillingInfoTab(self, self.NewPatient)
        # first tab shown will be the personal info tab
        self.shownTab = self.PersonalTab

        self.addNoteFrame = ctk.CTkFrame(
            self
        )
        # Create frame and buttons for switching tabs
        # Will need to set up later to only show relevant tabs based on which user is logged in.
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

        # button to return to the patent detailed view
        self.returnButton = ctk.CTkButton(
            self.buttonFrame,
            text="Back",
            font=FONT_BUTTON,
            width=100,
            height=40,
            command=lambda: MainWindow.switchPatientList(Data.System.getPatientList())
        )
        self.returnButton.grid(row=0, column=0, padx=5, pady=5)

        self.buttonFrame.grid(row=0, column=0, sticky="news", padx=8, pady=8)
        self.shownTab.grid(row=1, column=0, sticky="news")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

    # function that will allow the patient to be saved
    def turnOnSave(self):
        self.SaveButton.configure(state="normal")

    # function that will stop the patient from being able to be saved with invalid patient
    def turnOffSave(self):
        self.SaveButton.configure(state="disabled")

        # Functions to switch between the tabs using the buttons

    def switchPersonal(self):
        # Some tab buttons may not exist depending on the type of user logged in
        try:
            self.personalButton.configure(state="disabled")
        except (ValueError, NameError, AttributeError):
            pass
        try:
            self.medicalButton.configure(state="normal")
        except (ValueError, NameError, AttributeError):
            pass
        try:
            self.billingButton.configure(state="normal")
        except (ValueError, NameError, AttributeError):
            pass

        # Remove the previous tab to show the new one
        self.shownTab.grid_remove()
        self.shownTab = self.PersonalTab
        self.shownTab.grid(row=1, column=0, sticky="news")

    def switchMedical(self):
        # Some tab buttons may not exist depending on the type of user logged in
        try:
            self.personalButton.configure(state="normal")
        except (ValueError, NameError, AttributeError):
            pass
        try:
            self.medicalButton.configure(state="disabled")
        except (ValueError, NameError, AttributeError):
            pass
        try:
            self.billingButton.configure(state="normal")
        except (ValueError, NameError, AttributeError):
            pass

        # Remove the previous tab to show the new one
        self.shownTab.grid_remove()
        self.shownTab = self.MedicalTab
        self.shownTab.grid(row=1, column=0, sticky="news")

    def switchBilling(self):
        # Some tab buttons may not exist depending on the type of user logged in
        try:
            self.personalButton.configure(state="normal")
        except (ValueError, NameError, AttributeError):
            pass
        try:
            self.medicalButton.configure(state="normal")
        except (ValueError, NameError, AttributeError):
            pass
        try:
            self.billingButton.configure(state="disabled")
        except (ValueError, NameError, AttributeError):
            pass

        # Remove the previous tab to show the new one
        self.shownTab.grid_remove()
        self.shownTab = self.BillingTab
        self.shownTab.grid(row=1, column=0, sticky="news")


#############################################
# Tabs
#############################################


class PersonalInfoTab(ctk.CTkScrollableFrame):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget, orientation="horizontal")

        vcmd = (self.register(self.validatePhone), '%P', '%W')

        self.parentWidget = parentWidget

        # variables to know if each of the phone number entries are valid
        self.valid1 = True
        self.valid2 = True
        self.valid3 = True
        self.valid4 = True
        self.valid5 = True
        self.valid6 = True

        # error message for invalid phone number
        self.label_error = ttk.Label(self, foreground='red')
        self.label_error.grid(row=8, column=3, sticky=tk.W, padx=5)

        self.addNoteFrame = ctk.CTkFrame(
            self
        )
        # Entries for Personal Info Tab

        self.addNoteFrame.grid(row=1, column=2, sticky="nw", padx=PAD_SECTION, pady=PAD_SECTION)
        LabelBorder(self.addNoteFrame, "First Name Entry").grid(row=1, column=0, sticky="w", padx=PAD_LABEL,
                                                                pady=PAD_LABEL)
        self.FirstNameNote = ctk.StringVar()
        self.addFirstNameEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.FirstNameNote
        )
        self.addFirstNameEntry.grid(row=2, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Middle Name Entry").grid(row=3, column=0, sticky="w", padx=PAD_LABEL,
                                                                 pady=PAD_LABEL)
        self.MiddleNameNote = ctk.StringVar()
        self.addMiddleNameEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.MiddleNameNote
        )
        self.addMiddleNameEntry.grid(row=4, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Last Name Entry").grid(row=5, column=0, sticky="w", padx=PAD_LABEL,
                                                               pady=PAD_LABEL)
        self.LastNameNote = ctk.StringVar()
        self.addLastNameEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.LastNameNote
        )
        self.addLastNameEntry.grid(row=6, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Address Street Entry").grid(row=1, column=2, sticky="w", padx=PAD_LABEL,
                                                                    pady=PAD_LABEL)
        self.AddressStreetNote = ctk.StringVar()
        self.addAddressEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.AddressStreetNote
        )
        self.addAddressEntry.grid(row=2, column=2, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Address City Entry").grid(row=3, column=2, sticky="w", padx=PAD_LABEL,
                                                                  pady=PAD_LABEL)
        self.AddressCityNote = ctk.StringVar()
        self.addAddressEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.AddressCityNote
        )
        self.addAddressEntry.grid(row=4, column=2, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Address  State Entry").grid(row=5, column=2, sticky="w", padx=PAD_LABEL,
                                                                    pady=PAD_LABEL)
        self.AddressStateNote = ctk.StringVar()
        self.addAddressEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.AddressStateNote
        )
        self.addAddressEntry.grid(row=6, column=2, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Address Zip State Entry").grid(row=7, column=2, sticky="w", padx=PAD_LABEL,
                                                                       pady=PAD_LABEL)
        self.AddressZipNote = ctk.StringVar()
        self.addAddressEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.AddressZipNote
        )
        self.addAddressEntry.grid(row=8, column=2, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Mobile Phone Entry").grid(row=10, column=4, sticky="w", padx=PAD_LABEL,
                                                                  pady=PAD_LABEL)
        self.MobilePhoneNote = ctk.StringVar()
        self.addMobilePhoneEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            validate='focus',
            validatecommand=vcmd,
            width=350,
            textvariable=self.MobilePhoneNote
        )
        self.addMobilePhoneEntry.grid(row=11, column=4, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Home Phone Entry").grid(row=12, column=4, sticky="w", padx=PAD_LABEL,
                                                                pady=PAD_LABEL)
        self.HomePhoneNote = ctk.StringVar()
        self.addHomePhoneEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            validate='focus',
            validatecommand=vcmd,
            width=350,
            textvariable=self.HomePhoneNote
        )
        self.addHomePhoneEntry.grid(row=13, column=4, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Work Phone Entry").grid(row=14, column=4, sticky="w", padx=PAD_LABEL,
                                                                pady=PAD_LABEL)
        self.WorkPhoneNote = ctk.StringVar()
        self.addWorkPhoneEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            validate='focus',
            validatecommand=vcmd,
            width=350,
            textvariable=self.WorkPhoneNote
        )
        self.addWorkPhoneEntry.grid(row=15, column=4, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Emergency Contact 1 Name Entry").grid(row=8, column=0, sticky="w",
                                                                              padx=PAD_LABEL, pady=PAD_LABEL)
        self.EmergencyName1Note = ctk.StringVar()
        self.addEmergencyNameEntry1 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.EmergencyName1Note
        )
        self.addEmergencyNameEntry1.grid(row=9, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Emergency Phone Number 1 Entry").grid(row=10, column=0, sticky="w",
                                                                              padx=PAD_LABEL, pady=PAD_LABEL)
        self.EmergencyPhone1Note = ctk.StringVar()
        self.addEmergencyPhoneEntry1 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            validate='focus',
            validatecommand=vcmd,
            width=350,
            textvariable=self.EmergencyPhone1Note
        )
        self.addEmergencyPhoneEntry1.grid(row=11, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Emergency Contact 2 Name Entry").grid(row=12, column=0, sticky="w",
                                                                              padx=PAD_LABEL, pady=PAD_LABEL)
        self.EmergencyName2Note = ctk.StringVar()
        self.addEmergencyNameEntry2 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.EmergencyName2Note
        )
        self.addEmergencyNameEntry2.grid(row=13, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Emergency Phone Number 2 Entry").grid(row=14, column=0, sticky="w",
                                                                              padx=PAD_LABEL, pady=PAD_LABEL)
        self.EmergencyPhone2Note = ctk.StringVar()
        self.addEmergencyPhoneEntry2 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            validate='focus',
            validatecommand=vcmd,
            width=350,
            textvariable=self.EmergencyPhone2Note
        )
        self.addEmergencyPhoneEntry2.grid(row=15, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Emergency Contact 3 Name Entry").grid(row=16, column=0, sticky="w",
                                                                              padx=PAD_LABEL, pady=PAD_LABEL)
        self.EmergencyName3Note = ctk.StringVar()
        self.addEmergencyNameEntry3 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.EmergencyName3Note
        )
        self.addEmergencyNameEntry3.grid(row=17, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Emergency Phone Number 3 Entry").grid(row=18, column=0, sticky="w",
                                                                              padx=PAD_LABEL, pady=PAD_LABEL)
        self.EmergencyPhone3Note = ctk.StringVar()
        self.addEmergencyPhoneEntry3 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            validate='focus',
            validatecommand=vcmd,
            width=350,
            textvariable=self.EmergencyPhone3Note
        )
        self.addEmergencyPhoneEntry3.grid(row=19, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        # visitation
        LabelBorder(self.addNoteFrame, "Max Simultaneous Visitors").grid(row=10, column=2, sticky="w", padx=PAD_LABEL,
                                                                         pady=PAD_LABEL)
        self.MaxVisitorsNote = ctk.StringVar()
        self.addMaxVisitorsEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.MaxVisitorsNote
        )
        self.addMaxVisitorsEntry.grid(row=11, column=2, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Approved Visitor 1 Entry").grid(row=12, column=2, sticky="w", padx=PAD_LABEL,
                                                                       pady=PAD_LABEL)
        self.ApprovedVisitor1Note = ctk.StringVar()
        self.addApprovedVisitorEntry1 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.ApprovedVisitor1Note
        )
        self.addApprovedVisitorEntry1.grid(row=13, column=2, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Approved Visitor 2 Entry").grid(row=14, column=2, sticky="w", padx=PAD_LABEL,
                                                                       pady=PAD_LABEL)
        self.ApprovedVisitor2Note = ctk.StringVar()
        self.addApprovedVisitorEntry2 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.ApprovedVisitor2Note
        )

        self.addApprovedVisitorEntry2.grid(row=15, column=2, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Approved Visitor 3 Entry").grid(row=16, column=2, sticky="w", padx=PAD_LABEL,
                                                                       pady=PAD_LABEL)
        self.ApprovedVisitor3Note = ctk.StringVar()
        self.addApprovedVisitorEntry3 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.ApprovedVisitor3Note
        )
        self.addApprovedVisitorEntry3.grid(row=17, column=2, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        # Location
        LabelBorder(self.addNoteFrame, "Facility  Entry").grid(row=1, column=4, sticky="w", padx=PAD_LABEL,
                                                               pady=PAD_LABEL)
        self.FacilityNote = ctk.StringVar()
        self.addFacilityEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.FacilityNote
        )
        self.addFacilityEntry.grid(row=2, column=4, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Floor  Entry").grid(row=3, column=4, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)
        self.FloorNote = ctk.StringVar()
        self.addFloorEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.FloorNote
        )
        self.addFloorEntry.grid(row=4, column=4, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Room  Entry").grid(row=5, column=4, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)
        self.RoomNote = ctk.StringVar()
        self.addRoomEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.RoomNote
        )
        self.addRoomEntry.grid(row=6, column=4, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Bed  Entry").grid(row=7, column=4, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)
        self.BedNote = ctk.StringVar()
        self.addBedEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.BedNote
        )
        self.addBedEntry.grid(row=8, column=4, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

    # gets called when phone number entries are focused in or out
    # if invalid phone number, then call invalidPhone
    def validatePhone(self, value, entryName):
        """
        Validate the phone entry
        :param entryName:
        :param value:
        :return:
        """

        pattern = "^(\+\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$"
        if re.fullmatch(pattern, value) is None:
            self.invalidPhone(entryName)
            return False

        try:
            if entryName.find('8') > -1:
                self.valid1 = True
                self.addMobilePhoneEntry.configure(fg_color="white")
            if entryName.find('9') > -1:
                self.valid2 = True
                self.addHomePhoneEntry.configure(fg_color="white")
            if entryName.find('10') > -1:
                self.valid3 = True
                self.addWorkPhoneEntry.configure(fg_color="white")
            if entryName.find('12') > -1:
                self.valid4 = True
                self.addEmergencyPhoneEntry1.configure(fg_color="white")
            if entryName.find('14') > -1:
                self.valid5 = True
                self.addEmergencyPhoneEntry2.configure(fg_color="white")
            if entryName.find('16') > -1:
                self.valid6 = True
                self.addEmergencyPhoneEntry3.configure(fg_color="white")
        except AttributeError:
            pass
        self.label_error.configure(text="")
        # if all the phone numbers entries are valid then turn on the save button
        if self.valid1 is True and self.valid2 is True and self.valid3 is True and self.valid4 is True and self.valid5 is True and self.valid6 is True:
            self.parentWidget.turnOnSave()
        return True

    # called when a phone number entry is invalid
    # will turn off the save button and set the entry to red
    def invalidPhone(self, EntryName):
        self.label_error.configure(text="Please enter valid Phone Numbers")
        self.parentWidget.turnOffSave()
        try:
            if EntryName.find('8') > -1:
                self.valid1 = False
                self.addMobilePhoneEntry.configure(fg_color="red")
            if EntryName.find('9') > -1:
                self.valid2 = False
                self.addHomePhoneEntry.configure(fg_color="red")
            if EntryName.find('10') > -1:
                self.valid3 = False
                self.addWorkPhoneEntry.configure(fg_color="red")
            if EntryName.find('12') > -1:
                self.valid4 = False
                self.addEmergencyPhoneEntry1.configure(fg_color="red")
            if EntryName.find('14') > -1:
                self.valid5 = False
                self.addEmergencyPhoneEntry2.configure(fg_color="red")
            if EntryName.find('16') > -1:
                self.valid6 = False
                self.addEmergencyPhoneEntry3.configure(fg_color="red")
        except AttributeError:
            pass


class MedicalInfoTab(ctk.CTkScrollableFrame, ):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget, orientation="horizontal")

        self.addNoteFrame = ctk.CTkFrame(
            self
        )
        # medical tab info entries
        self.addNoteFrame.grid(row=3, column=2, sticky="nw", padx=PAD_SECTION, pady=PAD_SECTION)
        LabelBorder(self.addNoteFrame, "Family Doctor").grid(row=1, column=0, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)
        self.FamilyDoctorNote = ctk.StringVar()
        self.addFamilyDoctorEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.FamilyDoctorNote
        )
        self.addFamilyDoctorEntry.grid(row=2, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        self.addNoteFrame.grid(row=3, column=2, sticky="nw", padx=PAD_SECTION, pady=PAD_SECTION)
        LabelBorder(self.addNoteFrame, "Admittance Date").grid(row=3, column=0, sticky="w", padx=PAD_LABEL,
                                                               pady=PAD_LABEL)
        self.AdmittanceDateNote = ctk.StringVar()
        self.addAdmittanceDateEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.AdmittanceDateNote
        )
        self.addAdmittanceDateEntry.grid(row=4, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Admittance Time").grid(row=5, column=0, sticky="w", padx=PAD_LABEL,
                                                               pady=PAD_LABEL)
        self.AdmittanceTimeNote = ctk.StringVar()
        self.addAdmittanceTimeEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.AdmittanceTimeNote
        )
        self.addAdmittanceTimeEntry.grid(row=6, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Admittance Reason").grid(row=7, column=0, sticky="w", padx=PAD_LABEL,
                                                                 pady=PAD_LABEL)
        self.AdmittanceReasonNote = ctk.StringVar()
        self.AdmittanceReasonEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.AdmittanceReasonNote
        )
        self.AdmittanceReasonEntry.grid(row=8, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Discharge Date").grid(row=10, column=0, sticky="w", padx=PAD_LABEL,
                                                              pady=PAD_LABEL)
        self.DischargeDateNote = ctk.StringVar()
        self.addDischargeDateEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.DischargeDateNote
        )
        self.addDischargeDateEntry.grid(row=11, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Discharge Time").grid(row=13, column=0, sticky="w", padx=PAD_LABEL,
                                                              pady=PAD_LABEL)
        self.DischargeTimeNote = ctk.StringVar()
        self.addDischargeTimeEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.DischargeTimeNote
        )
        self.addDischargeTimeEntry.grid(row=14, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Prescription Medicine Name").grid(row=1, column=3, sticky="w", padx=PAD_LABEL,
                                                                          pady=PAD_LABEL)
        self.PrescriptionNameNote = ctk.StringVar()
        self.addPrescriptionNameEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.PrescriptionNameNote
        )
        self.addPrescriptionNameEntry.grid(row=2, column=3, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Prescriptions Amount").grid(row=4, column=3, sticky="w", padx=PAD_LABEL,
                                                                    pady=PAD_LABEL)
        self.PrescriptionAmountNote = ctk.StringVar()
        self.addPrescriptionAmountEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.PrescriptionAmountNote
        )
        self.addPrescriptionAmountEntry.grid(row=5, column=3, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Prescriptions Schedule").grid(row=7, column=3, sticky="w", padx=PAD_LABEL,
                                                                      pady=PAD_LABEL)
        self.PrescriptionScheduleNote = ctk.StringVar()
        self.addPrescriptionScheduleEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.PrescriptionScheduleNote
        )
        self.addPrescriptionScheduleEntry.grid(row=8, column=3, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Scheduled Procedures ").grid(row=10, column=3, sticky="w", padx=PAD_LABEL,
                                                                     pady=PAD_LABEL)
        self.ScheduledProceduresNote = ctk.StringVar()
        self.addScheduledProcedureEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.ScheduledProceduresNote
        )
        self.addScheduledProcedureEntry.grid(row=11, column=3, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Doctor  Notes ").grid(row=1, column=5, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)
        self.DoctornoteNote = ctk.StringVar()
        self.addDoctorNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.DoctornoteNote
        )
        self.addDoctorNoteEntry.grid(row=2, column=5, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Nurse  Notes ").grid(row=5, column=5, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)
        self.NursenoteNote = ctk.StringVar()
        self.addNurseNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.NursenoteNote
        )
        self.addNurseNoteEntry.grid(row=6, column=5, sticky="w", padx=PAD_COMP, pady=PAD_COMP)


class BillingInfoTab(ctk.CTkScrollableFrame):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget, orientation="horizontal")

        # valid command for only numbers in number entries
        vcmd = (parentWidget.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.addNoteFrame = ctk.CTkFrame(
            self
        )
        # entries for billing info tab
        self.addNoteFrame.grid(row=1, column=0, sticky="nw", padx=PAD_SECTION, pady=PAD_SECTION)
        LabelBorder(self.addNoteFrame, "Insurance Carrier").grid(row=1, column=0, sticky="w", padx=PAD_LABEL,
                                                                 pady=PAD_LABEL)
        self.InsuranceCarrierNote = ctk.StringVar()
        self.addInsuranceCarrierEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.InsuranceCarrierNote
        )
        self.addInsuranceCarrierEntry.grid(row=2, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Insurance Policy Account Number").grid(row=4, column=0, sticky="w",
                                                                               padx=PAD_LABEL, pady=PAD_LABEL)
        self.InsuranceAccountNumNote = ctk.StringVar()
        self.addInsurancePolicyAccountEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            validate='key',
            validatecommand=vcmd,
            width=350,
            textvariable=self.InsuranceAccountNumNote
        )
        self.addInsurancePolicyAccountEntry.grid(row=5, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Insurance Policy Group Number").grid(row=6, column=0, sticky="w", padx=PAD_LABEL,
                                                                             pady=PAD_LABEL)
        self.InsuranceGroupNumNote = ctk.StringVar()
        self.addInsuranceGroupEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            validatecommand=vcmd,
            width=350,
            textvariable=self.InsuranceGroupNumNote
        )
        self.addInsuranceGroupEntry.grid(row=7, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Charge").grid(row=1, column=4, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)
        self.ChargeNote = ctk.StringVar()
        self.addChargeEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            width=350,
            textvariable=self.ChargeNote
        )
        self.addChargeEntry.grid(row=2, column=4, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Charge Amount").grid(row=3, column=4, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)
        self.ChargeAmountNote = ctk.StringVar()
        self.addChargeAmountEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            validate='key',
            validatecommand=vcmd,
            width=350,
            textvariable=self.ChargeAmountNote
        )
        self.addChargeAmountEntry.grid(row=4, column=4, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        self.addChargeButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add Charge and Charge Amount",
            # command=lambda: [patient.addCharge("fsdf", self.ChargeAmountNote.get()), parentWidget.switchBilling()],
            command=lambda: self.addChargeNote(patient, self.ChargeNote.get(), self.ChargeAmountNote.get(),
                                               parentWidget),
            font=FONT_INFO,
            width=80
        )
        self.addChargeButton.grid(row=5, column=4, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Amount Paid").grid(row=8, column=4, sticky="w", padx=PAD_LABEL, pady=PAD_LABEL)
        self.AmountPaidNote = ctk.StringVar()
        self.addAmountPaidEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            validate='key',
            validatecommand=vcmd,
            width=350,
            textvariable=self.AmountPaidNote
        )
        self.addAmountPaidEntry.grid(row=9, column=4, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

        LabelBorder(self.addNoteFrame, "Amount paid by Insurance").grid(row=10, column=4, sticky="w", padx=PAD_LABEL,
                                                                        pady=PAD_LABEL)
        self.AmountPaidbyInsuranceNote = ctk.StringVar()
        self.addAmountPaidInsuranceEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONT_INFO,
            validate='key',
            validatecommand=vcmd,
            width=350,
            textvariable=self.AmountPaidbyInsuranceNote

        )
        self.addAmountPaidInsuranceEntry.grid(row=11, column=4, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

    # will refresh the charge table
    def addChargeRefresh(self, patient):
        self.chargesNoteFrame = ctk.CTkFrame(
            self
        )
        self.chargesNoteFrame.grid(row=1, column=6, sticky="nw", padx=PAD_SECTION, pady=PAD_SECTION)
        LabelBorder(self.chargesNoteFrame, "Charges and Amounts").grid(row=0, column=0, sticky="w", padx=PAD_LABEL,
                                                                       pady=PAD_LABEL)
        for i in range(len(patient.listCharges)):
            self.ChargesNote = LabelBorder(
                self.chargesNoteFrame,
                label=str(i + 1) + ".) " + patient.listCharges[i] + "    $" + str(patient.listChargesAmount[i]),
                isList=True
            )
            self.ChargesNote.grid(row=i + 1, column=0, sticky="w", padx=PAD_COMP, pady=PAD_COMP)

            # will add a charge and charge amount to the patient

    def addChargeNote(self, patient, chargeNote, chargesAmountNote, parentWidget):
        try:
            patient.addCharge(chargeNote, float(chargesAmountNote))
        except ValueError:
            pass
        self.addChargeRefresh(patient)

    # validation that will limit entries to only floats
    def validate(self, action, index, value_if_allowed,
                 prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

    # validation that will limit entries to only floats
    def validateFloat(self, action, index, value_if_allowed,
                      prior_value, text, validation_type, trigger_type, widget_name):
        # action=1 -> insert
        if action == '1':
            if text in ' 0123456789.-+':
                try:
                    float(value_if_allowed)
                    return True
                except ValueError:
                    return False
            else:
                return False
        else:
            return True

    # function that will take data from all the entry tabs and assign them to the patient


def finalizePatient(self):
    try:
        self.NewPatient.setFirstName(self.PersonalTab.FirstNameNote.get())
        self.NewPatient.setMiddleName(self.PersonalTab.MiddleNameNote.get())
        self.NewPatient.setLastname(self.PersonalTab.LastNameNote.get())

        address = [self.PersonalTab.AddressStreetNote.get(), self.PersonalTab.AddressCityNote.get(),
                   self.PersonalTab.AddressStateNote.get(), self.PersonalTab.AddressZipNote.get()]
        self.NewPatient.setAddress(address)

        self.NewPatient.setHomePhone(self.PersonalTab.HomePhoneNote.get())
        self.NewPatient.setWorkPhone(self.PersonalTab.WorkPhoneNote.get())
        self.NewPatient.setMobilePhone(self.PersonalTab.MobilePhoneNote.get())

        if self.PersonalTab.EmergencyName1Note.get() != "":
            self.NewPatient.addEmergencyContact(self.PersonalTab.EmergencyName1Note.get(),
                                                self.PersonalTab.EmergencyPhone1Note.get())
        if self.PersonalTab.EmergencyName2Note.get() != "":
            self.NewPatient.addEmergencyContact(self.PersonalTab.EmergencyName2Note.get(),
                                                self.PersonalTab.EmergencyPhone2Note.get())
        if self.PersonalTab.EmergencyName3Note.get() != "":
            self.NewPatient.addEmergencyContact(self.PersonalTab.EmergencyName3Note.get(),
                                                self.PersonalTab.EmergencyPhone3Note.get())

        Location = [self.PersonalTab.FacilityNote.get(), self.PersonalTab.FloorNote.get(),
                    self.PersonalTab.RoomNote.get(), self.PersonalTab.BedNote.get()]
        self.NewPatient.setLocation(Location)

        self.NewPatient.setNumAllowedVisitors(self.PersonalTab.MaxVisitorsNote.get())

        if self.PersonalTab.ApprovedVisitor1Note.get() != "":
            self.NewPatient.addAllowedVisitor(self.PersonalTab.ApprovedVisitor1Note.get())
        if self.PersonalTab.ApprovedVisitor1Note.get() != "":
            self.NewPatient.addAllowedVisitor(self.PersonalTab.ApprovedVisitor2Note.get())
        if self.PersonalTab.ApprovedVisitor1Note.get() != "":
            self.NewPatient.addAllowedVisitor(self.PersonalTab.ApprovedVisitor3Note.get())

    except (ValueError, NameError, AttributeError):
        pass

    try:
        self.NewPatient.setDateAdmittance(self.MedicalTab.AdmittanceDateNote.get())
        self.NewPatient.setTimeAdmittance(self.MedicalTab.AdmittanceTimeNote.get())
        self.NewPatient.setReasonAdmission(self.MedicalTab.AdmittanceReasonNote.get())

        self.NewPatient.setFamilyDoctor(self.MedicalTab.FamilyDoctorNote.get())

        self.NewPatient.setDateDischarge(self.MedicalTab.DischargeDateNote.get())
        self.NewPatient.setTimeDischarge(self.MedicalTab.DischargeTimeNote.get())

        self.NewPatient.addDoctorNote(self.MedicalTab.DoctornoteNote.get())
        self.NewPatient.addNurseNote(self.MedicalTab.NursenoteNote.get())

        self.NewPatient.addPrescription(self.MedicalTab.PrescriptionNameNote.get(),
                                        self.MedicalTab.PrescriptionAmountNote.get(),
                                        self.MedicalTab.PrescriptionScheduleNot.get())

        self.NewPatient.addScheduledProcedure(self.MedicalTab.ScheduledProceduresNote.get())
    except (ValueError, NameError, AttributeError):
        pass

    try:
        self.NewPatient.setInsuranceCarrier(self.BillingTab.InsuranceCarrierNote.get())
        self.NewPatient.setInsuranceAccountNumber(self.BillingTab.InsuranceAccountNumNote.get())
        self.NewPatient.setInsuranceGroupNumber(self.BillingTab.InsuranceGroupNumNote.get())

        self.NewPatient.setAmountPaid(float(self.BillingTab.AmountPaidNote.get()))
        self.NewPatient.updateAmountOwed()

        self.NewPatient.setAmountPaidByInsurance(float(self.BillingTab.AmountPaidByInsuranceNote.get()))
    except (ValueError, NameError, AttributeError):
        pass

        # ensure no information exceeds database character limit
    validate = Data.ValidateInfo.ValidateInfo()
    validate.checkEntry(self.NewPatient)
    truthValid, strIssue = validate.checkValidity(self.NewPatient, True)
    if not truthValid:
        if hasattr(self, 'invalidLabel'):
            self.invalidLabel.destroy()
        self.invalidLabel = ctk.CTkLabel(self, text=strIssue, font=("Courier", 18, "bold"))
        self.invalidLabel.place(relx=0.5, rely=0.11, anchor='center')
    else:
        Data.System.getPatientList().append(self.NewPatient)
        MainWindow.switchPatientList(Data.System.getPatientList())


# except AttributeError or NameError:
# pass
# try:
# self.patientRecords.append(self.NewPatient)
# except AttributeError or NameError:
# pass


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