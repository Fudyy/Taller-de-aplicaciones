from dataclasses import dataclass

@dataclass
class Usuario:
    rut: int
    contraseña: str
    nombre: str
    direccion: str
    telefono: str
    fecha_ingreso: str
    sexo: str
    cargo: str
    area: str