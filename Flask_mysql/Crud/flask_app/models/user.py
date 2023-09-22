from flask_app.config.mysqlconnection import connectToMySQL, DB

class user:

    def __init__(self,data):
     self.id = data['id']
     self.first_name = data['first_name']
     self.last_name = data['last_name']
     self.email = data['email']
     self.created_at = data['created_at']
     self.updated_at = data['updated_at']
    
    @classmethod
    def create(cls,data):
       query ="INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s)"
       
       return connectToMySQL('DB').query_db(query,data)
    @classmethod
    def read_all(cls):
       query = "select * from users"
       result=connectToMySQL('BD').query_db(query)

       users=[]
       
       for item in result :

          user= cls(item)
          users.append(user)

       return users
