import GUI.MainWindow
import Data.System

# use this file to start PIMS

Data.System.initialize()

window = GUI.MainWindow.MainWindow(Data.System.getPatientList(), Data.System.getUser())

window.mainloop()
