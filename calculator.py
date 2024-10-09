import math

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Erro: Por favor, insira um número válido.")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida."
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "Erro: Raiz quadrada de número negativo não é permitida."
    return math.sqrt(x)

def calculator():
    print("Bem-vindo à calculadora em Python!")
    while True:
        print("\nSelecione a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Potência")
        print("6. Raiz quadrada")
        print("7. Sair")

        escolha = input("Escolha uma opção (1/2/3/4/5/6/7): ")

        if escolha == '7':
            print("Saindo da calculadora.")
            break

        if escolha in ['1', '2', '3', '4', '5']:
            num1 = get_number_input("Digite o primeiro número: ")
            num2 = get_number_input("Digite o segundo número: ")

            if escolha == '1':
                print(f"Resultado: {num1} + {num2} = {add(num1, num2)}")
            elif escolha == '2':
                print(f"Resultado: {num1} - {num2} = {subtract(num1, num2)}")
            elif escolha == '3':
                print(f"Resultado: {num1} * {num2} = {multiply(num1, num2)}")
            elif escolha == '4':
                resultado = divide(num1, num2)
                print(f"Resultado: {num1} / {num2} = {resultado}")
            elif escolha == '5':
                print(f"Resultado: {num1} ** {num2} = {power(num1, num2)}")
        elif escolha == '6':
            num = get_number_input("Digite o número para calcular a raiz quadrada: ")
            resultado = sqrt(num)
            print(f"Resultado: sqrt({num}) = {resultado}")
        else:
            print("Erro: Opção inválida. Tente novamente.")

if __name__ == "__main__":
    calculator()
