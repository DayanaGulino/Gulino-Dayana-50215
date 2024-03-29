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
    