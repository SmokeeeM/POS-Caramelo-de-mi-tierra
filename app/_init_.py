from flask import Flask
import sqlite3
from rutas import *  # Add the missing import statement
app = Flask(__name__)
# Base de datos de productos
productos_db = sqlite3.connect('productos.db')

