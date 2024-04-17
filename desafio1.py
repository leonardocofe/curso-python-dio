menu = """
============== MENU =============
[d] DEPOSITAR
[s] SACAR
[v] VERIFICAR SALDO ATUAL
[f] FINALIZAR PROGRAMA
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  
  opcao = input(menu)

  if opcao == "d":
    valor = float(input("Informe o valor que deseja depositar: "))

    if valor > 0:
      saldo += valor
      extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
      print("Operação falhou, informe um valor válido!")

  elif opcao == "s":
    valor = float(input("Informe o valor que deseja sacar: "))
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
      print("Operação falhou! Saldo insuficiente!")

    elif excedeu_limite:
      print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
      print("Operação falhou! Número máximo de saques efetuado.")  

    elif valor > 0:
      saldo -= valor
      extrato += f"Saque: R${valor:.2f}\n"
      numero_saques += 1

    else:
      print("Operação falhou! Informe um valor válido.")
  
  elif opcao == "v":
    print("\n===============EXTRATO===============")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================")

  elif opcao == "f":
    break

  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")


  
 