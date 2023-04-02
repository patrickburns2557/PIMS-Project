from Data.sqlConnector import *
from Data.dataClasses import *

class addNewPatients():

    def __init__(self):

        self.db = myConnector()
        self.ID = self.db.checkRowCount()

    def newPatient(self, patient):

        # add row for new patient
        self.db.execute("INSERT into patients (patient_ID) VALUES (" + str(self.ID) + ")")

        # add personal info
        self.db.update("first_name", patient.firstName, self.ID)
        self.db.update("middle_name", patient.middleName, self.ID)
        self.db.update("last_name", patient.lastName, self.ID)

        self.db.update("address_street", patient.address[0], self.ID)
        self.db.update("address_city", patient.address[1], self.ID)
        self.db.update("address_zip", patient.address[2], self.ID)
        self.db.update("address_state", patient.address[3], self.ID)

        self.db.update("home_phone", patient.homePhone, self.ID)
        self.db.update("work_phone", patient.workPhone, self.ID)
        self.db.update("mobile_phone", patient.mobilePhone, self.ID)

        if patient.emergencyContactNames:
            self.db.update("emergency1_name", patient.emergencyContactNames[0], self.ID)
            self.db.update("emergency1_number", patient.emergencyContactNumbers[0], self.ID)
            self.db.update("emergency2_name", patient.emergencyContactNames[1], self.ID)
            self.db.update("emergency2_number", patient.emergencyContactNumbers[1], self.ID)

        # add medical info

        self.db.update("date_of_admittance", patient.dateAdmittance, self.ID)
        self.db.update("time_of_admittance", patient.timeAdmittance, self.ID)
        self.db.update("reason_for_admission", patient.reasonAdmission, self.ID)

        self.db.update("family_doctor", patient.familyDoctor, self.ID)
        self.db.update("discharge_date", patient.dateDischarge, self.ID)
        self.db.update("discharge_time", patient.timeDischarge, self.ID)

        self.doctorNotes = patient.doctorNotes
        self.notesString = ""
        for self.note in self.doctorNotes:
            self.notesString = self.notesString + self.note + "\n"

        self.db.update("doctor_treatment_notes", self.notesString, self.ID)

        self.nurseNotes = patient.nurseNotes
        self.notesString = ""
        for self.note in self.nurseNotes:
            self.notesString = self.notesString + self.note + "\n"

        self.db.update("nurse_treatment_notes", self.notesString, self.ID)

        self.prescriptionName = patient.prescriptionNames
        self.nameString = ""
        for self.name in self.prescriptionName:
            self.nameString = self.nameString + self.name + "\n"

        self.db.update("prescription_name", self.nameString, self.ID)

        self.prescriptionAmount = patient.prescriptionAmount
        self.amountString = ""
        for self.amount in self.prescriptionAmount:
            self.amountString = self.amountString + self.amount + "\n"

        self.db.update("prescription_amount", self.amountString, self.ID)

        self.prescriptionSchedule = patient.prescriptionSchedule
        self.scheduleString = ""
        for self.schedule in self.prescriptionSchedule:
            self.scheduleString = self.scheduleString + self.schedule + "\n"

        self.db.update("prescription_schedule", self.scheduleString, self.ID)

        self.procedures = patient.scheduledProcedures
        self.procedureString = ""
        for self.procedure in self.procedures:
            self.procedureString = self.procedureString + self.procedure + "\n"

        self.db.update("scheduled_procedures", self.procedureString, self.ID)

        # add location info

        self.db.update("facility_name", patient.locationFacility, self.ID)
        self.db.update("floor_number", patient.locationFloor, self.ID)
        self.db.update("room_number", patient.locationRoom, self.ID)
        self.db.update("bed_number", patient.locationBed, self.ID)

        self.db.update("allowed_visitor_amount", patient.numAllowedVisitors, self.ID)

        self.visitors = patient.allowedVisitors
        self.visitorString = ""
        for self.visitor in self.visitors:
            self.visitorString.append(self.visitor + "\n")

        self.db.update("allowed_visitor_names", self.visitorString, self.ID)

        self.db.update("insurance_carrier", patient.insuranceCarrier, self.ID)
        self.db.update("insurance_account_number", patient.insuranceAccountNumber, self.ID)
        self.db.update("insurance_group_number", patient.insuranceGroupNumber, self.ID)

        # add billing info
        
        self.chargeNames = patient.listCharges
        self.nameString = ""
        for self.name in self.chargeNames:
            self.nameString = self.nameString + self.name + "\n"

        self.db.update("billing_items_name", self.nameString, self.ID)
        
        self.chargeAmounts = patient.listChargesAmount
        self.amountString = ""
        for self.amount in self.chargeAmounts:
            self.amount = str(self.amount)
            self.amountString = self.amountString + self.amount + "\n"

        self.db.update("billing_items_amount", self.amountString, self.ID)

        self.db.update("amount_owed", patient.amountOwed, self.ID)
        self.db.update("amount_paid", patient.amountPaid, self.ID)
        self.db.update("paid_by_insurance", patient.amountPaidByInsurance, self.ID)