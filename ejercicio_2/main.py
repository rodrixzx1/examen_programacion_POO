#Ejercicio 2. Calculadora con herencia 
#Desarrolla ejercicio_2/main.py utilizando dos clases: Operacion (padre) y Resta (hija). 
#Operacion tendrá un __init__ que reciba y guarde dos números. 
#Operacion tendrá calcular() que regrese la suma de sus dos propiedades. 
#Operacion tendrá mostrarResultado() que llame a calcular() y muestre el resultado. 
#Resta heredará de Operacion y redefinirá calcular() para regresar la resta de las propiedades heredadas. No 
#necesita un constructor nuevo. 
#Solicitar dos números; crear un objeto de Operacion y otro de Resta; llamar a mostrarResultado() en ambos. 
#Mostrar el nombre de la operación desde el programa principal. 
#Guardar evidencia con los valores 20 y 8, y otra ejecución con otros valores. 


class Operacion(object):
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def calcular(self):
        return self.numero1 + self.numero2

    def mostrarResultado(self, nombre_operacion):
        resultado = self.calcular()
        print(f"Resultado de la {nombre_operacion}: {resultado}")


class Resta(Operacion):
    def calcular(self):
        return self.numero1 - self.numero2


if __name__ == "__main__":
    print("=== CALCULADORA CON HERENCIA ===")
    try:
        num1 = float(input("Ingrese el número 1: "))
        num2 = float(input("Ingrese el número 2: "))
    except ValueError:
        print("Valores inválidos. Usando valores por defecto: 20 y 8.")
        num1 = 20
        num2 = 8

    # Creación de objetos
    operacion_suma = Operacion(num1, num2)
    operacion_resta = Resta(num1, num2)

    print("\n--- RESULTADOS ---")
    print(f"Número 1: {num1}")
    print(f"Número 2: {num2}")
    operacion_suma.mostrarResultado("suma")
    operacion_resta.mostrarResultado("resta")