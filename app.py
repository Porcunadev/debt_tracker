from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] =''
app.config['MYSQL_DB'] = 'debt_tracker'

mysql = MySQL(app)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/login', methods = ['POST','GET'])
def track():
    if request.method == 'GET':
        return "False, I don't recognize you"

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        occupation = request.form['occupation']
        phonenumber = request.form['phonenumber']
        email = request.form['email']
        money = request.form['money']

        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO debts VALUES(%s,%s,%s,%s,%s,%s)''', (name,age,occupation,phonenumber,email,money))
        mysql.connection.commit()
        cursor.close()
        return f"Done deal, Tracked and Focused"
    
if __name__ == '__main__':
    app.run(debug=True)
