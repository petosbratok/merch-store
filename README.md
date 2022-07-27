

# Merch store

## About
Merch store is a fully functional e-commerce website for your clothes <br>
Link: [merch-store1.pythonanywhere.com](http://merch-store1.pythonanywhere.com) (**adblock recommended**)

Implemented features:
- List of all items on sale. Items info stored in a database.
- Product page with an ability to add item to cart if there is any in selected size.  
- Cart page where you can increase, decrease and remove items with a cool animation. Uses REST api for smooth experience.
- Checkout page with delivery info form.
- Actual Stripe payment. Payment can be validated using a separate webhook with Stripe CLI. 
- Order info. Every order has an id that starts with "ms-1".
- All the information is stored in a Postgres database. It consists of: items, orders, order items, delivery info.
-  Website has an admin page accessible at /admin. Login: admin, password: admin.
- Website is adapted for all kinds of screens.

# Setup

The first thing to do is to clone the repository:

$ git clone [https://github.com/petosbratok/merch-store](https://github.com/petosbratok/merch-store)

$ cd merch-store

Install Python and Pip.
Install the dependencies:

$ pip install -r requirements.txt

Once  `pip`  has finished downloading the dependencies:

$ cd project
$ python manage.py runserver

# Main links 
Home page:  `http://127.0.0.1:8000/`<br>
Product: `http://127.0.0.1:8000/product/<item_id>/`<br>
Cart `http://127.0.0.1:8000/cart/`<br>
Checkout: `http://127.0.0.1:8000/checkout/` <br>
Order: `http://127.0.0.1:8000/order/<order_id>/` <br>
Admin panel: `http://127.0.0.1:8000/admin/`

