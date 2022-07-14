import pandas as pd

def getCliente(idCliente):
    clientes = pd.read_csv('baseClientesHackaton2022.csv')
    return clientes[clientes.idCliente==idCliente]

def getUsuario(usuario):
    usuarios = pd.read_csv('baseUsuarios.csv')
    return usuarios[usuarios.usuario==usuario]

print(getUsuario("pacoG"))
print(getCliente("BF000002999"))
