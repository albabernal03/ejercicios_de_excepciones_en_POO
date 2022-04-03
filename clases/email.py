import re
class inicio_sesion():
  def __init__(self, direccion_correo, intentos, intentosMax, nombre):
    self.direccion_correo: direccion_correo
    self.intentos = intentos
    self.intentosMax= intentosMax
    self.nombre= nombre
  def comprobacion(self):
    intentos = 0
    intentosMax = 3

    while True and intentos < intentosMax:
      try:
        nombre = str(print(input('Introduzca su nombre:')))
      except SyntaxError:
        print('El nombre introducido es inválido')

      direccion_correo = print(input('Introduzca su dirección de correo:'))
      if re.search('@', direccion_correo):
        print('El correo electrónico introducido es váido')
        print('Bienvenido a la web', nombre, 'ha iniciado sesión')
      
      
    