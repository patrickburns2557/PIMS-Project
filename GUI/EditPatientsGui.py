import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import GUI.ScrollablePatientList as spl
import Data.System
import GUI.MainWindow as MainWindow
from Data.dataClasses import Patient
import re


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
        
        
        
        self.buttonFrame = ctk.CTkFrame(self)
        
        self.SaveButton = ctk.CTkButton(
            self.buttonFrame,
            text="Save Patient",
            font=FONTBUTTON,
            width=100,
            height=40,
            command=lambda:[finalizePatient(self,CurrentPatient), MainWindow.switchDetailedView(CurrentPatient)]
        )
        self.SaveButton.grid(row=0, column=4, padx=5, pady=5)   
        
        
         #first tab shown will be the personal info tab
        self.PersonalTab = PersonalInfoTab(self, CurrentPatient)
        self.shownTab = self.PersonalTab
        self.in_personal = 1
        self.in_billing = 0
        self.BillingTab = BillingInfoTab(self, CurrentPatient)
        
        
        self.addNoteFrame = ctk.CTkFrame(
            self
        )
        #Create frame and buttons for switching tabs
        
        
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
            command=lambda:MainWindow.switchDetailedView(CurrentPatient)
       )
        self.returnButton.grid(row=0, column=0, padx=5, pady=5)
         
    
        self.buttonFrame.grid(row=0, column=0, sticky="news", padx=8, pady=8)
        self.shownTab.grid(row=1, column=0, sticky="news")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
    #functions to turn save button off and on
    def turnOnSave(self):
            self.SaveButton.configure(state = "normal")
            
    def turnOffSave(self):
            self.SaveButton.configure(state = "disabled")
        
        
    #Functions to switch between the tabs using the buttons
    def switchPersonal(self):
        #Some tab buttons may not exist depending on the type of user logged in
        try:
            self.personalButton.configure(state="disabled")
        except AttributeError or NameError:
            pass

        try:
            self.billingButton.configure(state="normal")
        except AttributeError or NameError:
            pass

        #Remove the previous tab to show the new one
        self.shownTab.grid_remove()
        self.shownTab = self.PersonalTab
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
        
        #Remove the previous tab to show the new one
        self.shownTab.grid_remove()
        self.shownTab = self.BillingTab
        self.shownTab.grid(row=1, column=0, sticky="news")
        self.in_billing = 1
        self.in_personal = 0
        
        
        
        
        
#############################################
# Tabs
#############################################


