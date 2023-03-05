import tkinter as tk
import Data.dataClasses as dc
import GUI.PatientDetailedView as pdv
import GUI.ListView as lv

patientList = None
currentView = None
window = None

def initialize():
    global window
    global patientList
    global currentView

    patientList = []
    currentView = 0 #will probably initialize to the login screen on startup
    window = tk.Tk()
    window.geometry("1280x720")
    #window.resizable(width=False, height=True)
    window.title(__file__)
    window.iconbitmap('logo.ico')
    window.minsize(1280, 720)

# View = 
# 0 for login screen
# 1 for patient list
# 2 for patient summary
def switch(view):
    global window
    global currentView
    global patientList
    
    currentView.unbind_all("<MouseWheel>") #need to do this anytime the scrollable list is removed
    #and not replaced by another one so that errors don't occur when mouse wheel is scrolled
    
    currentView.destroy()
    #currentView = tk.Label(text="You have been replaced\nby a new frame", font=("Arial", 25))

    if view == 1: 
        currentView = lv.ListView(window, patientList)
        currentView.grid(row=1, column=1, sticky="news")

    if view == 2:
        p1 = dc.Patient()
        p1.setFirstName("Patrick")
        p1.setMiddleName("Wayne")
        p1.setLastname("Burns")
        p1.setAddress(["918 Main Road", "Huntsville", "Alabama", "35776"])
        p1.setHomePhone("555-123-4567")
        p1.setWorkPhone("555-456-7890")
        p1.setMobilePhone("555-789-0234")
        p1.addEmergencyContact("Emergency contact name 1", "555-233-4566")
        p1.addEmergencyContact("Emergency contact name two", "555-455-6788")
        p1.addEmergencyContact("Emergency contact name 3", "555-455-6788")
        p1.setNumAllowedVisitors("3")
        p1.addAllowedVisitor("Visitor 1")
        p1.addAllowedVisitor("Bob Jones")
        p1.addAllowedVisitor("George Washington")
        p1.addAllowedVisitor("Visitor 4")
        p1.setLocation(["up the hall", "floor", "room", "bed"])
        p1.setFamilyDoctor("Dr. Medical Doctor Man")
        p1.setDateAdmittance("January 17, 2020")
        p1.setTimeAdmittance("7:15PM")
        p1.setDateDischarge("April 2, 2020")
        p1.setTimeDischarge("8:20PM")
        p1.setReasonAdmission("Broken Arm")
        p1.addPrescription("Medicine 1", "15mg", "Every Morning")
        p1.addPrescription("Another Medicine", "3mg", "Every Night")
        p1.addScheduledProcedure("Surgery on leg at 3PM")
        p1.addScheduledProcedure("Another surgery at 5PM")
        p1.addDoctorNote("Patient needs medicine")
        p1.addDoctorNote("Patient is doing well")
        p1.addNurseNote("Patient had treatment at 7:15AM")
        p1.addNurseNote("Patient scheduled for surgery tomorrow")
        p1.setInsuranceCarrier("Big Insurance Company")
        p1.setInsuranceAccountNumber("123456789")
        p1.setInsuranceGroupNumber("987654")
        p1.setAmountPaid(481.1891024)
        p1.setAmountPaidByInsurance(15.81870)
        p1.addCharge("Broken leg repaired", 890.1333)
        p1.addCharge("Expensive Medicine administered", 443.145)

        currentView = pdv.PatientDetailedView(window, p1) 
        currentView.grid(row=1, column=1, sticky="news")