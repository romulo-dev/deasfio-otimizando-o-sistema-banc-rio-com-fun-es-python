Criei um módulo chamado operacoes para tornar o código mais limpo e chamar suas funções no módulo principal no menu de opções: 
```
import datetime



def sacar(saldoCliente, valor, extrato, numero_saques = 0, limite_saques = 500.00):

    dataSaque = datetime.datetime.today()

    valor = float(input("Digite o valor a ser sacado"))

    if valor > 0.00 and valor <= saldoCliente and type(valor) == float and valor <= limite_saques:

            if dataUltimoSaque is None:

               dataUltimoSaque = datetime.datetime.today()

               numero_saques += 1

               saldoCliente -= valor 

               extrato += f"Saque de R${valor:.2f} realizado em {dataUltimoSaque}\n"

            else: 

                if dataSaque.date() >=  dataUltimoSaque.today().date():

                    if numeroSaques == 3:

                        print("vc já atingiu o seu limite de saques por dia")

                    else:

                        numeroSaques += 1

                        dataUltimoSaque = dataSaque

                        saldoCliente -= valor

                        extrato += f"Saque de R${valor:.2f} realizado em {dataUltimoSaque}\n"

                else:

                    print("Ocorreu um erro")

    else:

        print("Você digitou 0 ou um valor negativo ou seu saldo não é suficiente para esse saque ou você digitou um valor inválido")    

    return saldoCliente | extrato



def deposito(saldo, valor, extrato):

    valor = float(input("Digite o valor a ser depositado: "))

    if valor > 0.00:

            DataDeposito = datetime.datetime.today()

            saldo += valor

            extrato += f"Deposito de R${valor :.2f} feito em {DataDeposito}\n"

            return saldo | extrato

    else:

        print("Você não digitou o valor corretamente")

        return None        



def verificaClienteTemCPF(lista_clientes, nome, cpf):

     for cliente in lista_clientes:

          if(cliente.nome == nome and cliente.cpf):

               return None

     return True



def criarCliente(lista_clientes):

     nome = input("Digite o nome do cliente")

     data_nascimento = input("Digite a data de nascimento")

     cpf = input("Digite o CPF")

     logradouro = input("Digite o logradouro")

     numero = int(input("Digite o número"))

     bairro = input("Digite o nome do bairro")

     cidade = input("Digite o nome da cidade")

     estado = input("Digite a sigla do estado")



     endereço = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"

     if(verificaClienteTemCPF(lista_clientes, nome, cpf)) != None:

          criente = {

               "nome": nome,

               "data_nascimentp": data_nascimento,

               "cpf": cpf,

               "endereco": endereço

          }

          lista_clientes.append(criente)



def criarContaCorrente(lista_contas, numero_conta, cliente, agencia = "0001", saldo_cliente = 0, extrato = 0):

     

     nova_conta = {

        "agencia": agencia,

        "numero_conta": numero_conta,

        "cliente": cliente,

        "saldo_cliente": saldo_cliente,

        "extrato": extrato

    }

    

     lista_contas.append(nova_conta)
```


Inseri os campos extrato e saldo_cliente em conta corrente, usei estrutura de dicionário para inserir conta na lista de contas correntes e inserir cliente na lista de clientes
