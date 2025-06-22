def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"
    
def main():
    print("Calculadora Básica en Python")
    print("Operaciones disponibles: +, -, *, /")

    try:
        a = float(input("Ingresa el primer número: "))
        operacion = input("Ingresa la operación (+ - * /): ")
        b = float(input("Ingresa el segundo número: "))

        if operacion == '+':
            resultado = suma(a, b)
        elif operacion == '-':
            resultado = resta(a, b)
        elif operacion == '*':
            resultado = multiplicacion(a, b)
        elif operacion == '/':
            resultado = division(a, b)
        else:
            resultado = "Operación no válida"

        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Entrada inválida. Asegúrate de ingresar números.")
if __name__ == '__main__':
    main()        