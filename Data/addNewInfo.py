from Data.sqlConnector import *
from Data.dataClasses import *

class addNewInfo():

    def __init__(self):

        self.db = myConnector()

    def updatePatient(self, patient, new):

        if new == True:
            self.ID = self.db.checkRowCount()
            # add row for patient if new
            self.db.execute("INSERT into patients (patient_ID) VALUES (" + str(self.ID) + ")")
            # else, get id of patient being updated
        else:
            self.ID = self.db.getID("patient_ID", patient.ID)

        # update personal info
        self.db.update("first_name", patient.firstName, self.ID)
        self.db.update("middle_name", patient.middleName, self.ID)
        self.db.update("last_name", patient.lastName, self.ID)

        self.db.update("address_street", patient.address[0], self.ID)
        self.db.update("address_city", patient.address[1], self.ID)
        self.db.update("address_state", patient.address[2], self.ID)
        self.db.update("address_zip", patient.address[3], self.ID)

        self.db.update("home_phone", patient.homePhone, self.ID)
        self.db.update("work_phone", patient.workPhone, self.ID)
        self.db.update("mobile_phone", patient.mobilePhone, self.ID)

        if patient.emergencyContactNames:
            self.db.update("emergency1_name", patient.emergencyContactNames[0], self.ID)
            self.db.update("emergency1_number", patient.emergencyContactNumbers[0], self.ID)
            self.db.update("emergency2_name", patient.emergencyContactNames[1], self.ID)
            self.db.update("emergency2_number", patient.emergencyContactNumbers[1], self.ID)

        # update location info

        self.db.update("facility_name", patient.location[0], self.ID)
        self.db.update("floor_number", patient.location[1], self.ID)
        self.db.update("room_number", patient.location[2], self.ID)
        self.db.update("bed_number", patient.location[3], self.ID)

        self.db.update("allowed_visitor_amount", patient.numAllowedVisitors, self.ID)

        self.visitors = patient.allowedVisitors
        self.visitorString = ""
        for self.visitor in self.visitors:
            if self.visitor != self.visitors[0]:
                self.visitorString += "\n"
            self.visitorString = self.visitorString + self.visitor

        self.db.update("allowed_visitor_names", self.visitorString, self.ID)

        self.db.update("insurance_carrier", patient.insuranceCarrier, self.ID)
        self.db.update("insurance_account_number", patient.insuranceAccountNumber, self.ID)
        self.db.update("insurance_group_number", patient.insuranceGroupNumber, self.ID)

        # update billing info

        self.chargeNames = patient.listCharges
        self.nameString = ""
        for self.name in self.chargeNames:
            if self.name != self.chargeNames[0]:
                self.nameString += "\n"
            self.nameString = self.nameString + self.name

        self.db.update("billing_items_name", self.nameString, self.ID)
        
        self.chargeAmounts = patient.listChargesAmount
        self.amountString = ""
        for self.amount in self.chargeAmounts:
            if self.amount != self.chargeAmounts[0]:
                self.amountString += "\n"
            self.amount = str(self.amount)
            self.amountString = self.amountString + self.amount

        self.db.update("billing_items_amount", self.amountString, self.ID)

        self.db.update("amount_owed", patient.amountOwed, self.ID)
        self.db.update("amount_paid", patient.amountPaid, self.ID)
        self.db.update("paid_by_insurance", patient.amountPaidByInsurance, self.ID)

        # only update medical info if new patient is being added
        if new == True:

            self.db.update("date_of_admittance", patient.dateAdmittance, self.ID)
            self.db.update("time_of_admittance", patient.timeAdmittance, self.ID)
            self.db.update("reason_for_admission", patient.reasonAdmission, self.ID)

            self.db.update("family_doctor", patient.familyDoctor, self.ID)
            self.db.update("discharge_date", patient.dateDischarge, self.ID)
            self.db.update("discharge_time", patient.timeDischarge, self.ID)

            self.doctorNotes = patient.doctorNotes
            self.notesString = ""
            for self.note in self.doctorNotes:
                if self.note != self.doctorNotes[0]:
                    self.notesString += "\n"
                self.notesString = self.notesString + self.note

            self.db.update("doctor_treatment_notes", self.notesString, self.ID)

            self.nurseNotes = patient.nurseNotes
            self.notesString = ""
            for self.note in self.nurseNotes:
                if self.note != self.nurseNotes[0]:
                    self.notesString += "\n"
                self.notesString = self.notesString + self.note

            self.db.update("nurse_treatment_notes", self.notesString, self.ID)

            self.prescriptionName = patient.prescriptionNames
            self.nameString = ""
            for self.name in self.prescriptionName:
                if self.name != self.prescriptionName[0]:
                    self.nameString += "\n"
                self.nameString = self.nameString + self.name

            self.db.update("prescription_name", self.nameString, self.ID)

            self.prescriptionAmount = patient.prescriptionAmount
            self.amountString = ""
            for self.amount in self.prescriptionAmount:
                if self.amount != self.prescriptionAmount[0]:
                    self.amountString += "\n"
                self.amountString = self.amountString + self.amount

            self.db.update("prescription_amount", self.amountString, self.ID)

            self.prescriptionSchedule = patient.prescriptionSchedule
            self.scheduleString = ""
            for self.schedule in self.prescriptionSchedule:
                if self.schedule != self.prescriptionSchedule[0]:
                    self.scheduleString += "\n"
                self.scheduleString = self.scheduleString + self.schedule

            self.db.update("prescription_schedule", self.scheduleString, self.ID)

            self.procedures = patient.scheduledProcedures
            self.procedureString = ""
            for self.procedure in self.procedures:
                if self.procedure != self.procedures[0]:
                    self.procedureString += "\n"
                self.procedureString = self.procedureString + self.procedure

            self.db.update("scheduled_procedures", self.procedureString, self.ID)