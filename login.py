import conexion
import os

print("ingrese su usuario")
usuario=(str(input()))
print("ingrese su contraseña")
auth=(str(input()))
print(usuario + " "+ auth )
u = conexion.getUsuario(usuario)
s=u['auth'].astype("string")
 
print("--------")
if s.iloc[0] == auth:
    print("Bienvenido " + u.nombreCompleto)
else:
    print("Usuario o contraseña incorrectos")
os.system("cls")
print("Ingrese el id del cliente")
idCliente=(str(input()))
c = conexion.getCliente(idCliente)
if u.perfil.astype("string").iloc[0] == "Manager":
    print(c)
elif u.perfil.astype("string").iloc[0] == "Validador":
    print("idCliente: " + c.idCliente.astype("string").iloc[0])
    print("nombre: " + c.nombre.astype("string").iloc[0])
    print("apellidoPaterno: " + c.apellidoPaterno.astype("string").iloc[0][0:3] + "***")
    print("apellidoMaterno: " + c.apellidoMaterno.astype("string").iloc[0][0:3] + "***")
    print("fechaNacimiento: " + c.fechaNacimiento.astype("string").iloc[0][0:3] + "***")
    print("sexo: " + c.sexo.astype("string").iloc[0])
    print("segmento: " + c.segmento.astype("string").iloc[0])
    print("nacionalidad: " + c.nacionalidad.astype("string").iloc[0][0:3] + "***")
    print("rfc: " + c.rfc.astype("string").iloc[0][0:3] + "***")
    print("tipoID: " + c.tipoID.astype("string").iloc[0][0:3] + "***")
    print("numeroID: " + c.numeroID.astype("string").iloc[0][0:3] + "***")
    print("cuenta: " + c.cuenta.astype("string").iloc[0])
    print("email: " + c.email.astype("string").iloc[0][0:3] + "***")
else:
    print("idCliente: " + c.idCliente.astype("string").iloc[0])
    print("nombre: " + c.nombre.astype("string").iloc[0])
    print("sexo: " + c.sexo.astype("string").iloc[0])
    print("segmento: " + c.segmento.astype("string").iloc[0])
    print("cuenta: " + c.cuenta.astype("string").iloc[0])



