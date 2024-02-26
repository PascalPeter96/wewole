from sqlite3 import Row
from config import *

import json
import MySQLdb.cursors
import re
from flask import render_template, request, redirect, url_for, session, make_response,jsonify
from werkzeug.utils import secure_filename
import MySQLdb.cursors
# format currency
@app.template_filter()
def currency_format(value):
    value = float(value)
    return "{:,.0f}".format(value)

#split page
@app.template_filter()
def par_format(value):
    x = value.split(",")
    return x

@app.route('/index')
@app.route('/')
def index():
    if "username" in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    # Output message if something goes wrong...
    msg = ''
    if request.method == 'POST':
        # Create variables for easy access
        username = request.form['username']
        password = hash_password(request.form['password'])
        # Check if account exists using MySQL
        cursor.execute('SELECT * FROM user WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['user_id']
            session['username'] = account['username']
            # Redirect to home page
            return redirect(url_for('index'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username or password'
            return render_template('login.html', error=msg)
    # Show the login form with message (if any)
    else:
        return render_template('login.html', error=msg)

@app.route('/logout')
def logout():
    if "username" in session:
        session.pop("username", None)
        session.pop("name", None)
        return redirect('login')
    else:
        return redirect('login')

    
@app.route('/members')
def members():
    cursor.execute("SELECT * FROM borrowers INNER JOIN groups on borrowers.group_id=groups.group_id")
    rows = cursor.fetchall()
    cursor.execute("SELECT * FROM groups order by group_name")
    sales = cursor.fetchall()
    res = {'data': rows, 'status': 'true', 'sales' : sales, }
    return render_template('members.html', **res)
   


@app.route('/add_members', methods=['POST', 'GET'])
def add_members():
    #`brower_id`, `fullname`, `address`, `occupation`, `salary`, `deposits`, `contact`, `next_kin`, `relationship`, `kin_contact`, `group_id`
    msg = ''
    if request.method == 'POST':
        catid = str(request.form['group_id'])
        fn= request.form['fullname']
        cl= request.form['address']
        ad= request.form['occupation']
        pa= float(request.form['salary'])
        con= request.form['contact']
        us= request.form['next_kin']
        kin= request.form['kin_contact']
               
    # creating variable for connection
        y = cursor.execute(
            'INSERT INTO   borrowers(`fullname`, `address`, `occupation`, `salary`, `contact`, `next_kin`, `kin_contact`, `group_id`) VALUES(%s, %s,  %s,  %s, %s, %s, %s, %s)', (fn, cl, ad, pa, con, us, kin, catid))
        conn.commit()
        if y:
    # displaying message
            res = {'msg': 'You have successfully registered !'}
            return redirect(url_for('members'))
        else:
            res = {'msg': 'Record not  registered'}
            return render_template('add_members.html', **res)
    else:
         
        cursor.execute("SELECT * FROM borrowers INNER JOIN groups on borrowers.group_id=groups.group_id")
        rows = cursor.fetchall()
        cursor.execute("SELECT * FROM groups order by group_name")
        sales = cursor.fetchall()
        res = {'data': rows, 'status': 'true', 'sales' : sales, }
        return render_template('add_members.html', **res)



@app.route('/add_group', methods=['POST', 'GET'])
def add_group():
    #`group_id`, `group_name`, `g_address`, `number`, `gcontact`
    msg = ''
    if request.method == 'POST':
        fn= request.form['group_name']
        cl= request.form['g_address']
        ad= request.form['number']
        con= request.form['gcontact']
           
               
    # creating variable for connection
        y = cursor.execute(
            'INSERT INTO   groups(`group_name`, `g_address`, `number`, `gcontact`) VALUES(%s, %s,  %s, %s)', (fn, cl, ad, con))
        conn.commit()
        if y:
    # displaying message
            res = {'msg': 'You have successfully registered !'}
            return redirect(url_for('groups'))
        else:
            res = {'msg': 'Record not  registered'}
            return render_template('add_group.html', **res)
    else:
         
         cursor.execute("SELECT * FROM   groups")
         data = cursor.fetchall()
         response = {'data': data, 'status': 'true', }
         return render_template('add_group.html', **response)


@app.route('/groups')
def groups(): 
    cursor.execute("SELECT * FROM  groups")
    data = cursor.fetchall()
    response = {'data': data, 'status': 'true', }
    return render_template('groups.html', **response)


@app.route('/loan_application', methods=['POST', 'GET'])
def loan_application():
    # `loan_id`, date,`amount`, `interest`, `total`, `duration`, `monthly`, `due_date`, `brower_id`
    msg = ''
    # applying empty validation
    if request.method == 'POST':
        # passing HTML form data into python variable.
        catid = str(request.form['group_id'])
        dt = get_time()
        fn = float(request.form['amount'])
        bo = float(request.form['interest'])
        rt = bo / 100 * fn
        so = fn + rt

# Convert 'du' to float
        du = float(request.form['duration'])
        mo = so / du

        de = request.form['due_date']
          
    # creating variable for connection
        y = cursor.execute(
            'INSERT INTO   loans(`date`, `amount`, `interest`, `rate`,`total`, `duration`, `monthly`, `due_date`, `group_id`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)', (dt, fn, bo, rt, so, du, mo, de, catid))
        conn.commit()
        if y:
    # displaying message
            res = {'msg': 'You have successfully registered !'}
            return redirect(url_for('viewloans'))
        else:
            res = {'msg': 'Record not  registered'}
            return render_template('loan_application.html', **res)
    else:
        cursor.execute("SELECT * FROM  loans INNER JOIN groups on loans.group_id=groups.group_id")
        data = cursor.fetchall()
        cursor.execute("SELECT * FROM groups order by group_name")
        sales = cursor.fetchall()
        response = {'data': data, 'status': 'true', 'sales' : sales, }
        return render_template('loan_application.html', **response)





    
@app.route('/all-loans')
def all_loans(): 
    return render_template('all-loans.html')



@app.route('/loan_payments', methods=['POST', 'GET'])
def loan_payments():
    #``Pay_id`, `date`, `paid`, `brower_id`, `loan_id`
    msg = ''
    # applying empty validation
    if request.method == 'POST':
        # passing HTML form data into python variable.
        accid = str(request.form['brower_id'])
        dt= get_time()
        pd = float(request.form['paid'])
        # creating variable for connection
        
        cursor.execute("SELECT * from loans where group_id=%s ",(accid,))
        row = cursor.fetchone()
        paid = row['paid'] + pd
        balance = row['total'] - paid
        if float(balance) <= row['total']:
            y = cursor.execute(
            'INSERT INTO payment_records (date, paid, group_id) VALUES (%s, %s, %s)', (dt, pd, accid))
        cursor.execute("UPDATE loans set paid=%s, balance=%s WHERE group_id=%s",(paid, balance, accid))
        conn.commit()
        if y:
            # displaying message
            res = {'msg': 'You have successfully registered !'}
            return redirect('/payment_records')
        else:
            res = {'msg': 'Record not  registered'}
            return render_template('loan_payments.html', **res)
    else:
        cursor.execute("SELECT * FROM payment_records p, loans l, groups a WHERE l.group_id =p.group_id AND a.group_id  = l.group_id ")
        data = cursor.fetchall()
        cursor.execute("SELECT * FROM borrowers")
        rows = cursor.fetchall()
        response = {'data': data, 'status': 'true', 'rows': rows,}
        return render_template('loan_payments.html', **response)


@app.route('/loan-defaulters')
def loan_defaulters(): 
    return render_template('loan-defaulters.html')

@app.route('/viewloans')
def viewloans(): 
    cursor.execute("SELECT * FROM  loans INNER JOIN groups on loans.group_id=groups.group_id")
    data = cursor.fetchall()
    cursor.execute("SELECT * FROM groups order by group_name")
    sales = cursor.fetchall()
    response = {'data': data, 'status': 'true', 'sales' : sales, }
    return render_template('viewloans.html', **response)

@app.route('/payment_records')
def payment_records(): 
    cursor.execute("SELECT * FROM  payment_records INNER JOIN groups on payment_records.group_id=groups.group_id")
    data = cursor.fetchall()
    cursor.execute("SELECT * FROM groups order by group_name")
    rows = cursor.fetchall()
    response = {'data': data, 'status': 'true', 'rows' : rows, }
    return render_template('payment_records.html', **response)



@app.route('/loan_report')
def loan_report(): 
    cursor.execute("SELECT * FROM  loans INNER JOIN borrowers on loans.brower_id=borrowers.brower_id")
    data = cursor.fetchall()
    cursor.execute("SELECT SUM(amount) AS amount FROM loans INNER JOIN borrowers on loans.brower_id=borrowers.brower_id",)
    amount = cursor.fetchone()['amount']
    cursor.execute("SELECT SUM(paid) AS paid FROM loans INNER JOIN borrowers on loans.brower_id=borrowers.brower_id",)
    paid = cursor.fetchone()['paid']
    cursor.execute("SELECT * FROM borrowers order by fullname")
    rows = cursor.fetchall()
    response = {'data': data, 'status': 'true', 'rows' : rows, 'amount' : amount, 'paid' : paid }
    return render_template('loan_report.html', **response)

@app.route('/saving_report')
def saving_report(): 
    cursor.execute("SELECT * FROM  savings INNER JOIN borrowers on savings.brower_id=borrowers.brower_id")
    data = cursor.fetchall()
    cursor.execute("SELECT SUM(deposit) AS deposit FROM savings INNER JOIN borrowers on savings.brower_id=borrowers.brower_id")
    deposit = cursor.fetchone()['deposit']
    cursor.execute("SELECT * FROM borrowers order by fullname")
    rows = cursor.fetchall()
    response = {'data': data, 'status': 'true', 'rows': rows, 'deposit': deposit}
    return render_template('saving_report.html', **response)

@app.route('/defaulters')
def defaulters(): 
    return render_template('defaulters.html')

@app.route('/arrears')
def arrears(): 
    return render_template('arrears.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Error handling...
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
# loan_application


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.route('/500')
def error500():
    abort(500)

@app.route('/messages/<int:idx>')
def message(idx):
    messages = ['Message Zero', 'Message One', 'Message Two']
    try:
        return render_template('message.html', message=messages[idx])
    except IndexError:
        abort(404)

@app.route('/saving', methods=['POST', 'GET'])
def saving():
    #`saving_id`, `date`, `deposit`, `banked`, `brower_id`
    msg = ''
    # applying empty validation
    if request.method == 'POST':
        # passing HTML form data into python variable.
        accid = str(request.form['brower_id'])
        dt= get_time()
        pd = float(request.form['deposit'])
        bd = request.form['banked']
        # creating variable for connection
        
        cursor.execute("SELECT * from borrowers where brower_id=%s ",(accid,))
        row = cursor.fetchone()
        deposits = row['deposits'] + pd
        y = cursor.execute(
            'INSERT INTO savings (date, deposit, banked, brower_id) VALUES (%s, %s, %s, %s)', (dt, pd, bd, accid))
        cursor.execute("UPDATE borrowers set deposits=%s WHERE brower_id=%s",(deposits, accid ))
        conn.commit()
        if y:
            # displaying message
            res = {'msg': 'You have successfully registered !'}
            return redirect('/viewsavings')
        else:
            res = {'msg': 'Record not  registered'}
            return render_template('saving.html', **res)
    else:
        cursor.execute("SELECT * FROM savings, borrowers WHERE savings.brower_id=borrowers.brower_id")
        data = cursor.fetchall()
        cursor.execute("SELECT * FROM borrowers")
        rows = cursor.fetchall()
        response = {'data': data, 'status': 'true', 'rows': rows,}
        return render_template('saving.html', **response)

@app.route('/viewsavings')
def viewsavings(): 
    cursor.execute("SELECT * FROM savings, borrowers WHERE savings.brower_id=borrowers.brower_id")
    data = cursor.fetchall()
    cursor.execute("SELECT * FROM borrowers")
    rows = cursor.fetchall()
    response = {'data': data, 'status': 'true', 'rows': rows,}
    return render_template('viewsavings.html', **response)





@app.route('/withdrawal', methods=['POST', 'GET'])
def withdrawal():
    #`with_id`, `date`, `withdrawal_amount`, `brower_id`
    msg = ''
    # applying empty validation
    if request.method == 'POST':
        # passing HTML form data into python variable.
        accid = str(request.form['brower_id'])
        dt= get_time()
        pd = float(request.form['withdrawal_amount'])
        # creating variable for connection
        
        cursor.execute("SELECT * from borrowers where brower_id=%s ",(accid,))
        row = cursor.fetchone()
        deposit = row['deposits'] - pd
        y = cursor.execute(
            'INSERT INTO withdrawal (date, withdrawal_amount, brower_id) VALUES (%s, %s, %s)', (dt, pd, accid))
        cursor.execute("UPDATE borrowers set deposits=%s WHERE brower_id=%s",(deposit, accid ))
        conn.commit()
        if y:
            # displaying message
            res = {'msg': 'You have successfully registered !'}
            return redirect('/withdrawal_records')
        else:
            res = {'msg': 'Record not  registered'}
            return render_template('withdrawal.html', **res)
    else:
        cursor.execute("SELECT * FROM withdrawal, borrowers WHERE withdrawal.brower_id=borrowers.brower_id")
        data = cursor.fetchall()
        cursor.execute("SELECT * FROM borrowers")
        rows = cursor.fetchall()
        response = {'data': data, 'status': 'true', 'rows': rows,}
        return render_template('withdrawal.html', **response)


@app.route('/withdrawal_records')
def withdrawal_records(): 
    cursor.execute("SELECT * FROM withdrawal, borrowers WHERE withdrawal.brower_id=borrowers.brower_id")
    data = cursor.fetchall()
    cursor.execute("SELECT * FROM borrowers")
    rows = cursor.fetchall()
    response = {'data': data, 'status': 'true', 'rows': rows,}
    return render_template('withdrawal_records.html', **response)



@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        retype = request.form['retype']

        # Check if password and retype match
        if password != retype:
            return render_template('register.html', msg='Passwords do not match')

        # Hash the password before storing it
        hashed_password = generate_password_hash(password)

        # Insert user data into the database
        try:
            cursor.execute(
                'INSERT INTO user (name, username, password) VALUES (%s, %s, %s)',
                (name, username, hashed_password)
            )
            conn.commit()
            return redirect(url_for('login'))  # Redirect to login page after successful registration
        except Exception as e:
            # Handle database insertion errors
            return render_template('register.html', msg='Error registering user')

    else:
        # Display registration form
        cursor.execute("SELECT * FROM user")
        data = cursor.fetchall()
        response = {'data': data, 'status': 'true'}
        return render_template('register.html', **response)





if __name__ == '__main__': 
    app.run(debug=True)