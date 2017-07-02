import os

DEBUG_MODE = False
PORT = 5001

BACKEND_PATH = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BACKEND_PATH, 'sessions.db')
DB_URI = 'sqlite:////' + DB_PATH

# DB_URI = 'sqlite:///:memory:'
