from flask import Blueprint, render_template, request, redirect
from app.models import bookstore, db

bookStoreRoutes = Blueprint('bookStoreRoutes', __name__)

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
        return redirect('/checkStock')
    else:
        return render_template("bookstore/newStock.html")


@bookStoreRoutes.route('/', methods=["GET","POST", "DELETE"])
def checkStock():
    if request.method == "GET":
        stockQuery = bookstore.query.all()
        return render_template('bookstore/checkStock.html', stock_iter = stockQuery)

@bookStoreRoutes.route('/delete/<int:id>')
def deleteRecords(id):
    deletationVar = bookstore.query.filter_by(isbn=id).first()
    db.session.delete(deletationVar)
    db.session.commit()
    return redirect('/')
