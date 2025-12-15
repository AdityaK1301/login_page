from flask import Flask, Response, jsonify, request, url_for, render_template, flash, redirect
from db import get_db_connection

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
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
        
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("INSERT INTO `users` (`name`, `email`, `mobile`, `password`) VALUES ('', '', '', '');")


 

if __name__ == "__main__":
    app.run(debug=True, port=6002)