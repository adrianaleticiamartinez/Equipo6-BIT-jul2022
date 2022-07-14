import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from forms.login.form_login_design import DiseñoFormularioLogin
from persistence.Repositorio.auth_user_repositorio import AuthUsarioRepositorio
from persistence.modelos import Auth_Usuario
import util.generic as utl
from forms.master.form_master import MasterPanel
from persistence.modelos import Auth_Usuario
import util.encriptarDesenciptar as Enc_DesEn




class formularioLogin(DiseñoFormularioLogin):
    def __init__(self):
        self.auth_repository = AuthUsarioRepositorio()
        super()._init()

    def verificar(self,user):
        print("El usuario ingresado es",user)
        print("El usuario ingresado es  self.auth_repository", self.auth_repository)


        '''
        user_db: Auth_Usuario = self.auth_repository.obtenerUsuarioNombre(
            self.usuario.get())
        print("Chido")
        if(self.isUser(user_db)):
            self.isPassword(self.password.get(), user_db)'''
            


    #   usu = self.usuario.get()
    #   password = self.password.get()
    #   if(usu =="root" and password == "1234"):
    #       self.ventana.destroy()
    #       MasterPanel()
    #   else:
    #       messagebox.showerror(message="La contraseña no es correcta", title="Mensaje")

   
    def isUser(self,user: Auth_Usuario):
        status: bool = True
        if(user == None):
            status = False
            messagebox.showerror(message="El usuario no existe, por favor registrese", title="Mensaje")
        return status

    def isPassword(self,user: Auth_Usuario):
        b_password = end_dec.decrypt(user.password)
        if(password == b_password):
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror(message="La contraseña no es correcta", title="Mensaje")
        
   
   
   
   
    def __init__(self):
        super().__init__()  

      



