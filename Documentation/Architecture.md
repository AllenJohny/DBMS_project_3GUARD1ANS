# **Overview**
### A web application where a person logs in as either a patient, doctor or admin, after which depending on the person provide some options to view,add or delete information from the database. 



# **Front-end**
### Each of the given pages are present in the application albeit based on the user some functions will be different.
### 1. Home page
- Information on number of hospitals and doctors.
- Option to login.

### 2. Login portal
- There is an individual page for patients, doctors and admin each.
- accesses the login databases aupon selecting 'Enter'.

### 3. Appointments
- Here, based on who accessed it , appointments can be **created** _(patients)_, **approved** _(admin)_, or **deleted** _(patient or admin)_.

### 4. View Medical History
-  Show all the entries from the medical history data of that particular patient.


# **Back-end**
####  ​Backend is created using Flaskapp.

# **Database**

#### Database is created on a cloud based service called Mongodb Atlas.                                                               

 ## _Tables_
- **Patient_login**   
   - _unique patient id, username, password._
- **Doctor_login**
   - _unique doctor id, username, password._
- **Admin_login**
   - _unique admin id, username, password._
- **Hospitals**
   - _hospital id, name, location._
- **Doctors**
   - _name, id, hospital id, field._
- **Admin**
   - _name, id,hospital id._
- **Appointments**
   - _patient id, doctor id, time, hospital._
- **Medical History** (for each patient)
   - _patient id, patient name, prescriptions, doctor id, doctor name, date._



