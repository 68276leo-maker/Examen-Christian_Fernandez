from clases.areas import Areas

def main():
    calculadora = Areas()

    # Calcular área de un triángulo
    base_t, altura_t = calculadora.leer_datos_triangulo()
    area_t = calculadora.calcular_area_triangulo(base_t, altura_t)
    calculadora.mostrar_resultado_triangulo(area_t)

    print()

    # Calcular área de un rectángulo
    base_r, altura_r = calculadora.leer_datos_rectangulo()
    area_r = calculadora.calcular_area_rectangulo(base_r, altura_r)
    calculadora.mostrar_resultado_rectangulo(area_r)

    print()

    # Calculos área de un círculo
    radio = calculadora.leer_datos_circulo()
    area_c = calculadora.calcular_area_circulo(radio)
    calculadora.mostrar_resultado_circulo(area_c)

if __name__ == "__main__":
    main()