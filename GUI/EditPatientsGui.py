import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk
import GUI.ScrollablePatientList as spl
import Data.System
import GUI.MainWindow as MainWindow
from Data.dataClasses import Patient
import Data.validateInfo


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
        self.PersonalTab = PersonalInfoTab(self, CurrentPatient)
        self.shownTab = self.PersonalTab
        self.in_personal = 1
        self.in_billing = 0
        
        
        
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
            command=lambda:MainWindow.switchDetailedView(CurrentPatient)
       )
        self.returnButton.grid(row=0, column=0, padx=5, pady=5)
        self.SaveButton = ctk.CTkButton(
            self.buttonFrame,
            text="Save Patient",
            font=FONTBUTTON,
            width=100,
            height=40,
            command=lambda:finalizePatient(self,CurrentPatient)
       )
        self.SaveButton.grid(row=0, column=4, padx=5, pady=5)    
    
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
        
        if(self.in_billing == 1 ):
            self.BillingTab = self.shownTab

        self.PersonalTab = PersonalInfoTab(self, CurrentPatient)
        self.shownTab = self.PersonalTab
        self.shownTab.grid(row=1, column=0, sticky="news")
        self.in_personal = 1
        self.in_billing = 0


 


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
        
        if(self.in_personal == 1 ):
            self.PersonalTab = self.shownTab
        
        self.BillingTab = BillingInfoTab(self, CurrentPatient)
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

    
            #self.addNoteFrame.grid(row=4, column=2, sticky="nw", padx=PADSECTION, pady=PADSECTION)
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
            font=FONTINFO,
            width=350,
            textvariable=self.MobilePhoneNote
        )
        self.addMobilePhoneEntry.grid(row=11, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)

            
    
        LabelBorder(self.addNoteFrame, "Home Phone Entry").grid(row=12, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.HomePhoneNote = ctk.StringVar(value = patient.homePhone)
        self.addHomePhoneEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.HomePhoneNote
        )
        self.addHomePhoneEntry.grid(row=13, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)

            
        LabelBorder(self.addNoteFrame, "Work Phone Entry").grid(row=14, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.WorkPhoneNote = ctk.StringVar(value = patient.workPhone)
        self.addWorkPhoneEntry = ctk.CTkEntry(
            self.addNoteFrame,
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


        
        LabelBorder(self.addNoteFrame, "Insurance Policy Account Number").grid(row=4, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.InsuranceAccountNumNote = ctk.StringVar(value = patient.insuranceAccountNumber)
        self.addInsurancePolicyAccountEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.InsuranceAccountNumNote
        )
        self.addInsurancePolicyAccountEntry.grid(row=5, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)

        
        LabelBorder(self.addNoteFrame, "Insurance Policy Group Number").grid(row=6, column=0, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.InsuranceGroupNumNote = ctk.StringVar(value = patient.insuranceGroupNumber)
        self.addInsuranceGroupEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.InsuranceGroupNumNote
        )
        self.addInsuranceGroupEntry.grid(row=7, column=0, sticky="w", padx=PADCOMP, pady=PADCOMP)

  
        
        LabelBorder(self.addNoteFrame, "Add a Charge").grid(row=1, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        try:
            self.ChargeNote = ctk.StringVar(value = patient.listCharges[0])
        except IndexError:
            self.ChargeNote = ctk.StringVar(value = 0)
        self.addChargeEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.ChargeNote
        )
        self.addChargeEntry.grid(row=2, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)
                
        LabelBorder(self.addNoteFrame, "Add a Charge Amount").grid(row=3, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        try:
            self.ChargeAmountNote = ctk.StringVar(value = patient.listChargesAmount[0])
        except IndexError:
            self.ChargeAmountNote = ctk.StringVar(value = 0)
        self.addChargeAmountEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.ChargeAmountNote
        )
        self.addChargeAmountEntry.grid(row=4, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)

 

        LabelBorder(self.addNoteFrame, "Amount Paid").grid(row=5, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.AmountPaidNote = ctk.StringVar(value = patient.amountPaid)
        self.addAmountPaidEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.AmountPaidNote
        )
        self.addAmountPaidEntry.grid(row=6, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)

 
        LabelBorder(self.addNoteFrame, "Amount paid by Insurance").grid(row=7, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.AmountPaidbyInsuranceNote = ctk.StringVar(value = patient.amountPaidByInsurance)
        self.addAmountPaidInsuranceEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.AmountPaidbyInsuranceNote        

        )
        self.addAmountPaidInsuranceEntry.grid(row=8, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)

        LabelBorder(self.addNoteFrame, "Amount Owed").grid(row=9, column=4, sticky="w", padx=PADLABEL, pady=PADLABEL)
        self.AmountOwedNote = ctk.StringVar(value = patient.amountOwed)
        self.addChargeOwedEntry = ctk.CTkEntry(
            self.addNoteFrame,
            font=FONTINFO,
            width=350,
            textvariable=self.AmountOwedNote
        )
        self.addChargeOwedEntry.grid(row=10, column=4, sticky="w", padx=PADCOMP, pady=PADCOMP)


def finalizePatient(self,UpdatedPatient):
    
    patientCopy = UpdatedPatient

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
        
        
        UpdatedPatient.addCharge(self.BillingTab.ChargeNote.get(), float(self.BillingTab.ChargeAmountNote.get()))
        
        UpdatedPatient.setAmountPaid(float(self.BillingTab.AmountPaidNote.get()))
        UpdatedPatient.setAmountOwed(float(self.BillingTab.AmountOwedNote.get()))
        
        UpdatedPatient.setAmountPaidByInsurance(float(self.BillingTab.AmountPaidbyInsuranceNote.get()))
    except AttributeError or NameError:
        pass   


    # ensure no information exceeds database character limit
    validate = Data.validateInfo.validateInfo()
    validate.checkEntry(UpdatedPatient)
    truthValid, strIssue = validate.checkValidity(UpdatedPatient, False)
    if truthValid == False:
        self.invalidLabel = ctk.CTkLabel(self, text=strIssue, font=("Courier", 18, "bold"))
        self.invalidLabel.place(relx = 0.5, rely = 0.11, anchor = 'center')
        UpdatedPatient = patientCopy
    else:
        MainWindow.switchDetailedView(UpdatedPatient)
        MainWindow.switchPatientList(Data.System.getPatientList())
    
 
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