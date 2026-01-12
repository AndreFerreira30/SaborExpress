import os

restaurantes = [{'nome': "Praça",'categoria': 'Japonesa','ativo': False}, 
                 {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                 {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}
]

def exibir_nome_programa():
    """
    Esta função tem como objetivo exibir o nome do projeto de forma estilizada
    
    """

    print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def exibir_opcoes():
    """
    Esta funçaõ tem como objetivo exibir as opções disponiveis ao usuario utilizar

    """
    print("[1] - Cadastrar restaurantes")
    print("[2] - Listar restaurantes")
    print("[3] - Alternar estado do restaurante")
    print("[4] - Sair\n")

def exibir_subtitulo(texto):
    """
    Função com o objetivo de estilizar os subtitulos quando selecionado uma opção no menu
    Inputs:
    -linha (ira realizar criar um "cabeçalho" no subtitulo com *, somente para fins esteticos)
    """
    os.system("cls")
    linha = '*' * (len(texto)+4)
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():
    """
    Docstring para finalizar o app, exibindo o subtitulo antes de encerrar
    """
    exibir_subtitulo("Finalizando app")

def voltar_ao_menu():
    """
    Retorna ao menu, chamando o matodo main() 
    Output - retorna ao menu principal
    """
    print(input("\nDigite qualquer tecla para voltar ao menu principal: "))
    main()

def opcao_invalida():
    """
    Ativida quando acontece um erro no codigo, diagnosticando e chamando a função de retorno ao menu principal
    Output:
    - Retorna ao menu principal
    """
    print('Opção invalida \n')
    voltar_ao_menu()

def cadastrar_novo_restaurante():
    """
    Cadastra um novo restaurante
    Inputs:
    - Nome do restaurante 
    - Categoria

    Outputs:
    adiciona um novorestaurante a lista de restaurantes
    """
    exibir_subtitulo("Cadastrando novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite a categoria do restaurante {nome_do_restaurante}: ")
    dados_restaurante = {"nome": nome_do_restaurante, 'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f"cadastrado com sucesso")
    voltar_ao_menu()

def listar_restaurantes():
    """
    Lista todos os restaurantes
    Outputs: 
    - Exibe todos os restaurantes da lista
    """
    exibir_subtitulo("Listando restaurantes ")
    print("Nome do restaurante".ljust(22) + " | " + "Categoria".ljust(21) + "| Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = "ativado " if restaurante['ativo'] else 'desativado'
        print(f"- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante} ")
    voltar_ao_menu()

def alternar_estado_restaurante():
    """
    Altera o estado do restaurante entre ativo e inativo
    Output:
    - Exibe uma mensagem indicado o sucesso da operação
    """
    exibir_subtitulo("Alterando o estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante['ativo'] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print (mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")

    voltar_ao_menu()

def escolher_opcao():
    """
    Solicita e executa a opção escolhida pelo usuario
    Outputs:
    - Executa a opção escolhida pelo usuario
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if(opcao_escolhida == 1):
            cadastrar_novo_restaurante()
        elif(opcao_escolhida == 2):
            listar_restaurantes()
        elif(opcao_escolhida == 3):
            alternar_estado_restaurante()
        elif(opcao_escolhida == 4):
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    """
    Função principal do sistemas
    """
    os.system("cls")
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()
