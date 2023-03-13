create database patient_information;

use patient_information;

create table patients
(patient_ID int, last_name varchar(20), first_name varchar(20), middle_name varchar(20), 
address_street varchar(50), address_city varchar(20), address_state varchar(20), address_zip varchar(20), 
home_phone varchar(20), work_phone varchar(20), mobile_phone varchar(20), 
emergency1_name varchar(50), emergency1_number varchar(20), 
emergency2_name varchar(50), emergency2_number varchar(20), 
date_of_admittance varchar(10), time_of_admittance varchar(10), reason_for_admission varchar(100), 
family_doctor varchar(20), 
facility_name varchar(20),
floor_number varchar(10), room_number varchar(10), bed_number varchar(10),
discharge_date varchar(10), discharge_time varchar(10), 
doctor_treatment_notes text, nurse_treatment_notes text, 
prescription_name text, prescription_amount text, prescription_schedule text, 
scheduled_procedures text, 
insurance_carrier varchar(50), insurance_account_number varchar(20), insurance_group_number varchar(20),
billing_items_name text, billing_items_amount text, amount_paid decimal(10, 2), amount_owed decimal(10, 2), paid_by_insurance decimal(10,2),
allowed_visitor_amount varchar(3), allowed_visitor_names text);

insert into patients values
(0, "Garcia", "Sophia", "Maria", 
"1281 Meadow Ln", "Huntsville", "AL", "35801", 
"(424)-890-9354", "(424)-209-1293", "(424)-108-3280", 
"Vivian Garcia", "(424)-129-3280", 
"Ruben Garcia", "(424)-209-3278",
"26-OCT18", "16:13", "severe chest pain", 
"Dr. Smith", 
"ICU", "5th", "518", "C", "30-OCT18", "12:30",
"Patient experienced heart attack, schedule for coronary angioplasty", 
"Patient experienced severe chest pain and an elevated heart rate. Vitals stable after surgery.", 
"Aspirin\nClopidogrel", "81mg\n75mg", "Twice a day\nOnce a day", 
"coronary angioplasty",
"Blue Cross Blue Shield", "123456789", "BCBS001", 
"Aspirin\nClopidogrel\nsurgery", "530.27\n510.25\n23642.89", 
6500.00, 18183.41, 10500.00,
"1", "Vivian Garcia");

insert into patients values
(1, "Patel", "Benjamin", "David", 
"3579 Pine St", "Athens", "AL", "35614", 
"(845)-643-3296", "(845)-248-1083", "(238)-139-5932", 
"Jaxon Patel", "(378)-103-439", 
"Omar Lucero", "(845)-198-034",
"31-DEC18", "02:38", "allergic reaction", "Dr. Kent", 
"ER", "2nd", "213", "A", "31-DEC18", "06:30", 
"Patient given Epinephrine injection and Intravenous antihistamines. Monitor until breathing is stable.",
"Swelling reduced and breathing stabilized after treatment.", 
"Benadryl", "60mg", "Twice a day", "N/A", 
"Aetna", "0987654321", "AETNA002",
"Benadryl", "525.60",
525.60, 0.00, 0.00,
"3", "Jaxon Patel\nOmar Lucero\nJada Thompson");

insert into patients values
(2, "Nguyen", "Isabella", "Rose", 
"901 Oak Ave", "Knoxville", "TN", "37914", 
"(605)-590-8273", "(605)-294-9853", "(605)-293-901", 
"Mckayla David", "(605)-298-1203", 
"Kyle Nguyen", "(605)-138-4321",
"6-JAN19", "18:22", "kidney disease", "Dr. Brown", 
"Dialysis Center", "7th", "702", "B", "10-JAN19", "10:30", 
"Too much fluid in blood, schedule patient for dialysis.", 
"Patient's weight and blood pressure appear normal.", 
"Calcium Carbonate", "100mg", "Once a day, in the morning", "Dialysis", 
"United Healthcare", "2568101214", "UHC003",
"Calcium Carbonate\nDialysis", "182.31\n5200.75",
5100.00, 283.06, 200.00,
"1", "Kyle Nguyen");

insert into patients values
(3, "Smith", "Jacob", "Alexander", 
"222 Elmwood Dr", "Florence", "AL", "35630", 
"(219)-690-3651", "(219)-304-3842", "(138)-948-1938", 
"Robert Smith", "(256)-315-9032", 
"Alex Smith", "(251)-487-2109",
"19-OCT19", "06:47", "respiratory distress", "Dr. Patel", 
"ICU", "3rd", "341", "D", "26-OCT19", "13:21", 
"Patient is suffering from acute respiratory distress syndrome, should be kept on mechanical ventilator until oxygen levels improve and scheduled for a tracheostomy.", 
"Patient's oxygen levels are steadily improving.", 
"Aldactone", "50mg", "Twice a day", "Tracheostomy", 
"Cigna", "9876543210", "CIGNA004",
"Aldactone\nTracheostomy", "313.20\n20346.65",
10000.00, 10659.85, 10000.00,
"2", "Robert Smith\nAlex Smith");

