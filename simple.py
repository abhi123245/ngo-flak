from flask import Flask,render_template,request,redirect
import sqlite3 as sql
import razorpay
app=Flask(__name__, template_folder="templates")
app = Flask(__name__, static_url_path='/static')

# app = Flask(__name__, template_folder="views")
# app = Flask(__name__, template_folder="path/to/whatever")
@app.route('/')
def first_page():
	return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/issue')
def issue():
	return render_template("issue.html")

@app.route('/project')
def project():
	return render_template("project.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")


@app.route('/registrationform')
def registrationForm():
	return render_template("registrationForm.html")

@app.route('/donate',methods=['GET','POST'])
def donate():
	# if request.method=='GET':
	# 	return render_template("donate.html")
	# else:
        formData=request.form
        client = razorpay.Client(auth=("rzp_test_n8uWvDZ7OQxiVF", "Z43ydwqWszIwqcewygbCChEs"))
        client.set_app_details({"title" : "<YOUR_APP_TITLE>", "version" : "<YOUR_APP_VERSION>"})
        DATA = {

            "amount": 100,
            "currency": "INR",
         }
        order_amount = 50000
        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'
        notes = {'Shipping address': 'Bommanahalli, Bangalore'}   # OPTIONALclient.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes)        print(response)
        response=client.order.create(data=DATA)
        print(response)
        return render_template("payment.html",response=[response,formData])
		# name=request.form['Name']
		# email=request.form['Email']
		# phone=request.form['Phone']
		# add=request.form['Addr']
		# aadhar=request.form['Aadhar']
		# cur.execute("INSERT INTO Donate (name,email,phone,address,aadhar) VALUES (?,?,?,?,?)",(name,email,phone,add,aadhar))
		# con.commit()
		# cur.close()

@app.route('/charge',methods=['GET','POST'])
def charge():
 print("====here coming")
 formData=request.form
 client = razorpay.Client(auth=("rzp_test_n8uWvDZ7OQxiVF", "Z43ydwqWszIwqcewygbCChEs"))
 data=formData.to_dict(flat=True)
 print(data)
 print(type(data))


 params_dict = {
     'razorpay_order_id': data["razorpay_order_id"],
     'razorpay_payment_id': data["razorpay_payment_id"],
     'razorpay_signature': data["razorpay_signature"]
 }
 print(params_dict)
 ab=client.utility.verify_payment_signature(params_dict)

 print(ab)
 return {"status":"success"}