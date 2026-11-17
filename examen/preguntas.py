"""
PARTE 1. Interpretación y complementación
"""
#Actividad 1. Identificar elementos de POO
class Producto(object): 
    def __init__(self, nombre, precio): 
        self.nombre = nombre 
        self.precio = precio 
        self.total = 0 

    def calcularTotal(self, cantidad): 
        self.total = self.precio * cantidad 

    def mostrarTotal(self): 
    print(f"Producto: {self.nombre}") 
    print(f"Total: ${self.total:.2f}") 

producto1 = Producto("Cuaderno", 35) 
producto1.calcularTotal(3) 
producto1.mostrarTotal()

# 1 cual es el nombre de la clase?
# R: Producto
# 2 cuales son sus propiedades?
# R: nombre, precio y total
# 3. cuales son sus metodos?
# R: __init__, calcularTotal y mostrarTotal
# 4. que funcion cumple __init__?
# R: Es el metodo constructor que inicializa las propiedades del objeto al crearlo
# 5. para que se utiliza self?
# R: Hace referencia a la instancia actual de la clase, para acceder a sus atributos y metodos
# 6. en que instruccion se crea un objeto?
# R: producto1 = Producto("Cuaderno", 35)
# 7. cual es el nombre del objeto?
# R: producto1
# 8. ¿Cómo se llama a calcularTotal()?
# R: producto1.calcularTotal(3)
# 9. que valores recibe el constructor cuando se crea el objeto?
# R: "Cuaderno" (para nombre) y 35 (para precio)
# 10. que resultado mostrara el programa?
# R: 
# Producto: Cuaderno
# Total: $105.00


#Actividad 2: completar codigo

class Rectangulo(object):
    def __init__(self, base, altura):
        # COMPLETAR: guardar las propiedades
        self.base = base
        self.altura = altura

    def calcularArea(self):
        # COMPLETAR: regresar el área
        return self.base * self.altura

    def mostrarArea(self):
        # COMPLETAR: mostrar el resultado
        area = self.calcularArea()
        print(f"El área del rectángulo es: {area}")

# COMPLETAR: crear un objeto con base 8 y altura 5
rectangulo1 = Rectangulo(8, 5)

# COMPLETAR: llamar al metodo para mostrar el área
if __name__ == "__main__":
    rectangulo1.mostrarArea()


# Actividad 3. Interpretar herencia
class Operacion(object): 
    def __init__(self, numero1, numero2): 
        self.numero1 = numero1 
        self.numero2 = numero2 
  
    def calcular(self): 
        return self.numero1 + self.numero2 
  
class Multiplicacion(Operacion): 
    def calcular(self): 
        return self.numero1 * self.numero2

operacion1 = Operacion(8, 4) 
operacion2 = Multiplicacion(8, 4) 
print(operacion1.calcular()) 
print(operacion2.calcular()) 

# 1. ¿Cuál es la clase padre?
# R: operacion
# 2. ¿Cuál es la clase hija?
# R: multiplicacion
# 3. ¿Cómo se indica la herencia?
# R: Colocando el nombre de la clase padre entre paréntesis al definir la clase hija: class Multiplicacion(Operacion):
# 4. ¿Qué propiedades utiliza la clase hija?
# R: numero1 y numero2
# 5. ¿Por qué puede utilizarlas sin definir su propio __init__?
# R: Porque al haber herencia, la clase hija hereda automaticamente el constructor y los atributos de la clase padre
# 6. ¿Por qué los métodos calcular() tienen resultados distintos?
# R: por la sobreescritura de metodos, la clase hija redefine calcular() para realizar una multiplicacion
# 7. ¿Qué valores se imprimen?
# R: 
# 12 (resultado de 8 + 4)
# 32 (resultado de 8 * 4)
# 8. ¿Qué sucedería si eliminamos calcular() de Multiplicacion?
# R: Heredaria el metodo calcular() de la clase padre operacion, por lo que imprimiria la suma (12) en ambos casos