from flask import Flask, render_template, request, redirect, url_for from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stock.db' db = SQLAlchemy(app)

class Stock(db.Model):
id = db.Column(db.Integer, primary_key=True)
stock_name = db.Column(db.String(100), nullable=False)
stock_quantity = db.Column(db.Integer, nullable=False)

@app.route('/', methods=['GET', 'POST']) def index(): if request.method == 'POST': stock_name = request.form['stock_name'] stock_quantity = request.form['stock_quantity'] username = request.form['username']

<code>stock = Stock(stock_name=stock_name, stock_quantity=stock_quantity)
db.session.add(stock)
db.session.commit()

return redirect(url_for('profile'))

@app.route('/profile') def profile(): return render_template('profile.html')

if __name__ == '__main__': app.run(debug=True)

The code above generates the following Python code:

from flask import Flask, render_template, request, redirect, url_for from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stock.db' db = SQLAlchemy(app)

class Stock(db.Model):
id = db.Column(db.Integer, primary_key=True)
stock_name = db.Column(db.String(100), nullable=False)
stock_quantity = db.Column(db.Integer, nullable=False)

@app.route('/', methods=['GET', 'POST']) def index(): if request.method == 'POST': stock_name = request.form['stock_name'] stock_quantity = request.form['stock_quantity'] username = request.form['username']

<code>stock = Stock(stock_name=stock_name, stock_quantity=stock_quantity)
db.session.add(stock)
db.session.commit()

return redirect(url_for('profile'))

@app.route('/profile') def profile(): return render_template('profile.html')

if __name__ == '__main__': app.run(debug=True)