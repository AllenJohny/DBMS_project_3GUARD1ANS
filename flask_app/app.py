from flask import Flask,render_template,redirect,url_for,request
from pymongo import MongoClient
from flask_pymongo import PyMongo


app = Flask(__name__)



client = MongoClient('mongodb://localhost:27017/')
db = client.medicords


#client = MongoClient('mongodb://localhost:27017/')
#db = client.medicords

#app.config['MONGO_URI']='mongodb+srv://Allen:Password1@dbmsproject.hqrwo.mongodb.net/Project?retryWrites=true&w=majority'
#mongodb_client=PyMongo(app)


#client = MongoClient("mongodb+srv://Allen:Password1@dbmsproject.hqrwo.mongodb.net/medicords?retryWrites=true&w=majority")
#db = mongodb_client.medicords


@app.route('/',methods=['GET','POST'])
def homepage():
    if request.method=='POST':
            if request.method('PATIENT')=='PATIENT':
                return redirect(url_for('patient'))

            elif request.form.get('DOCTOR')=='DOCTOR':
                task = 1
                return redirect(url_for('login'))
    return render_template('homepage.html')


@app.route('/home',methods=['GET','POST'])
def main():
     global task
     if request.method=='POST':
          if request.form.get('DOCTOR')=='DOCTOR':
             task = 1
             return redirect(url_for('login'))


          elif request.form.get('PATIENT')=='PATIENT':
              task = 2
              return redirect(url_for('patient'))


     elif request.method=='GET':
          return render_template('index.html')
     print('hello')
      
@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/login',methods=['GET','POST'])
def login():
    task=1
    if task == 1:
        collection = db.doctors_details
        if request.form.get('signup')=='signup':
            name = request.form['name']
            sname=request.form['sname']
            email = request.form['email']
            phone = request.form['phone']
            spec = request.form['specialization']
            username_new = request.form['username_new']
            password_new = request.form['password_new']
            temp = db.doctors_details.find()
            flag = 0
            for i in temp:
                if i['username']==username_new:
                    flag=1
                    break
            if flag ==0:
                post = {'name':name , 'sname': sname ,'email':email , 'phone':phone , 'spec':spec , 'username':username_new , 'password':password_new}
                postID = db.doctors_details.insert_one(post).inserted_id
                emp = db.doctors_details.find()
            return render_template('login.html')

        elif request.form.get('signin')=='signin':
            user = request.form['username']
            passw = request.form['password']
            acc = db.doctors_details.find_one({"username":user})
            if passw==acc["password"]:
                global user_d
                user_d = user
                global nam
                nam  = acc['name']
                global speci
                speci = acc['spec']
                global emaili
                emaili = acc['email']
                global usern
                usern = acc['username']
                return redirect(url_for('doctorhome'))
    return render_template('login.html')


@app.route('/patient',methods=['GET','POST'])
def patient():
    task=2
    if task == 2:

        collection = db.patient_details
        if request.form.get('signup')=='signup':
            name = request.form['name']
            sname = request.form['sname']
            email = request.form['email']
            phone = request.form['phone']
            username_new = request.form['username_new']
            password_new = request.form['password_new']
            temp = db.patient_details.find()
            flag = 0
            for i in temp:
                if i['username']==username_new:
                    flag=1
                    break
            if flag ==0:
                post = {'name':name ,'sname':sname, 'email':email , 'phone':phone ,  'username':username_new , 'password':password_new}
                postID = db.patient_details.insert_one(post).inserted_id
                emp = db.patient_details.find()

            return render_template('login_patient.html')
        elif request.form.get('signin1')=='signin1':
            user = request.form['username']
            passw = request.form['password']
            acc = db.patient_details.find_one({"username":user})
            if passw==acc["password"]:
                global user_p
                user_p = user
                global nam
                nam  = acc['name']
                global emaili
                emaili = acc['email']
                global usern
                usern = acc['username']
                return redirect(url_for('patienthome'))


    return render_template('login_patient.html')



@app.route('/doctorhome',methods=['GET','POST'])
def doctorhome():
    global task_doc
    task_doc = 0
    data1 = db.appointment.find({"doctor":nam})   #.sort([("date", pymongo.ASCENDING), ("time", pymongo.DESCENDING)])
    if request.method=='POST':
        if request.form.get('addappointment')=='addappointment':
            task_doc=1
            return redirect(url_for('addappointment'))
        if request.form.get('add_medical_data')=='add_medical_data':
            task_doc=2
            return redirect(url_for('adddata'))
        if request.form.get('see_medical_data')=='see_medical_data':
            task_doc=3
            return redirect(url_for('searchp'))
        if request.form.get('delete')=='delete':
            task_doc=4
            return redirect(url_for('delappoint_doc'))
    return render_template('doctor_home.html',name1 =nam , data1 = data1)





