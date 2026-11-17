
from sqlalchemy import create_engine, select, String
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    Session
)


# =====================================
# TODO ORM 1 - CONFIGURAR LA CONEXION
# =====================================

# Crear el engine para conectar con
# una base SQLite llamada zapateria.db


# =====================================
# TODO ORM 2 - CREAR LA CLASE BASE
# =====================================

# Crear la clase Base utilizando
# DeclarativeBase.


# =====================================
# TODO ORM 3 - CREAR EL MODELO ZAPATO
# =====================================

# Construir la clase Zapato.
#
# Tabla: zapatos
#
# Atributos:
# - id: entero, clave primaria
# - modelo: texto
# - talla: entero
# - precio: real
#
# Utilizar Mapped y mapped_column.


# =====================================
# TODO ORM 4 - CREAR LA TABLA
# =====================================

def inicializar_bd():
    # Crear las tablas del modelo
    # utilizando el engine.
    pass


# =====================================
# TODO ORM 5 - REGISTRAR ZAPATO
# =====================================

def crear_zapato(modelo, talla, precio):
    # Crear un objeto Zapato.
    # Abrir una sesion.
    # Agregar el objeto.
    # Confirmar la transaccion.
    #
    # Retornar True si se registro.
    return False


# =====================================
# TODO ORM 6 - LISTAR ZAPATOS
# =====================================

def listar_zapatos():
    # Consultar todos los objetos
    # Zapato utilizando SQLAlchemy.
    #
    # Retornar una lista de objetos.
    return []


# =====================================
# TODO ORM 7 - BUSCAR POR ID
# =====================================

def buscar_zapato(id_zapato):
    # Buscar un Zapato por su ID.
    #
    # Retornar el objeto encontrado
    # o None si no existe.
    return None


# =====================================
# TODO ORM 8 - ACTUALIZAR PRECIO
# =====================================

def actualizar_precio(id_zapato, nuevo_precio):
    # Buscar el zapato por ID.
    # Modificar el atributo precio.
    # Confirmar el cambio.
    #
    # Retornar True si se actualizo.
    # Retornar False si no existe.
    return False


# =====================================
# TODO ORM 9 - ELIMINAR ZAPATO
# =====================================

def eliminar_zapato(id_zapato):
    # Buscar el zapato por ID.
    # Eliminar el objeto con el ORM.
    # Confirmar la transaccion.
    #
    # Retornar True si se elimino.
    # Retornar False si no existe.
    return False