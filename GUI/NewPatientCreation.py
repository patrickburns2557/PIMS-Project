import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk
import GUI.ScrollablePatientList as spl
import Data.System
import GUI.MainWindow as MainWindow
from Data.dataClasses import Patient

FONTINFO = ("Courier", 18)
FONTINFOOLD = ("Courier")
FONTBUTTON = ("Courier", 20)
PADSECTION = 15
PADLABEL = 2
PADCOMP = 3

class NewPatientView(ctk.CTkFrame):
    def __init__(self, parentWidget, user):
        super().__init__(parentWidget)
        
        self.NewPatient = Patient()
        
        
         #first tab shown will be the personal info tab
        self.shownTab = PersonalInfoTab(self, self.NewPatient)
        
        
        
        self.addNoteFrame = ctk.CTkFrame(
            self
        )
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
        self.personalButton.grid(row=0, column=1, padx=5, pady=5)

        #Only show the medical tab to Doctor and Nurse user types
        if Data.System.getUserType() == 0 or Data.System.getUserType() == 1:
            self.medicalButton = ctk.CTkButton(
                self.buttonFrame,
                text="Medical Information",
                command=lambda:self.switchMedical(),
                font=FONTBUTTON,
                width=270,
                height=40,
            )
            self.medicalButton.grid(row=0, column=2, padx=5, pady=5)
        
        #Only show billing tab for Doctor, Nurse, and Office Staff user types
        if Data.System.getUserType() == 0 or Data.System.getUserType() == 1 or Data.System.getUserType() == 2:
            self.billingButton = ctk.CTkButton(
                self.buttonFrame,
                text="Billing Information",
                command=lambda:self.switchBilling(),
                font=FONTBUTTON,
                width=270,
                height=40,
            )
            self.billingButton.grid(row=0, column=3, padx=5, pady=5)

        self.returnButton = ctk.CTkButton(
            self.buttonFrame,
            text="Back",
            font=FONTBUTTON,
            width=100,
            height=40,
            command=lambda:MainWindow.switchPatientList(Data.System.getPatientList())
       )
        self.returnButton.grid(row=0, column=0, padx=5, pady=5)
    
    
        self.buttonFrame.grid(row=0, column=0, sticky="news", padx=8, pady=8)
        self.shownTab.grid(row=1, column=0, sticky="news")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        
    #Functions to switch between the tabs using the buttons
    def switchPersonal(self):
        #Some tab buttons may not exist depending on the type of user logged in
        try:
            self.personalButton.configure(state="disabled")
        except AttributeError or NameError:
            pass
        try:
            self.medicalButton.configure(state="normal")
        except AttributeError or NameError:
            pass
        try:
            self.billingButton.configure(state="normal")
        except AttributeError or NameError:
            pass
        
        #Destroy the current tab before loading the new one
        for i in self.shownTab.winfo_children():
            i.destroy()
        self.shownTab.destroy()

        self.shownTab = PersonalInfoTab(self, self.NewPatient)
        self.shownTab.grid(row=1, column=0, sticky="news")



    def switchMedical(self):
        #Some tab buttons may not exist depending on the type of user logged in
        try:
            self.personalButton.configure(state="normal")
        except AttributeError or NameError:
            pass
        try:
            self.medicalButton.configure(state="disabled")
        except AttributeError or NameError:
            pass
        try:
            self.billingButton.configure(state="normal")
        except AttributeError or NameError:
            pass

        #Destroy the current tab before loading the new one
        for i in self.shownTab.winfo_children():
            i.destroy()
        self.shownTab.destroy()

        self.shownTab = MedicalInfoTab(self, self.NewPatient)
        self.shownTab.grid(row=1, column=0, sticky="news")



    def switchBilling(self):
        #Some tab buttons may not exist depending on the type of user logged in
        try:
            self.personalButton.configure(state="normal")
        except AttributeError or NameError:
            pass
        try:
            self.medicalButton.configure(state="normal")
        except AttributeError or NameError:
            pass
        try:
            self.billingButton.configure(state="disabled")
        except AttributeError or NameError:
            pass

        #Destroy the current tab before loading the new one
        for i in self.shownTab.winfo_children():
            i.destroy()
        self.shownTab.destroy()
        
        self.shownTab = BillingInfoTab(self, self.NewPatient)
        self.shownTab.grid(row=1, column=0, sticky="news")
        
        
