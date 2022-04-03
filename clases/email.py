import re
class inicio_sesion():
  def __init__(self, direccion_correo, intentos, intentosMax, nombre):
    self.direccion_correo: direccion_correo
    self.intentos = intentos
    self.intentosMax= intentosMax
    self.nombre= nombre