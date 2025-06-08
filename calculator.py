"""Calculadora simple en Python"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Calculadora simple")
    parser.add_argument("num1", type=float, help="Primer número")
    parser.add_argument("operation", choices=["+", "-", "*", "/"], help="Operación")
    parser.add_argument("num2", type=float, help="Segundo número")
    args = parser.parse_args()

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    result = operations[args.operation](args.num1, args.num2)
    green = "\033[92m"
    reset = "\033[0m"
    print(f"{green}Resultado: {result}{reset}")
