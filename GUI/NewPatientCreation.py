import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk
import GUI.ScrollablePatientList as spl
import Data.System
import GUI.MainWindow
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

#        self.returnButton = ctk.CTkButton(
#            self.buttonFrame,
#            text="Back",
#            font=FONTBUTTON,
#            width=100,
#            height=40,
#            command=lambda:MainWindow.switchPatientList(Data.System.getPatientList())
#       )
#        self.returnButton.grid(row=0, column=0, padx=5, pady=5)
    
    
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
        self.addNoteFrame.grid(row=3, column=2, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.addNoteFrame, "First Name Entry").grid(row=1, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=2, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )
        
        #self.addNoteFrame.grid(row=4, column=2, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.addNoteFrame, "Middle Name Entry").grid(row=3, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=4, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )
            #self.addNoteFrame.grid(row=4, column=2, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.addNoteFrame, "Last Name Entry").grid(row=5, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=6, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )
        
        LabelBorder(self.addNoteFrame, "Address   Entry").grid(row=1, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=2, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )
        
        
        LabelBorder(self.addNoteFrame, "Mobile Phone   Entry").grid(row=1, column=3, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=2, column=3, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )        
        
        LabelBorder(self.addNoteFrame, "Home Phone   Entry").grid(row=3, column=3, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=4, column=3, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )  
        
                
        LabelBorder(self.addNoteFrame, "Work Phone   Entry").grid(row=5, column=3, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=6, column=3, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )  
        
        
        LabelBorder(self.addNoteFrame, "Emergency Contact 1 Name   Entry").grid(row=10, column = 0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=11, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )  
        LabelBorder(self.addNoteFrame, "Emergency  Phone Number 1 Entry").grid(row=12, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=13, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )  
        LabelBorder(self.addNoteFrame, "Emergency Contact 2 Name   Entry").grid(row=14, column = 0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=15, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )  
        LabelBorder(self.addNoteFrame, "Emergency  Phone Number 2 Entry").grid(row=16, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=17, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        ) 
        LabelBorder(self.addNoteFrame, "Emergency Contact 3 Name   Entry").grid(row=18, column = 0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=19, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )  
        LabelBorder(self.addNoteFrame, "Emergency  Phone Number 3 Entry").grid(row=20, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=21, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )               
        
        
        
        #vistation
        LabelBorder(self.addNoteFrame, "Max Simalataneous Visitors").grid(row=5, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=6, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )    
        LabelBorder(self.addNoteFrame, "Approved Vistor 1 Entry").grid(row=7, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=8, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )    
        LabelBorder(self.addNoteFrame, "Approved Vistor 2 Entry").grid(row=9, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=10, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )                    
        LabelBorder(self.addNoteFrame, "Approved Vistor 3 Entry").grid(row=11, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=12, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )          
         
        #Location  
        LabelBorder(self.addNoteFrame, "Facility  Entry").grid(row=1, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=2, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )                    
        LabelBorder(self.addNoteFrame, "Floor  Entry").grid(row=3, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=4, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )                    
        LabelBorder(self.addNoteFrame, "Room  Entry").grid(row=5, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=6, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )                    
        LabelBorder(self.addNoteFrame, "Bed  Entry").grid(row=7, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.note = ctk.StringVar()
        self.addNoteEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.note
        )
        self.addNoteEntry.grid(row=8, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)
        self.addNoteButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add",
            font=FONTINFO,
            width=80
        )                    
                                                                            
                                     
        
class MedicalInfoTab(ctk.CTkFrame):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget)
        
        
class BillingInfoTab(ctk.CTkFrame):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget)
        
        
        
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