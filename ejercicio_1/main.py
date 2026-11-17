#Crear la clase Estacionamiento. Su constructor __init__ recibe horas y las guarda como propiedad. 
#Crear calcularPago() para devolver el importe total calculado con if/elif/else. 
#Crear mostrarRecibo() que utilice calcularPago() y muestre horas e importe con dos decimales. 
#En el programa principal, solicitar las horas, comprobar que sea un entero mayor que cero, crear un objeto y 
#llamar a mostrarRecibo(). 
#Ejecutar al menos los casos de 2, 4 y 6 horas; guardar capturas de dos ejecuciones. 

class Estacionamiento:
    def __init__(self, horas):
        self.horas = horas

    def calcularPago(self):
        # Aplicar tarifa según el rango de horas
        if 1 <= self.horas <= 2:
            tarifa = 15.00
        elif 3 <= self.horas <= 5:
            tarifa = 12.00
        else:
            tarifa = 10.00
        
        return self.horas * tarifa

    def mostrarRecibo(self):
        total = self.calcularPago()
        print("\n--- RECIBO DE ESTACIONAMIENTO ---")
        print(f"Horas: {self.horas}")
        print(f"Total a pagar: ${total:.2f}\n")


if __name__ == "__main__":
    print("=== SISTEMA DE COBRO DE ESTACIONAMIENTO ===")
    while True:
        try:
            horas_ingresadas = int(input("Ingrese las horas estacionadas (entero mayor a 0): "))
            if horas_ingresadas > 0:
                break
            print("Error: El número de horas debe ser mayor a cero.")
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

    # Crear el objeto y mostrar el recibo
    estacionamiento = Estacionamiento(horas_ingresadas)
    estacionamiento.mostrarRecibo()