#############################################
# Tabs
#############################################


class PersonalInfoTab(ctk.CTkFrame):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget)
        
        self.addNoteFrame = ctk.CTkFrame(
            self
        )
        self.addNoteFrame.grid(row=1, column=2, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.addNoteFrame, "First Name Entry").grid(row=1, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addFirstNameEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addFirstNameEntry.grid(row=2, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addFirstNameButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )
        
        self.addFirstNameButton.configure(command=lambda: self.addFirstName(patient, self.note.get()))
        self.addFirstNameButton.grid(row=2, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        LabelBorder(self.addNoteFrame, "Middle Name Entry").grid(row=3, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addMiddleNameEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addMiddleNameEntry.grid(row=4, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addMiddleNameButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )
        
        self.addMiddleNameButton.configure(command=lambda: self.addMiddleName(patient, self.note.get()))
        self.addMiddleNameButton.grid(row=4, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
            #self.addNoteFrame.grid(row=4, column=2, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.addNoteFrame, "Last Name Entry").grid(row=5, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addLastNameEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addLastNameEntry.grid(row=6, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addLastNameButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )
        
        self.addLastNameButton.configure(command=lambda: self.addLastName(patient, self.note.get()))
        self.addLastNameButton.grid(row=6, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        
        LabelBorder(self.addNoteFrame, "Address Entry").grid(row=1, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addAddressEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addAddressEntry.grid(row=2, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addAddressButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )
        
        self.addAddressButton.configure(command=lambda: self.addAddress(patient, self.note.get()))
        self.addAddressButton.grid(row=2, column=3, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        
        LabelBorder(self.addNoteFrame, "Mobile Phone Entry").grid(row=10, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addMobilePhoneEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addMobilePhoneEntry.grid(row=11, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addMobilePhoneButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )   
        
        self.addMobilePhoneButton.configure(command=lambda: self.addMobilePhone(patient, self.note.get()))
        self.addMobilePhoneButton.grid(row=11, column=5, sticky="w", padx=PADCOMP, pady=PADCOMP)
             
        
        LabelBorder(self.addNoteFrame, "Home Phone Entry").grid(row=12, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addHomePhoneEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addHomePhoneEntry.grid(row=13, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addHomePhoneButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )  
        self.addHomePhoneButton.configure(command=lambda: self.addHomePhone(patient, self.note.get()))
        self.addHomePhoneButton.grid(row=13, column=5, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
                
        LabelBorder(self.addNoteFrame, "Work Phone Entry").grid(row=14, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addWorkPhoneEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addWorkPhoneEntry.grid(row=15, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addWorkPhoneButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )  
        self.addWorkPhoneButton.configure(command=lambda: self.addWorkPhone(patient, self.note.get()))
        self.addWorkPhoneButton.grid(row=15, column=5, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        
        LabelBorder(self.addNoteFrame, "Emergency Contact 1 Name Entry").grid(row=8, column = 0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addEmergencyNameEntry1 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addEmergencyNameEntry1.grid(row=9, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addEmergencyNameButton1 = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )  
        
        self.addEmergencyNameButton1.configure(command=lambda: self.addEmergencyContact(patient, self.note.get()))
        self.addEmergencyNameButton1.grid(row=9, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        LabelBorder(self.addNoteFrame, "Emergency Phone Number 1 Entry").grid(row=10, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addEmergencyPhoneEntry1 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addEmergencyPhoneEntry1.grid(row=11, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addEmergencyPhoneButton1 = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )  
        self.addEmergencyPhoneButton1.configure(command=lambda: self.addEmergencyContact(patient, self.note.get()))
        self.addEmergencyPhoneButton1.grid(row=11, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        
        LabelBorder(self.addNoteFrame, "Emergency Contact 2 Name Entry").grid(row=12, column = 0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addEmergencyNameEntry2 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addEmergencyNameEntry2.grid(row=13, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addEmergencyNameButton2 = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )  
        self.addEmergencyNameButton2.configure(command=lambda: self.addEmergencyContact(patient, self.note.get()))
        self.addEmergencyNameButton2.grid(row=13, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        
        LabelBorder(self.addNoteFrame, "Emergency Phone Number 2 Entry").grid(row=14, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addEmergencyPhoneEntry2 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addEmergencyPhoneEntry2.grid(row=15, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addEmergencyPhoneButton2 = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        ) 
        
        self.addEmergencyPhoneButton2.configure(command=lambda: self.addEmergencyContact(patient, self.note.get()))
        self.addEmergencyPhoneButton2.grid(row=15, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        
        LabelBorder(self.addNoteFrame, "Emergency Contact 3 Name Entry").grid(row=16, column = 0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addEmergencyNameEntry3 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addEmergencyNameEntry3.grid(row=17, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addEmergencyNameButton3 = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )  
        self.addEmergencyNameButton3.configure(command=lambda: self.addEmergencyContact(patient, self.note.get()))
        self.addEmergencyNameButton3.grid(row=17, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        LabelBorder(self.addNoteFrame, "Emergency Phone Number 3 Entry").grid(row=18, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addEmergencyPhoneEntry3 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addEmergencyPhoneEntry3.grid(row=19, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addEmergencyPhoneButton3 = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )               
        self.addEmergencyPhoneButton3.configure(command=lambda: self.addEmergencyContact(patient, self.note.get()))
        self.addEmergencyPhoneButton3.grid(row=19, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        
        #vistation
        LabelBorder(self.addNoteFrame, "Max Simalataneous Visitors").grid(row=5, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addMaxVisitorsEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addMaxVisitorsEntry.grid(row=6, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addMaxVisitorsButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )    
        
        self.addMaxVisitorsButton.configure(command=lambda: self.addMaxVisitors(patient, self.note.get()))
        self.addMaxVisitorsButton.grid(row=6, column=3, sticky="w", padx=PADCOMP, pady=PADCOMP)

        LabelBorder(self.addNoteFrame, "Approved Vistor 1 Entry").grid(row=7, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addAprovedVisitorEntry1 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addAprovedVisitorEntry1.grid(row=8, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addApprovedVisitorButton1 = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )   
        
        self.addApprovedVisitorButton1.configure(command=lambda: self.addAllowedVisitor(patient, self.note.get()))
        self.addApprovedVisitorButton1.grid(row=8, column=3, sticky="w", padx=PADCOMP, pady=PADCOMP)
         
        LabelBorder(self.addNoteFrame, "Approved Vistor 2 Entry").grid(row=9, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addAprovedVisitorEntry2 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        
        
        self.addAprovedVisitorEntry2.grid(row=10, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addApprovedVisitorButton2 = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )         
        
        self.addApprovedVisitorButton2.configure(command=lambda: self.addAllowedVisitor(patient, self.note.get()))
        self.addApprovedVisitorButton2.grid(row=10, column=3, sticky="w", padx=PADCOMP, pady=PADCOMP)
                
        LabelBorder(self.addNoteFrame, "Approved Vistor 3 Entry").grid(row=11, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addAprovedVisitorEntry3 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addAprovedVisitorEntry3.grid(row=12, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addAprovedVisitorEntry3 = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )          
        self.addAprovedVisitorEntry3.configure(command=lambda: self.addAllowedVisitor(patient, self.note.get()))
        self.addAprovedVisitorEntry3.grid(row=12, column=3, sticky="w", padx=PADCOMP, pady=PADCOMP)
         
        #Location  
        LabelBorder(self.addNoteFrame, "Facility  Entry").grid(row=1, column=5, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addFacililtyEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addFacililtyEntry.grid(row=2, column=5, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addFacililtyButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )    
        
        self.addFacililtyButton.configure(command=lambda: self.addLocation(patient, self.note.get()))
        self.addFacililtyButton.grid(row=2, column=6, sticky="w", padx=PADCOMP, pady=PADCOMP)
                         
        LabelBorder(self.addNoteFrame, "Floor  Entry").grid(row=3, column=5, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addFloorEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addFloorEntry.grid(row=4, column=5, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addFloorButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )           
        
        self.addFloorButton.configure(command=lambda: self.addLocation(patient, self.note.get()))
        self.addFloorButton.grid(row=4, column=6, sticky="w", padx=PADCOMP, pady=PADCOMP)
                 
        LabelBorder(self.addNoteFrame, "Room  Entry").grid(row=5, column=5, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addRoomEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addRoomEntry.grid(row=6, column=5, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addRoomButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )               
        
        self.addRoomButton.configure(command=lambda: self.addLocation(patient, self.note.get()))
        self.addRoomButton.grid(row=6, column=6, sticky="w", padx=PADCOMP, pady=PADCOMP)
             
        LabelBorder(self.addNoteFrame, "Bed  Entry").grid(row=7, column=5, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addBedEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addBedEntry.grid(row=8, column=5, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addBedButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )  
        
        self.addBedButton.configure(command=lambda: self.addLocation(patient, self.note.get()))
        self.addBedButton.grid(row=8, column=6, sticky="w", padx=PADCOMP, pady=PADCOMP)
                               
                                                                            
    def addFirstName(self, patient,FirstName):
        patient.setFirstName(FirstName)
        
    def addMiddleName(self, patient,MiddleName):
        patient.setMiddleName(MiddleName)
        
    def addLastName(self, patient,LastName):
        patient.setLastName(LastName)
        
    def addAddress(self, patient,Address):
        patient.setAddress(Address)
        
    def addHomePhone(self, patient,HomePhone):
        patient.setHomePhone(HomePhone)
        
    def addWorkPhone(self, patient,WorkPhone):
        patient.setWorkPhone(WorkPhone)
        
    def addEmergencyContact(self, patient,EmergencyContact):
        patient.setFirstName(EmergencyContact)
        
    def addMaxVisitors(self, patient,NumAllowedVisitor):
        patient.setNumAllowedVisitors(NumAllowedVisitor)
   
    def addAllowedVisitor(self, patient,Visitor):
        patient.addAllowedVisitor(Visitor)
        
    def addLocation(self, patient,Location):
        patient.setLocation(Location)
        
class MedicalInfoTab(ctk.CTkFrame):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget)
        
        
        self.addNoteFrame = ctk.CTkFrame(
            self
        )
        self.addNoteFrame.grid(row=3, column=2, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.addNoteFrame, "Family Doctor").grid(row=1, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addFamilyDoctorEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addFamilyDoctorEntry.grid(row=2, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addFamilyDoctorButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )   
        self.addFamilyDoctorButton.configure(command=lambda: self.addFamilyDoctor(patient, self.note.get()))
        self.addFamilyDoctorButton.grid(row=2, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)

        self.addNoteFrame.grid(row=3, column=2, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.addNoteFrame, "Admittance Date").grid(row=3, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addAdmittanceDateEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addAdmittanceDateEntry.grid(row=4, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addAdmitanceDateButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )
        self.addAdmitanceDateButton.configure(command=lambda: self.addAdmitanceDate(patient, self.note.get()))
        self.addAdmitanceDateButton.grid(row=4, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)     

        LabelBorder(self.addNoteFrame, "Admittance Time").grid(row=5, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addAdmitanceTimeEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addAdmitanceTimeEntry.grid(row=6, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addAdmitanceTimeButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )
        self.addAdmitanceTimeButton.configure(command=lambda: self.addAdmitanceTime(patient, self.note.get()))
        self.addAdmitanceTimeButton.grid(row=6, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)    
        
        LabelBorder(self.addNoteFrame, "Admittance Reason").grid(row=7, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.AdmitanceReasonEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.AdmitanceReasonEntry.grid(row=8, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addAdmitanceReasonButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )
        
        self.addAdmitanceReasonButton.configure(command=lambda: self.addAdmitanceReasonButton(patient, self.note.get()))
        self.addAdmitanceReasonButton.grid(row=8, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)   
        
        LabelBorder(self.addNoteFrame, "Discharge Date").grid(row=10, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addDischargeDateEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addDischargeDateEntry.grid(row=11, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addDischargeDateButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )
        
        self.addDischargeDateButton.configure(command=lambda: self.addDischargeDate(patient, self.note.get()))
        self.addDischargeDateButton.grid(row=11, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)   
        
        LabelBorder(self.addNoteFrame, "Discharge Time").grid(row=13, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addDischargeTimeEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addDischargeTimeEntry.grid(row=14, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addDischargeTimeButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )
        
        self.addDischargeTimeButton.configure(command=lambda: self.addDischargeTime(patient, self.note.get()))
        self.addDischargeTimeButton.grid(row=14, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP) 
        
        LabelBorder(self.addNoteFrame, "Prescription Medicine Name").grid(row=1, column=3, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addPrescriptionNameEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addPrescriptionNameEntry.grid(row=2, column=3, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addPrescriptionNameButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )
        
        self.addPrescriptionNameButton.configure(command=lambda: self.addPrescriptionName(patient, self.note.get()))
        self.addPrescriptionNameButton.grid(row=2, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP) 
        
        LabelBorder(self.addNoteFrame, "Prescriptions Amount").grid(row=4, column=3, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addPrescriptionAmountEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addPrescriptionAmountEntry.grid(row=5, column=3, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addPrescriptionAmountButton   = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )
        
        self.addPrescriptionAmountButton.configure(command=lambda: self.addPrescriptionAmount(patient, self.note.get()))
        self.addPrescriptionAmountButton.grid(row=5, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP) 
        

        
        LabelBorder(self.addNoteFrame, "Prescriptions Schedule").grid(row=7, column=3, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addPrescriptionScheduleEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addPrescriptionScheduleEntry.grid(row=8, column=3, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addPrescriptionEntryButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )
        
        self.addPrescriptionEntryButton.configure(command=lambda: self.addPrescriptionEntry(patient, self.note.get()))
        self.addPrescriptionEntryButton.grid(row=8, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP) 
        
        LabelBorder(self.addNoteFrame, "Scheduled Procedures ").grid(row=10, column=3, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addScheduledProcedureEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addScheduledProcedureEntry.grid(row=11, column=3, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addScheduledProcedureButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )
        self.addScheduledProcedureButton.configure(command=lambda: self.addPrescriptionButton(patient, self.note.get()))
        self.addScheduledProcedureButton.grid(row=11, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP) 
        
        LabelBorder(self.addNoteFrame, "Doctor  Notes ").grid(row=1, column=5, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addDoctorNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addDoctorNoteEntry.grid(row=2, column=5, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addDoctorNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )
        self.addDoctorNoteButton.configure(command=lambda: self.addDoctorNote(patient, self.note.get()))
        self.addDoctorNoteButton.grid(row=2, column=6, sticky="w", padx=PADCOMP, pady=PADCOMP) 
        
        LabelBorder(self.addNoteFrame, "Nurse  Notes ").grid(row=5, column=5, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addNurseNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addNurseNoteEntry.grid(row=6, column=5, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNurseNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )
        self.addNurseNoteButton.configure(command=lambda: self.addNurseNote(patient, self.note.get()))
        self.addNurseNoteButton.grid(row=6, column=6, sticky="w", padx=PADCOMP, pady=PADCOMP) 


    def addDateAdmittance(self, patient,DateAdmin):
        patient.setDateAdmittance(DateAdmin)
        
    def addTimeAdmitance(self, patient,TimeAdmitance):
        patient.setTimeAdmittance(TimeAdmitance)
        
    def addDateDischarge(self, patient,DateDischarge):
        patient.setDateDischarge(DateDischarge)
        
    def addTimeDischarge(self, patient,TimeDischarge):
        patient.setTimeDischarge(TimeDischarge)
        
    def addPrescriptionName(self, patient,PrescriptionName):
        patient.addPrescription(PrescriptionName)
        
    def addPrescriptionSchedule(self, patient,PrescriptionSchedule):
        patient.addPrescription(PrescriptionSchedule)
        
    def addDoctorNote(self, patient,DoctorNote):
        patient.addDoctorNote(DoctorNote)
        
    def addNurseNote(self, patient,NurseNote):
        patient.addNurseNote(NurseNote)
        
    def addScheduledProcedure(self, patient,ScheduledProcedure):
        patient.addScheduledProcedure(ScheduledProcedure)
        
class BillingInfoTab(ctk.CTkFrame):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget)
        
        
        self.addNoteFrame = ctk.CTkFrame(
            self
        )
        self.addNoteFrame.grid(row=1, column=0, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.addNoteFrame, "Insurance Carrier").grid(row=1, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addInsuranceCarrierEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addInsuranceCarrierEntry.grid(row=2, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addInsuranceCarrierButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )   
        
        self.addInsuranceCarrierButton.configure(command=lambda: self.addInsuranceCarrier(patient, self.note.get()))
        self.addInsuranceCarrierButton.grid(row=2, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP) 

        
        LabelBorder(self.addNoteFrame, "Insurance Policy Account Number").grid(row=4, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addInsurancePolicyAccountEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addInsurancePolicyAccountEntry.grid(row=5, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addInsurancePolicyAccountButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        ) 
        
        self.addInsurancePolicyAccountButton.configure(command=lambda: self.addInsurancePolicyAccount(patient, self.note.get()))
        self.addInsurancePolicyAccountButton.grid(row=5, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP) 
 
        
        LabelBorder(self.addNoteFrame, "Insurance Policy Group Number").grid(row=6, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addInsuranceGroupEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addInsuranceGroupEntry.grid(row=7, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addInsuranceGroupButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )  
        
        self.addInsuranceGroupButton.configure(command=lambda: self.addNurseNote(patient, self.note.get()))
        self.addInsuranceGroupButton.grid(row=7, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP) 
  
        
        LabelBorder(self.addNoteFrame, "Amount  Paid").grid(row=9, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addAmountPaidEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addAmountPaidEntry.grid(row=10, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addAmountPaidButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )   

        self.addAmountPaidButton.configure(command=lambda: self.addAmountPaid(patient, self.note.get()))
        self.addAmountPaidButton.grid(row=10, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP) 
 

        LabelBorder(self.addNoteFrame, "Amount  Owed").grid(row=12, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addAmountOwedEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addAmountOwedEntry.grid(row=13, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addAmountOwedButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )   

        self.addAmountOwedButton.configure(command=lambda: self.addAmountOwed(patient, self.note.get()))
        self.addAmountOwedButton.grid(row=13, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP) 
 

        LabelBorder(self.addNoteFrame, "Add a chargeOwed").grid(row=1, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addChargeOwedEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addChargeOwedEntry.grid(row=2, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addChargeOwedButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        ) 
        self.addChargeOwedButton.configure(command=lambda: self.addChargeOwed(patient, self.note.get()))
        self.addChargeOwedButton.grid(row=2, column=5, sticky="w", padx=PADCOMP, pady=PADCOMP) 
 
    def addInsuranceCarrier(self, patient,InsuranceCarrier):
        patient.setInsuranceCarrier(InsuranceCarrier)
        
    def addInsuranceAccountNumber(self, patient,InsuranceAccountNumber):
        patient.setInsuranceAccountNumber(InsuranceAccountNumber)

    def addInsuranceGroupNumber(self, patient,InsuranceGroupNumber):
        patient.setInsuranceGroupNumber(InsuranceGroupNumber)
        
    def addAmmountPaid(self, patient,AmountPaid):
        patient.setAmountPaid(AmountPaid)
        
    def addAmountPaidByInsurance(self, patient,AmountPaidByInsurance):
        patient.setAmountPaidByInsurance(AmountPaidByInsurance)
        
    def addChargeOwed(self, patient,Charge):
        patient.addCharge(Charge)
 
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