@app.route('/patienthome',methods=['GET','POST'])
def patienthome():
    global task_pat
    task_pat = 0
    data = db.medical_history.find({"patient":nam})
    if request.method=='POST':
        if request.form.get('records')=='records':
            task_pat = 1
            return redirect(url_for('addappointmentpat'))
        if request.form.get('appointment')=='appointment':
            task_pat=2
            return redirect(url_for('seeappoint'))

    return render_template('patient_home.html' , name1 = nam , data = data)



@app.route('/addappointment',methods=['GET','POST'])
def addappointment():
    if task_doc==1:
        if request.method=='POST':
            if request.form.get('appoint')=='appoint':
                naam = request.form['naam']
                date = request.form['date']
                time = request.form['time']
                #dname=db.doctors_details.find({"username":user_d},{"name":1,"_id":0})
                post = {'doctor':nam , 'patient':naam , 'date':date ,'time':time }
                postID = db.appointment.insert_one(post).inserted_id
        return render_template('add_appointment.html')

        
@app.route('/addappointmentpat',methods=['GET','POST'])
def addappointmentpat():
    data4=db.availability.find()
    if task_pat==1:
        if request.method=='POST':
            if request.form.get('appoint')=='appoint':
                naam = request.form['naam']
                date = request.form['date']
                time = request.form['time']
                #dname=db.doctors_details.find({"username":user_d},{"name":1,"_id":0})
                post = {'doctor':naam , 'patient':nam , 'date':date , 'time':time }
                postID = db.appointment.insert_one(post).inserted_id
        return render_template('add_appointmentpat.html',data4=data4)

@app.route('/adddata',methods=['GET','POST'])
def adddata():
    if task_doc==2:
        if request.method=='POST':
            if request.form.get('data')=='data':
                description = request.form['description']
                Pname = request.form['Pname']
                year = request.form['saal']
                post = {'doctor':nam , 'description':description , 'patient':Pname , 'year':year}
                postID = db.medical_history.insert_one(post).inserted_id
        return render_template('add_data.html')

@app.route('/searchp',methods=['GET','POST'])
def searchp():
    if task_doc==3:
        if request.method=='POST':
            if request.form.get('enter')=='enter':
                global pname
                pname=request.form['pname'] 
                return redirect(url_for('seedata'))
    return render_template('searchp.html')

@app.route('/seedata',methods=['GET','POST'])
def seedata():
    data2 = db.medical_history.find({"patient":pname})
    if task_doc==3:
        return render_template('see_data.html' , data2 = data2)

@app.route('/addmedical',methods = ['GET','POST'])
def addmedical():
    if task_pat==1:
        if request.method=='POST':
            if request.form.get('data')=='data':
                disease = request.form['disease']
                mont = request.form['mont']
                year = request.form['saal']
                post = {'patient':user_p , 'disease':disease , 'month':mont , 'year':year}
                postID = db.medical_history.insert_one(post).inserted_id
        return render_template('add_data.html')
    return render_template('add_medicalHistory.html')

@app.route('/seeappoint',methods = ['GET','POST'])
def seeappoint():
    if task_pat==2:
        data3 = db.appointment.find({"patient":nam})
        if request.method=='POST':
            if request.form.get('delete')=='delete':
                return redirect(url_for('delappoint'))                
        return render_template('see_appoint_pat.html',data3 = data3)



@app.route('/delappoint',methods=['GET','POST'])
def delappoint():
    if task_pat==2:
        data3 = db.appointment.find({"patient":nam})
        if request.method=='POST':
            if request.form.get('del')=='del':
                doctor=request.form['doctor']
                date=request.form['date']
                time=request.form['time']
                db.appointment.delete_one({"doctor":doctor,"patient":nam,"date":date,"time":time})
        return render_template('del_appoint_pat.html',data3 = data3)

@app.route('/delappoint_doc',methods=['GET','POST'])
def delappoint_doc():
    if task_doc==4:
        data1 = db.appointment.find({"doctor":nam})
        if request.method=='POST':
            if request.form.get('del')=='del':
                patient=request.form['patient']
                date=request.form['date']
                time=request.form['time']
                db.appointment.delete_one({"doctor":nam,"patient":patient,"date":date,"time":time})
        return render_template('del_appoint_doc.html',data1 = data1)




@app.route('/seedoc',methods = ['GET','POST'])
def seedoc():
    if task_pat==3:
        data4 = db.treats.find({"patient":user_p})
        if request.method=='POST':
            if request.form.get('adddoc')=='adddoc':
                doc = request.form['doname']
                post = {'doc':doc , 'patient':user_p}
                postID = db.treats.insert_one(post).inserted_id
            return render_template('seedoc.html',data4 = data4)
        return render_template('seedoc.html',data4 = data4)


if __name__=='__main__':
    task = 0
    app.run(debug=True)