import GUI.MainWindow
import Data.System


Data.System.initialize()

window = GUI.MainWindow.MainWindow(Data.System.getPatientList(), Data.System.getUser())

window.mainloop()
