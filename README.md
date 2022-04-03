<h1 align="center">	Ejercicio de excepciones</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/albabernal03/ejercicios_de_excepciones_en_POO)

***

<h2>¿De qué trata esta tarea?</h2>
En esta tarea hemos resuelto un ejercicio, en el cual se nos pide validar una dirección de correo electrónico

***

## Indice

1. Ejercicio 

***

## Ejercicio 1:

**Código:**

```
import re

class incio_sesion():
    def __init__(self, direccion_correo, intentos, intentosMax, nombre):
        self.direccion_correo = direccion_correo
        self.intentos= intentos
        self.intentosMax= intentosMax
        self.nombre= nombre
         
    def comprobacion(self):
        intentos = 0
        intentosMax = 3

        while True and intentos < intentosMax:
            try:
                nombre = str(print(input('Introduzca su nombre:')))
            except SyntaxError:
                print('El nombre introducido no es válido')

    
            direccion_correo = print(input("Introduzca su correo para poder iniciar sesion: "))
   

            if re.search('@', direccion_correo):
                print('El correo electrónico es valido')
                print('Bienvenido a la web', nombre)
                break
                
            elif re.search('@', direccion_correo) == None:
                print('El correo introducido no es válido')

            intentos += 1

        if intentos == intentosMax:
            print('Posible ciberataque')
        



print(incio_sesion.comprobacion('direccion_correo, intentos, intentosMax, nombre'))            

       



```
