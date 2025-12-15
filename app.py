from flask import Flask, Response, jsonify, request, url_for, render_template, flash, redirect
from db import get_db_connection
from datetime import datetime, timedelta

app = Flask(__name__)

def get_current_date_time():
    now = datetime.now()
    return now.strftime('%Y-%m-%d'), now.strftime('%I:%M:%S %p')

@app.route('/', methods=['GET', 'POST'])
def Index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * from users")
    fetch = cursor.fetchall()

    msg = None
    msg_type = None 
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']
        password = request.form['password']

        if not all([name, email, mobile, password]):
            flash('All field required', 'danger')
            return redirect(url_for('create'))
        
        add_date, add_time = get_current_date_time()
        
        
        cursor.execute("INSERT INTO `users` (`name`, `email`, `mobile`, `password`, `add_date`, `add_time`) VALUES (%s, %s, %s, %s, %s, %s)", (name, email, mobile, password, add_date, add_time))
        conn.commit()
        cursor.close()
        conn.close()

    return render_template('index.html', fetch=fetch)


if __name__ == "__main__":
    app.run(debug=True, port=6002)