class PersonalInfoTab(ctk.CTkScrollableFrame):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget, orientation= "horizontal")
       
       
        self.parentWidget = parentWidget
       
        #self.Edit = EditPatientView
        
        vcmd = (self.register(self.validatephone), '%P', '%W')
        #ivcmd = (self.register(self.on_invalid),)  
        
        self.label_error = ttk.Label(self, foreground='red')
        self.label_error.grid(row=8, column=8, sticky=tk.W, padx=5)      
    
        self.addNoteFrame = ctk.CTkFrame(
            self
        )
        self.addNoteFrame.grid(row=1, column=2, sticky="nw", padx=PADSECTION, pady=PADSECTION)
        LabelBorder(self.addNoteFrame, "First Name Entry").grid(row=1, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.FirstNameNote = ctk.StringVar(value = patient.firstName)
        self.addFirstNameEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.FirstNameNote
        )
        self.addFirstNameEntry.grid(row=2, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)
        

    
        LabelBorder(self.addNoteFrame, "Middle Name Entry").grid(row=3, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.MiddleNameNote = ctk.StringVar(value = patient.middleName)
        self.addMiddleNameEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.MiddleNameNote
        )
        self.addMiddleNameEntry.grid(row=4, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)

    
        
        LabelBorder(self.addNoteFrame, "Last Name Entry").grid(row=5, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.LastNameNote = ctk.StringVar(value = patient.lastName)
        self.addLastNameEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.LastNameNote
        )
        self.addLastNameEntry.grid(row=6, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)

    
    
        LabelBorder(self.addNoteFrame, "Address Street Entry").grid(row=1, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.AdressStreetNote = ctk.StringVar(value = patient.address[0])
        self.addAddressEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.AdressStreetNote
        )
        self.addAddressEntry.grid(row=2, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)

        LabelBorder(self.addNoteFrame, "Address City Entry").grid(row=3, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.AddressCityNote = ctk.StringVar(value = patient.address[1])
        self.addAddressEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.AddressCityNote
        )
        self.addAddressEntry.grid(row=4, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)
               
        LabelBorder(self.addNoteFrame, "Address  State Entry").grid(row=5, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.AddressStateNote = ctk.StringVar(value = patient.address[2])
        self.addAddressEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.AddressStateNote
        )
        self.addAddressEntry.grid(row=6, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        LabelBorder(self.addNoteFrame, "Address Zip State Entry").grid(row=7, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.AddressZipNote = ctk.StringVar(value = patient.address[3])
        self.addAddressEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.AddressZipNote
        )
        self.addAddressEntry.grid(row=8, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)
    
        LabelBorder(self.addNoteFrame, "Mobile Phone Entry").grid(row=10, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.MobilePhoneNote = ctk.StringVar(value = patient.mobilePhone)
        self.addMobilePhoneEntry = ctk.CTkEntry(
            self.addNoteFrame,
            validate='focus',
            validatecommand = vcmd,
            font=FONTINFO,
            width=350,
            textvariable=self.MobilePhoneNote
        )
        self.addMobilePhoneEntry.grid(row=11, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)

            
    
        LabelBorder(self.addNoteFrame, "Home Phone Entry").grid(row=12, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.HomePhoneNote = ctk.StringVar(value = patient.homePhone)
        self.addHomePhoneEntry = ctk.CTkEntry(
            self.addNoteFrame,
            validate='focus',
            validatecommand = vcmd,
            font=FONTINFO,
            width=350,
            textvariable=self.HomePhoneNote
        )
        self.addHomePhoneEntry.grid(row=13, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)

            
        LabelBorder(self.addNoteFrame, "Work Phone Entry").grid(row=14, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.WorkPhoneNote = ctk.StringVar(value = patient.workPhone)
        self.addWorkPhoneEntry = ctk.CTkEntry(
            self.addNoteFrame,
            validate='focus',
            validatecommand = vcmd,
            font=FONTINFO,
            width=350,
            textvariable=self.WorkPhoneNote
        )
        self.addWorkPhoneEntry.grid(row=15, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)


        LabelBorder(self.addNoteFrame, "Emergency Contact 1 Name Entry").grid(row=8, column = 0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        try:
            self.EmergencyName1Note = ctk.StringVar(value = patient.emergencyContactNames[0])
        except IndexError:
            self.EmergencyName1Note = ctk.StringVar()
        self.addEmergencyNameEntry1 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.EmergencyName1Note
        )
        self.addEmergencyNameEntry1.grid(row=9, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)



        LabelBorder(self.addNoteFrame, "Emergency Phone Number 1 Entry").grid(row=10, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        try:
            self.EmergencyPhone1Note = ctk.StringVar(value = patient.emergencyContactNumbers[0])
        except IndexError:
            self.EmergencyPhone1Note = ctk.StringVar()
        self.addEmergencyPhoneEntry1 = ctk.CTkEntry(
            self.addNoteFrame,
            validate='focus',
            validatecommand = vcmd,
            font=FONTINFO,
            width=350,
            textvariable=self.EmergencyPhone1Note
        )
        self.addEmergencyPhoneEntry1.grid(row=11, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)

    
       
        LabelBorder(self.addNoteFrame, "Emergency Contact 2 Name Entry").grid(row=12, column = 0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        try:
            self.EmergencyName2Note = ctk.StringVar(value = patient.emergencyContactNames[1])
        except IndexError:
            self.EmergencyName2Note = ctk.StringVar()
        self.addEmergencyNameEntry2 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.EmergencyName2Note
        )
        self.addEmergencyNameEntry2.grid(row=13, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)

    
        
        LabelBorder(self.addNoteFrame, "Emergency Phone Number 2 Entry").grid(row=14, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        try:
            self.EmergencyPhone2Note = ctk.StringVar(value = patient.emergencyContactNumbers[1])
        except IndexError:
            self.EmergencyPhone2Note = ctk.StringVar()
        self.addEmergencyPhoneEntry2 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            validate='focus',
            validatecommand = vcmd,
            width=350,
            textvariable=self.EmergencyPhone2Note
        )
        self.addEmergencyPhoneEntry2.grid(row=15, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)

    
        
        LabelBorder(self.addNoteFrame, "Emergency Contact 3 Name Entry").grid(row=16, column = 0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        try:
            self.EmergencyName3Note = ctk.StringVar(value = patient.emergencyContactNames[2])
        except IndexError:
            self.EmergencyName3Note = ctk.StringVar()
        self.addEmergencyNameEntry3 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.EmergencyName3Note
        )
        self.addEmergencyNameEntry3.grid(row=17, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)

        

        LabelBorder(self.addNoteFrame, "Emergency Phone Number 3 Entry").grid(row=18, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        try:
            self.EmergencyPhone3Note = ctk.StringVar(value = patient.emergencyContactNumbers[2])
        except IndexError:
            self.EmergencyPhone3Note = ctk.StringVar()
        self.addEmergencyPhoneEntry3 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            validate='focus',
            validatecommand = vcmd,
            width=350,
            textvariable=self.EmergencyPhone3Note
        )
        self.addEmergencyPhoneEntry3.grid(row=19, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)

    
    
        #vistation
        LabelBorder(self.addNoteFrame, "Max Simultaneous Visitors").grid(row=10, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.MaxVisitorsNote = ctk.StringVar(value = patient.numAllowedVisitors)
        self.addMaxVisitorsEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.MaxVisitorsNote
        )
        self.addMaxVisitorsEntry.grid(row=11, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)


        LabelBorder(self.addNoteFrame, "Approved Vistor 1 Entry").grid(row=12, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        try:
            self.ApprovedVisitor1Note = ctk.StringVar(value = patient.allowedVisitors[0])
        except IndexError:
            self.ApprovedVisitor1Note = ctk.StringVar()
        self.addAprovedVisitorEntry1 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.ApprovedVisitor1Note
        )
        self.addAprovedVisitorEntry1.grid(row=13, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)

        LabelBorder(self.addNoteFrame, "Approved Vistor 2 Entry").grid(row=14, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        try:
            self.ApprovedVisitor2Note = ctk.StringVar(value = patient.allowedVisitors[1])
        except IndexError:
            self.ApprovedVisitor2Note = ctk.StringVar()
        self.addAprovedVisitorEntry2 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.ApprovedVisitor2Note
        )
        
        
        self.addAprovedVisitorEntry2.grid(row=15, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)
 
            

        LabelBorder(self.addNoteFrame, "Approved Vistor 3 Entry").grid(row=16, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        try:
            self.ApprovedVisitor3Note = ctk.StringVar(value = patient.allowedVisitors[2])
        except IndexError:
            self.ApprovedVisitor3Note = ctk.StringVar()
        self.addAprovedVisitorEntry3 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.ApprovedVisitor3Note
        )
        self.addAprovedVisitorEntry3.grid(row=17, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        LabelBorder(self.addNoteFrame, "Approved Vistor 4 Entry").grid(row=18, column=2, sticky="w", padx=PADLABEL, pady=PADLABEL)
        try:
            self.ApprovedVisitor4Note = ctk.StringVar(value = patient.allowedVisitors[3])
        except IndexError:
            self.ApprovedVisitor4Note = ctk.StringVar()
        self.addAprovedVisitorEntry4 = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.ApprovedVisitor4Note
        )
        self.addAprovedVisitorEntry4.grid(row=19, column=2, sticky="w", padx=PADCOMP, pady=PADCOMP)

        
        #Location  
        LabelBorder(self.addNoteFrame, "Facility  Entry").grid(row=1, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.FacilityNote = ctk.StringVar(value = patient.location[0])
        self.addFacililtyEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.FacilityNote
        )
        self.addFacililtyEntry.grid(row=2, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)

                        
        LabelBorder(self.addNoteFrame, "Floor  Entry").grid(row=3, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.FloorNote = ctk.StringVar(value = patient.location[1])
        self.addFloorEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.FloorNote
        )
        self.addFloorEntry.grid(row=4, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)

                
        LabelBorder(self.addNoteFrame, "Room  Entry").grid(row=5, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.RoomNote = ctk.StringVar(value = patient.location[2])
        self.addRoomEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.RoomNote
        )
        self.addRoomEntry.grid(row=6, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)

            
        LabelBorder(self.addNoteFrame, "Bed  Entry").grid(row=7, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.BedNote = ctk.StringVar(value = patient.location[3])
        self.addBedEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.BedNote
        )
        self.addBedEntry.grid(row=8, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        

   
    #def show_message(self, error='', color='black'):
        #self.label_error['text'] = error
        

    def validatephone(self, value, EntryName ):

        """
        Validat the phone entry
        :param value:
        :return:
        """

        #pattern = "^(+\d{1,2}\s?)?(?\d{3})?[\s.-]?\d{3}[\s.-]?\d{4}$"
        pattern = "^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$"
        #pattern = "^(+\d{1,2}\s?)?(?\d{3})?[\s.-]?\d{3}[\s.-]?\d{4}$"
        if re.fullmatch(pattern, value) is None:
            self.invalidePhone(EntryName)
            return False
        self.parentWidget.turnOnSave()


        try:
            if(EntryName.find('8') > -1):
                self.addMobilePhoneEntry.configure(fg_color = "white")
            if(EntryName.find('9') > -1):
                self.addHomePhoneEntry.configure(fg_color = "white")
            if(EntryName.find('10') > -1):
                self.addWorkPhoneEntry.configure(fg_color = "white")
            if(EntryName.find('12') > -1):
                self.addEmergencyPhoneEntry1.configure(fg_color = "white")
            if(EntryName.find('14') > -1):
                self.addEmergencyPhoneEntry2.configure(fg_color = "white")
            if(EntryName.find('16') > -1):
                self.addEmergencyPhoneEntry3.configure(fg_color = "white")
        except AttributeError:
            pass
        self.label_error.configure(text = "")
        return True


    def invalidePhone(self, EntryName):
        self.label_error.configure(text = "Please enter valid Phone Numbers")
        self.parentWidget.turnOffSave()
        try:
            if(EntryName.find('8') > -1):
                self.addMobilePhoneEntry.configure(fg_color = "red")
            if(EntryName.find('9') > -1):
                self.addHomePhoneEntry.configure(fg_color = "red")
            if(EntryName.find('10') > -1):
                self.addWorkPhoneEntry.configure(fg_color = "red")
            if(EntryName.find('12') > -1):
                self.addEmergencyPhoneEntry1.configure(fg_color = "red")
            if(EntryName.find('14') > -1):
                self.addEmergencyPhoneEntry2.configure(fg_color = "red")
            if(EntryName.find('16') > -1):
                self.addEmergencyPhoneEntry3.configure(fg_color = "red")
        except AttributeError:
            pass


                          






        
class BillingInfoTab(ctk.CTkScrollableFrame):
    def __init__(self, parentWidget, patient):
        super().__init__(parentWidget, orientation= "horizontal")
       
        vcmd = (parentWidget.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        
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


        
        LabelBorder(self.addNoteFrame, "Insurance Policy Account Number").grid(row=4, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.InsuranceAccountNumNote = ctk.StringVar(value = patient.insuranceAccountNumber)
        self.addInsurancePolicyAccountEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            validate = 'key',
            validatecommand = vcmd,
            width=350,
            textvariable=self.InsuranceAccountNumNote
        )
        self.addInsurancePolicyAccountEntry.grid(row=5, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)

        
        LabelBorder(self.addNoteFrame, "Insurance Policy Group Number").grid(row=6, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.InsuranceGroupNumNote = ctk.StringVar(value = patient.insuranceGroupNumber)
        self.addInsuranceGroupEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            validate = 'key',
            validatecommand = vcmd,
            width=350,
            textvariable=self.InsuranceGroupNumNote
        )
        self.addInsuranceGroupEntry.grid(row=7, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)

        LabelBorder(self.addNoteFrame, "Amount Paid").grid(row=1, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.AmountPaidNote = ctk.StringVar(value = patient.amountPaid)
        self.addAmountPaidEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            validate = 'key',
            validatecommand = vcmd,
            width=350,
            textvariable=self.AmountPaidNote
        )
        self.addAmountPaidEntry.grid(row=2, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)

 
        LabelBorder(self.addNoteFrame, "Amount paid by Insurance").grid(row=3, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.AmountPaidbyInsuranceNote = ctk.StringVar(value = patient.amountPaidByInsurance)
        self.addAmountPaidInsuranceEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            validate = 'key',
            validatecommand = vcmd,
            width=350,
            textvariable=self.AmountPaidbyInsuranceNote        

        )
        self.addAmountPaidInsuranceEntry.grid(row=4, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)

        LabelBorder(self.addNoteFrame, "Amount Owed").grid(row=5, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.AmountOwedNote = ctk.StringVar(value = patient.amountOwed)
        self.addChargeOwedEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            validate = 'key',
            validatecommand = vcmd,
            width=350,
            textvariable=self.AmountOwedNote
        )
        self.addChargeOwedEntry.grid(row=6, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)

        LabelBorder(self.addNoteFrame, "Charge").grid(row=7, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.addChargeDesNote = ctk.StringVar(value =0 )
        self.addChargeEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.addChargeDesNote
        )
        self.addChargeEntry.grid(row=8, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)
        

                
        LabelBorder(self.addNoteFrame, "Charge Amount").grid(row=9, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.addChargeAmountNote = ctk.StringVar(value =0.0 )
        self.addChargeAmountEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            validate = 'key',
            validatecommand = vcmd,
            width=350,
            textvariable=self.addChargeAmountNote
        )
        self.addChargeAmountEntry.grid(row=10, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)

        self.addChargeButton = ctk.CTkButton(
            self.addNoteFrame,
            text="Add Charge and Charge Amount",
            #command=lambda: [patient.addCharge("fsdf", self.ChargeAmountNote.get()), parentWidget.switchBilling()],
            command = lambda: self.addChargeNoteFun(patient, self.addChargeDesNote.get(), self.addChargeAmountNote.get(), parentWidget),
            font=FONTINFO,
            width=80
        )
        self.addChargeButton.grid(row=11, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)
        
        self.addChargeRefresh(patient)
        
    def addChargeRefresh(self, patient):
        self.listChargesFrame = ctk.CTkFrame(
            self
        )
        self.listChargesFrame.grid(row=1, column=6, sticky="nw", padx=PADSECTION, pady=PADSECTION, rowspan=10)
        self.ChargeNameNoteList = []
        self.ChargeAmountNoteList = []
        LabelBorder(self.listChargesFrame, "List of Charges").grid(row=0, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL, columnspan=2)
        for i in range(len(patient.listCharges)):
            self.ChargeNameNote = ctk.StringVar(value = patient.listCharges[i])
            self.singleChargeFrame = ctk.CTkFrame(self.listChargesFrame)
            self.chargeName = ctk.CTkEntry(
                self.singleChargeFrame,
                textvariable= self.ChargeNameNote,
                justify=ctk.LEFT,
                font=FONTINFO
            )
            self.ChargeNameNoteList.append(self.ChargeNameNote)
            self.ChargeAmountNote = ctk.StringVar(value = "{:.2f}".format(patient.listChargesAmount[i]))
            self.chargeName.grid(row=0, column=0, sticky="w", padx=PADCOMP)
            self.chargeAmount = ctk.CTkEntry(
                self.singleChargeFrame,
                textvariable= self.ChargeAmountNote,
                justify=ctk.RIGHT,
                font=FONTINFO
            )
            self.ChargeAmountNoteList.append(self.ChargeAmountNote)
            self.chargeAmount.grid(row=0, column=1, sticky="e", padx=10)
            self.singleChargeFrame.grid(row=i+1, column=0, sticky="ew", padx=PADCOMP, pady=PADCOMP)
            self.singleChargeFrame.grid_columnconfigure(0, weight=1)  

    def addChargeNoteFun(self, patient, chargeNote, chargesAmountNote, parentWidget):
        patient.addCharge(chargeNote, float(chargesAmountNote))
        self.addChargeRefresh(patient)

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
    def validate_float(self, action, index, value_if_allowed,
        prior_value, text, validation_type, trigger_type, widget_name):
        # action=1 -> insert
        if(action=='1'):
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
        
    
def finalizePatient(self,UpdatedPatient):
    try:
        UpdatedPatient.setFirstName(self.PersonalTab.FirstNameNote.get())
        UpdatedPatient.setMiddleName(self.PersonalTab.MiddleNameNote.get())
        UpdatedPatient.setLastname(self.PersonalTab.LastNameNote.get())
        
        
        address = [self.PersonalTab.AdressStreetNote.get(),self.PersonalTab.AddressCityNote.get(),self.PersonalTab.AddressStateNote.get(),self.PersonalTab.AddressZipNote.get()]
        UpdatedPatient.setAddress(address)
        
        UpdatedPatient.setHomePhone(self.PersonalTab.HomePhoneNote.get())
        UpdatedPatient.setWorkPhone(self.PersonalTab.WorkPhoneNote.get())
        UpdatedPatient.setMobilePhone(self.PersonalTab.MobilePhoneNote.get())

        Location = [self.PersonalTab.FacilityNote.get(),self.PersonalTab.FloorNote.get(),self.PersonalTab.RoomNote.get(),self.PersonalTab.BedNote.get()]
        UpdatedPatient.setLocation(Location)
        
        
        UpdatedPatient.setNumAllowedVisitors(self.PersonalTab.MaxVisitorsNote.get())
        

    except AttributeError or NameError:
        pass
    

#emergency contacts    
    try:    
        UpdatedPatient.emergencyContactNames[0] = (self.PersonalTab.EmergencyName1Note.get())
        UpdatedPatient.emergencyContactNumbers[0] = (self.PersonalTab.EmergencyPhone1Note.get()) 
    except IndexError or AttributeError:
        if(self.PersonalTab.EmergencyName1Note.get() != "" and self.PersonalTab.EmergencyPhone1Note.get() != ""):
            UpdatedPatient.addEmergencyContact(self.PersonalTab.EmergencyName1Note.get(), self.PersonalTab.EmergencyPhone1Note.get()) 
   
    try:    
        UpdatedPatient.emergencyContactNames[1] = (self.PersonalTab.EmergencyName2Note.get())
        UpdatedPatient.emergencyContactNumbers[1] = (self.PersonalTab.EmergencyPhone2Note.get()) 
    except IndexError or AttributeError:
        if(self.PersonalTab.EmergencyName2Note.get() != "" and self.PersonalTab.EmergencyPhone2Note.get() != ""):
            UpdatedPatient.addEmergencyContact(self.PersonalTab.EmergencyName2Note.get(), self.PersonalTab.EmergencyPhone2Note.get()) 
    
    try:    
        UpdatedPatient.emergencyContactNames[2] = (self.PersonalTab.EmergencyName3Note.get())
        UpdatedPatient.emergencyContactNumbers[2] = (self.PersonalTab.EmergencyPhone3Note.get()) 
    except IndexError or AttributeError:
        if(self.PersonalTab.EmergencyName3Note.get() != "" and self.PersonalTab.EmergencyPhone3Note.get() != ""):
            UpdatedPatient.addEmergencyContact(self.PersonalTab.EmergencyName3Note.get(), self.PersonalTab.EmergencyPhone3Note.get()) 
            




#approved visitors
    try:    
        UpdatedPatient.allowedVisitors[0] = (self.PersonalTab.ApprovedVisitor1Note.get())
    except IndexError or AttributeError:
        if((self.PersonalTab.ApprovedVisitor1Note.get()) != ""):
            UpdatedPatient.allowedVisitors.append(self.PersonalTab.ApprovedVisitor1Note.get()) 
            
    try:    
        UpdatedPatient.allowedVisitors[1] = (self.PersonalTab.ApprovedVisitor2Note.get())
    except IndexError or AttributeError:
        if((self.PersonalTab.ApprovedVisitor2Note.get()) != ""):
            UpdatedPatient.allowedVisitors.append(self.PersonalTab.ApprovedVisitor2Note.get()) 
            
    try:    
        UpdatedPatient.allowedVisitors[2] = (self.PersonalTab.ApprovedVisitor3Note.get())
    except IndexError or AttributeError:
        if((self.PersonalTab.ApprovedVisitor3Note.get()) != ""):
            UpdatedPatient.allowedVisitors.append(self.PersonalTab.ApprovedVisitor3Note.get()) 
            
    try:    
        UpdatedPatient.allowedVisitors[3] = (self.PersonalTab.ApprovedVisitor4Note.get())
    except IndexError or AttributeError:
        if((self.PersonalTab.ApprovedVisitor4Note.get()) != ""):
            UpdatedPatient.allowedVisitors.append(self.PersonalTab.ApprovedVisitor4Note.get()) 
    
    

    
    try:  
        UpdatedPatient.setInsuranceCarrier(self.BillingTab.InsuranceCarrierNote.get())
        UpdatedPatient.setInsuranceAccountNumber(self.BillingTab.InsuranceAccountNumNote.get())
        UpdatedPatient.setInsuranceGroupNumber(self.BillingTab.InsuranceGroupNumNote.get())   
        
    except AttributeError or NameError:
        pass    
 
    try:
        for i in range(len(UpdatedPatient.listCharges)):
            UpdatedPatient.listCharges[i] = self.BillingTab.ChargeNameNoteList[i].get()
            UpdatedPatient.listChargesAmount[i] = float(self.BillingTab.ChargeAmountNoteList[i].get())       
    except IndexError or AttributeError:
        pass
    
    
    
    
    try:        
        UpdatedPatient.setAmountPaid(float(self.BillingTab.AmountPaidNote.get()))
        UpdatedPatient.setAmountOwed(float(self.BillingTab.AmountOwedNote.get()))
        
        UpdatedPatient.setAmountPaidByInsurance(float(self.BillingTab.AmountPaidbyInsuranceNote.get()))
    except ValueError:
        pass
 
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