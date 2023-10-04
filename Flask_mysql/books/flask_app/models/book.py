from flask_app.config.mysqlconnection import connectToMySQL, DB

from flask_app.models import author

class Book:
   
    def __init__ (self,data):
     self.id= data['id']
     self.title= data['title']
     self.num_of_pages= data['num_of_pages']
     self.created_at= data['created_at']
     self.updated_at= data['updated_at']
     self.authors_who_liked=[]
     self.author_liked=[]


    @classmethod
    def create(cls,data):

        query="INSERT INTO books (title, num_of_pages) VALUES (%(title)s,%(num_of_pages)s);"
        result= connectToMySQL(DB).query_db(query,data)
        return result
    
    @classmethod
    def select_all(cls):
        query="SELECT * FROM books;"
        result= connectToMySQL(DB).query_db(query)
        books =[]

        for item in result:

            books.append(cls(item))

        return books
    
    @classmethod
    def get_by_id(cls, data):
     query = "SELECT * FROM books WHERE id = %(id)s;"
     result = connectToMySQL(DB).query_db(query, data)
     book = None
     if result:
        book = cls(result[0])
     return book
    
    @classmethod
    def favorite_by_author():
       query="SELECT * FROM books "

    @classmethod
    def add_favorite(cls,data):
        query = "INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        return connectToMySQL('BD').query_db(query,data)

    @classmethod
    def favorite_by_authors(cls, data):
     query = """
        SELECT authors.* FROM books
        LEFT JOIN favorites ON favorites.book_id = books.id
        LEFT JOIN authors ON favorites.author_id = authors.id
        WHERE books.id = %(id)s;
    """
     results = connectToMySQL(DB).query_db(query, data)

     authors_who_like = []

     for item in results:
        data_author = {
            'id': item['id'],
            'name': item['name'],
            'created_at': item['created_at'],
            'updated_at': item['updated_at']
        }
        authors_who_like.append(data_author)

     return authors_who_like


