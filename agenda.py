AGENDA = {}

# Funcoes
def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print('>>>>>> Agenda vazia')

def buscar_contato(contato):
    try:
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('Endereco:', AGENDA[contato]['endereco'])
        print('Email:', AGENDA[contato]['email'])
        print('---------------------------------------')
    except KeyError:
        print('>>>>>> Contato {} nao encontrado'.format(contato))
    except Exception as error:
        print('>>>>>> Um erro inesperado ocorreu: ', error)        

def ler_detalhes_contato():
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o email do contato: ')
    endereco = input('Digite o endereco do contato: ')
    return telefone, email, endereco
 

def incluir_editar_contato(contato, telefone, endereco, email):
    AGENDA[contato] = {
        'telefone': telefone,
        'endereco': endereco,
        'email': email,
    }
    salvar()
    print('>>>>>> Contato {} adicionado/editado com sucesso!'.format(contato))

def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print()
        print('>>>>>> Contato {} excluido com sucesso!'.format(contato))
        print()
    except KeyError:
        print('>>>>>> Contato {} nao encontrado!'.format(contato))    
    except Exception as error:
        print('>>>>>> Um erro inesperado ocorreu: ', error)

def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                endereco = AGENDA[contato]['endereco']
                email = AGENDA[contato]['email']

                arquivo.write('{},{},{},{}\n'.format(contato, telefone, endereco, email)) 
        print('>>>>>> Agenda exportada com sucesso!')
    except Exception as error:
        print('>>>>>> Um erro inesperado ocorreu: ', error)

def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_editar_contato(nome, telefone, endereco, email)
    except FileNotFoundError:
        print('>>>>>> Arquivo nao encontrado!')
    except Exception as error:
        print('>>>>>> Um erro inesperado ocorreu: ', error)   

def salvar():
    exportar_contatos('database.csv')

def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'telefone': telefone,
                    'endereco': endereco,
                    'email': email,
                }
        print('>>>>>> Database carregada com sucesso! \n {} contatos carregados'.format(len(AGENDA)))   
    except FileNotFoundError:
        print('>>>>>> Arquivo nao encontrado!')
    except Exception as error:
        print('>>>>>> Um erro inesperado ocorreu: ', error)

def imprimir_menu():
    print('------------------------------------')
    print('1 - Mostrar todos os contatos')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar contatos para CSV')
    print('7 - Importar contatos CSV')
    print('0 - Fechar agenda')
    print('------------------------------------')

# Inicio do programa
carregar()
while True:
    imprimir_menu()

    opcao = input('Digite uma opcao: ')
    if opcao == '1':
        mostrar_contatos()
    elif opcao == '2':
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)
    elif opcao == '3':
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('>>>>>> Contato já existente')
        except KeyError: 
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
    elif opcao == '4':
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('>>>>>> Editando contato', contato)
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
        except KeyError: 
            print('>>>>>> Contato nao existente')
    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)
    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo a ser exportado: ')
        exportar_contatos(nome_do_arquivo)
    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo a ser importado: ')
        importar_contatos(nome_do_arquivo)
    elif opcao == '0':
        print('>>>>>> Agenda fechada')
        break  
    else:
        print('>>>>>> Opcao invalida')
