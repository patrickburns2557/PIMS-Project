import GUI.MainWindow
import Data.System

# Use this file to start PIMS

Data.System.initialize()

window = GUI.MainWindow.MainWindow(Data.System.getPatientList(), Data.System.getUser())



window.mainloop()
