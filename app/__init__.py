
from flask import Flask


"""
Initialize the Flask application
"""
app = Flask(__name__,
            static_folder='static',
            template_folder='templates')



from app import views