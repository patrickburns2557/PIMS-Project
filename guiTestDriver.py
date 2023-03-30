import GUI.MainWindow
from Data.dataClasses import *
import Data.System
import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk


Data.System.initialize()


window = GUI.MainWindow.MainWindow(Data.System.getPatientList(), Data.System.getUser())

testText = ctk.CTkLabel(window, text="Testing Buttons:", font=("Arial", 20))
testText.grid(row=0, column=1, sticky="e")

lightButton = ctk.CTkButton(window, text="Light mode", font=("Arial", 20), command=lambda:ctk.set_appearance_mode("light"))
lightButton.grid(row=0, column=4, padx=2, pady=2)
darkButton = ctk.CTkButton(window, text="Dark mode", font=("Arial", 20), command=lambda:ctk.set_appearance_mode("dark"))
darkButton.grid(row=0, column=5, padx=2, pady=2)

bigScaleButton = ctk.CTkButton(window, text="Bigger scaling", font=("Arial", 20), command=lambda:ctk.set_widget_scaling(1.2))
bigScaleButton.grid(row=0, column=6, padx=2, pady=2)
smallScaleButton = ctk.CTkButton(window, text="Smaller scaling", font=("Arial", 20), command=lambda:ctk.set_widget_scaling(1))
smallScaleButton.grid(row=0, column=7, padx=2, pady=2)

userButton = ctk.CTkButton(window, text="PrintUserInfo", font=("Arial", 20), command=lambda:print("Type: " + str(Data.System.getUserType())))
userButton.grid(row=0, column=8, padx=2, pady=2)

logoutButton = ctk.CTkButton(window, text="Logout", font=("Arial", 20), command=lambda:[Data.System.logoutUser(), GUI.MainWindow.switchLoginView(Data.System.getUser())])
logoutButton.grid(row=0, column=9, padx=2, pady=2)


window.mainloop()
