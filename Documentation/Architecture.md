<<<<<<< HEAD
=======

>>>>>>> 1606cdc50baebc7ebce136350d8021bccdb2ae25
# **Overview**
### A web application where a person logs in as either a patient or doctor after which depending on the person provide some options to make appoinments, see medical history etc.



# **Front-end**
### Each of the given pages are present in the application albeit based on the user some functions will be different.
### 1. Home page
- Option to login.

### 2. Login portal
- There is an individual page for patients and doctors.
- accesses the login databases upon selecting 'Enter'.

### 3. Appointments
- Here appointments can be **made** or **viewed** _(patients or doctor)_.

### 4. View Medical History
-  Show all the entries from the medical history data of that particular patient.


# **Back-end**
####  ​Backend is created using Flaskapp.

# **Database**

#### Database is created on the local MongoDB database.                                                               

 ## _Tables_
- **Patient_login**   
   - _name,surname,username, password._
- **Doctor_login**
   - _name,surname,specialization, username, password._
- **Appointments**
   - _patient name, doctor name, time,date._
- **Medical History** (for each patient)
   - _patient name, prescriptions, doctor name, date._
- **Availability**

