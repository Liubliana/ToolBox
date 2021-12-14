#Carlos Sabados (cs) é o único funcionário
#Senha: 0042

from datetime import *
import pickle
import getpass

data_atual = date.today()
data_br = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)
senhas = open('Nome_senha.txt', 'r', encoding='utf8')
acesso = 1
dias = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')

resposta = 'Deve ser um número inteiro!'

dic = open("ferramentas_dic.txt", 'rb')
classes = pickle.load(dic)
dic.close()

def abrir_arq(nome):
    arquivo = open(nome, 'a', encoding='utf8')
    arquivo.close()

def pontos (tam = 100):
    return '-' * tam

def interface(x, tam):
    print(pontos())
    alinhamento = ' ' * tam
    print(alinhamento, x)
    print(pontos())

def menu(classes):
    for i in classes:
            print('{} - {}' .format(i, classes[i][1]['classe']))

def erro(pergunta, resposta):
    b = 0
    while b == 0:
        try:
            x = int(input(pergunta))
            b = 1
            break
        except:
            print(resposta)
        finally:
            b = 0
    return x

def menu2(classes):
    print('')
    menu(classes)
    pergunta = 'Qual classe deseja acessar? '
    resposta = 'Deve ser um número inteiro'
    op = erro(pergunta, resposta)
    if op != 5 and op in classes:
        print('')
        for i in classes:
            if classes[op] == classes[i]:
                for g in classes[op]:
                    print('{}- {}'.format(g, classes[op][g]['nome']))

    return op

def dicionario(classes):
    dic = open('ferramentas_dic.txt', 'wb')
    pickle.dump(classes, dic)
    dic.close()
    dic = open('ferramentas_dic.txt', 'rb')
    classes = pickle.load(dic)
    dic.close()
    return classes

def ferramentas(classes, op):
    for g in classes[op]:
        print('{}- {}'.format(g, classes[op][g]['nome']))

def monitor(x, y, mensagem, parametro):
    iniciais = input('Digite as iniciais do email da Cesar School do aluno: ')
    leitura_arq = leitura('Nome_senha.txt')
    arquivo = open('Nome_senha.txt', 'w', encoding='utf8')
    tamanho = len(leitura_arq)
    count = 0

    for l in leitura_arq:
        palavras = l.split()
        if iniciais == palavras[4]:
            if parametro in l:
                arquivo.write(l.replace(x, y))
                print(mensagem)
        else:
            arquivo.write(l)
            count = count + 1
            if count == tamanho:
                print('Erro! Pessoa não encontrada :/')

    arquivo.close()
    print('\nLISTA DE MONITORES ATUAL')
    leitura_arq = leitura('Nome_senha.txt')
    for l in leitura_arq:
        if 'Monitor' in l:
            textinho = l.split()
            print(textinho[0]+ ' '+ textinho[1]+ ' '+ textinho[2]+ ' '+ textinho[7]+ ' '+ textinho[8])
    print('')

def leitura(x):
    arquivo = open(x, 'r', encoding='utf8')
    leitura = arquivo.readlines()
    arquivo.close()
    return leitura

def ler(nome):
    abrir_arq(nome)
    arquivo = open(nome, 'r', encoding='utf8')
    print(arquivo.read())
    arquivo.close()

while acesso != 0:
    interface('LOG IN', 47)
    senhas.seek(0)
    iniciais = input('Digite suas iniciais do email da Cesar School: ')
    if acesso == 1:
        for linha in senhas:
            string_linha = linha.split()
            if iniciais == string_linha[4] and 'F' == string_linha[11]:
                senha = getpass.getpass("Digite sua senha: ")
                if senha == string_linha[10]:
                    print('Oi', string_linha[6])
                    matricula_f = string_linha[8]
                    nome = string_linha[1]+' '+string_linha[2]
                    acesso = 0
                    break

                else:
                    print('Senha incorreta')
                    break
        else:
            print('Iniciais não encontradas')
    else:
        acesso = 0

