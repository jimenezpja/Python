import json
import re

class Usuario:
    def __init__(self, nombre, apellido, correo, telefono, id=None):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        self.id = id

    def to_json(self):
        return json.dumps(self.__dict__)

def validar_correo(correo):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, correo) is not None

def validar_telefono(telefono):
    regex = r"^\+\d{1,3}\s?\d{1,15}$"
    return re.match(regex, telefono) is not None

def cargar_usuarios():
    try:
        with open("usuarios.txt", "r") as archivo:
            usuarios = []
            for linea in archivo:
                usuario_json = json.loads(linea)
                usuario = Usuario(**usuario_json)
                usuarios.append(usuario)
            return usuarios
    except FileNotFoundError:
        return []

def guardar_usuarios(usuarios):
    with open("usuarios.txt", "w") as archivo:
        for usuario in usuarios:
            archivo.write(usuario.to_json() + "\n")

def mostrar_menu():
    print("1. Registrar usuario")
    print("2. Eliminar usuario por id")
    print("3. Actualizar usuario por id")
    print("4. Ver usuarios")
    print("5. Salir")

def registrar_usuario(usuarios):
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    correo = input("Ingrese el correo: ")
    telefono = input("Ingrese el teléfono: ")

    while not validar_correo(correo):
        print("Correo electrónico inválido. Intente nuevamente.")
        correo = input("Ingrese el correo: ")

    while not validar_telefono(telefono):
        print("Número de teléfono inválido. Intente nuevamente.")
        telefono = input("Ingrese el teléfono: ")

    nuevo_usuario = Usuario(nombre, apellido, correo, telefono, len(usuarios) + 1)
    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)
    print("Usuario registrado exitosamente.")

def eliminar_usuario(usuarios, id):
    for i, usuario in enumerate(usuarios):
        if usuario.id == id:
            del usuarios[i]
            guardar_usuarios(usuarios)
            print("Usuario eliminado.")
            return
    print("Usuario no encontrado.")

def actualizar_usuario(usuarios, id):
    for usuario in usuarios:
        if usuario.id == id:
            nombre = input("Ingrese el nuevo nombre: ")
            apellido = input("Ingrese el nuevo apellido: ")
            correo = input("Ingrese el nuevo correo: ")
            telefono = input("Ingrese el nuevo teléfono: ")

            while not validar_correo(correo):
                print("Correo electrónico inválido. Intente nuevamente.")
                correo = input("Ingrese el correo: ")

            while not validar_telefono(telefono):
                print("Número de teléfono inválido. Intente nuevamente.")
                telefono = input("Ingrese el teléfono: ")

            usuario.nombre = nombre
            usuario.apellido = apellido
            usuario.correo = correo
            usuario.telefono = telefono
            guardar_usuarios(usuarios)
            print("Usuario actualizado exitosamente.")
            return
    print("Usuario no encontrado.")

def ver_usuarios(usuarios):
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        for usuario in usuarios:
            print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Apellido: {usuario.apellido}, Correo: {usuario.correo}, Teléfono: {usuario.telefono}")

if __name__ == "__main__":
    usuarios = cargar_usuarios()

    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        try:
            opcion = int(opcion)
            if opcion == 1:
                registrar_usuario(usuarios)
            elif opcion == 2:
                id = int(input("Ingrese el ID del usuario a eliminar: "))
                eliminar_usuario(usuarios, id)
            elif opcion == 3:
                id = int(input("Ingrese el ID del usuario a actualizar: "))
                actualizar_usuario(usuarios, id)
            elif opcion == 4:
                ver_usuarios(usuarios)
            elif opcion == 5:
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Ingrese una opción válida.")