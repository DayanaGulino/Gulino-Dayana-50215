class DatosCliente:
    def __init__(self, nombre, apellidos, DNI, Ciudad, nacionalidad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.DNI = DNI
        self.Ciudad = Ciudad
        self.nacionalidad = nacionalidad

    def obtener_nombre(self):
        return f"Su nombre es {self.nombre}"
    
    def obtener_apellidos(self):
        return f"Su apellido es {self.apellidos}"
    
    def obtener_DNI(self):
        return f"Su DNI es {self.DNI}"
    
    def obtener_nacionalidad(self):
        return f"Su nacionalidad es {self.nacionalidad}"
    
    def __str__(self):
        return f"Su nombre completo es {self.nombre} {self.apellidos}, con DNI número: {self.DNI}, identificada en la ciudad de: {self.Ciudad}, nacionalidad {self.nacionalidad}"

class AccionCliente(DatosCliente):
    def __init__(self, nombre, apellidos, DNI, Ciudad, nacionalidad):
        super().__init__(nombre, apellidos, DNI, Ciudad, nacionalidad)
        self.compras_realizadas = []

    def realizar_compra(self, producto, monto):
        self.compras_realizadas.append(producto)
        return f"{self.nombre} has comprado éxitosamente tu producto: {producto} y has abonado un total de: {monto}."


    def agradecer_compra(self):
        return f"¡Gracias por tu compra! ¡Que lo difrutes!"


    def cancelar_compra(self, producto):
        if producto in self.compras_realizadas:
            self.compras_realizadas.remove(producto)
            return f"{self.nombre} has cancelado tu compra: {producto}."
        
    def sugerir_mas_productos(self):
        return "¿Quieres ver más productos?"
    

Juan = AccionCliente("Juan", "Perez", "12345678", "Buenos Aires", "Argentino")
print(Juan.realizar_compra("Zapatillas Nike", 3000))
print(Juan.agradecer_compra())
print(Juan.cancelar_compra("Zapatillas Nike"))
print(Juan.sugerir_mas_productos())