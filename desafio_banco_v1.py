# O objetivo é implementar três operações essenciais: depósito, saque e extrato. O sistema será desenvolvido para um banco que busca monetizar suas operações. Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python e criar um sistema funcional que simule as operações bancárias
print("Seja bem-vindo.")
MENU = ("""Qual operação deseja realizar?
[1] - SAQUE
[2] - DEPOSITO
[3] - EXTRATO
[0] - SAIR

=> """)
OPCOES = [0, 1, 2, 3]
saldo = 1000
historico = []
LIMITE_SAQUE_DIARIO = 3
LIMITE_SAQUE = 500
numero_saque = 0
CAB = " - EXTRATO - "
ROD = "#"
def sacar(saldo, valor_saque,LIMITE_SAQUE):
    
    if valor_saque < 0:
        print("FALHA: Valor não permitido.")
        print(ROD.center(50,"#"))
    elif valor_saque > LIMITE_SAQUE:
        print(ROD.center(50,"#"))
        print("FALHA: Tentativa de saque ultrapassa o limite permitido.")
        print(ROD.center(50,"#"))
        
    elif valor_saque <= saldo and valor_saque <= LIMITE_SAQUE:
        saldo -= valor_saque
        historico.append(f"- Você sacou R${valor_saque:.2f}.")
        print(f"Você sacou R${valor_saque}. Saldo restante: R${saldo:.2f}")
        print(ROD.center(50,"#"))
    else:
        print("FALHA: Limite de saldo insuficiente.")
        print(ROD.center(50,"#"))
    return saldo 

def depositar(saldo, valor_deposito):
    if valor_deposito >= 0:
        saldo += valor_deposito
        historico.append(f"- Você depositou R${valor_deposito:.2f}.")
        print(ROD.center(50,"#"))
        print(f"Você depositou R${valor_deposito}. Saldo restante: R${saldo:.2f}")  
        print(ROD.center(50,"#"))
    else:
        print('FALHA: Valor para deposito inválido.')
        print(ROD.center(50,"#"))
    return saldo

def extrato(saldo):
    print(CAB.center(50, "#"))
    if not historico:
        print(" - Você ainda não realizou nenhuma operação.")
    else:
        for item in historico:
            print(item)
        print(ROD.center(50,"#"))
        print(f"Saldo em conta = R${saldo:.2f}")
    print(ROD.center(50,"#"))
        
while True:
    opcao = int(input(MENU))

    if opcao == 1:
        if numero_saque < LIMITE_SAQUE_DIARIO:
            valor_saque = float(input("Qual valor deseja sacar? "))
            saldo = sacar(saldo, valor_saque, LIMITE_SAQUE)
            numero_saque += 1
        elif numero_saque >= LIMITE_SAQUE_DIARIO:
            print(ROD.center(50,"#"))
            print("FALHA: Você atingiu o limite de saques diário.")
            print(ROD.center(50,"#"))
        
    elif opcao == 2:
        valor_deposito = float(input("Qual valor deseja depositar? "))
        saldo = depositar(saldo, valor_deposito)
        
    elif opcao == 3:
        extrato(saldo)
    
    elif opcao not in OPCOES:
        print(ROD.center(50,"#"))
        print('FALHA: Opção inválida. Tente novamente')
        print(ROD.center(50,"#"))
    elif opcao == 0:
        print(ROD.center(50,"#"))
        print("Obrigada pela preferencia!")
        print(ROD.center(50,"#"))    
        break
    