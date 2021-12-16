# About Backend routes

## 1. '/' 
- Url for the homepage 

## 2. '/login'
- Page where the doctor can login and also signup.

## 3. '/patient'
- Page where the patient can login or signup.

## 4. '/doctorhome'
- This is the screen after logging in as doctor.
 ### It displays the doctors appoinments along with 4 buttons for "making an appoinment", "Adding a medical history entry",  "viewing a particular patient's medical history" and "delete appointment".

- "Make appoinment" button leads to url /adddappointment on clicking.
- "Add med History" button leads to url /adddata on clicking.
- "View med history" button leads to url /searchp on clicking.
- "Delete appointment" button leadds to url /delappoint_doc on clicking.

## 5. '/addappointment'
- Here the doctor enters patients name ,date and time for appoinment and click "make appoinment" upon which that data is loaded into the database for appointments.

## 6. '/adddata'
- The medical history data entered by the doctor is saved into the medical history database.

## 7. '/searchp'
- A page that ask for the patient's name whose medical history needs to be viewed. Redirects to '/seedata' .

## 8. '/seedata'
- Views the medical history of the person whose name was entered.

## 9. '/patienthome'
- Page that opens on logging in as a patient.
 ### Displays the medical history of that patient along with 3 buttons "make appoinments", "see appointments" and "delete appointment".

- 'make appointment' leads to url '/addappointmentpat' on clicking.
- 'see appointments' leads to url '/seeappoint' on clicking.
- 'delete appointment' leads to url '/delappoint' on clicking.

## 10. '/addappointmentpat'
- Appoinment made and stored in the database.

## 11. '/seeappoint'
- For viewing appointments of that particular patient. Retrieved from the database.

## 12. '/delappoint'
- A patient cancel an appointment. 

## 13. '/delappoint_doc'
- Doctor cancel an appoinment.