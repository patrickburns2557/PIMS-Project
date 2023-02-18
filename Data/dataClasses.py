#classes for the program
#Users, patients, login, etc...
#we may want to split this up further

class Patient():
    def __init__(self, firstName, lastName, location):
        self.firstName = firstName
        self.lastName = lastName
        self.location = location