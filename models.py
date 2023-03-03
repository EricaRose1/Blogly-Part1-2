"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()



# MODELS BELOW:
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                    primary_key= True,
                    autoincrement=True)
    
    first_name = db.Column(db.String(25),
                        nullable=False)

    last_name = db.Column(db.String(25),
                        nullable=False)
    
    image_url = db.Column(db.String(200), 
                        nullable=True)
    
    @property
    def full_name(self):
        '''Return full name of user.'''

        return f"{self.first_name} {self.last_name}"
        
def connect_db(app):
    db.app = app
    db.init_app(app)


