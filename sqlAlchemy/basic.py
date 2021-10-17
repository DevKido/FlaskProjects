from flask_sqlalchemy import SQLAlchemy




class User(db.Model):
    
    id = 

    def __init__(self, name='NULL', age=0):
        self.name = name
        self.age = age