from app import app, db
from app.mail import send
from app.models import Users
from app.generation import gen_code
from validate_email import validate_email
from flask import render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        general_gen_code = gen_code()
        hash_password = generate_password_hash(general_gen_code)
        if validate_email(email, verify=True):

            try:
                user = Users(email=request.form.get('email'), generation_code=hash_password)
                db.session.add(user)
                db.session.flush()
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print('Ошибка добавления в бд', e)

            send(email_getter=email, gen_email_code=general_gen_code)

        return redirect(url_for('verifypage'))

    return render_template('index.html')


@app.route('/verifypage', methods=['GET', 'POST'])
def verifypage():
    if request.method == 'POST':
        verificationcode = request.form.get('verificationcode')
        if check_password_hash(Users.query.all()[0].generation_code, verificationcode.strip()):
            return redirect(url_for('success'))

        return redirect(url_for('verifypage'))

    return render_template('verifypage.html')


@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')



