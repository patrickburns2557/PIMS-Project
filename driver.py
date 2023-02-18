import GUI.ScrollablePatientList as spl
import GUI.PatientDetailedView as PDV
from Data.dataClasses import *
import tkinter as tk
import tkinter.ttk as ttk

patientList = []
currentView = 0 #will probably initialize to the login screen on startup
window = tk.Tk()
window.geometry("1024x768")
#window.resizable(width=False, height=True)
window.title(__file__)
window.iconbitmap('logo.ico')


def switch():
    global window
    global currentView
    
    currentView.unbind_all("<MouseWheel>") #need to do this anytime the scrollable list is removed
    #and not replaced by another one so that errors don't occur when mouse wheel is scrolled
    
    
    currentView.destroy()
    #currentView = tk.Label(text="You have been replaced\nby a new frame", font=("Arial", 25))
    p1 = Patient("patrick", "burns", "up the hall")

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
        patientList.append(Patient(first, last, location))
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
        patientList.append(Patient(first, last, location))
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
        patientList.append(Patient(first, last, location))
    currentView.destroy()
    currentView = spl.ScrollablePatientList(window, patientList)
    currentView.grid(row=1, column=1, sticky="news")








patientList = []
patientList.append(Patient("Richard", "jackson", "down the hall"))
patientList.append(Patient("patrick", "burns", "up the hall"))
patientList.append(Patient("Amy", "Jones", "first floor"))
patientList.append(Patient("Bob", "Jones", "Third floor"))
patientList.append(Patient("My First Name", "My Last Name", "My Location"))
for i in range(50):
    first = "first " + str(i)
    last = "last " + str(i)
    location = "location " + str(i)
    patientList.append(Patient(first, last, location))


topLabel = tk.Button(window,text="DetailedViewTest",font=("Arial", 20), command=lambda: switch())
bottomLabel = tk.Button(window,text="Create 5",font=("Arial", 20), command=lambda: create5())
leftLabel = tk.Button(window,text="Create\n10",font=("Arial", 20), command=lambda: create10())
rightLabel = tk.Button(window,text="Create\n50",font=("Arial", 20), command=lambda: create50())
topLabel.grid(row=0, column=1)
bottomLabel.grid(row=2, column=1)
leftLabel.grid(row=1, column=0)
rightLabel.grid(row=1, column=2)



currentView = spl.ScrollablePatientList(window, patientList)
#scroll.pack(fill="both", expand=True)
currentView.grid(row=1, column=1, sticky="news")


#showme.grid(row=0, column=0, sticky="nesw")
#window.grid_rowconfigure(0, weight=1)
#window.grid_columnconfigure(0, weight=1)

#window.grid_columnconfigure(0, weight=0)
#window.grid_columnconfigure(2, weight=0)
#window.grid_rowconfigure(0, weight=0)
#window.grid_rowconfigure(2, weight=0)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)





window.mainloop()