insert into patients values
(4, "Lee", "Madison", "Elizabeth", 
"4407 Maple Dr", "Atlanta", "GA", "30303", 
"(872)-574-2514", "(872)-238-5392", "(891)-130-6532", 
"Lilith Carter", "(872)-321-4398", 
"Lainey Nixon", "(872)-901-3781",
"2-FEB20", "09:33", "car accident", "Dr. Pike", 
"ER", "9th", "926", "F", "9-FEB20", "18:25", 
"Patient is suffering from traumatic brain injuries and internal bleeding, scheduled for craniotomy and thoracotomy.", 
"Blood pressure has stabilized after surgery.", 
"Ritalin", "30mg", "Three times a day", "Craniotomy, thoracotomy", 
"Humana", "147258360", "HUMANA005",
"Ritalin\nCraniotomy\nThoracotomy", "600.20\n23040.62\n15300.85",
8000.00, 30941.05, 30000.00,
"4", "Lilith Carter\nNixon Lainey\nLily Chen\nXavier Davis");

insert into patients values
(5, "Brown", "William", "Thomas", 
"6543 Cedar Rd", "Buffalo", "NY", "14201", 
"(720)-725-1927", "(720)-182-9684", "(714)-984-4082", 
"Blaine Brown", "(714)-903-2471", 
"Blaze Rojas", "(871)-891-1911",
"18-JUN20", "20:11", "Meningitis", "Dr. Martin", 
"ER", "6th", "609", "E", "2-JUL20", "11:40", 
"Patient is suffering from bacterial meningitis, needs surgical treatment to repair dural lacerations.",
"Inflammations have decreased and vitals are stable.", 
"Penicillin\nCeftriaxone", "100mg\n50mg", "Twice a day\nThree times a day", "Dural repair", 
"Kaiser Permanente", "3692581470", "KP006",
"Penicillin\nCeftriaxone\nDural repair", "120.42\n230.67\n5670.20",
5021.29, 1000.00, 1000.00,
"3", "Blaine Brown\nBlaze Rojas\nNathan Kim");

insert into patients values
(6, "Williams", "Chloe", "Grace", 
"987 Birch Ln", "Gadsden","AL", "35901", 
"(917)-836-9214", "(917)-248-0483", "(917)-281-5832", 
"Ryder Hines", "(801)-388-9012", 
"Skyla Williams", "(917)-836-1283",
"10-AUG21", "10:52", "shark bite", "Dr. Ingram", 
"STC", "4th", "417", "G", "10-SEP21", "17:30", 
"Patient's arm has suffered from irreparable tissue damage, must be amputated.", 
"Keeping patient's stump elevated, vitals have stayed stable.", 
"Ibuprofen\nCarbamazepine", "100mg\n50mg", "As many times as needed\nTwice a day", "Amputation", 
"Anthem", "135790862", "ANTHEM007",
"Ibuprofen\Carbamazepine\nAmputation", "50.25\n96.53\n10600.70",
1700.00, 9047.48, 9047.48,
"1", "Skyla Williams");

insert into patients values
(7, "Davis", "Ethan", "Michael", 
"777 Willow Ave", "Nashville", "TN", "37027", 
"(563)-807-3568", "(563)-139-5083", "(582)-240-7654", 
"Tristan Davis", "(563)-881-1920", 
"Abby Davis", "(563)-139-6601",
"9-MAY22", "01:12", "stroke", "Dr. Lester", 
"ER", "8th", "813", "H", "16-MAY22", "08:30", 
"tPA injected into patient's vein, craniotomy needed to repair blood vessels.", 
"Body temperature and blood pressure appear normal, breathing rate is low.", 
"Aspirin", "100mg", "Twice a day", "Craniotomy", 
"Blue Shield of California", "9876543211", "BSC008",
"Aspirin\nCraniotomy", "50.20\n5000.92",
551.12, 4500.00, 4000.00,
"2", "Tristan Davis\nAbby Davis");

insert into patients values
(8, "Rodriguez", "Olivia", "Anne", 
"3338 Spruce St", "Huntsville", "AL", "35811", 
"(301)-870-2943", "(301)-402-1390", "(301)-384-1038", 
"Heidi Rodriguez", "(301)-653-7706", 
"Andrew Rodriguez", "(301)-879-0038",
"2-FEB23", "12:06", "gastrointestinal distress", "Dr. Smith", 
"GIC", "10th", "1045", "J", "9-FEB23", "10:50",
"Patient suffering from gastroenteritis, schedule for laparoscopic surgery.", 
"Frequency of diarrhoea and vomiting have decreased, increased patient's fluid intake.", 
"Imodium", "200mg", "Once a day", "Laparoscopic surgery", 
"Health Net", "4567890123", "HN009",
"Imodium\nLaparoscopic surgery", "637.31\n10700.83",
7000.00, 4338.14, 4000.00,
"3", "Heidi Rodriguez\nAndrew Rodriguez\nSarah Lee");

insert into patients values
(9, "Martinez", "Lucas", "Gabriel", 
"555 Oakwood Blvd", "Jackson", "MS", "39174", 
"(534)-217-9843", "(534)-238-1273", "(534)-198-4329", 
"Ryan Herring", "(397)-992-4291", 
"Lila Fitzpatrick", "(534)-397-5656",
"20-FEB23", "15:40", "cancer", "Dr. Tipper", 
"HSP", "1st", "106", "K", "25-FEB23", "12:30",
"Patient has lung cancer, needs surgery and chemotherapy.",
"Provided patient with humidifier, vitals are stable.", 
"Carboplatin\nCisplatin", "20mg\n50mg", "Three times a day\nTwice a day","Wedge resection, chemotherapy", 
"AARP", "123456789", "AARP010",
"Carboplatin\nCisplatin\nWedge resection\nChemotherapy", "533.05\n607.37\n5600.82\n10000.90",
6742.14, 10000.00, 10000.00,
"4","Ryan Herring\nLila Fitzpatrick\nOlivia White\nEthan Johnson");