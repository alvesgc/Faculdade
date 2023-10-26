class Conta:
   def __init__(self, numero, cpf, nomeTitular, saldo):
      self.numero = numero
      self.cpf = cpf
      self.nomeTitular = nomeTitular
      self.saldo = saldo
      
def main():
  c1 = Conta(numero:1, cpf:1, nomeTitular:"Alisson", saldo:1000)
  print(f"O saldo da conta é {c1.saldo}")
  print(f"Numero da conta: {c1.numero}")
  print(f"CPF do titular: {c1.cpf}")
  print(f"Nome do titular: {c1.nomeTitular}")

if __name__ == "__main__":
  main()