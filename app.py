from flask import Flask, render_template
from models import db, Product, Order

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crochet.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from flask_migrate import Migrate
migrate = Migrate(app, db)

@app.route('/')
def home():
    products = Product.query.all()
    return render_template('products.html', products=products)

@app.route('/orders')
def orders():
    all_orders = Order.query.all()
    return render_template('orders.html', orders=all_orders)

if __name__ == '__main__':
    app.run(debug=True)