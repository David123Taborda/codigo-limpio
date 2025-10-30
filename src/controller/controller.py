from model.database import Session, Producto  # importa tus clases del modelo

class Controller:
    def __init__(self):
        self.session = Session()

    def insertar_producto(self, nombre, precio, cantidad):
        try:
            nuevo = Producto(nombre=nombre, precio=precio, cantidad=cantidad)
            self.session.add(nuevo)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            print("Error insertando producto:", e)
            return False

    def buscar_producto(self, nombre):
        try:
            resultado = self.session.query(Producto).filter_by(nombre=nombre).first()
            return resultado
        except Exception as e:
            print("Error buscando producto:", e)
            return None

    def modificar_producto(self, nombre, nuevo_precio, nueva_cantidad):
        try:
            producto = self.session.query(Producto).filter_by(nombre=nombre).first()
            if producto:
                producto.precio = nuevo_precio
                producto.cantidad = nueva_cantidad
                self.session.commit()
                return True
            return False
        except Exception as e:
            self.session.rollback()
            print("Error modificando producto:", e)
            return False
