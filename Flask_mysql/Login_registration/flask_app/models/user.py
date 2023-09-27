from flask_app.config.mysqlconnection import connectToMySQL, DB

class User:

    def __init__(self,data):
     self.id = data['id']
     self.first_name = data['first_name']
     self.last_name = data['last_name']
     self.email = data['email']
     self.password= data['password']
     self.created_at = data['created_at']
     self.updated_at = data['updated_at']
    
    @classmethod
    def create(cls,data):
       query ="INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
       
       return connectToMySQL('DB').query_db(query,data)
    
    @classmethod
    def get_one(cls,data):
       query = "select * from users where id=%(id)s;"
       result= connectToMySQL('BD').query_db(query,data)
       user = None
       if result != []:
          user = cls(result[0])
       return user
    
    @classmethod
    def find_by_email_and_password(cls,data):
        query ="select * from users where email=%(email)s and password=%(password)s;"
        return connectToMySQL(DB).query_db(query,data)
       

      
