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
   - _unique patient id, username, password._
- **Doctor_login**
   - _unique doctor id, username, password.__
- **Appointments**
   - _patient id, doctor id, time, hospital._
- **Medical History** (for each patient)
   - _patient id, patient name, prescriptions, doctor id, doctor name, date._
- **Availability**

