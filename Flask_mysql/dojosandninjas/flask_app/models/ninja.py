from flask_app.config.mysqlconnection import connectToMySQL , DB
from flask_app.models.dojo import Dojo

class Ninja: 
    def __init__(self,data):
        self.id= data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.age=data['age']
        self.created_at= data['created_at']
        self.updated_at=data['updated_at']
        self.dojo_id=None

    @classmethod
    def create(cls,data):
     query="INSERT INTO ninjas (first_name,last_name,age,dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s)"
     return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def select_all(cls):
     query ="SELECT * from ninjas JOIN dojos ON ninja.dojo_id= dojo.id WHERE ninjas.id=%(id)s"
     results = connectToMySQL(DB).query_db(query)

     ninjas =[]
     if results != []:
      for item in results: 

        ninja=cls(item)

        dojo_data = {
           
            'id': item['id'],
            'name':item['name'],
            'created_at':item['created_at'],
            'updated_at':item['updated_at']
                }
    
        ninjas.append(ninja)
        
        Ninja.dojo =Dojo(dojo_data)
        
     return ninjas


    @classmethod
    def get_one_ninja(cls,data):
     query="SELECT * form ninjas JOIN dojo ON ninjas.dojo_id=dojo.id where ninjas.id=%(id)s"
     results = connectToMySQL(DB).query_db(query,data)

     ninja = None
     if results != []:
        
           ninja=cls(results[0])

           dojo_data={
              'id' : results[0]['id'],
              'name' : results[0]['name'],
              'created_at' : results[0]['created_at'],
              'updated_at' : results[0]['updated_at']
           }

           dojo = Dojo(dojo_data)
           ninja.dojo = dojo
           return ninja

    @classmethod
    def update_ninja(data):
     query="UPDATE ninjas SET first_name=%(first_name)s, last_name%(last_name)s, age=%(age)s"
     return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def delete_ninja(cls,data):
     query ="DELETE FROM ninjas WHERE id=%(id)s"
     return connectToMySQL(DB).query_db(query,data)
    
    @classmethod
    def all_ninjas_in_dojo(cls,data):
      query="SELECT * from ninjas where dojo_id=%(id)s;"
      
      results=connectToMySQL(DB).query_db(query,data)      
      ninjas=[]
      for item in results:
      
        ninjas.append(cls(item))

      return ninjas


      


    




