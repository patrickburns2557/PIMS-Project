import tkinter as tk
import tkinter.ttk as ttk


border_effects = {

    "flat": tk.FLAT,

    "sunken": tk.SUNKEN,

    "raised": tk.RAISED,

    "groove": tk.GROOVE,

    "ridge": tk.RIDGE,

}


window = tk.Tk()

window.geometry("800x600")
#window.resizable(width=False, height=True)
window.wm_attributes('-transparentcolor', 'purple')


#individual patient list entry
class patientListWidget(tk.Frame):
    numInstances = 0
    def __init__(self, parentWidget, firstName, lastName, location):
        #make every other one have a gray background
        patientListWidget.numInstances += 1
        if patientListWidget.numInstances % 2 == 1:
            super().__init__(parentWidget, bg="grey")
        else:
            super().__init__(parentWidget)
        

        #frame to hold the label
        firstNameFrame = tk.Frame(
            self,
            relief=tk.RAISED,
            borderwidth=1,
            bg="orange"
        )
        firstNameFrame.grid(row=0,column=0, padx=3, pady=3)
        firstNameLabel = tk.Label(
            firstNameFrame,
            text=firstName,
            width=20,
            anchor="w",
            justify=tk.LEFT,
            #bg="purple"
        )
        firstNameLabel.pack(padx=2, pady=2)

        #frame to hold the label
        lastNameFrame = tk.Frame(
            self,
            relief=tk.RAISED,
            borderwidth=1,
            bg="blue"
        )
        lastNameFrame.grid(row=0,column=1, padx=3, pady=3)
        lastNameLabel = tk.Label(
            lastNameFrame,
            text=lastName,
            width=20,
            anchor="w",
            justify=tk.LEFT,
            #bg="purple"
        )
        lastNameLabel.pack(padx=2, pady=2)


        #space in between last name and location
        spacer = tk.Frame(
            self,
            relief=tk.RAISED,
            borderwidth=1,
            bg="yellow",
            width=300
        )
        spacer.grid(row=0,column=2, padx=3, pady=3)


        #frame to hold the label
        locationFrame = tk.Frame(
            self,
            relief=tk.RAISED,
            borderwidth=1,
            bg="green"
        )
        locationFrame.grid(row=0,column=3, padx=3, pady=3)
        locationLabel = tk.Label(
            locationFrame,
            text=location,
            width=20,
            anchor="w",
            justify=tk.LEFT,
            #bg="purple"
        )
        locationLabel.pack(padx=2, pady=2)


class Patient():
    def __init__(self, firstName, lastName, location):
        self.firstName = firstName
        self.lastName = lastName
        self.location = location



#scrollable list example: https://stackoverflow.com/questions/3085696/adding-a-scrollbar-to-a-group-of-widgets-in-tkinter/3092341#3092341
class Example(tk.Frame):
    #take in parameters for parent widget and a list of patients
    def __init__(self, parent, patientList):

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        self.populate(patientList)

    def populate(self, patientList):
        for p in patientList:
            patient = patientListWidget(self.frame, p.firstName, p.lastName, p.location)
            patient.pack()
        

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")





patientList = []
patientList.append(Patient("richard", "jackson", "down the hall"))
patientList.append(Patient("patrick", "burns", "up the hall"))
patientList.append(Patient("Amy", "Jones", "first floor"))
patientList.append(Patient("Bob", "Jones", "Third floor"))
patientList.append(Patient("My First Name", "My Last Name", "My Location"))
for i in range(50):
    first = "first " + str(i)
    last = "last " + str(i)
    location = "location " + str(i)
    patientList.append(Patient(first, last, location))

showme = Example(window, patientList)
showme.pack(side="left", fill="both", expand=True)

#p1 = Patient("testfirst", "testlast", "testlocation")
#wid = patientListWidget(window, p1.firstName, p1.lastName, p1.location).pack()

window.mainloop()