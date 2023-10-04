from flask_app.config.mysqlconnection import connectToMySQL, DB

from flask_app.models.book import Book


class Author:


    def __init__(self,data):
        self.id= data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.book=None
        self.books_liked=[]

    @classmethod
    def create(cls,data):

        query="INSERT INTO authors (name) VALUES (%(name)s);"
        result= connectToMySQL(DB).query_db(query,data)
        return result
    
    @classmethod
    def select_all(cls):
        query="SELECT * FROM authors;"
        result= connectToMySQL(DB).query_db(query)
        authors =[]

        for item in result:

            authors.append(cls(item))

        return authors


    @classmethod
    def favorite_books(cls, data):
     query = """
        SELECT books.* FROM authors
        LEFT JOIN favorites ON favorites.author_id = authors.id
        LEFT JOIN books ON favorites.book_id = books.id
        WHERE authors.id = %(id)s;
    """
     results = connectToMySQL(DB).query_db(query, data)

     books_liked = []

     for item in results:
        data_book = {
            'id': item['id'],
            'title': item['title'],
            'num_of_pages': item['num_of_pages'],
            'created_at': item['created_at'],
            'updated_at': item['updated_at']
        }
        books_liked.append(data_book)

     return books_liked
            
    @classmethod
    def get_by_id(cls,data):
           query="SELECT * from authors where id=%(id)s;"
           results = connectToMySQL(DB).query_db(query,data)
           author =None
           if results != []:
            author=cls(results[0])
           return author
            
