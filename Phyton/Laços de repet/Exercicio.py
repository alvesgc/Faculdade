'''Escreva um programa em Python que calcule o IMC do usuário e apresente seu estado 
de saúde conforme as informações abaixo:'''

def calcIMC():
  peso, altura = eval(input("Digite seu peso:")), eval(input("Digite sua altura: "))
  calculoImc = peso/altura**2
  
  if calculoImc < 18.5:
        return "Abaixo do peso"
  elif 18.5 <= calculoImc < 25:
        return "Peso ideal"
  elif 25 <= calculoImc < 30:
        return "Levemente acima do peso"
  elif 30 <= calculoImc < 35:
        return "Obesidade grau I"
  elif 35 <= calculoImc < 40:
        return "Obesidade grau II"
  else:
        return "Obesidade grau III"
calcIMC()
    