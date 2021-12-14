from datetime import *
from random import randint
import pickle
import getpass

data_atual = date.today()
data_br = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)
senhas = open('Nome_senha.txt', 'r', encoding='utf8')
dias = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')

dic = open("ferramentas_dic.txt", 'rb')
classes = pickle.load(dic)
dic.close()

def menu(classes):
    for i in classes:
            print('{} - {}' .format(i, classes[i][1]['classe']))

def pontos (tam = 100):
    return '-' * tam

def interface(x, tam):
    print(pontos())
    alinhamento = ' ' * tam
    print(alinhamento, x)
    print(pontos())

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

def ler(nome):
    abrir_arq(nome)
    arquivo = open(nome, 'r', encoding='utf8')
    print(arquivo.read())
    arquivo.close()

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

def retirar (x, z):
    arquivo = open(x, 'a', encoding='utf8')
    arquivo.write(z)
    arquivo.close()

def abrir_arq(nome):
    arquivo = open(nome, 'a', encoding='utf8')
    arquivo.close()

def retirar2():

    add_al = data_e_hora.strftime('%d/%m/%Y %H:%M') + ': ' + \
             classes[op][ferramenta_opcao]['nome'] + '\n\n'

    add_carro = classes[op][ferramenta_opcao]['nome'] + '\n'

    add_f = data_e_hora.strftime('%d/%m/%Y %H:%M') + ': ' + string_linha[1] + ', ' + matricula + '\n\n'

    add_g = data_e_hora.strftime('%d/%m/%Y %H:%M') + ': ' + string_linha[1] + ', ' + matricula + ': ' + \
            classes[op][ferramenta_opcao]['nome'] + '\n\n'

    for v in range(qtdd_retirada):
        retirar(nome_arquivo_al, add_al)
        retirar(nome_carrinho, add_carro)
        retirar(nome_arquivo_f, add_f)
        retirar('Histórico_geral.txt', add_g)

    print('\nComo usar:', classes[op][ferramenta_opcao]['como usar'])
    print('\nLocalização: \n', classes[op][ferramenta_opcao]['localizacao'])

def agendamento(dia, hora, D, t, t2):
    arquivo = open('Agendamentos_Impressora3D.txt', 'r', encoding='utf8')
    leitura2 = arquivo.readlines()
    str_l = str(leitura2)
    arquivo.close()
    if dia in str_l:
        for r in leitura2:
            split = r.split()
            if r != '\n':
                if dia == split[0]:
                    print(D+ ' - '+ dia)
                    for i in range(2):
                        if hora[i] != split[1]:
                            if t == '  ':
                                print(t + hora[i]+'\n')
                            else:
                                print(str(i) + ' - '+ hora[i]+'\n')

    else:
        print(D+' - '+dia)
        print(t + hora[0])
        print(t2 + hora[1]+'\n')

def devolver(arquivo_nome, x, y, e, qtdd_devolvida):
    arquivo = open(arquivo_nome, 'r', encoding='utf8')
    linhas = arquivo.readlines()
    arquivo.close()
    arquivo = open(arquivo_nome, 'w', encoding='utf8')

    for l in linhas:
        if x in l:
            if y in l:
                if '#Devolvido ' not in l:
                    if e < qtdd_devolvida:
                        data_e_hora = datetime.now()
                        f_devolvida = '      #Devolvido (' + data_e_hora.strftime('%d/%m/%Y %H:%M') + ')' + '\n'
                        arquivo.write(l.replace('\n', f_devolvida))
                        e = e + 1
                    else:
                        arquivo.write(l)
                else:
                    arquivo.write(l)
            else:
                arquivo.write(l)

    arquivo.close()

def report(arquivo_erro, report, erro):
    texto = report + data_e_hora.strftime('%d/%m/%Y %H:%M') + ' - ' + string_linha[0] + ', ' + matricula + ':  ' + erro + '\n\n'
    arquivo_erro.write(texto)
    arquivo_erro.close()
    print("Muito obrigado pela sua atenção e relato, vamos analisá-lo xD")
    enter = input('\nAperte enter para continuar\n')

def curso(x):
    if 'CC' == string_linha[x]:
        curso = 'Ciências da Computação'
    if 'D' == string_linha[x]:
        curso = 'Design'
    return curso

