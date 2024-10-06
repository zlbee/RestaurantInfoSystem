import os
import time
from datetime import datetime

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# global parameters
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
initialized = False

# create database instance
db = SQLAlchemy(app)


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Menu %r>' % self.id


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        menu_content = request.form['content']
        new_menu = Menu(content=menu_content)

        try:
            db.session.add(new_menu)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue add your menu.'
    else:
        menus = Menu.query.order_by(Menu.date_created).all()
        return render_template('index.html', menus=menus)


@app.route('/delete/<int:id>')
def delete(id):
    menu_to_delete = Menu.query.get_or_404(id)

    try:
        db.session.delete(menu_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that menu.'


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    menu = Menu.query.get_or_404(id)

    if request.method == 'POST':
        menu.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your menu.'

    else:
        return render_template('update.html', task=menu)


def wait_for_db():
    import psycopg2
    from psycopg2 import OperationalError

    while True:
        try:
            # try to connect
            conn = psycopg2.connect(os.environ.get('DATABASE_URL'))
            conn.close()
            break
        except OperationalError:
            print("Waiting for the database to be ready...")
            time.sleep(2)


def create_tables():
    global initialized
    if not initialized:
        with app.app_context():
            db.create_all()
        initialized = True


if __name__ == "__main__":
    wait_for_db()
    create_tables()
    app.run(debug=True, host='0.0.0.0', port=5000)
