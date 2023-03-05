from Data.Printer import Printer
from Data.dataClasses import Patient

patientList = []
ptr = Printer()
#ptr.printPatients() #uncomment to test a empty patient list
for i in range(10):
    first = "first " + str(i)
    last = "last " + str(i)
    location = "location " + str(i)
    p = Patient(first,last,[location, "floor", "room", "bed"])
    #p.setFirstName() ; p.setLastname() ; p.setLocation()
    patientList.append(p)
    #ptr.addPatient(patientList)
    ptr.addPatient(p)
ptr.printPatients()




