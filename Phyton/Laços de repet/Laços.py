## Utilizando o laço for 
## Para nome (interação com for) faça: 
## Print de cada nome em nomes.
nomes = ["Alisson", "Gustavo", "Cadu"]
for nome in nomes:
  print(nome)
  
## Utilizando o laço while

palavra = input("Digite uma palavra: \n")
while palavra.lower != "sair":
  palavra = input("Digite sair para sair do laço: \n")
print("Você saiu do laço!")

## Utilizando um laço ifinito, com a instrução break

while True:
  palavra = input("Digite sair para sair do laço: \n")
  if palavra == "sair":
    break 
print("Você digitou sair e agora está fora do laço!")

## Caso haja varios laços o break será relativo ao laço que esta inserido.

while True:
  print("Voce está no primeiro laço!")
  opcao1 = input("Deseja sair do laço? Digite SIM para isso. \n")
  if opcao1 == "SIM":
   break
  else:
       while True: 
         print("Voce está no segundo laço!")
         opcao2 = input("Deseja sair do laço? Digite SIM para isso. \n")
         if opcao2 == "SIM": 
           break
         print("Voce saiu do segundo laço!")
print("Voce saiu do primeiro laço!")
        
## Instrução continue

for num in range(1, 11):
  if num == 0:
    continue  
  else: 
    print(num)
print("Laço encerrado")

      