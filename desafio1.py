BEM_VINDO = "\033[1;4;94m{0}|SEJA BEM VINDO(A)|{0}\033[0m".format("_"*10)

def exibir_menu():
    return str(input("""
\033[94m[Faça a(s) operação(ões) que deseja!]\033[0m

Digite \033[93m(1)\033[0m para \033[92mDEPÓSITO\033[0m
Digite \033[93m(2)\033[0m para \033[91mSAQUE\033[0m
Digite \033[93m(3)\033[0m para \033[95mEXTRATO\033[0m
Digite \033[93m(4)\033[0m para \033[94mSAIR\033[0m
"""))

saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3

print(BEM_VINDO)

while True:
    menu = exibir_menu()
    opcao = menu
    
    if opcao == "1":
        dep = float(input("Digite o valor do seu depósito: "))
        saldo += dep
        extrato += f"Depósito: +{dep:.2f}\n"
        print(f"Depósito de \033[92mR${dep:.2f}\033[0m realizado com sucesso.")
     
    elif opcao == "2":
        if LIMITE_SAQUES > 0:
            
            saque = float(input("Digite o valor que deseja sacar: "))
            if saque <= saldo:
                saldo -= saque
                extrato += f"Saque: -{saque:.2f}\n"
                LIMITE_SAQUES -= 1
                print(f"Saque de \033[91mR${saque:.2f}\033[0m realizado com sucesso.")
            else:
                print("Saldo insuficiente para saque.")
        else:
            print("Limite de saques diários atingido.")
    
    elif opcao == "3":
        print("\n\033[95mExtrato:")
        print(extrato)
        print(f"Saldo atual: R${saldo:.2f}")
        
    elif opcao == "4":
        print('''\033[94m
Saindo...
Finalizando as operações!
Obrigado pela preferência!\033[0m''')
        break
    else:
     
     if opcao != ["1, 4"]:
        print("\033[91mERRO! Entrada inválida! Tente as opções acima!\033[0m")
     
     else:
        print("\033[91mERRO! Entrada inválida! Tente as opções acima!\033[0m")