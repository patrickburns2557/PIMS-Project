import tkinter as tk
import tkinter.ttk as ttk
import GUI.MainWindow

#individual patient list entry to be used in ScrollablePatientList
class SinglePatientListWidget(tk.Frame):
    numInstances = 0
    def __init__(self, parentWidget, patient):
        #make every other one have a gray background
        SinglePatientListWidget.numInstances += 1
        if SinglePatientListWidget.numInstances % 2 == 1:
            super().__init__(parentWidget, bg="grey")
        else:
            super().__init__(parentWidget)

        self.patient = patient

        #frame to hold the label
        self.firstNameFrame = tk.Frame(
            self,
            relief=tk.RAISED,
            borderwidth=1,
            bg="black"
        )
        self.firstNameFrame.grid(row=0,column=0, padx=3, pady=3)
        try:
            self.firstNameButton = tk.Button(
                self.firstNameFrame,
                text=self.patient.firstName,
                width=20,
                anchor="w",
                justify=tk.LEFT,
                command=lambda: GUI.MainWindow.switchDetailedView(self.patient)
            )
            self.firstNameButton.pack(padx=2, pady=2)
        except:#placeholder text if the first name fails to load
            self.firstNameLabel = tk.Label(
                self.firstNameFrame,
                text="FIRST NAME",
                width=20,
                anchor="w",
                justify=tk.LEFT
            )
            self.firstNameLabel.pack(padx=2, pady=2)
        

        #frame to hold the label
        self.lastNameFrame = tk.Frame(
            self,
            relief=tk.RAISED,
            borderwidth=1,
            bg="black"
        )
        self.lastNameFrame.grid(row=0,column=1, padx=3, pady=3)
        try:
            self.lastNameLabel = tk.Label(
                self.lastNameFrame,
                text=self.patient.lastName,
                width=20,
                anchor="w",
                justify=tk.LEFT
            )
            self.lastNameLabel.pack(padx=2, pady=2)
        except: #placeholder text if the last name fails to load
            self.lastNameLabel = tk.Label(
            self.lastNameFrame,
            text="LAST NAME",
            width=20,
            anchor="w",
            justify=tk.LEFT
            )
            self.lastNameLabel.pack(padx=2, pady=2)


        #space in between last name and location
        #make sure the spacer is the same color as the grid behind it
        if SinglePatientListWidget.numInstances % 2 == 1:
            self.spacer = tk.Frame(
                self,
                width=300,
                bg="grey"
            )
        else:
            self.spacer = tk.Frame(
                self,
                width=300,
            )
        self.spacer.grid(row=0,column=2, padx=0, pady=3, sticky="news")

        #frame to hold the label
        self.locationFrame = tk.Frame(
            self,
            relief=tk.RAISED,
            borderwidth=1,
            bg="black"
        )

        self.locationFrame.grid(row=0,column=3, padx=3, pady=3)
        try:
            self.locationLabel = tk.Label(
                self.locationFrame,
                text=(self.patient.location[0] + "\n" + self.patient.location[1] + "\n" + self.patient.location[2] + "\n" + self.patient.location[3]),
                width=20,
                anchor="w",
                justify=tk.LEFT
            )
            self.locationLabel.pack(padx=2, pady=2)
        except:#placeholder text if the location fails to load
            self.locationLabel = tk.Label(
            self.locationFrame,
            text="LOCATION",
            width=20,
            anchor="w",
            justify=tk.LEFT
            )
            self.locationLabel.pack(padx=2, pady=2)
        
        #Resize the spacer to fill any extra window size
        self.grid_columnconfigure(2, weight=1)

#reuse the SinglePatientListWidget to be the label at the top of the list
class PatientListTopLabel(SinglePatientListWidget):
    def __init__(self, parentWidget):
        frontColor = "#ffffff"
        backColor = "#889dcd"
        super().__init__(parentWidget, "")
        self.firstNameLabel.config(bg=backColor, fg=frontColor)
        self.lastNameLabel.config(bg=backColor, fg=frontColor)
        self.locationLabel.config(bg=backColor, fg=frontColor)
        self.spacer.config(bg=backColor)
        self.endSpacer = tk.Label(self, width=1, bg=backColor)
        self.endSpacer.grid(row=0, column=4, padx=3, pady=3)
        self.config(bg=backColor)



#Class to create a scrollable list of patient names given a list of Patient objects
class ScrollablePatientList(tk.Frame):
    def __init__(self, parent, patientList):
        tk.Frame.__init__(self, parent)
        self.propagate(False)
        #create a canvas that will be used to scroll on
        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        #Scrollbar to scroll the canvas
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        #frame to put widgets in that will be put in the canvas
        #since the frame itself is unable to be scrolled
        scrollable_frame = ttk.Frame(self.canvas)

        #change the canvas scroll region anytime the scrollable frame changes
        scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        #make the canvas update it's position when mousewheel is moved
        scrollable_frame.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

        #tell the canvas to draw the scrollable_frame
        self.canvas.create_window((0,0), window=scrollable_frame, anchor="n", tags="scrollable_frame")
        
        #Resize the canvas window to fill the size of the canvas anytime the canvas size changes
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig("scrollable_frame", width=self.canvas.winfo_width()))
        
        #tell the scrollbar to move when the y-position of the canvas changes
        self.canvas.configure(yscrollcommand=scrollbar.set)

        #Load in the patients to list
        PatientListTopLabel(self).pack(side=tk.TOP, fill="both", expand=False)
        for p in patientList:
            patient = SinglePatientListWidget(scrollable_frame, p)
            patient.pack(fill="both", expand=True)
        
        
        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        