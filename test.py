from flask import Flask
# redirect, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# from models import Employee
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manas.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# app.run(host='127.0.0.1', port=8000)

@app.route('/')
def hello():
    return "Welcome!"
if __name__ =="__main__":
    app.run(debug=True)
# @app.route('/data/create' , methods = ['GET','POST'])
# def create():
#     if request.method == 'GET':
#         return render_template('createpage.html')
 
#     if request.method == 'POST':
#         employee_id = request.form['employee_id']
#         name = request.form['name']
#         age = request.form['age']
#         position = request.form['position']
#         employee = Employee(employee_id=employee_id, name=name, age=age, position = position)
#         db.session.add(employee)
#         db.session.commit()
#         return redirect('/data')