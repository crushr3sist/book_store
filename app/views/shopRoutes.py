from flask import Blueprint, render_template, request, redirect
from app.models import bookstore, db
from werkzeug.utils import secure_filename
import os
from flask_uploads import configure_uploads, IMAGES, UploadSet # https://www.section.io/engineering-education/how-to-handle-file-uploads-with-flask/

bookStoreRoutes = Blueprint('bookStoreRoutes', __name__)

@bookStoreRoutes.route('/addStock', methods=['GET','POST'])
def addStock():
    if request.method == "POST":
        picture = request.files['picture']
        picture_path = os.path.join('static/photouploads', picture)
        picture.save(picture_path)

        newStockRequest = bookstore(
            request.form["isbn"],
            request.form["name"],
            request.form["author"],
            request.form["date"],
            request.form["description"],
            picture_path,
            request.form["trade"],
            request.form["retail"],
            request.form["books"],
            )
        db.session.add(newStockRequest)
        db.session.commit()
        return redirect('/checkStock')
    else:
        return render_template("bookstore/newStock.html")


@bookStoreRoutes.route('/checkStock', methods=['GET','POST'])
def checkStock():
    return "You posted"