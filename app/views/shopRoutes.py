from flask import Blueprint, render_template, request, redirect, session
# importing flask dependencies

from app.models import bookstore, db
# importing the database variables

from app import app
#importing the app variable

bookStoreRoutes = Blueprint('bookStoreRoutes', __name__)
# creating the bookstore blueprint

# @bookStoreRoutes.route('/reinitialise')
# def initCart():

#     if (request.method == 'POST'):
#         session['cart'] = 0
#         init_flag = True
#         return redirect('/')
#     else:
#         return render_template('bookstore/session.html')
# the session variable resetter

@bookStoreRoutes.route('/addStock', methods=['GET','POST'])
def addStock():
# route for creating a book record

    if request.method == "POST":
    # handing the post request with regstering the book stock

        newStockRequest = bookstore(
            request.form["isbn"],
            request.form["name"],
            request.form["author"],
            request.form["date"],
            request.form["description"],
            request.form["trade"],
            request.form["retail"],
            request.form["books"],
            )
        # creating the new record

        db.session.add(newStockRequest)
        # adding to the session 

        db.session.commit()
        # writting to the database

        return redirect('/')
        # redirecting to the homepage to show all the books available for purchase
    else:
        return render_template("bookstore/newStock.html")
    # handing the get request with simply rendering the form template


@bookStoreRoutes.route('/', methods=["GET","POST"])
def checkStock():
    # displays the books available for purchase
    init_flag = False
    if request.method == "GET":
        if init_flag:
            stockQuery = bookstore.query.all()
            return render_template('bookstore/checkStock.html', stock_iter = stockQuery, cart= session['cart'])
        # renders the template with form required to handle functionality with post requests
        if init_flag == False:
            session['cart'] = 0
            init_flag = True
            return redirect('/')

@bookStoreRoutes.route('/delete/<int:id>')
# route to handle deleting a book record, implimentation of CRUD functionality 
def deleteRecords(id):
    # using url arguments to pass information 
    deletationVar = bookstore.query.filter_by(isbn=id).first()
    db.session.delete(deletationVar)
    db.session.commit()
    # deleting the variable selected 
    return redirect('/')

@bookStoreRoutes.route('/addToCart/<int:id>',methods=["GET","POST"])
def addToCart(id):
    # using the same principles from the delete route by passing variables
    # through the url

    deletationVar = bookstore.query.filter_by(isbn=id).first() 
    # quering the database for the record containing the isbn

    if deletationVar.quantity<1:
        pass
    # disallowing negative values for the stock
    else:
        deletationVar.quantity -= 1
        session['cart'] += 1
    # handling stock being appended to the "cart"
    db.session.commit()
    # writing the changes
    return redirect('/')

@bookStoreRoutes.route('/checkout')
def checkout():
    price1 = str(int(session['cart']) * 3 + 1)
    # calculating the checkout price    
    return render_template('bookstore/checkout.html', price1 = price1, price2 = int(price1)+1)
    # rendering the template with the price vairables 