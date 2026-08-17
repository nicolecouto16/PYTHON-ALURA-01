import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo': False},
               {'nome':'Pizza', 'categoria':'Pizza', 'ativo': True},
               {'nome':'Cantina', 'categoria':'Italiana', 'ativo': False}]
               
def exibir_nome_do_programa():
    '''
    Aqui sera exibido o nome do nosso programa atraves de um print'''
    print("Sabor Express\n")

def exibir_opcoes():
    '''Ja aqui sera exibido nossas opções dentro dessa função
    Como:
    - Cadastrar
    -Listar
    -Alterar o estado
    -Saida
    '''
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")

def finalizar_app():
    '''Nesse caso sera o finalizar app, apos selecionar a  
    opção 4 da função exibir_opcoes'''
   exibir_subtitulo('Finalizar app!')

def voltar_ao_menu_principal():
    '''Ao selecionar um opção, para sair basta 
    clicar em qualquer tecla, que retornara na pag inicial do programa'''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    '''Se não tiver a opção escolhida ele ira retornar opção inavalida'''
    print("Opção invalida!\n")
    voltar_ao_menu_principal()
    
def exibir_subtitulo(texto):
    ''''Apos ter selecionado o que desejar tera seu subtitulo
        -cls: Para limpar o terminal
        -len: para deixar visualmente mais bonito o subtitulo, com o *
    '''
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha) 
    print(texto)
    print(linha) 
    print()
    
def cadastrar_novo_restaurante():
    '''Essa função é responsavel por cadastrar um novo restaurante  
    Inputs:
    -Nome do restaurante
    -Categoria
    
    Outputs:
    -Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurente que deseja cadastrar: ")
    categoria = input(f"Digite o nome do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {'nome': nome_do_restaurante, 
    'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante: {nome_do_restaurante} foi cadastrado com sucesso!\n")
    voltar_ao_menu_principal()

def listar_restaurente():
    '''Nessa função vamos estar listando os restaurantes
        -.ljust(20): deixara visualmente arrumado para ter o mesmo espaçamento
        -ativado/desativado: para saber como esta o restaurante
    '''
    exibir_subtitulo('Listando restaurantes')
    
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(22)} | Status ')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}") 

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Nessa sera possivel alterar o estado do restaurante
    -True
    -False
    Pare mudar  o "status", caso um restaurante tirar ativo posso deixar ele desativado
    assim tambem para se estiver desativado
    -Caso ao digitar e não tiver o restaurante desejado sera enviado uma mensagem
    que o restaurante naõ foi encontrado
    '''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input("Digite o nome do restaurante que dejesa alterar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True 
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurente {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
            print("O restaurante não foi encontardo")

    voltar_ao_menu_principal()

    

def escolher_opcoes():
    '''4 Opções para o restaurante
    -Cadastrar : 1
    -Listar : 2
    -Alternar : 3
    -Finalizar : 4
    '''
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
    
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurente()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''A main é principal, nela vamos estar:
       -cls
       -exibindo o nome do programa
       -exibindo nossas opções
       -e podendo escolher qual queremos      
        '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == "__main__":
    main()
    

