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

class EditPatientView(ctk.CTkFrame):
    def __init__(self, parentWidget, user, CurrentPatient):
        super().__init__(parentWidget)
        
        #self.NewPatient = Patient()
        
        
         #first tab shown will be the personal info tab
        self.shownTab = PersonalInfoTab(self, CurrentPatient)
        
        
        
        self.addNoteFrame = ctk.CTkFrame(
            self
        )
        #Create frame and buttons for switching tabs
        #Will need to setup later to only show relavant tabs based on which user is logged in.
        self.buttonFrame = ctk.CTkFrame(self)
        self.personalButton = ctk.CTkButton(
            self.buttonFrame,
            text="Personal Information",
            command=lambda:self.switchPersonal(CurrentPatient),
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
                command=lambda:self.switchMedical(CurrentPatient),
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
                command=lambda:self.switchBilling(CurrentPatient),
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
    def switchPersonal(self, CurrentPatient):
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

        self.shownTab = PersonalInfoTab(self, CurrentPatient)
        self.shownTab.grid(row=1, column=0, sticky="news")



    def switchMedical(self,CurrentPatient):
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

        self.shownTab = MedicalInfoTab(self, CurrentPatient)
        self.shownTab.grid(row=1, column=0, sticky="news")



    def switchBilling(self, CurrentPatient):
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
        
        self.shownTab = BillingInfoTab(self, CurrentPatient)
        self.shownTab.grid(row=1, column=0, sticky="news")
        
        
#############################################
# Tabs
#############################################


class PersonalInfoTab(ctk.CTkScrollableFrame):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget, orientation= "horizontal")
        
        self.addNoteFrame = ctk.CTkFrame(
            self
        )
        self.addNoteFrame.grid(row=1, column=2, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.addNoteFrame, "First Name Entry").grid(row=1, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.firstnamenote   = ctk.StringVar(value = patient.firstName)
        self.addFirstNameEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable = self.firstnamenote
        )
        self.addFirstNameEntry.grid(row=2, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addFirstNameButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )
        
        self.addFirstNameButton.configure(command=lambda: self.addFirstName(patient, self.firstnamenote.get()))
        self.addFirstNameButton.grid(row=2, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        LabelBorder(self.addNoteFrame, "Middle Name Entry").grid(row=3, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.MiddleNameNote = ctk.StringVar(value = patient.middleName)
        self.addMiddleNameEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.MiddleNameNote
        )
        self.addMiddleNameEntry.grid(row=4, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addMiddleNameButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )
        
        self.addMiddleNameButton.configure(command=lambda: self.addMiddleName(patient, self.MiddleNameNote.get()))
        self.addMiddleNameButton.grid(row=4, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
            #self.addNoteFrame.grid(row=4, column=2, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.addNoteFrame, "Last Name Entry").grid(row=5, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.lastNameNote   = ctk.StringVar(value = patient.lastName)
        self.addLastNameEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.lastNameNote
        )
        self.addLastNameEntry.grid(row=6, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addLastNameButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )
        
        self.addLastNameButton.configure(command=lambda: self.addLastName(patient, self.lastNameNote.get()))
        self.addLastNameButton.grid(row=6, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        
        LabelBorder(self.addNoteFrame, "Address Entry").grid(row=1, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.AddressNote   = ctk.StringVar(value = patient.address)
        self.addAddressEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.AddressNote
        )
        self.addAddressEntry.grid(row=2, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addAddressButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )
        
        self.addAddressButton.configure(command=lambda: self.addAddress(patient, self.noAddressNotete.get()))
        self.addAddressButton.grid(row=2, column=3, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        
        LabelBorder(self.addNoteFrame, "Mobile Phone Entry").grid(row=10, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.MobilePhoneNote = ctk.StringVar(value = patient.mobilePhone)
        self.addMobilePhoneEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.MobilePhoneNote
        )
        self.addMobilePhoneEntry.grid(row=11, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addMobilePhoneButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )   
        
        self.addMobilePhoneButton.configure(command=lambda: self.addMobilePhone(patient, self.MobilePhoneNote.get()))
        self.addMobilePhoneButton.grid(row=11, column=5, sticky="w", padx=PADCOMP, pady=PADCOMP)
             
        
        LabelBorder(self.addNoteFrame, "Home Phone Entry").grid(row=12, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.HomePhoneNote = ctk.StringVar(value = patient.homePhone)
        self.addHomePhoneEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.HomePhoneNote
        )
        self.addHomePhoneEntry.grid(row=13, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addHomePhoneButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )  
        self.addHomePhoneButton.configure(command=lambda: self.addHomePhone(patient, self.HomePhoneNote.get()))
        self.addHomePhoneButton.grid(row=13, column=5, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
                
        LabelBorder(self.addNoteFrame, "Work Phone Entry").grid(row=14, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.WorkPhoneNote = ctk.StringVar(value = patient.workPhone)
        self.addWorkPhoneEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.WorkPhoneNote
        )
        self.addWorkPhoneEntry.grid(row=15, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addWorkPhoneButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )  
        self.addWorkPhoneButton.configure(command=lambda: self.addWorkPhone(patient, self.WorkPhoneNote.get()))
        self.addWorkPhoneButton.grid(row=15, column=5, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        
        LabelBorder(self.addNoteFrame, "Emergency Contact 1 Name Entry").grid(row=8, column = 0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.EmergencyContact1Note = ctk.StringVar(value = patient.emergencyContactNames[0])
        self.addEmergencyNameEntry1 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.EmergencyContact1Note
        )
        self.addEmergencyNameEntry1.grid(row=9, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addEmergencyNameButton1 = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )  
        
        self.addEmergencyNameButton1.configure(command=lambda: self.addEmergencyContact(patient, self.EmergencyContact1Note.get(),1,1))
        self.addEmergencyNameButton1.grid(row=9, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        LabelBorder(self.addNoteFrame, "Emergency Phone Number 1 Entry").grid(row=10, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.EmergencyPhone1Note = ctk.StringVar(value = patient.emergencyContactNumbers[0])
        self.addEmergencyPhoneEntry1 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.EmergencyPhone1Note
        )
        self.addEmergencyPhoneEntry1.grid(row=11, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addEmergencyPhoneButton1 = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )  
        self.addEmergencyPhoneButton1.configure(command=lambda: self.addEmergencyContact(patient, self.EmergencyPhone1Note.get(),2,1))
        self.addEmergencyPhoneButton1.grid(row=11, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        
        LabelBorder(self.addNoteFrame, "Emergency Contact 2 Name Entry").grid(row=12, column = 0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.EmergencyContact2Note = ctk.StringVar(value = patient.emergencyContactNames[1])
        self.addEmergencyNameEntry2 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.EmergencyContact2Note
        )
        self.addEmergencyNameEntry2.grid(row=13, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addEmergencyNameButton2 = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )  
        self.addEmergencyNameButton2.configure(command=lambda: self.addEmergencyContact(patient, self.EmergencyContact2Note.get(),1,2))
        self.addEmergencyNameButton2.grid(row=13, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        
        LabelBorder(self.addNoteFrame, "Emergency Phone Number 2 Entry").grid(row=14, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.EmergencyPhone2Note = ctk.StringVar(value = patient.emergencyContactNumbers[1])
        self.addEmergencyPhoneEntry2 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.EmergencyPhone2Note
        )
        self.addEmergencyPhoneEntry2.grid(row=15, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addEmergencyPhoneButton2 = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        ) 
        
        self.addEmergencyPhoneButton2.configure(command=lambda: self.addEmergencyContact(patient, self.EmergencyPhone2Note.get(),2,2))
        self.addEmergencyPhoneButton2.grid(row=15, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        
        LabelBorder(self.addNoteFrame, "Emergency Contact 3 Name Entry").grid(row=16, column = 0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.EmergencyName3Note = ctk.StringVar(value = patient.emergencyContactNames[2])
        self.addEmergencyNameEntry3 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.EmergencyName3Note
        )
        self.addEmergencyNameEntry3.grid(row=17, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addEmergencyNameButton3 = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )  
        self.addEmergencyNameButton3.configure(command=lambda: self.addEmergencyContact(patient, self.EmergencyName3Note.get(),1,3))
        self.addEmergencyNameButton3.grid(row=17, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        LabelBorder(self.addNoteFrame, "Emergency Phone Number 3 Entry").grid(row=18, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.EmergencyPhone3Note = ctk.StringVar(value = patient.emergencyContactNumbers[2])
        self.addEmergencyPhoneEntry3 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.EmergencyPhone3Note
        )
        self.addEmergencyPhoneEntry3.grid(row=19, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addEmergencyPhoneButton3 = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )               
        self.addEmergencyPhoneButton3.configure(command=lambda: self.addEmergencyContact(patient, self.EmergencyPhone3Note.get(),2,3))
        self.addEmergencyPhoneButton3.grid(row=19, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        
        #vistation
        LabelBorder(self.addNoteFrame, "Max Simultaneous Visitors").grid(row=5, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.MaxVisitorsNote = ctk.StringVar()
        self.addMaxVisitorsEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.MaxVisitorsNote
        )
        self.addMaxVisitorsEntry.grid(row=6, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addMaxVisitorsButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )    
        
        self.addMaxVisitorsButton.configure(command=lambda: self.addMaxVisitors(patient, self.MaxVisitorsNote.get()))
        self.addMaxVisitorsButton.grid(row=6, column=3, sticky="w", padx=PADCOMP, pady=PADCOMP)

        LabelBorder(self.addNoteFrame, "Approved Vistor 1 Entry").grid(row=7, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.ApprovedVisitor1Note = ctk.StringVar()
        self.addAprovedVisitorEntry1 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.ApprovedVisitor1Note
        )
        self.addAprovedVisitorEntry1.grid(row=8, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addApprovedVisitorButton1 = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )   
        
        self.addApprovedVisitorButton1.configure(command=lambda: self.addAllowedVisitor(patient, self.ApprovedVisitor1Note.get()))
        self.addApprovedVisitorButton1.grid(row=8, column=3, sticky="w", padx=PADCOMP, pady=PADCOMP)
         
        LabelBorder(self.addNoteFrame, "Approved Vistor 2 Entry").grid(row=9, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.ApprovedVisitor2Note = ctk.StringVar()
        self.addAprovedVisitorEntry2 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.ApprovedVisitor2Note
        )
        
        
        self.addAprovedVisitorEntry2.grid(row=10, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addApprovedVisitorButton2 = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )         
        
        self.addApprovedVisitorButton2.configure(command=lambda: self.addAllowedVisitor(patient, self.ApprovedVisitor2Note.get()))
        self.addApprovedVisitorButton2.grid(row=10, column=3, sticky="w", padx=PADCOMP, pady=PADCOMP)
                
        LabelBorder(self.addNoteFrame, "Approved Vistor 3 Entry").grid(row=11, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.ApprovedVisitor3Note = ctk.StringVar()
        self.addAprovedVisitorEntry3 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.ApprovedVisitor3Note
        )
        self.addAprovedVisitorEntry3.grid(row=12, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addAprovedVisitorEntry3 = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )          
        self.addAprovedVisitorEntry3.configure(command=lambda: self.addAllowedVisitor(patient, self.ApprovedVisitor3Note.get()))
        self.addAprovedVisitorEntry3.grid(row=12, column=3, sticky="w", padx=PADCOMP, pady=PADCOMP)
         
        #Location  
        LabelBorder(self.addNoteFrame, "Facility  Entry").grid(row=1, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.FacilityNote = ctk.StringVar()
        self.addFacililtyEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.FacilityNote
        )
        self.addFacililtyEntry.grid(row=2, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addFacililtyButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )    
        
        self.addFacililtyButton.configure(command=lambda: self.addLocation(patient, self.FacilityNote.get()))
        self.addFacililtyButton.grid(row=2, column=5, sticky="w", padx=PADCOMP, pady=PADCOMP)
                         
        LabelBorder(self.addNoteFrame, "Floor  Entry").grid(row=3, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.FloorNote = ctk.StringVar()
        self.addFloorEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.FloorNote
        )
        self.addFloorEntry.grid(row=4, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addFloorButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )           
        
        self.addFloorButton.configure(command=lambda: self.addLocation(patient, self.FloorNote.get()))
        self.addFloorButton.grid(row=4, column=5, sticky="w", padx=PADCOMP, pady=PADCOMP)
                 
        LabelBorder(self.addNoteFrame, "Room  Entry").grid(row=5, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.RoomNote = ctk.StringVar()
        self.addRoomEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.RoomNote
        )
        self.addRoomEntry.grid(row=6, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addRoomButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )               
        
        self.addRoomButton.configure(command=lambda: self.addLocation(patient, self.RoomNote.get()))
        self.addRoomButton.grid(row=6, column=5, sticky="w", padx=PADCOMP, pady=PADCOMP)
             
        LabelBorder(self.addNoteFrame, "Bed  Entry").grid(row=7, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.BedNote = ctk.StringVar()
        self.addBedEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.BedNote
        )
        self.addBedEntry.grid(row=8, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addBedButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )  
        
        self.addBedButton.configure(command=lambda: self.addLocation(patient, self.note.get()))
        self.addBedButton.grid(row=8, column=5, sticky="w", padx=PADCOMP, pady=PADCOMP)
                               
                                                                            
    def addFirstName(self, patient, FirstName):
        patient.setFirstName(FirstName)
        
    def addMiddleName(self, patient, MiddleName):
        patient.setMiddleName(MiddleName)
        
    def addLastName(self, patient, LastName):
        patient.setLastname(LastName)
        
    def addAddress(self, patient, Address):
        patient.setAddress(Address)
        
    def addHomePhone(self, patient, HomePhone):
        patient.setHomePhone(HomePhone)
        
    def addWorkPhone(self, patient, WorkPhone):
        patient.setWorkPhone(WorkPhone)
        
        
    #NameOrPhone should be an integer of 1 or 2 name =1 phone =2
    #EmergencyIndex should be 1 2 3    
    def addEmergencyContact(self, patient,EmergencyContactTemp, NameOrPhone, EmergencyIndex):
        #if(EmergencyIndex == 1):
          #  if(NameOrPhone == 1):
                #EmergencyPhone1 = EmergencyContactTemp
            #else:
                #EmergencyName1 = EmergencyContactTemp
            patient.addEmergencyContact(EmergencyContactTemp)
        
        
        
        
    def addMaxVisitors(self, patient,NumAllowedVisitor):
        patient.setNumAllowedVisitors(NumAllowedVisitor)
   
    def addAllowedVisitor(self, patient,Visitor):
        patient.addAllowedVisitor(Visitor)
        
    def addLocation(self, patient,Location):
        patient.setLocation(Location)
        
class MedicalInfoTab(ctk.CTkScrollableFrame, ):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget, orientation= "horizontal")
        
        
        self.addNoteFrame = ctk.CTkFrame(
            self
        )
        self.addNoteFrame.grid(row=3, column=2, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.addNoteFrame, "Family Doctor").grid(row=1, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.FamilyDoctorNote = ctk.StringVar()
        self.addFamilyDoctorEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.FamilyDoctorNote
        )
        self.addFamilyDoctorEntry.grid(row=2, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addFamilyDoctorButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )   
        self.addFamilyDoctorButton.configure(command=lambda: self.addFamilyDoctor(patient, self.FamilyDoctorNote.get()))
        self.addFamilyDoctorButton.grid(row=2, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)

        self.addNoteFrame.grid(row=3, column=2, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.addNoteFrame, "Admittance Date").grid(row=3, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.AdmittanceDateNote = ctk.StringVar()
        self.addAdmittanceDateEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.AdmittanceDateNote
        )
        self.addAdmittanceDateEntry.grid(row=4, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addAdmitanceDateButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )
        self.addAdmitanceDateButton.configure(command=lambda: self.addAdmitanceDate(patient, self.AdmittanceDateNote.get()))
        self.addAdmitanceDateButton.grid(row=4, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)     

        LabelBorder(self.addNoteFrame, "Admittance Time").grid(row=5, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.AdmittanceTimeNote = ctk.StringVar()
        self.addAdmitanceTimeEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.AdmittanceTimeNote
        )
        self.addAdmitanceTimeEntry.grid(row=6, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addAdmitanceTimeButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )
        self.addAdmitanceTimeButton.configure(command=lambda: self.addAdmitanceTime(patient, self.AdmittanceTimeNote.get()))
        self.addAdmitanceTimeButton.grid(row=6, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)    
        
        LabelBorder(self.addNoteFrame, "Admittance Reason").grid(row=7, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.AdmittanceReasonNote = ctk.StringVar()
        self.AdmitanceReasonEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.AdmittanceReasonNote
        )
        self.AdmitanceReasonEntry.grid(row=8, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addAdmitanceReasonButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )
        
        self.addAdmitanceReasonButton.configure(command=lambda: self.addAdmitanceReasonButton(patient, self.AdmittanceReasonNote.get()))
        self.addAdmitanceReasonButton.grid(row=8, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)   
        
        LabelBorder(self.addNoteFrame, "Discharge Date").grid(row=10, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.DischargeNote = ctk.StringVar()
        self.addDischargeDateEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.DischargeNote
        )
        self.addDischargeDateEntry.grid(row=11, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addDischargeDateButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )
        
        self.addDischargeDateButton.configure(command=lambda: self.addDischargeDate(patient, self.DischargeNote.get()))
        self.addDischargeDateButton.grid(row=11, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP)   
        
        LabelBorder(self.addNoteFrame, "Discharge Time").grid(row=13, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.DischargeTimeNote = ctk.StringVar()
        self.addDischargeTimeEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.DischargeTimeNote
        )
        self.addDischargeTimeEntry.grid(row=14, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addDischargeTimeButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )
        
        self.addDischargeTimeButton.configure(command=lambda: self.addDischargeTime(patient, self.DischargeTimeNote.get()))
        self.addDischargeTimeButton.grid(row=14, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP) 
        
        LabelBorder(self.addNoteFrame, "Prescription Medicine Name").grid(row=1, column=3, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.PrescriptionNameNote = ctk.StringVar()
        self.addPrescriptionNameEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.PrescriptionNameNote
        )
        self.addPrescriptionNameEntry.grid(row=2, column=3, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addPrescriptionNameButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )
        
        self.addPrescriptionNameButton.configure(command=lambda: self.addPrescriptionName(patient, self.PrescriptionNameNote.get()))
        self.addPrescriptionNameButton.grid(row=2, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP) 
        
        LabelBorder(self.addNoteFrame, "Prescriptions Amount").grid(row=4, column=3, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.PrescriptionAmount = ctk.StringVar()
        self.addPrescriptionAmountEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.PrescriptionAmount
        )
        self.addPrescriptionAmountEntry.grid(row=5, column=3, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addPrescriptionAmountButton   = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )
        
        self.addPrescriptionAmountButton.configure(command=lambda: self.addPrescriptionAmount(patient, self.PrescriptionAmount.get()))
        self.addPrescriptionAmountButton.grid(row=5, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP) 
        

        
        LabelBorder(self.addNoteFrame, "Prescriptions Schedule").grid(row=7, column=3, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.PrescriptionScheduleNote = ctk.StringVar()
        self.addPrescriptionScheduleEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.PrescriptionScheduleNote
        )
        self.addPrescriptionScheduleEntry.grid(row=8, column=3, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addPrescriptionEntryButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )
        
        self.addPrescriptionEntryButton.configure(command=lambda: self.addPrescriptionEntry(patient, self.PrescriptionScheduleNote.get()))
        self.addPrescriptionEntryButton.grid(row=8, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP) 
        
        LabelBorder(self.addNoteFrame, "Scheduled Procedures ").grid(row=10, column=3, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.ScheduleProcedureNote = ctk.StringVar()
        self.addScheduledProcedureEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.ScheduleProcedureNote
        )
        self.addScheduledProcedureEntry.grid(row=11, column=3, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addScheduledProcedureButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )
        self.addScheduledProcedureButton.configure(command=lambda: self.addPrescriptionButton(patient, self.ScheduleProcedureNote.get()))
        self.addScheduledProcedureButton.grid(row=11, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP) 
        
        LabelBorder(self.addNoteFrame, "Doctor  Notes ").grid(row=1, column=5, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.DoctorNote = ctk.StringVar()
        self.addDoctorNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.DoctorNote
        )
        self.addDoctorNoteEntry.grid(row=2, column=5, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addDoctorNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )
        self.addDoctorNoteButton.configure(command=lambda: self.addDoctorNote(patient, self.DoctorNote.get()))
        self.addDoctorNoteButton.grid(row=2, column=6, sticky="w", padx=PADCOMP, pady=PADCOMP) 
        
        LabelBorder(self.addNoteFrame, "Nurse  Notes ").grid(row=5, column=5, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.NurseNote = ctk.StringVar()
        self.addNurseNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.NurseNote
        )
        self.addNurseNoteEntry.grid(row=6, column=5, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNurseNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )
        self.addNurseNoteButton.configure(command=lambda: self.addNurseNote(patient, self.NurseNote.get()))
        self.addNurseNoteButton.grid(row=6, column=6, sticky="w", padx=PADCOMP, pady=PADCOMP) 


    def addDateAdmittance(self, patient, DateAdmin):
        patient.setDateAdmittance(DateAdmin)
        
    def addTimeAdmitance(self, patient, TimeAdmitance):
        patient.setTimeAdmittance(TimeAdmitance)
        
    def addDateDischarge(self, patient, DateDischarge):
        patient.setDateDischarge(DateDischarge)
        
    def addTimeDischarge(self, patient, TimeDischarge):
        patient.setTimeDischarge(TimeDischarge)
        
    def addPrescriptionName(self, patient, PrescriptionName):
        patient.addPrescription(PrescriptionName)
                
    def addPrescriptionAmount(self, patient, PrescriptionAmount):
        patient.addPrescription(PrescriptionAmount)
        
    def addPrescriptionSchedule(self, patient, PrescriptionSchedule):
        patient.addPrescription(PrescriptionSchedule)
        
    def addDoctorNote(self, patient, DoctorNote):
        patient.addDoctorNote(DoctorNote)
        
    def addNurseNote(self, patient, NurseNote):
        patient.addNurseNote(NurseNote)
        
    def addScheduledProcedure(self, patient, ScheduledProcedure):
        patient.addScheduledProcedure(ScheduledProcedure)
        
class BillingInfoTab(ctk.CTkScrollableFrame):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget, orientation= "horizontal")
        
        
        self.addNoteFrame = ctk.CTkFrame(
            self
        )
        self.addNoteFrame.grid(row=1, column=0, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.addNoteFrame, "Insurance Carrier").grid(row=1, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.InsuranceCarrierNote = ctk.StringVar(value = patient.insuranceCarrier)
        self.addInsuranceCarrierEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.InsuranceCarrierNote
        )
        self.addInsuranceCarrierEntry.grid(row=2, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addInsuranceCarrierButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )   
        
        self.addInsuranceCarrierButton.configure(command=lambda: self.addInsuranceCarrier(patient, self.InsuranceCarrierNote.get()))
        self.addInsuranceCarrierButton.grid(row=2, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP) 

        
        LabelBorder(self.addNoteFrame, "Insurance Policy Account Number").grid(row=4, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.InsurancePolicyNote = ctk.StringVar(value = patient.insuranceAccountNumber)
        self.addInsurancePolicyAccountEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.InsurancePolicyNote
        )
        self.addInsurancePolicyAccountEntry.grid(row=5, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addInsurancePolicyAccountButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        ) 
        
        self.addInsurancePolicyAccountButton.configure(command=lambda: self.addInsurancePolicyAccount(patient, self.InsurancePolicyNote.get()))
        self.addInsurancePolicyAccountButton.grid(row=5, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP) 
 
        
        LabelBorder(self.addNoteFrame, "Insurance Policy Group Number").grid(row=6, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.InsuranceGroupNumberNote = ctk.StringVar(value = patient.insuranceGroupNumber)
        self.addInsuranceGroupEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.InsuranceGroupNumberNote
        )
        self.addInsuranceGroupEntry.grid(row=7, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addInsuranceGroupButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )  
        
        self.addInsuranceGroupButton.configure(command=lambda: self.addNurseNote(patient, self.InsuranceGroupNumberNote.get()))
        self.addInsuranceGroupButton.grid(row=7, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP) 
  
        
        LabelBorder(self.addNoteFrame, "Amount  Paid").grid(row=9, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.AmountPaidNote = ctk.StringVar(value = patient.amountPaid)
        self.addAmountPaidEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.AmountPaidNote
        )
        self.addAmountPaidEntry.grid(row=10, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addAmountPaidButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )   

        self.addAmountPaidButton.configure(command=lambda: self.addAmountPaid(patient, self.AmountPaidNote.get()))
        self.addAmountPaidButton.grid(row=10, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP) 
 

        LabelBorder(self.addNoteFrame, "Amount  Owed").grid(row=12, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.AmountOwedNote = ctk.StringVar(value = patient.amountOwed)
        self.addAmountOwedEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.AmountOwedNote
        )
        self.addAmountOwedEntry.grid(row=13, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addAmountOwedButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        )   

        self.addAmountOwedButton.configure(command=lambda: self.addAmountOwed(patient, self.AmountOwedNote.get()))
        self.addAmountOwedButton.grid(row=13, column=1, sticky="w", padx=PADCOMP, pady=PADCOMP) 
 

        LabelBorder(self.addNoteFrame, "Add a charge Owed").grid(row=1, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.ChargeOwedNote = ctk.StringVar(value = patient.amountOwed)
        self.addChargeOwedEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.ChargeOwedNote
        )
        self.addChargeOwedEntry.grid(row=2, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addChargeOwedButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Edit",
            font=FONTINFO,
            width=80
        ) 
        self.addChargeOwedButton.configure(command=lambda: self.addChargeOwed(patient, self.note.ChargeOwedNote()))
        self.addChargeOwedButton.grid(row=2, column=5, sticky="w", padx=PADCOMP, pady=PADCOMP) 
 
    def addInsuranceCarrier(self, patient, InsuranceCarrier):
        patient.setInsuranceCarrier(InsuranceCarrier)
        
    def addInsuranceAccountNumber(self, patient, InsuranceAccountNumber):
        patient.setInsuranceAccountNumber(InsuranceAccountNumber)

    def addInsuranceGroupNumber(self, patient, InsuranceGroupNumber):
        patient.setInsuranceGroupNumber(InsuranceGroupNumber)
        
    def addAmmountPaid(self, patient, AmountPaid):
        patient.setAmountPaid(AmountPaid)
        
    def addAmountPaidByInsurance(self, patient, AmountPaidByInsurance):
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