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

    def __str__(self):
        return f"Rut: {self.rut}\n" \
               f"Nombre: {self.nombre}\n" \
               f"Dirección: {self.direccion}\n" \
               f"Teléfono: {self.telefono}\n" \
               f"Fecha de ingreso: {self.fecha_ingreso}\n" \
               f"Sexo: {self.sexo}\n" \
               f"Cargo: {self.cargo}\n" \
               f"Área: {self.area}"