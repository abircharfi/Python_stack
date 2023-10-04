from flask_app import app 
from flask_app.config import mysqlconnection
from flask import render_template , redirect , request
from flask_app.models.book import Book
from flask_app.models.author import Author


@app.route('/new_book')

def from_new ():
 
 books=Book.select_all()
 return render_template('add_book.html', books=books)


@app.route('/add_book' , methods =['POST'])

def new_book():
 
 Book.create(request.form)
 return redirect('/new_book')

@app.route('/books/<int:id>')

def show_book(id):
 
 data ={ 'id': id} 
 book = Book.get_by_id(data)
 authors=Book.favorite_by_authors(data)
 other_authors= Author.select_all()
 liked_authors_ids = [author['id'] for author in authors]
 author_not_like = [author for author in other_authors if author.id not in liked_authors_ids]

 return render_template('show_book.html', book=book, authors=authors , author_not_like=author_not_like)

@app.route('/add_new_author_favorite/<int:book_id>' , methods=['POST'])
def add_author_favorite(book_id):
    selected_author_id = int(request.form['selected_author_id'])
    data = {'book_id': book_id, 'author_id': selected_author_id}
    Book.add_favorite(data)
    return redirect(f'/books/{book_id}')

