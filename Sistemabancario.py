menu = """
========MENU========

    [d] depositar
    [s] sacar
    [e] extrato
    [q] sair

====================    
=> """
valor = 0
valor_saque = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
         saldo += valor
         extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! O Valor informado é invalido")

    elif opcao == "s":
        print("Saque")
        valor_saque = float(input("Informe o valor do saque:"))
                        
        if(valor_saque <= 500) and (numero_saques < LIMITE_SAQUES) and (valor_saque <= saldo):
           
            if valor_saque > 0:
               saldo -= valor_saque
               print("O valor sacado é de: " , "R$",valor_saque)
            
               numero_saques += 1
               extrato += f"Saque: R$ {valor_saque:.2f}\n"
    
               print("\n Saque realizado com sucesso")
            else:
                print("Operação falhou!")
       
        elif numero_saques == LIMITE_SAQUES:
            print("Limite de saque atingido")

        else:
          print("Operação Saque inválida")

    elif opcao == "e":
     print("\n================ EXTRATO ================")
     print("Não foram realizadas movimentações." if not extrato else extrato)
     print(f"\nSaldo: R$ {saldo:.2f}")
     print("==========================================")

    elif opcao == "q":
        print("Saindo...")
        break


    else:
        print("Operação inválida, por favor selecione novamanente a operação desejada.")
