from flask import Flask, render_template


app = Flask(__name__)


@app.route("/",methods=["GET","POST"])
def home():
    return "hello"


@app.route("/login",methods=["GET","POST"])
def login():
     return "hello"

if __name__ == '__main__':
    app.run(debug=True)






















# from flask import Flask, render_template,request,redirect,url_for, session
# import csv

# '''
# Red underlines? Install the required packages first: 
# Open the Terminal in PyCharm (bottom left). 

# On Windows type:
# python -m pip install -r requirements.txt

# On MacOS type:
# pip3 install -r requirements.txt

# This will install the packages from requirements.txt for this project.
# '''


# app = Flask(__name__)


# def is_user_registered(email):
#     with open("data.csv", mode="r") as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip header
#         for row in reader:
#             if row and row[0] == email:
#                 return True
#     return False





# @app.route("/register", methods=["GET","POST"])

# def register():
   
#    if request.method == "POST":
#         firstname =  request.form["firstname"]
#         lastname =  request.form["lastname"]
#         email =  request.form["email"]
#         password =  request.form["password"]
#         data = [email,firstname,lastname,password]
#         if not firstname or not lastname or not password:
#              error = "missing field"
#              return render_template('register.html',message=error)

#         if len(password) < 8:
#              error = "short password"
#              return render_template('register.html',message=error)

#         if is_user_registered(email) == True:
#                 error = "already a member , please login"
#                 return render_template('register.html',message=error)
           
#         with open("data.csv" ,mode="a") as file:   
#                writer = csv.writer(file)
#                writer.writerow(data)
#         return redirect(url_for('secret'))
    
#    return render_template('register.html')
    
# @app.route("/secret")
# def secret():
#     return render_template('secret.html')

   
    


# if __name__ == '__main__':
#     app.run(debug=True)
