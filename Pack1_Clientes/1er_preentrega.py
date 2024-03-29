Base_de_datos_usuarios = {}

def registrarse_en_sistema():
    usuario = input("Por favor ingresa tu nombre completo: ")

    usuario_ya_existe = False

    if usuario in Base_de_datos_usuarios:
        print("No pudimos crear tu usuario porque ya lo has creado anteriormente. Ve a la sección de ingreso para navegar en la web.")
        usuario_ya_existe = True
    else:
        clave = input("Por favor introduzca una contraseña válida: ")

        while len(clave) < 5:
            print("La contraseña debe tener al menos 5 caracteres.")
            clave = input("Por favor, intenta nuevamente: ")

        Base_de_datos_usuarios[usuario] = clave

    return usuario_ya_existe

usuario_existente = registrarse_en_sistema()

if not usuario_existente:
    print("¡Bienvenido a nuestro sistema! Tienes un descuento del 10% en tu primer compra. ")

    def iniciar_sesion():
        chance = 2
        while chance > 0:
            usuario_BD = input("Ingrese su nombre completo: ")
            clave_BD = input("Por favor introduce tu contraseña: ")

            if usuario_BD in Base_de_datos_usuarios and clave_BD == Base_de_datos_usuarios[usuario_BD]:
                print("Has ingresado correctamente.")
                break
            else:
                chance -= 1
                if chance > 0:
                    print(f"El usuario o la contraseña son incorrectos. Te queda {chance} intentos.")
                else:
                    print("Agotaste tus 3 intentos. Has bloqueado el acceso.")

    iniciar_sesion()

def leer_datos():
    for ind, (usuario, clave) in enumerate(Base_de_datos_usuarios.items()):
        print(f"Índice: {ind + 1}, Usuario: {usuario}, Contraseña: {clave}")

leer_datos()