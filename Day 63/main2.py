from django.shortcuts import render
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"

db.create_all()

@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', book_stack=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        b_name = request.form["book"]
        b_author = request.form["author"]
        b_rating = request.form["rating"]
        new_book = Book(title=b_name, author=b_author, rating=b_rating)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        #UPDATE RECORD
        b_id = request.form["id"]
        book_to_update = Book.query.get(b_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    b_id = request.args.get('id')
    b_selected = Book.query.get(b_id)
    return render_template("edit_rating.html", book=b_selected)

@app.route("/delete")
def delete():
    b_id = request.args.get('id')

    #DELETE RECORD BY ID
    book_to_delete = Book.query.get(b_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)