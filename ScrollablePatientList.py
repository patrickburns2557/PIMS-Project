import tkinter as tk
import tkinter.ttk as ttk

#individual patient list entry
class SinglePatientListWidget(tk.Frame):
    numInstances = 0
    def __init__(self, parentWidget, firstName, lastName, location):
        #make every other one have a gray background
        SinglePatientListWidget.numInstances += 1
        if SinglePatientListWidget.numInstances % 2 == 1:
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
            justify=tk.LEFT
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
            justify=tk.LEFT
        )
        lastNameLabel.pack(padx=2, pady=2)

        #space in between last name and location
        #make sure the spacer is the same color as the grid behind it
        if SinglePatientListWidget.numInstances % 2 == 1:
            spacer = tk.Frame(
                self,
                width=300,
                bg="grey"
            )
        else:
            spacer = tk.Frame(
                self,
                width=300,
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
            justify=tk.LEFT
        )
        locationLabel.pack(padx=2, pady=2)
        
        #Resize the spacer to fill any extra window size
        self.grid_columnconfigure(2, weight=1)


        

class PatientListTop(tk.Frame):
    def __init__(self, parentWidget):
        super().__init__(parentWidget)
        color = "#889dcd"
        firstNameLabel = tk.Label(
            self,
            text="FIRST NAME",
            bg=color,
            fg="#ffffff",
            width=20,
            #anchor="w",
            #justify=tk.LEFT,
        )
        firstNameLabel.grid(row=0, column=0, padx=3, pady=3)
        
        lastNameLabel = tk.Label(
            self,
            text="LAST NAME",
            bg=color,
            fg="#ffffff",
            width=20,
            #anchor="w",
            #justify=tk.LEFT
        )
        lastNameLabel.grid(row=0, column=1, padx=3, pady=3)

        spacer = tk.Frame(
            self,
            width=300,
            bg=color
        )
        spacer.grid(row=0, column=2, padx=3, pady=3, sticky="news")

        locationLabel = tk.Label(
            self,
            text="LOCATION",
            bg=color,
            fg="#ffffff",
            width=20,
            #anchor="w",
            #justify=tk.LEFT
        )
        locationLabel.grid(row=0, column=3, padx=3, pady=3)

        self.grid_columnconfigure(2, weight=1)


class PatientList(tk.Frame):
    def __init__(self, parent, patientList):
        tk.Frame.__init__(self, parent)
        #create a canvas that will be used to scroll on
        canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        #Scrollbar to scroll the canvas
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        #frame to put widgets in that will be put in the canvas
        #since the frame itself is unable to be scrolled
        scrollable_frame = ttk.Frame(canvas)

        #change the canvas scroll region anytime the scrollable frame changes
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        #make the canvas update it's position when mousewheel is moved
        scrollable_frame.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

        #tell the canvas to draw the scrollable_frame
        canvas.create_window((0,0), window=scrollable_frame, anchor="n", tags="scrollable_frame")
        
        #Resize the canvas window to fill the size of the canvas anytime the canvas size changes
        canvas.bind("<Configure>", lambda e: canvas.itemconfig("scrollable_frame", width=canvas.winfo_width()))
        
        #tell the scrollbar to move when the y-position of the canvas changes
        canvas.configure(yscrollcommand=scrollbar.set)

        #Load in the patients to list
        PatientListTop(scrollable_frame).pack(fill="both", expand=True)
        for p in patientList:
            patient = SinglePatientListWidget(scrollable_frame, p.firstName, p.lastName, p.location)
            patient.pack(fill="both", expand=True)
        
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)



#patientList = []
#patientList.append(Patient("richard", "jackson", "down the hall"))


