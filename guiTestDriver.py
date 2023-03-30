import GUI.MainWindow
from Data.dataClasses import *
import Data.System
import Data.Printer
import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk


Data.System.initialize()


window = GUI.MainWindow.MainWindow(Data.System.getPatientList(), Data.System.getUser())

testText = ctk.CTkLabel(window, text="Testing Buttons:", font=("Arial", 20))
testText.grid(row=0, column=1, sticky="e")

#Move this to the top bar class when that's made
switchVar = ctk.StringVar(value="off")
def switchAppearance():
    if switchVar.get() == "on":
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")
switch = ctk.CTkSwitch(window, text="Dark Mode", command=switchAppearance, variable=switchVar, onvalue="on", offvalue="off", font=("Arial", 20))
switch.grid(row=0, column=3, padx=2, pady=2)


#lightButton = ctk.CTkButton(window, text="Light mode", font=("Arial", 20), command=lambda:ctk.set_appearance_mode("light"))
#lightButton.grid(row=0, column=4, padx=2, pady=2)
#darkButton = ctk.CTkButton(window, text="Dark mode", font=("Arial", 20), command=lambda:ctk.set_appearance_mode("dark"))
#darkButton.grid(row=0, column=5, padx=2, pady=2)

#Move this to the top bar class when that's made
switchVarScale = ctk.StringVar(value="off")
def switchScaling():
    if switchVarScale.get() == "on":
        ctk.set_widget_scaling(1.2)
    else:
        ctk.set_widget_scaling(1.0)
switchScale = ctk.CTkSwitch(window, text="Increase Scaling", command=switchScaling, variable=switchVarScale, onvalue="on", offvalue="off", font=("Arial", 20))
switchScale.grid(row=0, column=4, padx=2, pady=2)

#bigScaleButton = ctk.CTkButton(window, text="Bigger scaling", font=("Arial", 20), command=lambda:ctk.set_widget_scaling(1.2))
#bigScaleButton.grid(row=0, column=6, padx=2, pady=2)
#smallScaleButton = ctk.CTkButton(window, text="Smaller scaling", font=("Arial", 20), command=lambda:ctk.set_widget_scaling(1))
#smallScaleButton.grid(row=0, column=7, padx=2, pady=2)

printButton = ctk.CTkButton(window, text="Print", font=("Arial", 20), command=lambda:Data.Printer.initPrint(0))
printButton.grid(row=0, column=8, padx=2, pady=2)

#Move this to the top bar class when that's made
logoutButton = ctk.CTkButton(window, text="Logout", font=("Arial", 20), command=lambda:[Data.System.logoutUser(), GUI.MainWindow.switchLoginView(Data.System.getUser())])
logoutButton.grid(row=0, column=9, padx=2, pady=2)




window.mainloop()
