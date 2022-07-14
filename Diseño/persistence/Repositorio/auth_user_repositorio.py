import sqlalchemy as db 
from persistence.modelos import Auth_Usuario
from sqlalchemy.orm import Session
import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

class AuthUsarioRepositorio():
    def __init__(self):
        self.conexion = mysql.connector.connect(
            HOST = '.' ,
            PORT = '3306',
            USER ='PC',
            PASSWORD = '12345',
            DB_NAME = 'BBVA')
        #esta linea de abajo guarda los daatos en memoria RAM
        #self.engine = db.creae_engine('sqlite:///db/login.sqlite',echo=False,future=False)


    def obtenerUsuarioNombre(self, user_name: str):
        user: Auth_Usuario = None
        with Session(self.engine) as session:
            user= session.query(Auth_Usuario).filter_by(
                username=user_name).first()
        return user

    def insertarUsurio(self, user: Auth_Usuario):
        with Session(self.engine) as session:
            session.add(user)
            session.commit()
            

