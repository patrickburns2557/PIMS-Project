import GUI.ScrollablePatientList as spl
import GUI.PatientDetailedView as pdv
import GUI.ListView as lv
import GUI.MainWindow
from Data.dataClasses import *
import tkinter as tk
import tkinter.ttk as ttk

patientList = []


def switch():
    global window
    global currentView
    
    currentView.unbind_all("<MouseWheel>") #need to do this anytime the scrollable list is removed
    #and not replaced by another one so that errors don't occur when mouse wheel is scrolled
    
    
    currentView.destroy()
    #currentView = tk.Label(text="You have been replaced\nby a new frame", font=("Arial", 25))
    

    currentView = pdv.PatientDetailedView(window, p1) 
    currentView.grid(row=1, column=1, sticky="news")



def create5():
    global patientList
    global currentView
    global window
    patientList.clear()
    for i in range(5):
        first = "first " + str(i)
        last = "last " + str(i)
        location = "location " + str(i)
        p = Patient()
        p.setFirstName(first) ; p.setLastname(last) ; p.setLocation([location, "floor", "room", "bed"])
        patientList.append(p)
    currentView.destroy()
    currentView = lv.ListView(window, patientList)
    currentView.grid(row=1, column=1, sticky="news")

def create10():
    global patientList
    global currentView
    global window
    patientList.clear()
    for i in range(10):
        first = "first " + str(i)
        last = "last " + str(i)
        location = "location " + str(i)
        p = Patient()
        p.setFirstName(first) ; p.setLastname(last) ; p.setLocation([location, "floor", "room", "bed"])
        patientList.append(p)
    currentView.destroy()
    currentView = lv.ListView(window, patientList)
    currentView.grid(row=1, column=1, sticky="news")

def create50():
    global patientList
    global currentView
    global window
    patientList.clear()
    for i in range(50):
        first = "first " + str(i)
        last = "last " + str(i)
        location = "location " + str(i)
        p = Patient()
        p.setFirstName(first) ; p.setLastname(last) ; p.setLocation([location, "floor", "room", "bed"])
        patientList.append(p)
    currentView.destroy()
    currentView = lv.ListView(window, patientList)
    currentView.grid(row=1, column=1, sticky="news")








patientList = []
p1 = Patient()
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
patientList.append(p1)
p = Patient()
p.setFirstName("Richard") ; p.setLastname("jackson") ; p.setLocation(["down the hall", "floor", "room", "bed"])
patientList.append(p)
p = Patient()
p.setFirstName("Amy") ; p.setLastname("Jones") ; p.setLocation(["first floor", "floor", "room", "bed"])
patientList.append(p)
p = Patient()
p.setFirstName("patrick") ; p.setLastname("burns") ; p.setLocation(["up the hall", "floor", "room", "bed"])
patientList.append(p)
p = Patient()
p.setFirstName("My First Name") ; p.setLastname("MyLastName") ; p.setLocation(["My Location", "floor", "room", "bed"])
patientList.append(p)
for i in range(50):
    first = "first " + str(i)
    last = "last " + str(i)
    location = "location " + str(i)
    p = Patient()
    p.setFirstName(first) ; p.setLastname(last) ; p.setLocation([location, "floor", "room", "bed"])
    patientList.append(p)


window = GUI.MainWindow.MainWindow(patientList)

topLabel = tk.Button(window,text="DetailedViewTest",font=("Arial", 20), command=lambda: GUI.MainWindow.switchDetailedView(p1))
topLabel.grid(row=0, column=1)

topLabel2 = tk.Button(window, text="List View", font=("Arial", 20), command=lambda: GUI.MainWindow.switchPatientList(patientList))
topLabel2.grid(row=0, column=2)


window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)


window.mainloop()