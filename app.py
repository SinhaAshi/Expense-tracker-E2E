from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Ashi@str0n9'
app.config['MYSQL_DB'] = 'ET'

mysql = MySQL(app)


@app.route('/')
def home():
    return render_template('home.html')



@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        amount = request.form['amount']
        category = request.form['category']
        date = request.form['date']

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO expensetracker1 (amount, category, date) VALUES (%s, %s, %s)",
            (amount, category, date)
        )
        mysql.connection.commit()
        cur.close()

        return redirect('/view')

    return render_template('add.html')


@app.route('/view')
def view_expenses():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM expensetracker1")
    data = cur.fetchall()
    cur.close()

    return render_template('view.html', expenses=data)



@app.route('/update', methods=['GET', 'POST'])
def update_expense():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM expensetracker1")
    data = cur.fetchall()

    if request.method == 'POST':
        id = request.form['id']
        amount = request.form['amount']
        category = request.form['category']
        date = request.form['date']

        cur.execute(
            "UPDATE expensetracker1 SET amount=%s, category=%s, date=%s WHERE id=%s",
            (amount, category, date, id)
        )
        mysql.connection.commit()
        cur.close()

        return redirect('/view')

    cur.close()
    return render_template('update.html', expenses=data)



@app.route('/delete', methods=['GET', 'POST'])
def delete_expense():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM expensetracker1")
    data = cur.fetchall()

    if request.method == 'POST':
        id = request.form['id']

        cur.execute("DELETE FROM expensetracker1 WHERE id=%s", (id,))
        mysql.connection.commit()
        cur.close()

        return redirect('/view')

    cur.close()
    return render_template('delete.html', expenses=data)


@app.route('/total')
def total():
    cur = mysql.connection.cursor()
    cur.execute("SELECT SUM(amount) FROM expensetracker1")
    total = cur.fetchone()[0]
    cur.close()

    if total is None:
        total = 0

    return render_template('total.html', total=total)


if __name__ == '__main__':
    app.run(debug=True)