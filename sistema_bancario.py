print(f"{'SISTEMA BANCÁRIO PYTHON':=^60}")

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu = """

[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

=>"""

while True:

    opcao = input(menu)

    if opcao == "d":
        dep = float(input("Valor de depósito: R$"))

        if dep > 0:
            saldo += dep
            extrato += f"Depósito: R$ {dep:.2f}\n"

        else:
            print("Operação falhou, digite um número válido!")
    
    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            saq = float(input("Valor do saque: R$"))

            if saq <= limite:
                if saq <= saldo:
                    saldo -= saq
                    extrato += f"Saque: R$ {saq:.2f}\n"
                    numero_saques += 1
                else:
                    print("Operação falhou, valor de saque maior que o saldo.")
            else:
                print("Valor de saque maior que o limite! Operação inválida.")
        else:
            print("Operação falhou, você já fez todos saques possíveis diários.")
    
    elif opcao == "e":
        print(f"{'EXTRATO':=^20}")
        print("Não foram realizadas operações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print(f'{20*"="}')

    elif opcao == "q":
        print("Obrigado pela visita! Volte sempre.")
        break

    else:
        print("Opção inválida, tente novamente!")
    
        
        