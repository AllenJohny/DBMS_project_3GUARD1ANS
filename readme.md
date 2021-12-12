# Medical History and Appoinments web application

## About

### This is a web application for use by doctors and patients. Here the medical history of patients can be accessed for ease of convenience for both the doctors and patients. It is also possible to create appointments with doctors based on their availability.


## Getting started

### Make sure that python-flask, PyMongo are installed in your system, else you can install them using

- ##### python -m pip install pymongo
- ##### pip install Flask

### For setting up database, first make sure that you have MongoDB installed in your system

###### 1. Go to command prompt

###### 2. Type mongo

###### 3. Create a db called medicords

###### 4. Create the following collections
   - appointment
   - availability
   - doctors_details
   - medical_history
   - patient_details


### To run the code enter the 'flask_app' directory in the terminal and run

- ##### python run.py

- ##### Then open [ localhost:5000/home ](http://localhost:5000/home )  in your browser