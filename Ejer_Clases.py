# Clase CURSO
class Curso:
    def __init__(self, fecha_inicio, titulo, descripcion, objetivos, programa, costo, duracion_meses, foto, estado, categoria):
        self.fecha_inicio = fecha_inicio
        self.titulo = titulo
        self.descripcion = descripcion
        self.objetivos = objetivos
        self.programa = programa
        self.costo = costo
        self.duracion_meses = duracion_meses
        self.foto = foto
        self.estado = estado
        self.categoria = categoria
        self.clases = []  # Lista de las clases asociadas al curso

# Clase CLASE DE UN CURSO
class Clase:
    def __init__(self, fecha, titulo, contenido, url_drive, docente):
        self.fecha = fecha
        self.titulo = titulo
        self.contenido = contenido
        self.url_drive = url_drive
        self.docente = docente

# Clase DOCENTE
class Docente:
    def __init__(self, apellido, nombre, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email):
        self.apellido = apellido
        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email
        self.cursos = []  # Lista de los cursos asociados al docente

# Clase USUARIO FINAL
class UsuarioFinal:
    def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono_celular, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email
        self.clave_acceso = None
        self.estado = "Inactivo"  # Por defecto, el estado estará en INACTIVO
        self.compras = []  # Lista de las compras asociadas al usuario
        self.cursos_inscritos = []  # Lista de los cursos a los que el usuario se inscribió

# Clase ADMINISTRADOR
class Administrador:
    def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono_celular, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email

# Clase ROL DE DOCENTE
class RolDocente:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

# Clase ROL DE ADMINISTRADOR
class RolAdministrador:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

# Clase COMPRA
class Compra:
    def __init__(self, fecha_compra, usuario, monto_total, medio_pago, datos_pago):
        self.fecha_compra = fecha_compra
        self.usuario = usuario
        self.monto_total = monto_total
        self.medio_pago = medio_pago
        self.datos_pago = datos_pago

# Clase MEDIO DE PAGO
class MedioPago:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

# Clase DATOS DE PAGO
class DatosPago:
    def __init__(self, numero_tarjeta, fecha_expiracion, nombre_titular, banco):
        self.numero_tarjeta = numero_tarjeta
        self.fecha_expiracion = fecha_expiracion
        self.nombre_titular = nombre_titular
        self.banco = banco




# HERENCIA
# Clase para representar un Usuario
class Usuario:
    def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono_celular, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email
        self.estado = "Inactivo"  # Por defecto, el estado es inactivo

# Clase para representar un Docente (hereda de Usuario)
class Docente(Usuario):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email):
        super().__init__(nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono_celular, email)
        self.cursos = []  # Lista de cursos asociados al docente

# Clase para representar una Compra
class Compra:
    def __init__(self, id_compra, id_carrito_compra, id_medios_pago, id_usuario, fecha, monto_total):
        self.id_compra = id_compra
        self.id_carrito_compra = id_carrito_compra
        self.id_medios_pago = id_medios_pago
        self.id_usuario = id_usuario
        self.fecha = fecha
        self.monto_total = monto_total

# Clase para representar Medios de Contacto
class MediosContacto:
    def __init__(self, id_medio_contacto, fecha, email, telefono, direccion, nombre):
        self.id_medio_contacto = id_medio_contacto
        self.fecha = fecha
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.nombre = nombre

# Enumeración para Tipos de Medio de Contacto (hereda de MediosContacto)
class TiposMedioContacto(MediosContacto):
    WhatsApp = 1
    CorreoElectronico = 2
    CallCenter = 3
    ReferidoInterno = 4
