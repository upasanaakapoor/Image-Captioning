from flask import Flask,render_template,request,session,logging,url_for,redirect,flash
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
#from flask_mysqldb import MySQL
#from passlib.hash import sha256_crypt
engine = create_engine("mysql+pymysql://root:1234567@localhost/flaskapp")
					 #("mysql+pymysql://username:password@localhost/databsename")	
db=scoped_session(sessionmaker(bind=engine))

app=Flask(__name__)
app.secret_key="1234567imagecaptiongenerator"
val=0

#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = '1234567'
#app.config['MYSQL_DB'] = 'flaskapp'

#mysql=MySQL(app)

@app.route("/")
def home():
	return render_template("home.html")

# register form
@app.route("/register", methods=["GET","POST"])
def register():
	if request.method == "POST":
		name = request.form.get("name")
		username = request.form.get("username")
		password = request.form.get("password")
		confirm = request.form.get("confirm")
		#secure_password = sha256_crypt.encrypt(str(password))

		if password == password:
#			cur=mysql.connection.cursor()
			db.execute("INSERT INTO users(name,username,password) VALUES(:name,:username,:password)",{"name":name,"username":username,"password":password})
			db.commit()
#			mysql.connection.commit()
#			cur.close()
			flash("Your registration was successful !","success")
			return redirect(url_for('login'))
		else:
			flash("please enter the correct password","danger")
			return render_template("register.html")
	return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
	if request.method == "POST":
		username = request.form.get("username")
		password = request.form.get("password")
		data = db.execute("SELECT * FROM users WHERE username=username AND password=password",{"username":username, "password":password}).fetchone()
		#data = db.fetchone()
		#passworddata = db.execute("SELECT password FROM users WHERE username=username",{"username":username}).fetchone()
		
		'''if usernamedata is None:
			flash("Invalid username", "danger")
			return render_template("login.html")'''
		#else:
		#if sha256_crypt.verify( password,data[2]) and (data[1]== username):
		if data:
			
			flash("You have logged in successfully", "success")
			return redirect(url_for('generatecaption'))
		else:
			
			flash("Please enter the correct password","danger")
			return render_template("login.html")


	return render_template("login.html")

@app.route("/generatecaption")
def generatecaption():
	return render_template("generatecaption.html")

@app.route("/logout")
def logout():
	return render_template("logout.html")

if __name__=="__main__":
	
	app.run(debug=True)