from flask import Flask
import one_dimension
import two_dimension

app = Flask(__name__)

from app import routes
