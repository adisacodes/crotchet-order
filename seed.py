from app import app
from models import db, Product, Order

with app.app_context():
    Order.query.delete()
    Product.query.delete()

    beanie = Product(name="Beanie", price=800, description="Warm crochet beanie")
    tote = Product(name="Tote Bag", price=1500, description="Handmade crochet tote bag")
    scarf = Product(name="Scarf", price=1200, description="Cozy crochet scarf")

    db.session.add_all([beanie, tote, scarf])
    db.session.commit() 

    order1 = Order(customer_name="Faith Wanjiru", quantity=2, product_id=beanie.id)
    order2 = Order(customer_name="John Mwangi", quantity=1, product_id=tote.id)
    order3 = Order(customer_name="Grace Achieng", quantity=3, product_id=scarf.id)

    db.session.add_all([order1, order2, order3])
    db.session.commit()

    print("Database seeded successfully!")