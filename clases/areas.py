class Areas:
    def __init__(self):
        pass

    #Triángulo
    def leer_datos_triangulo(self):
        base = float(input("Introduce la base del triángulo: "))
        altura = float(input("Introduce la altura del triángulo: "))
        return base, altura

    def calcular_area_triangulo(self, base, altura):
        return (base * altura) / 2

    def mostrar_resultado_triangulo(self, area):
        print(f"El área del triángulo es: {area:.2f}")

    #Rectángulo
    def leer_datos_rectangulo(self):
        base = float(input("Introduce la base del rectángulo: "))
        altura = float(input("Introduce la altura del rectángulo: "))
        return base, altura

    def calcular_area_rectangulo(self, base, altura):
        return base * altura

    def mostrar_resultado_rectangulo(self, area):
        print(f"El área del rectángulo es: {area:.2f}")