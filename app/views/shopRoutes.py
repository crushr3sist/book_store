from flask import Blueprint, render_template, request, redirect, session
from app.models import bookstore, db
from app import app

bookStoreRoutes = Blueprint('bookStoreRoutes', __name__)

@bookStoreRoutes.route('/createCart')
def initCart():
    session['cart'] = 0
    return str(session['cart'])

@bookStoreRoutes.route('/addStock', methods=['GET','POST'])
def addStock():
    if request.method == "POST":
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
        db.session.add(newStockRequest)
        db.session.commit()
        return redirect('/')
    else:
        return render_template("bookstore/newStock.html")

@bookStoreRoutes.route('/', methods=["GET","POST"])
def checkStock():
    if request.method == "GET":
        stockQuery = bookstore.query.all()
        return render_template('bookstore/checkStock.html', stock_iter = stockQuery, cart= session['cart'])

@bookStoreRoutes.route('/delete/<int:id>')
def deleteRecords(id):
    deletationVar = bookstore.query.filter_by(isbn=id).first()
    db.session.delete(deletationVar)
    db.session.commit()
    return redirect('/')

@bookStoreRoutes.route('/addToCart/<int:id>',methods=["GET","POST"])
def addToCart(id):
    
    deletationVar = bookstore.query.filter_by(isbn=id).first() 
    if deletationVar.quantity<1:
        pass
    else:
        deletationVar.quantity -= 1
        session['cart'] += 1
    db.session.commit()
    return redirect('/')

@bookStoreRoutes.route('/checkout')
def checkout():
    
    return render_template('bookstore/checkout.html')