while acesso == 0:
    interface('OPÇÕES', 47)
    print('')
    print('1 - Ferramentas')
    print('2 - Gerenciar estudantes')
    print('3 - Históricos')
    print('4 - Ver reports')
    print('5 - Códigos')
    print('6 - Ver perfil')
    pergunta = '\nDigite o que deseja acessar: '
    opcao1 = erro(pergunta, resposta)

    if opcao1 == 1:
        interface('FERRAMENTAS', 45)
        print('1 - Ver histórico')
        print('2 - Gerenciar ferramentas')
        print('-1 - Voltar para o menu')
        pergunta = 'Escolha uma opção: '
        resposta = 'Deve ser um número inteiro'
        opcao2 = erro(pergunta, resposta)
        if opcao2 == 1:
            op = menu2(classes)
            if op != 5 and op in classes:
                pergunta = 'Digite o número da ferramenta que deseja acessar o histórico: '
                ferramenta_opcao = erro(pergunta, resposta)

                if ferramenta_opcao in classes[op]:
                    interface('HISTÓRICO', 45)
                    nome_arquivo_f = 'Histórico ferramenta_' + classes[op][ferramenta_opcao][
                        'nome'] + '.txt'
                    abrir_arq(nome_arquivo_f)
                    arquivo_f = open(nome_arquivo_f, 'r', encoding='utf8')
                    print(arquivo_f.read())
                    arquivo_f.close()
                    enter = input('\nAperte enter para continuar\n')

            elif op == 5:
                abrir_arq('Agendamentos_Impressora3D.txt')
                agendamentos = open('Agendamentos_Impressora3D.txt', 'r', encoding='utf8')
                print(agendamentos.read())
                agendamentos.close()
                enter = input('\nAperte enter para continuar\n')

            else:
                print('Opção inválida')

        elif opcao2 == 2:
            interface('GERENCIAR FERRAMENTAS', 40)
            print('1 - Adicionar ferramenta')
            print('2 - Editar quantidade de uma ferramenta')
            print('3 - Remover ferramenta')
            print('-1 - Sair')
            pergunta = '\nDigite o que deseja acessar: '
            opcao2 = erro(pergunta, resposta)

            if opcao2 == 1:
                interface('CADASTRO DE FERRAMENTA', 39)
                nome = input('Digite o nome da ferramenta: ')
                qtdd = input('\nDigite a quantidade em estoque: ')
                funcao = input('\nDigite as funções da ferramenta (ex: cortar, segurar, furar). Para terminar, digite "sair": ')
                funcoes = []

                while funcao != 'sair' and funcao != 'Sair':
                    funcoes.append(funcao)
                    funcao = input('\nDigite as funções da ferramenta (ex: cortar, segurar, furar), para terminar, digite "sair": ')

                w = 0
                while w == 0:
                    try:
                        perigo = bool(int(input('\nEla é perigosa?\n0 - NÃO\n1 - SIM\n--> ')))
                        break
                    except:
                        print('Deve ser digitado 0 ou 1')
                    finally:
                        w=0

                print('')
                menu(classes)
                pergunta ='Digite o número da classe (se não existir, digite o número da nova): '
                classe_n = erro(pergunta, resposta)
                local = input('\nDigite a localização da ferramenta: ')
                como_usar = input('\nDigite como usar a ferramenta: ')

                if perigo == True:
                    perigo_str = 'sim'

                else:
                    perigo_str = 'não'

                count = len(classes)
                j = 0

                for i in classes:
                    j = j + 1
                    if i == classe_n:
                        for g in classes[classe_n]:
                            contador = len(classes[classe_n])
                            classe = classes[classe_n][1]['classe']
                            ferramenta_n = contador + 1
                            j = j - 1


                    elif j == count:
                        classe = input('Qual o nome da nova classe?')
                        ferramenta_n = 1


                classes.update({classe_n: {ferramenta_n : {'nome': nome, 'como usar': como_usar, 'funcao': funcoes, 'localizacao': local, 'classe': classe,
                                                    'perigo': perigo_str, 'quantidade': qtdd}}})

                classes = dicionario(classes)
                print('Ferramenta adicionada com sucesso!')

            elif opcao2 == 2 or opcao2 == 3:
                while opcao2 == 2 or opcao2 == 3:
                    if opcao2 == 2:
                        interface('EDITAR QUANTIDADE DA FERRAMENTA', 34)
                    elif opcao2 == 3:
                        interface('REMOVER FERRAMENTA', 41)
                    op = menu2(classes)

                    if op != 5 and op in classes:
                        if opcao2 == 2:
                            pergunta = '\nDigite o número da ferramenta que deseja EDITAR a quantidade ou -1 para sair: '
                            ferramenta_opcao = erro(pergunta, resposta)

                            if ferramenta_opcao == -1:
                                break

                            elif ferramenta_opcao in classes:
                                print('Você selecionou a ferramenta "'+classes[op][ferramenta_opcao]['nome']+ '", deseja continuar? (s/n) ')
                                sn = input()

                                if sn == 's' or sn == 'S':
                                    print('\nHá '+ str(classes[op][ferramenta_opcao]['quantidade'])+' dessa ferramenta')
                                    pergunta = 'Digite a nova quantidade: '
                                    qtdd_nova = erro(pergunta, resposta)
                                    classes[op][ferramenta_opcao]['quantidade'] = qtdd_nova
                                    classes = dicionario(classes)
                                    print('\nQuantidade alterada com sucesso! Agora há ' + str(classes[op][ferramenta_opcao]['quantidade']) + ' da ferramenta "' +classes[op][ferramenta_opcao]['nome']+'"')
                                    break
                                elif sn == 'n' or sn == 'N':
                                    continue

                                else:
                                    print('Digite apenas "s" ou "n"')
                            else:
                                print('Opção inválida, essa ferramenta não existe')


                        elif opcao2 == 3:
                            pergunta = '\nDigite o número da ferramenta que deseja REMOVER ou -1 para sair: '
                            ferramenta_opcao = erro(pergunta, resposta)

                            if ferramenta_opcao == -1:
                                break

                            elif ferramenta_opcao in classes:
                                print('Você selecionou a ferramenta "' + classes[op][ferramenta_opcao][
                                    'nome'] + '", deseja continuar? (s/n) ')
                                sn = input()

                                if sn == 's' or sn == 'S':
                                    del(classes[op][ferramenta_opcao])
                                    classes = dicionario(classes)
                                    print('Ferramenta removida com sucesso!')
                                    break

                                elif sn == 'n' or sn == 'N':
                                    continue

                                else:
                                    print('Digite apenas "s" ou "n"')
                            else:
                                print('Opção inválida, essa ferramenta não existe')

                    elif op == 5 and op in classes:
                        print('A área da impressora não pode ser alterada!')

                    else:
                        print('Essa classe não existe! Digite uma opção válida.')

            elif opcao2 == -1:
                continue

            else:
                print('Digite uma opção válida!')

    elif opcao1 == 2:
        interface('GERENCIAR ESTUDANTES', 42)
        print('1 - Gerenciar aluno')
        print('2 - Gerenciar monitor')
        print('-1 - Sair')
        pergunta = '\nDigite o que deseja acessar: '
        opcao2 = erro(pergunta, resposta)

        if opcao2 == 1:
            interface('GERENCIAR ALUNO', 42)
            print('1 - Cadastrar aluno')
            print('2 - Editar aluno')
            print('3 - Remover aluno')
            print('-1 - Sair')
            pergunta = '\nO que deseja fazer? '
            opcao3 = erro(pergunta, resposta)

            if opcao3 == 1:
                interface('CADASTRAR ALUNO', 42)
                nome = input('Digite o primeiro nome do aluno: ')
                sobrenome = input('Digite o último nome do aluno: ')
                iniciais = input('Digite as iniciais do email da Cesar School do aluno: ')
                nome_pref = input('Digite o nome de preferencia do aluno: ')
                matricula = input('Digite a matrícula do aluno: ')
                curso_l = input('Qual o curso? CC ou D')

                w = 0
                while w == 0:
                    curso_l = input('Qual o curso? CC ou D')
                    if curso_l == 'cc' or curso == 'CC' or curso == 'Cc' or curso == 'cC':
                        curso = 'CC'
                        break

                    elif curso_l == 'd' or curso == 'D':
                        curso = 'D'
                        break

                    else:
                        curso = input('Curso não existente, digite novamente')

                senha = input('Digite a senha definida pelo aluno: ')
                arquivo = open('Nome_senha.txt', 'a', encoding='utf8')
                texto = 'Nome: '+ nome+' '+sobrenome+'      Iniciais: '+iniciais+'      Nome_pref: '+nome_pref+'        Matrícula: '+matricula+'    Senha:'+senha+' '+curso+'\n'
                arquivo.write(texto)
                arquivo.close()

            elif opcao3 == 2:
                b = 0
                while b == 0:
                    interface('EDITAR ALUNO', 42)
                    print('1 - Nome e Sobrenome')
                    print('2 - Matrícula')
                    print('3 - Senha')
                    print('4 - Nome de preferência')
                    print('-1 - Sair')
                    pergunta = 'O que deseja editar? '
                    opcao4 = erro(pergunta, resposta)

                    if opcao4 == -1:
                        break

                    iniciais = input('Digite as iniciais do aluno que deseja editar: ')

                    leitura_arq = leitura('Nome_senha.txt')
                    arquivo = open('Nome_senha.txt', 'w', encoding='utf8')
                    tamanho = len(leitura_arq)
                    count = 0
                    x = 0

                    for l in leitura_arq:
                        l_split = l.split()
                        if iniciais == l_split[4]:
                            if opcao4 == 1:
                                nome = input('Digite o novo nome: ')
                                sobrenome = input('Digite o novo sobrenome: ')
                                nome_antigo = l_split[1] + ' ' + l_split[2]
                                nome_novo = nome+' '+sobrenome
                                arquivo.write(l.replace(nome_antigo, nome_novo))
                                print('Nome alterado com sucesso!')
                                x = x + 1

                            elif opcao4 == 2:
                                matricula = input('Digite a nova matrícula: ')
                                matricula_nova = 'Matrícula: '+ matricula
                                matricula_antiga = 'Matrícula: '+ l_split[8]
                                arquivo.write(l.replace(matricula_antiga, matricula_nova))
                                print('Matrícula alterada com sucesso!')
                                x = x + 1

                            elif opcao4 == 3:
                                senha_antiga = input('Peça para o aluno digitar sua senha antiga: ')
                                senha_txt = 'Senha: ' + senha_antiga
                                if senha_antiga == l_split[10]:
                                    senha_nova = input('Peça para o aluno digitar sua nova senha: ')
                                    senha_nova_texto = 'Senha: ' + senha_nova
                                    arquivo.write(l.replace(senha_txt, senha_nova_texto))
                                    print('Senha alterada com sucesso!')
                                    x = x + 1

                                else:
                                    print('Senha incorreta')
                                    arquivo.write(l)

                            elif opcao4 == 4:
                                nome_pref = input('Digite o novo nome de preferência: ')
                                nome_pref_texto = 'Nome_pref: ' + nome_pref
                                nome_pref_antigo = 'Nome_pref: ' + l_split[6]
                                arquivo.write(l.replace(nome_pref_antigo, nome_pref_texto))
                                print('Nome alterado com sucesso!')
                                x = x + 1

                        else:
                            arquivo.write(l)
                            count = count + 1
                            limite = tamanho - 1
                            if count == limite and x == 1:
                                arquivo.close()
                                break

                            elif count == tamanho:
                                print('Aluno não encontrado')
                                arquivo.close()

            elif opcao3 == 3:
                interface('REMOVER ALUNO', 42)
                iniciais = input('Digite as iniciais do aluno que deseja editar: ')
                leitura_arq = leitura('Nome_senha.txt')
                tamanho = len(leitura_arq)
                arquivo = open('Nome_senha.txt', 'w', encoding='utf8')
                count = 0
                for l in leitura_arq:
                    l_split = l.split()

                    if iniciais == l_split[4]:
                        print('Aluno removido com sucesso')

                    else:
                        arquivo.write(l)
                        count = count + 1
                        if count == tamanho:
                            print('Aluno não encontrado')
                break

            elif opcao3 == -1:
                break

            else:
                print('Digite uma opção válida')

        elif opcao2 == 2:
            b = 0
            while b == 0:
                interface('GERENCIAR MONITOR', 41)
                print('1 - Adicionar monitor')
                print('2 - Remover monitor')
                print('-1 - Sair')

                pergunta = '\nO que deseja fazer? '
                opcao3 = erro(pergunta, resposta)

                if opcao3 == 1:
                    interface('ADICIONAR MONITOR', 41)
                    mensagem = 'Monitor adicionado com sucesso!'
                    monitor('\n', ' #Monitor\n', mensagem, '')
                    enter = input('\nAperte enter para continuar')
                    break

                elif opcao3 == 2:
                    interface('REMOVER MONITOR', 42)
                    mensagem = 'Monitor removido com sucesso!'
                    monitor(' #Monitor\n', '\n', mensagem, '#Monitor')
                    enter = input('\nAperte enter para continuar')
                    break

                elif opcao3 == -1:
                    print('\nVoltando para o menu')
                    break

                else:
                    print('Opção inválida')

    elif opcao1 == 3:
        w = 0
        while w == 0:
            interface('HISTÓRICO', 44)
            print('1 - Ver histórico individual')
            print('2 - Ver histórico geral')
            print('-1 - Sair')
            pergunta = '\nDigite a opção que deseja: '
            opcao3 = erro(pergunta, resposta)

            if opcao3 == 1:
                interface('HISTÓRICO INDIVIDUAL', 40)
                iniciais = input('Digite as iniciais do aluno: ')
                alunos = leitura('Nome_senha.txt')
                tamanho = len(alunos)
                count = 0

                for l in alunos:
                    l_split = l.split()
                    if iniciais == l_split[4]:
                        nome = l_split[1]
                        matricula = l_split[8]
                        nome_arquivo_al = 'Histórico_aluno_' + nome + '_' + matricula + '.txt'
                        print('')
                        leitura_al = ler(nome_arquivo_al)

                        enter = input('\nAperte enter para continuar')
                        break

                    else:
                        count = count + 1
                        if count == tamanho:
                            print('Aluno não encontrado')

            elif opcao3 == 2:
                interface('HISTÓRICO GERAL', 42)
                print(' ')
                ler('Histórico_geral.txt')
                enter = input('\nAperte enter para continuar')
                break

            elif opcao3 == -1:
                print('Voltando para o menu')
                break

            else:
                print('Digite uma opção válida!')

    elif opcao1 == 4:
        interface('REPORTS', 46)
        ler('Erros.txt')
        enter = input('\nAperte enter para continuar')

    elif opcao1 == 5:
        interface('CÓDIGOS DE LIBERAÇÃO', 40)
        ler('Codigos.txt')
        enter = input('\nAperte enter para continuar')

    elif opcao1 == 6:
        interface('PERFIL', 47)
        print('Nome: '+nome)
        print("\nNome de preferência: ", string_linha[6])
        print("\nMatrícula: ", string_linha[8])
        print('\nCargo: Funcionário')
        enter = input('\nAperte enter para continuar')