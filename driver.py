import ScrollablePatientList as spl
import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()

window.geometry("800x600")
#window.resizable(width=False, height=True)
#window.wm_attributes('-transparentcolor', 'purple')
window.title(__file__)
window.iconbitmap('logo.ico')


patientList = []
patientList.append(spl.Patient("Richard", "jackson", "down the hall"))
patientList.append(spl.Patient("patrick", "burns", "up the hall"))
patientList.append(spl.Patient("Amy", "Jones", "first floor"))
patientList.append(spl.Patient("Bob", "Jones", "Third floor"))
patientList.append(spl.Patient("My First Name", "My Last Name", "My Location"))
for i in range(15):
    first = "first " + str(i)
    last = "last " + str(i)
    location = "location " + str(i)
    patientList.append(spl.Patient(first, last, location))



showme = spl.Example(window, patientList)
showme.pack(side="left", fill="both", expand=True)







window.mainloop()