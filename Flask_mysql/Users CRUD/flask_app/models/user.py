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
       query ="INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"
       
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
    @classmethod
    def get_one(cls,data):
       query = "select * from users where id=%(id)s;"
       result= connectToMySQL('BD').query_db(query,data)
       user = None
       if result != []:
          user = cls(result[0])
       return user
    
    @classmethod
    def update(cls,data):
       query = "UPDATE users SET first_name= %(first_name)s,last_name=%(last_name)s,email=%(email)s where id=%(id)s"
       return connectToMySQL('BD').query_db(query,data)
    

    @classmethod
    def delete(cls,data):
       query="DELETE FROM users where id=%(id)s;"
       return connectToMySQL('DB').query_db(query,data)
       

      
