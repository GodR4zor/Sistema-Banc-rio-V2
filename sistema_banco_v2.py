
# Import

import textwrap

# Menu
def menu():
    menu = """\n
    ==================== MENU ====================
    
    Digite a letra da acao que deseja realizar
    
    [d] : Depositar
    [s] : Sacar
    [e] : Extrato
    [c] : Criar Usuario
    [cc]: Criar Conta
    [l] : Lista de contas
    [q] : Sair

    => """

    return input(textwrap.dedent(menu))

# Funcao SACAR:
def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    # Verificacoes

    saques_excedido = numero_saques >= limite_saques
    valor_excedido = valor > limite
    valor_negativo = valor < 0

    if saques_excedido:
        print("\n==== Limite de saque diario excedido ====")
    
    elif valor_excedido:
        print("\n==== Valor de saque excedido! ====")
    
    elif valor_negativo:
        print("\n==== Valor digitado invalido! ====")
    
    else:
        saldo -= valor
        extrato += f"Saque Realizado: R${valor}\n"
        numero_saques += 1
        print(textwrap.dedent("\n========= Saque Realizado com Sucesso! ========="))

    return saldo, extrato, numero_saques

# Funcao DEPOSITO:
def deposito(saldo, valor, extrato):

    # Verificacao
    valor_negativo = valor < 0
    valor_maior_saldo = valor > saldo

    if valor_negativo:
        print("Valor digitado invalido!")
    else:
        saldo += valor
        extrato += f"Deposito Realizado: R${valor}\n"
        print(textwrap.dedent(("========= Deposito Realizado com Sucesso! =========")))
    
    return saldo, extrato

# Funcao EXTRATO:
def extrato(saldo, /,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Funcao FILTAR_USUARIO:
def filtrar_usuario(cpf, usuarios):
    # Verifica se ja existe usuario com o mesmo CPF
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    # Caso exista retorna o usuario, caso nao exista retorna NONE``
    return usuarios_filtrados[0] if usuarios_filtrados else None

# Funcao CRIAR_USUARIO:
def criar_usuario(usuarios):
    cpf = int(input("Digite o numero do CPF: "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n==== Ja existe uma conta com este usuario! ====")
        return

    nome = input("Informe seu nome completo\n=> ")
    data_de_nascimento = input("Digite a data de nascimento (dd/mm/yyyy)\n=> ")
    endereco = input("Digite o seu endereco (logradouro, n, bairro - cidade - sigla/estado)\n=> ")

    usuarios.append({"Nome": nome, "Data de Nascimento": data_de_nascimento, "CPF": cpf, "Endereco": endereco})
    
    print("==== USUARIO CRIADO COM SUCESSO ====")

# Funcao CRIAR_CONTA:
def criar_conta(AGENCIA, numero_conta, usuarios):
    cpf = int(input("Digite o numero do CPF: "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("==== CONTA CRIADA COM SUCESSO! ====")
        return {"Agencia": AGENCIA, "Numero da Conta": numero_conta, "Usuario": usuario}
    
    print("\n==== USUARIO NAO ENCONTRADO! ====")

def listar_contas(contas):
    
    for conta in contas:
        linha = f"""
            Agencia:\t{conta["Agencia"]}
            C/C:\t{conta["Numero da Conta"]}
            Titular:\t{conta["Usuario"]["Nome"]}
        """
        print("=" * 100)
        print(linha)

# Funcionamento
def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato_registro = ""
    numero_saques = 0

    contas = []
    usuarios = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Digite o valor que deseja depositar: "))
            saldo, extrato_registro = deposito(saldo, valor, extrato_registro)
    
        elif opcao == "s":
            valor = float(input("Digite o valor que deseja sacar: "))
            saldo, extrato_registro, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato_registro, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
    
        elif opcao == "e":
            extrato(saldo, extrato=extrato_registro)

        # Criar usuario
        elif opcao == "c":
            criar_usuario(usuarios)

        # Criar conta
        elif opcao == "cc":
            numero_da_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_da_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            break

# Rodando Codigo:
main()