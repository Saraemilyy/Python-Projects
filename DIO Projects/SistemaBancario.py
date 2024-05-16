from datetime import datetime


menu = """
   [d] Depositar
   [s] Sacar
   [e] Extrato
   [x] Sair

=> """

LIMITESAQUESISTEMA = 3
LimiteDinheiroSaqueSistema = 500.00
SaldoUsuario = 0.0
Extrato = ""
Valor = 0.0
QuantidadeSaques = 1

while True:
    opcao = input(menu)
    
    if opcao == "d":
        Valor = float(input("Digite o valor para depósito:"))
        if Valor > 0:
            SaldoUsuario += Valor
            data_hora_atual = datetime.now().strftime("%Y-%m-%d ás %H:%M")
            Extrato += f"Depósito: R$ {Valor:.2f} em {data_hora_atual}\n"
            print(f"O valor de R$ {Valor} foi depositado na sua conta.")
        else:
            print("A operação falhou. O valor informado é inválido.")

    elif opcao == "s":
        ExcedeuSaque = QuantidadeSaques > LIMITESAQUESISTEMA
        if ExcedeuSaque:
            print(f"Você atingiu o imite de saque diário. Segue quantidade de saques permitidos: {LIMITESAQUESISTEMA}")
        else:
            Valor = float(input(f"Valor disponível na sua conta: R$ {SaldoUsuario}. Valor limite de saque é de: R$ {LimiteDinheiroSaqueSistema}. Digite o valor do seu saque: "))
            ExcedeuSaldo = SaldoUsuario < Valor
            ExcedeuLimite = Valor > LimiteDinheiroSaqueSistema
            if ExcedeuSaldo:
                print(f"O valor excedeu o seu saldo atual, por favor, tente novamente. Seu saldo disponível é de: {SaldoUsuario}")
            elif ExcedeuLimite: 
                print(f"O valor exceu o limite de valor de saque. Segue valor máximo permitido: R$ {LimiteDinheiroSaqueSistema}")
            else:
                QuantidadeSaques += 1
                SaldoUsuario -= Valor
                data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                Extrato += f"Saque: R$ {Valor:.2f} em {data_hora_atual}\n"
                print(f"Saque no valor de R$ {Valor} realizado com sucesso! Saldo disponível na conta: R$ {SaldoUsuario}.")
    elif opcao == "e":
        print(Extrato)
    elif opcao == "x":
        break
    else:
        print("Operação inválida, por favor, selecione uma opção listada.")
