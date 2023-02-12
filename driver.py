import ScrollablePatientList as spl
from dataClasses import *
import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()

window.geometry("800x600")
#window.resizable(width=False, height=True)
#window.wm_attributes('-transparentcolor', 'purple')
window.title(__file__)
window.iconbitmap('logo.ico')


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



topLabel = tk.Label(
    window,
    text="Top Widget",
    font=("Arial", 20)
)

bottomLabel = tk.Label(
    window,
    text="Bottom Widget",
    font=("Arial", 20)
)

leftLabel = tk.Label(
    window,
    text="Left\nWidget",
    font=("Arial", 20)
)

rightLabel = tk.Label(
    window,
    text="Right\nWidget",
    font=("Arial", 20)
)


topLabel.pack(side=tk.TOP)
bottomLabel.pack(side=tk.BOTTOM)
leftLabel.pack(side=tk.LEFT)
rightLabel.pack(side=tk.RIGHT)


showme = spl.ScrollablePatientList(window, patientList)
showme.pack(fill="both", expand=True)
#showme.grid(row=0, column=0, sticky="nesw")
#window.grid_rowconfigure(0, weight=1)
#window.grid_columnconfigure(0, weight=1)




window.mainloop()