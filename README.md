Patient Information Management System (PIMS)

# Table of Contents

[Table of Contents]

- [About PIMS]
  - [Details]
  - [System Requirements]
  - [Source Code]
  - [Contributors]
- [Getting Started]
  - [Header]
  - [Login Screen]
- [Application Views]
  - [Patient List View]
  - [Patient Details View]
    - [Adding Doctor Note]
    - [Adding Nurse Note]

# 


# About PIMS


## Details

PIMS is an application for hospitals that easily lets doctors, nurses, office staff, and volunteers create and monitor data for every patient in the hospital.


## System Requirements

- Windows 10 or 11


## Source Code

- Github: <https://github.com/patrickburns2557/CS499Project> 

- Python Version

  - 3.10

- Library Requirements Format: &lt;name> == &lt;version>

  - customtkinter==5.1.2
  - darkdetect==0.8.0
  - mysql-connector-python==8.0.32
  - numpy==1.24.2
  - pandas==2.0.0
  - Pillow==9.5.0
  - protobuf==3.20.3
  - python-dateutil==2.8.2
  - pytz==2023.3
  - six==1.16.0
  - tzdata==2023.3

- To start, run PIMS.py


## Contributors

- Patrick B
- Jackson C
- Brian K
- Madison S
- Bryson W


# Getting Started

Run the PIMS executable.


## Header

The top header buttons will remain constant throughout use of the program. They are as follows:

- Dark Mode toggle

  - Click to toggle between a dark and light theme.

- Increase Scaling toggle

  - Click to enlarge all the text in the application.

- Print

  - This button will only function when a user is logged in. When viewing the list of patients, it will print all the details a user is allowed to view for every patient. When viewing a single patient, it will print all the details a user is allowed to view for only that patient.

- Logout

  - This allows the user to go back to the login screen at any time.


## Login Screen

When the application is launched, the user will be greeted by a login screen. It will require a username and password. Consult the IT admin for login credentials. If you do not have an IT admin try the following credentials:

|             |             |
| ----------- | ----------- |
| Username:   | Password:   |
| doctor      | doctor      |
| nurse       | nurse       |
| officestaff | officestaff |
| volunteer   | volunteer   |

Click Log In when the user has entered a valid username and password. The user will be brought to the patients list view.

To log out and return to the login screen, click the \`logout\` button in the top right corner.


# Application Views


## Patient List View

In this view, the user will see a search box, a way to add patients, and a list of patients.

- Create New Patient

  - This button allows the user to start inputting new patient information.

  - There are three tabs of information to fill out

    - Personal
    - Medical
    - Billing

  - Enter all desired patient information for each tab.

  - When finished, click ‘SavePatient’.

  - The patient information will be saved, and the user will be taken to the Patient List View

- Search box

  - Click on the search box then type in any name. 
  - Click ‘Search’ to only show users with the name you searched for.
  - Delete the text in the search box then click ‘Search’ to show all the users again.

- List of patients

  - This is a list of all patients in the database.
  - All users will be able to view: First, Middle, and Last name. As well as Facility, Floor, Room, and Bed.
  - Click on any name to open the Patients Details View.


## Patient Details View

In this view, the user will be able to see different information about a patient based on what privileges their user type has described below. Depending on the user, they will be able to see different tabs. Clicking on a tab will display different information described below. The user will also be able to see a second print button next to the patient’s name.

Back:

- This button will return to the Patient List View.

Print:

- This button will only print the information shown on the specific tab for the currently viewed user.

Tabs:

- Personal Information

  - firstName 
  - middleName 
  - lastName 
  - address 
  - homePhone 
  - workPhone 
  - mobilePhone 
  - emergencyContactNames 
  - emergencyContactNumbers
  - location 
  - locationFacility
  - locationFloor 
  - locationRoom 
  - locationBed 
  - numAllowedVisitors
  - allowedVisitors


- Medical Information

  - dateAdmittance 
  - timeAdmittance 
  - reasonAdmission 
  - familyDoctor 
  - dateDischarge 
  - timeDischarge 
  - doctorNotes 
  - nurseNotes  
  - prescriptionNames 
  - prescriptionAmount 
  - prescriptionSchedule
  - scheduledProcedures


- Billing Information

  - insuranceCarrier 
  - insuranceAccountNumber
  - insuranceGroupNumber
  - listCharges 
  - listChargesAmount 
  - amountPaid 
  - amountOwed 
  - amountPaidByInsurance

Privileges:

- Doctor

  - Will be able to view all information on a patient
  - Will be able to create doctor’s notes

- Nurse

  - Will be able to view all information on a patient
  - Will be able to create nurse’s notes

- Office Staff

  - Will be able to view patient personal information 
  - Will be able to view billing information
  - Will be able to edit personal and billing information

- Volunteers

  - Will be able to view patient personal information


### Adding Doctor Note

- Ensure you are logged in as a doctor
- Click on a patient’s name to enter the patient detailed view
- Click on the \`Medical Information\` tab
- Look for the \`Add New Note\` section
- Type a note into the text box
- Click \`Add\`
- The note will be appended to the \`Doctor Notes\` section


### Adding Nurse Note

- Ensure you are logged in as a nurse
- Click on a patient’s name to enter the patient detailed view
- Click on the \`Medical Information\` tab
- Look for the \`Add New Note\` section
- Type a note into the text box
- Click \`Add\`
- The note will be appended to the \`Nurse Notes\` section
