import GUI.ScrollablePatientList as spl
import GUI.PatientDetailedView as pdv
import GUI.ListView as lv
from Data.dataClasses import *
import tkinter as tk
import tkinter.ttk as ttk
import GUI.utility as guiUtil

guiUtil.initialize()

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

p = Patient()
p.setFirstName("Richard") ; p.setLastname("jackson") ; p.setLocation(["down the hall", "floor", "room", "bed"])
guiUtil.patientList.append(p)
p = Patient()
p.setFirstName("Amy") ; p.setLastname("Jones") ; p.setLocation(["first floor", "floor", "room", "bed"])
guiUtil.patientList.append(p)
p = Patient()
p.setFirstName("patrick") ; p.setLastname("burns") ; p.setLocation(["up the hall", "floor", "room", "bed"])
guiUtil.patientList.append(p)
p = Patient()
p.setFirstName("My First Name") ; p.setLastname("MyLastName") ; p.setLocation(["My Location", "floor", "room", "bed"])
guiUtil.patientList.append(p)
for i in range(50):
    first = "first " + str(i)
    last = "last " + str(i)
    location = "location " + str(i)
    p = Patient()
    p.setFirstName(first) ; p.setLastname(last) ; p.setLocation([location, "floor", "room", "bed"])
    guiUtil.patientList.append(p)


topLabel = tk.Button(guiUtil.window,text="DetailedViewTest",font=("Arial", 20), command=lambda: guiUtil.switch(2))
#bottomLabel = tk.Button(window,text="Create 5",font=("Arial", 20), command=lambda: create5())
#leftLabel = tk.Button(window,text="Create\n10",font=("Arial", 20), command=lambda: create10())
#rightLabel = tk.Button(window,text="Create\n50",font=("Arial", 20), command=lambda: create50())
topLabel.grid(row=0, column=1)
#bottomLabel.grid(row=2, column=1)
#leftLabel.grid(row=1, column=0)
#rightLabel.grid(row=1, column=2)

#currentView = spl.ScrollablePatientList(window, patientList)
guiUtil.currentView = lv.ListView(guiUtil.window, guiUtil.patientList)
#scroll.pack(fill="both", expand=True)

guiUtil.currentView.grid(row=1, column=1, sticky="news")

guiUtil.window.grid_rowconfigure(1, weight=1)
guiUtil.window.grid_columnconfigure(1, weight=1)

guiUtil.window.mainloop()