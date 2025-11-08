def calculadora(numero1, numero2, operacao):
    if operacao == '+':
        return numero1 + numero2
    elif operacao == '-':
        return numero1 - numero2
    elif operacao == '*':
        return numero1 * numero2
    elif operacao == '/':
        return numero1 / numero2
    else:
        return "Operação inválida"


# teste ;-;

print(calculadora(10, 5, '+'))
print(calculadora(8, 2, '/'))
print(calculadora(100, 5, '*'))
print(calculadora(50, 10, '-'))
