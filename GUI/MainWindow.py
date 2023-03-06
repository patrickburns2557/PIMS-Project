import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk
import GUI.ScrollablePatientList as spl
import GUI.PatientDetailedView as pdv
import GUI.ListView as lv
from Data.dataClasses import *

class MainWindow(ctk.CTk):
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("dark-blue")
    #print(ctk.get_appearance_mode())
    window = None #Class variable to hold itself in so that other classes can make calls to the MainWindow class and change the window's views
    def __init__(self, patientList):
        super().__init__()
        MainWindow.window = self #Store self into class variable upon creation

        self.geometry("1280x720")
        #window.resizable(width=False, height=True)
        #self.title(__file__)
        self.title("Patient Information Management System (PIMS)")
        #Skip loading window icon if it fails since it's not strictly necessary
        try:
            self.iconbitmap('./logo.ico')
        except:
            pass
        self.minsize(1280, 720)
        
        self.currentView = lv.ListView(self, patientList) #Default view when starting program
        self.currentView.grid(row=1, column=1, sticky="news", columnspan=10)

#Function to allow other classes to change the current view in the window to PatientDetailedView
def switchDetailedView(patient):
    MainWindow.window.currentView.destroy()

    MainWindow.window.currentView = pdv.PatientDetailedView(MainWindow.window, patient) 
    MainWindow.window.currentView.grid(row=1, column=1, sticky="news",columnspan=10)

def switchPatientList(patientList):
    MainWindow.window.currentView.destroy()

    MainWindow.window.currentView = lv.ListView(MainWindow.window, patientList)
    MainWindow.window.currentView.grid(row=1, column=0, sticky="news", columnspan=10)
