import GUI.MainWindow
import Data.System

Data.System.initialize()

Data.System.loadDatabase()

GUI.MainWindow.MainWindow(Data.System.getPatientList(), Data.System.getUser())
