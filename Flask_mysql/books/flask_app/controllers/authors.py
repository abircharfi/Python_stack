from flask_app import app 
from flask_app.config import mysqlconnection
from flask import render_template , redirect , request
from flask_app.models.author import Author
from flask_app.models.book import Book


@app.route('/')

def redir():
 return redirect('/authors')

@app.route('/authors')

def get_authors():
 
 authors=Author.select_all()
 return render_template('index.html', authors=authors)


@app.route('/new_author' , methods=['POST'])
def new_author():
 Author.create(request.form)
 return redirect('/authors')


@app.route('/authors/<int:id>')

def fav(id):
 data = { 'id': id }
 books_liked = Author.favorite_books(data)
 author= Author.get_by_id(data)
 other_books= Book.select_all()
 liked_book_ids = [book['id'] for book in books_liked]
 books_not_liked = [book for book in other_books if book.id not in liked_book_ids]
 return render_template('favorite_by_author.html', books_liked=books_liked, author=author, books_not_liked=books_not_liked)

@app.route('/add_new_favorite/<int:author_id>' , methods=['POST'])
def add_new_favorite(author_id):
    selected_book_id = int(request.form['selected_book_id'])
    data = {'author_id': author_id, 'book_id': selected_book_id}
    Book.add_favorite(data)
    return redirect(f'/authors/{author_id}')

 