def leitura(x):
    arquivo = open(x, 'r', encoding='utf8')
    leitura = arquivo.readlines()
    arquivo.close()
    return leitura

matriz = 0
while matriz == 0:
    acesso = 1
    while acesso != 0:
        interface('LOG IN', 47)
        senhas.seek(0)
        iniciais = input('Digite suas iniciais do email da Cesar School: ')
        if acesso == 1:
            for linha in senhas:
                string_linha = linha.split()
                if iniciais == string_linha[4]:
                    senha = getpass.getpass("Digite sua senha: ")
                    if senha == string_linha[10]:
                        print('Oi', string_linha[6])
                        matricula = string_linha[8]
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

        nome_arquivo_al = 'Histórico_aluno_' + string_linha[1] + '_' + matricula + '.txt'
        nome_carrinho = 'Carrinho_' + string_linha[1] + '_' + matricula + '.txt'

        print('')
        interface('OPÇÕES', 47)
        print('1 - Ferramentas')
        print('2 - Ver histórico')
        print('3 - Reportar reclamação, aviso ou comentário')
        print('4 - Ver carrinho')
        print('5 - Ver perfil')
        print('6 - Pesquisar ferramenta por função')
        print('-1 - Sair')

        pergunta = '\nDigite qual área deseja acessar: '
        resposta = 'Digite uma opção válida! São aceitos números de 1 a 10.'
        opcao1 = erro(pergunta, resposta)

        if opcao1 == 1:
            interface('CLASSES', 46)
            menu(classes)
            pergunta = '\nDigite qual classe deseja acessar: '
            resposta = 'Devem ser números inteiros! Digite uma opção válida.'
            op = erro(pergunta, resposta)

            if op != 5:
                if op in classes:
                    interface('FERRAMENTAS', 45)
                    for i in classes:
                        if classes[op] == classes[i]:
                            for g in classes[op]:
                                opcoes = print('{}- {}' .format (g, classes[op][g]['nome']))

                            pergunta = '\nDigite o número da ferramenta que deseja: '
                            resposta = 'Deve ser um número inteiro'
                            ferramenta_opcao = erro(pergunta, resposta)

                            if ferramenta_opcao in classes[op]:
                                B = 0
                                while B == 0:
                                    nome_arquivo_f = 'Histórico_ferramenta_' + classes[op][ferramenta_opcao][
                                        'nome'] + '.txt'

                                    print('\nVocê selecionou a ferramenta', classes[op][ferramenta_opcao]['nome'])
                                    print('O que deseja fazer?')
                                    print('1 - Retirar ferramenta')
                                    print('2 - Devolver ferramenta')
                                    print('3 - Saber como usar a ferramenta')
                                    print('4 - Saber onde a ferramenta está')
                                    print('5 - Saber quais as funcões da ferramenta')
                                    print('-1 - Sair para o menu principal\n')

                                    pergunta = 'Digite o número da opção: '
                                    resposta = 'Deve ser um número inteiro!'
                                    menu_opcao = erro(pergunta, resposta)

                                    if menu_opcao == 1:
                                        print('Você selecionou retirar a ferramenta', classes[op][ferramenta_opcao]['nome'], ', deseja continuar? (s/n)')
                                        sn = input()
                                        if sn == 'n' or sn == 'N':
                                            continue
                                        elif sn == 's' or sn == 'S':
                                            #txt por pessoa       ## Gravar Quantidades!!
                                            print('Há '+ str(classes[op][ferramenta_opcao]['quantidade'])+ ' para a retirada')
                                            pergunta ='Quantas ferramentas "'+ classes[op][ferramenta_opcao]['nome']+ '" deseja retirar? '
                                            resposta = 'Deve ser um número inteiro!'
                                            qtdd_retirada = erro(pergunta, resposta)

                                            qtdd_disponivel = classes[op][ferramenta_opcao]['quantidade']
                                            qtdd_sobra = qtdd_disponivel - qtdd_retirada
                                            data_e_hora = datetime.now()
                                            v = 0

                                            if qtdd_sobra >= 0:
                                                if classes[op][ferramenta_opcao]['perigo'] == 'sim':
                                                    codigos = open('Codigos.txt', 'a', encoding='utf8')
                                                    cod = randint(10000, 99999)
                                                    data_e_hora = datetime.now()
                                                    escrever = data_e_hora.strftime('%d/%m/%Y %H:%M') + ': '+ string_linha[1] + ', ' + classes[op][ferramenta_opcao]['nome'] + '         cod = ' + str(cod) + ' \n\n'
                                                    escrever2 = data_e_hora.strftime('%d/%m/%Y %H:%M') + ': '+ string_linha[1] + ', ' + classes[op][ferramenta_opcao]['nome'] + '         cod = ' + str(cod)
                                                    codigos.write(escrever)
                                                    codigos.close()
                                                    cont = 0
                                                    tentativa = 0

                                                    while cont <= 1:
                                                        codigo_responsavel = input('\nPeça o código de liberação para algum responsável: ')
                                                        leitura_cod = leitura('Codigos.txt')
                                                        codigos.close()
                                                        cont = 0
                                                        tentativa = cont +1
                                                        tamanho =  len(leitura_cod)

                                                        for z in leitura_cod:
                                                            if escrever2 in z:
                                                                if codigo_responsavel in z:
                                                                    retirar2()
                                                                    cont = 2
                                                                    classes[op][ferramenta_opcao]['quantidade'] = qtdd_disponivel - qtdd_retirada
                                                                    classes = dicionario(classes)
                                                                    leitura_cod2 = leitura('Codigos.txt')
                                                                    codigos = open('Codigos', 'w', encoding='utf8')
                                                                    for y in leitura_cod2:
                                                                        if y != z:
                                                                            codigos.write(y)
                                                                    codigos.close()

                                                                    print('A ferramenta foi retirada com sucesso')
                                                                    break

                                                            else:
                                                                cont = cont+ 1

                                                                if cont == tamanho:
                                                                    print('Código errado, liberação negada!')
                                                                    print('Você tem mais uma tentativa')

                                                                    if tentativa == 2:
                                                                        print('Acabaram suas tentativas :/')
                                                                        break
                                                else:
                                                    retirar2()
                                                    classes[op][ferramenta_opcao]['quantidade'] = qtdd_disponivel - qtdd_retirada
                                                    classes = dicionario(classes)

                                                    print('A ferramenta foi retirada com sucesso')
                                                    break

                                            else:
                                                print('Não foi possível concluir a retirada')
                                                print('Há', qtdd_disponivel, 'ferramentas disponíveis')
                                        else:
                                            print('Você deve digitar apenas "s" ou "n"!')

                                    elif menu_opcao == 2:
                                        pergunta = ('Quantas ferramentas "' + classes[op][ferramenta_opcao]['nome'] + '" deseja devolver? ')
                                        resposta = 'Deve ser um número inteiro!'
                                        qtdd_devolvida = erro(pergunta, resposta)
                                        qtdd_disponivel = classes[op][ferramenta_opcao]['quantidade']

                                        carrinho = open(nome_carrinho, 'r', encoding='utf8')
                                        linhas_carrinho = carrinho.readlines()

                                        linhas_carrinho_str = str(linhas_carrinho)
                                        carrinho.close()
                                        i = 0
                                        e = 0
                                        f = 0
                                        g = 0

                                        quantidade_l = linhas_carrinho_str.count(classes[op][ferramenta_opcao]['nome'])
                                        if classes[op][ferramenta_opcao]['nome'] in linhas_carrinho_str:
                                            if qtdd_devolvida <= quantidade_l:
                                                for c in linhas_carrinho:
                                                    if classes[op][ferramenta_opcao]['nome'] in c:
                                                     #txt do carrinho
                                                        carrinho = open(nome_carrinho, 'r', encoding='utf8')
                                                        linhas = carrinho.readlines()
                                                        carrinho.close()
                                                        carrinho = open(nome_carrinho, 'w', encoding='utf8')
                                                        for l in linhas:
                                                           if classes[op][ferramenta_opcao]['nome'] not in l:
                                                               carrinho.write(l)
                                                           else:
                                                               if i >= qtdd_devolvida:
                                                                   carrinho.write(l)
                                                               i = i + 1

                                                        carrinho.close()
                                                        carrinho = open(nome_carrinho, 'r', encoding='utf8')
                                                        print('Você ainda falta devolver:\n', carrinho.read())
                                                        carrinho.close()

                                                nome_aluno = string_linha[1]+', '+matricula

                                                devolver(nome_arquivo_al, classes[op][ferramenta_opcao]['nome'], classes[op][ferramenta_opcao]['nome'], e, qtdd_devolvida)

                                                devolver('Histórico_geral.txt', nome_aluno, classes[op][ferramenta_opcao]['nome'], f, qtdd_devolvida)

                                                devolver(nome_arquivo_f, nome_aluno, nome_aluno, g, qtdd_devolvida)

                                                classes[op][ferramenta_opcao]['quantidade'] = qtdd_disponivel + qtdd_devolvida
                                                classes = dicionario(classes)

                                                enter = input('\nFerramenta devolvida com sucesso, aperte enter para continuar')
                                                break

                                            else:
                                                enter = input('Voce não possui essa quantidade de ferramentas')
                                        else:
                                            enter = input('Voce não possui essa ferramenta para devolvê-la')

                                    elif menu_opcao == 3:
                                        interface('COMO USAR', 46)
                                        print(classes[op][ferramenta_opcao]['nome'] + ': '+ classes[op][ferramenta_opcao]['como usar'])

                                    elif menu_opcao == 4:
                                        interface('LOCALIZAÇÃO', 45)
                                        print(classes[op][ferramenta_opcao]['nome'] + ': '+ '\n'+ classes[op][ferramenta_opcao]['localizacao'])

                                    elif menu_opcao == 5:
                                        interface('FUNÇÕES', 47)
                                        print('Essa ferramenta serve para: ', classes[op][ferramenta_opcao]['funcao'])

                                    elif menu_opcao == -1:
                                        B = 1
                                        break

                                    else:

                                        print('Digite uma opção válida')
                            else:
                                print('Digite uma opção válida! Essa ferramenta não existe')

            elif op == 5:
                b = 0
                while b == 0:
                    if b == 0:
                        interface('AGENDAMENTO: IMPRESSORA 3D', 37)
                        print('1 - Agendar')
                        print('-1 - Voltar ao menu')
                        pergunta = 'Digite uma opção: '
                        resposta = 'Deve ser um número inteiro'
                        agend = erro(pergunta, resposta)
                        if agend == 1:
                            arquivo = open('Agendamentos_Impressora3D.txt', 'a', encoding='utf8')
                            arquivo.close()
                            data_hoje = date.today()
                            dia_hoje = dias[data_hoje.weekday()]

                            print('\nPara qual dia deseja reservar?\n')
                            lista_horas = ['12:00', '15:30']
                            arquivo = open('Agendamentos_Impressora3D.txt', 'r', encoding='utf8')
                            leitura = arquivo.readlines()
                            leitura_str = str(leitura)
                            arquivo.close()
                            dias_opcao = []
                            d = 0

                            for x in range(7):
                                data_sugerida = date.fromordinal(data_atual.toordinal() + d)
                                dia_sugerido = data_sugerida.weekday()
                                nome_dia = dias[dia_sugerido]
                                data_formatada = data_sugerida.strftime('%d/%m/%Y')
                                a = 0
                                if nome_dia == 'Sábado' or nome_dia == 'Domingo':
                                    d = d + 1
    
                                else:
                                    if data_formatada in leitura_str:
                                        for l in leitura:
                                            split = l.split()
                                            if l != '\n':
                                                if data_formatada == split[0]:
                                                    a = a + 1
                                                    dias_opcao.append(data_formatada)
                                                    if a == 2:
                                                        del(dias_opcao[-1])
                                                        del(dias_opcao[-1])

                                    else:
                                        dias_opcao.append(data_formatada)

                                arquivo = open('Agendamentos_Impressora3D.txt', 'r', encoding='utf8')
                                leitura = arquivo.readlines()
                                leitura_str = str(leitura)
                                arquivo.close()

                                d = d + 1
                                tamanho = len(dias_opcao)
                                if tamanho == 4:
                                    break

                            del(dias_opcao[-1])
                            g = 0
                            while g == 0:
                                D = 1
                                for D in range(1, 4):
                                    d = D - 1
                                    dia = dias_opcao[d]
                                    D_str = str(d)
                                    agendamento(dia, lista_horas, D_str, '  ', '  ')

                                pergunta = 'Digite a opção que deseja: '
                                resposta = 'Deve ser um número inteiro de 1 a 3'
                                numero_escolhido = erro(pergunta, resposta)

                                if numero_escolhido <= 2:
                                    print('')
                                    dia_escolhido = dias_opcao[numero_escolhido]
                                    agendamento(dia_escolhido, lista_horas, 'Dia', '0 - ', '1 - ')
                                    g = g + 1
                                    break

                                else:
                                    print('Deve se um número de 0 a 2 (0, 1 ou 2)')
                            g = 0
                            while g == 0:
                                pergunta = 'Digite o número da hora que deseja: '
                                resposta = 'Deve ser um número inteiro'
                                n_hora = erro(pergunta, resposta)

                                hora_escolhida = lista_horas[n_hora]

                                print('Você selecionou a data {}, hora: {}, confirma? (s/n)'.format(dia_escolhido, hora_escolhida))
                                sn = input()
                                if sn == 's':
                                    arquivo = open('Agendamentos_Impressora3D.txt', 'a', encoding='utf8')
                                    texto = dia_escolhido + ' ' + hora_escolhida + ' - ' + string_linha[1] + ' '+ string_linha[2] + '  ' + string_linha[8]+ '\n\n'
                                    arquivo.write(texto)
                                    arquivo.close()
                                    enter = input('\nAgendamento realizado com sucesso!\nAperte enter para continuar\n')
                                    g = 1
                                    b = 1
                                    break
                                elif sn == 'n':
                                    g = 1
                                    break
                                else:
                                    print('Digigite uma resposta válida (s ou n)!')

                        elif agend == -1:
                            b = 1
                            break

                        else:
                            print('Digite uma opção válida! (1 ou 2)')
            else:
                print('Essa classe existe')

        elif opcao1 == 2:
            interface('HISTÓRICO PESSOAL', 42)
            print('Suas últimas ferramentas foram: ')
            abrir_arq(nome_arquivo_al)
            arquivo_al = open(nome_arquivo_al, 'r', encoding='utf8')
            print(arquivo_al.read())
            arquivo_al.close()
            enter = input('\nAperte enter para continuar\n')

        elif opcao1 == 3:
            b = 0
            while b == 0:
                interface('RECLAMAÇÕES E AVISOS', 40)
                print('O que você gostaria de relatar?')
                print('1 - Material danificado')
                print('2 - Material faltando')
                print('3 - Outro')
                print('-1 - Voltar para o menu')
                pergunta = '\n Digite a opção: '
                resposta = 'Deve ser um número inteiro'

                opcao_erro = erro(pergunta, resposta)

                arquivo_erro = open('Erros.txt', 'a', encoding='utf8')
                data_e_hora = datetime.now()

                if opcao_erro == 1:
                    texto = input('O que se encontra danificado? ')
                    reporte = 'Material Danificado - '
                    report(arquivo_erro, reporte, texto)
                    break

                elif opcao_erro == 2:
                    texto = input('O que se encontra em falta? ')
                    reporte = 'Material Faltando - '
                    report(arquivo_erro, reporte, texto)
                    break

                elif opcao_erro == 3:
                    texto = input('Escreva o que deseja reportar: ')
                    reporte = 'Outro - '
                    report(arquivo_erro, reporte, texto)
                    break

                elif opcao_erro == -1:
                    break

                else:
                    print('Digite uma opção válida')

        elif opcao1 == 4:
            interface('CARRINHO', 46)
            abrir_arq(nome_carrinho)
            carrinho = open(nome_carrinho, 'r', encoding='utf8')
            print(carrinho.read())
            carrinho.close()
            enter = input('\nAperte enter para continuar\n')

        elif opcao1 == 5:
            interface('PERFIL', 47)
            print("Nome: ", string_linha[1], string_linha[2])
            print("\nNome de preferência: ", string_linha[6])
            print("\nMatrícula: ", string_linha[8])

            cursando = ''
            if '#Monitor' == string_linha[-1]:
                cursando = curso(-2)
            else:
                cursando = curso(-1)

            print('\nCurso:', cursando)
            enter = input('\n\nAperte enter para continuar\n')

        elif opcao1 == 6:
            funcao = input('Digite a função que procura (ex: cortar): ')
            print('\nAs ferramentas que apresentam essa função são:')
            for i in classes:
                for g in classes[i]:
                    if funcao in classes[i][g]['funcao']:
                        print(classes[i][g]['nome'])

            enter = input('\nAperte enter para continuar')

        elif opcao1 == -1:
            acesso = 1
            print('Você saiu da sua conta')
            break

        else:
            print('Digite uma opção válida')


