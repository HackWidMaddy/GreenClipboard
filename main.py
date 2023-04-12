from flask import Flask
from flask import render_template, request, redirect, session
import pymysql
import flask
import random
import string
from flask_mail import Mail


app = Flask(__name__)


def connect_to_database():
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='greenclipboard')
    return conn


@app.route('/')
def index():
    conn = pymysql.connect(host='localhost', user='root',
                           password='', db='greenclipboard')
    conn = connect_to_database()

    cursor = conn.cursor()
    sql = "DELETE FROM myclipboard WHERE time >= DATE_SUB(CURDATE(), INTERVAL 100 DAY) AND time < CURDATE()"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

    return render_template('index.html')


@app.route('/online', methods=['GET', 'POST'])
def online():
    if request.method == 'POST':
        number = ''
        num_rows = 0

        for i in range(0, 4):
            random_number = random.randint(1, 9)
            number = number + str(random_number)

        actual_data = (number)
        sql = "SELECT * FROM myclipboard WHERE number=%s"
        conn = pymysql.connect(host='localhost', user='root',
                               password='', db='greenclipboard')
        cursor = conn.cursor()
        conn = connect_to_database()
        cursor.execute(sql, actual_data)
        conn.commit()
        num_rows = cursor.rowcount
        cursor.close()
        conn.close()

        if num_rows > 0:
            for i in range(0, 4):
                random_number = random.randint(1, 9)
                number = number + str(random_number)

        data = request.form.get("data")
        actual_data = (data, number)

        conn = pymysql.connect(host='localhost', user='root',
                               password='', db='greenclipboard')
        conn = connect_to_database()

        cursor = conn.cursor()
        sql = "INSERT INTO myclipboard(data,number) VALUES (%s, %s)"
        cursor.execute(sql, actual_data)
        conn.commit()
        cursor.close()
        conn.close()

        return render_template('index.html', number1=number)


@app.route('/retrive', methods=['GET', 'POST'])
def retrive():
    if request.method == 'POST':

        code = request.form.get("code")
        conn = connect_to_database()
        cursor = conn.cursor()

        sql = "SELECT * FROM myclipboard WHERE number=%s"
        cursor.execute(sql, (code))
        result = cursor.fetchone()
        mydata = result[2]

        return render_template('index.html', mydata1=mydata)


app.run(debug=True)
