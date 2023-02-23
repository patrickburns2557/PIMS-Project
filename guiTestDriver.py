import GUI.ScrollablePatientList as spl
import GUI.PatientDetailedView as PDV
from Data.dataClasses import *
import tkinter as tk
import tkinter.ttk as ttk

patientList = []
currentView = 0 #will probably initialize to the login screen on startup
window = tk.Tk()
window.geometry("1280x720")
#window.resizable(width=False, height=True)
window.title(__file__)
window.iconbitmap('logo.ico')
window.minsize(1280, 720)

def switch():
    global window
    global currentView
    
    currentView.unbind_all("<MouseWheel>") #need to do this anytime the scrollable list is removed
    #and not replaced by another one so that errors don't occur when mouse wheel is scrolled
    
    
    currentView.destroy()
    #currentView = tk.Label(text="You have been replaced\nby a new frame", font=("Arial", 25))
    p1 = Patient()
    p1.setFirstName("patrick")
    p1.setLastname("burns")
    p1.setLocation(["up the hall", "floor", "room", "bed"])

    currentView = PDV.PatientDetailedView(window, p1) 
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
    currentView = spl.ScrollablePatientList(window, patientList)
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
    currentView = spl.ScrollablePatientList(window, patientList)
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
    currentView = spl.ScrollablePatientList(window, patientList)
    currentView.grid(row=1, column=1, sticky="news")








patientList = []
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


topLabel = tk.Button(window,text="DetailedViewTest",font=("Arial", 20), command=lambda: switch())
bottomLabel = tk.Button(window,text="Create 5",font=("Arial", 20), command=lambda: create5())
leftLabel = tk.Button(window,text="Create\n10",font=("Arial", 20), command=lambda: create10())
rightLabel = tk.Button(window,text="Create\n50",font=("Arial", 20), command=lambda: create50())
topLabel.grid(row=0, column=1)
bottomLabel.grid(row=2, column=1)
leftLabel.grid(row=1, column=0)
rightLabel.grid(row=1, column=2)



currentView = spl.ScrollablePatientList(window, patientList)

currentView.grid(row=1, column=1, sticky="news")

window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)





window.mainloop()