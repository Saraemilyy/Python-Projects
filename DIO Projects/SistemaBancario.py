import textwrap

def menu():
    menu = """\n
    ================= MENU =====================
    [d]\tDepositar
    [s]\tSacar
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [e]\tExtrato
    [x]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(SaldoUsuario, valor, Extrato, /):
    if valor > 0:
        SaldoUsuario += valor
        Extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print(f"\n=== Depósito no valor de {valor} feito com sucesso! ===")
    else:
        print("@@@ Operação Falhou! O valor informado é inválido. @@@")
    return SaldoUsuario, Extrato

def sacar(*, SaldoUsuario, valor, Extrato, LimiteDinheiroSaqueSistema, QuantidadeSaques, LIMITESAQUESISTEMA):
    ExcedeuSaldo = valor > SaldoUsuario
    ExcedeuLimite = valor > LimiteDinheiroSaqueSistema
    ExcedeuSaque = QuantidadeSaques > LIMITESAQUESISTEMA
    
    if ExcedeuSaldo:
        print("\n@@@ Operação falhou! Você não tem saldo o suficiente. @@@")
    elif ExcedeuLimite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif ExcedeuSaque:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    elif valor > 0:
        SaldoUsuario -= valor
        Extrato += f"Saque:\t\t R$ {valor:.2f}\n"
        QuantidadeSaques += 1
        print(f"\n=== Saque realizado com sucesso no valor de {valor}!. ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return SaldoUsuario, Extrato

def exibir_extrato(SaldoUsuario, /, *, Extrato):
    print("\n============== EXTRATO ==============")
    print("Não foram realizadas movimentações." if not Extrato else Extrato)
    print(f"\nSaldo:\t\tR$ {SaldoUsuario:.2f}")
    print("=========================================")

def criar_usuarios(Usuarios):
    cpf = input("Informe o CPF (somente números): ")
    Usuario = filtrar_usuario(cpf, Usuarios)
    if Usuario:
        print("\n Já existe usuário com esse CPF. @@@")
        return
    nome = input("Informe o nome completo:")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    Usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, Usuarios):
   UsuariosFiltrados  = [Usuario for Usuario in Usuarios if Usuario['cpf'] == cpf]
   return UsuariosFiltrados[0] if UsuariosFiltrados else None

def criar_conta(agencia, numero_conta, Usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, Usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITESAQUESISTEMA = 3
    AGENCIA = "0001"
    LimiteDinheiroSaqueSistema = 500
    SaldoUsuario = 0.0
    Extrato = ""
    Valor = 0
    QuantidadeSaques = 1
    Usuarios = []
    Contas = []

    while True:
        opcao = menu()
        
        if opcao == "d":
            valor = float(input("Informe o valor do seu depósito: "))
            SaldoUsuario, Extrato = depositar(SaldoUsuario, valor, Extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            SaldoUsuario, Extrato = sacar(
                SaldoUsuario=SaldoUsuario,
                valor=valor,
                Extrato=Extrato,
                LimiteDinheiroSaqueSistema=LimiteDinheiroSaqueSistema,
                QuantidadeSaques=QuantidadeSaques,
                LIMITESAQUESISTEMA=LIMITESAQUESISTEMA,
            )

        elif opcao == "nc":
            numero_conta = len(Contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, Usuarios)
            if conta:
                Contas.append(conta)

        elif opcao == "nu":
            criar_usuarios(Usuarios)
        
        elif opcao == "lc":
            listar_contas(Contas)
            
        elif opcao == "e":
            exibir_extrato(SaldoUsuario, Extrato=Extrato)

        elif opcao == "x":
            break
        else:
            print("Operação inválida, por favor, selecione uma opção listada.")

main()
