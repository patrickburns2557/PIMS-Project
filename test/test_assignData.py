#!/usr/bin/python
from Data.AssignData import *


def test_loadPatientList():
    list = patientList()
    list.createList()
    records = list.getList()

    assert records[0].firstName == "Sophia"
    assert records[0].amountPaidByInsurance == 0.00
    assert records[1].firstName == "Benjamin"
    assert records[1].amountPaidByInsurance == 0.00
