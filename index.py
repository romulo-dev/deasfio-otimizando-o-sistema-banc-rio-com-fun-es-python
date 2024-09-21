import datetime
from operacoes import deposito, sacar, criarCliente, criarContaCorrente



clientes = []
lista_contas = []

def findConta(cliente):
    cliente = input("Digite o nome do cliente")
    for c in clientes:
        if(c.nome == cliente):
            for conta in lista_contas:
                if(conta.nome == c.nome):
                    return conta
     
    
    print("Cliente não encontrado")
    return None

while True:

    conta = findConta()
    if(conta != None):
        print("D - para depositar")
        print("S - para sacar")
        print("E - para tirar extrato")
        print("C - criar cliente")
        print("CC - criar conta corrente")
        print("Q - para sair")
        opcao = str(input("Selecione uma opcao: "))

        if opcao == "D":
            deposito(conta.saldo_cliente, conta.extrato)
        elif opcao == "S":
            sacar(conta.saldo_cliente, conta.extrato)    
        elif opcao == "E":
            print(conta.extrato)
        elif opcao == "C":
            criarCliente(clientes)
        elif opcao == "CC":
            criarContaCorrente()
        elif opcao == "Q":
            print("Saindo...")
            break
        else:
            print("Você digitou um caractere inválido")

        

