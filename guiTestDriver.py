import GUI.ScrollablePatientList as spl
import GUI.PatientDetailedView as pdv
import GUI.ListView as lv
import GUI.MainWindow
from Data.dataClasses import *
import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk



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
p1.setLocation(["Facility 7", "Floor 2", "Room 213", "Bed 1"])
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
p.setFirstName("Richard") ; p.setLastname("jackson") ; p.setLocation(["Facility 3", "Floor 1", "Room 12", "Bed 2"])
patientList.append(p)
p = Patient()
p.setFirstName("Amy") ; p.setLastname("Jones") ; p.setLocation(["Facility 1", "Floor 4", "Room 419", "Bed 1"])
patientList.append(p)
p = Patient()
p.setFirstName("patrick") ; p.setLastname("burns") ; p.setLocation(["Facility 1", "Floor 3", "Room 363", "Bed 3"])
patientList.append(p)
p = Patient()
p.setFirstName("My First Name") ; p.setLastname("MyLastName") ; p.setLocation(["My Facility", "My Floor", "My Room", "My Bed"])
patientList.append(p)
for i in range(20):
    first = "first " + str(i)
    last = "last " + str(i)
    location = "location " + str(i)
    p = Patient()
    p.setFirstName(first) ; p.setLastname(last) ; p.setLocation([location, "floor", "room", "bed"])
    patientList.append(p)


window = GUI.MainWindow.MainWindow(patientList)

testText = ctk.CTkLabel(window, text="Testing Buttons:", font=("Arial", 20))
testText.grid(row=0, column=1, sticky="e")

detailButton = ctk.CTkButton(window,text="DetailedViewTest",font=("Arial", 20), command=lambda: GUI.MainWindow.switchDetailedView(p1))
detailButton.grid(row=0, column=2, padx=2, pady=2)


listButton = ctk.CTkButton(window, text="List View", font=("Arial", 20), command=lambda: GUI.MainWindow.switchPatientList(patientList))
listButton.grid(row=0, column=3, padx=2, pady=2)

lightButton = ctk.CTkButton(window, text="Light mode", font=("Arial", 20), command=lambda:ctk.set_appearance_mode("light"))
lightButton.grid(row=0, column=4, padx=2, pady=2)
darkButton = ctk.CTkButton(window, text="Dark mode", font=("Arial", 20), command=lambda:ctk.set_appearance_mode("dark"))
darkButton.grid(row=0, column=5, padx=2, pady=2)

window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)


window.mainloop()
