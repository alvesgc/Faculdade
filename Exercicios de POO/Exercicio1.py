def soma(a,b):
    return a + b
def sub(a,b):
    return a - b
def mult(a,b):
    return a * b
def div(a,b):
    return a / b
def calculadora():
  while True: 
    print("Escolha a operação desejada: ")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    
    escolha = eval(input("Digite a operácão desejada: "))
    
    if escolha == 5:
      print("Obrigado por usar a calculadora!")
      break
    if escolha not in (1,2,3,4,5):
      print("Opção inválida!")
      continue
    
    num1 = eval(input("Digite o primeiro número: "))
    num2 = eval(input("Digite o segundo número: "))
    if escolha == 1: 
       resultado = num1 + num2
    elif escolha == 2:
       resultado = num1 - num2
    elif escolha == 3:
       resultado = num1 * num2
    elif escolha == 4:
       resultado = num1 / num2
       
    print(f"O resultado da operação é: {resultado}")
    
    continuar = input.to("Deseja continuar? (S/N): ")
    if continuar != "S":
      print("Obrigado por usar a calculadora!")
      break
calculadora()
