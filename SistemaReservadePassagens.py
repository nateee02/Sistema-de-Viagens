print('\n')
print("===== BEM VINDO A VIAÇÃO UNIÃO SANTA CRUZ =====",'\n')
OpcaoUsuario = 0
while OpcaoUsuario != 3:
    print('''
    |--------------------------|
    |[1] RESERVAR UMA PASSAGEM |
    |[2] LIBERAR UMA RESERVA   |
    |[3] SAIR DO PROGRAMA      |
    |--------------------------|
    ''')
    OpcaoUsuario = (input("Por favor, digite uma das opções acima: "))

    if OpcaoUsuario == "1":
        print('''
        |-----------------------------------------------------|
        |               ROTA               | HORÁRIO | VALOR  |
        |-----------------------------------------------------|
        |[1] Porto Alegre -> Florianópolis |   6H    | R$19,45|
        |[2] Porto Alegre -> Florianópolis |   16H   | R$23,50|
        |[3] Porto Alegre -> Criciúma      |   6H    | R$12,90|
        |[4] Porto Alegre -> Criciúma      |   16H   | R$15,90|
        |[5] Criciúma -> Florianópolis     |   10H   | R$7,30 |
        |[6] Criciúma -> Florianópolis     |   20H   | R$10,30|
        |-----------------------------------------------------|
        ''')
        def GerencimanetoAssentos(Arqv = ''):   
            Arquivo = open(Arqv)
            Linhas = Arquivo.readlines()
            for linha in Linhas:
                print(linha,'\n')
            print('Numero total de assentos: 46')

            SelecionaAssento = int(input("Selecione o assento: "))
            if SelecionaAssento > len(Linhas):
                print('Este assento não existe')
                exit()

            AssentoSelecionado = Linhas[int(SelecionaAssento) -1]
            TextoDividido = AssentoSelecionado.split('-')

            if TextoDividido[1].strip() != 'Livre':
                print('Assento ocupado')
                exit()
            TextoDividido[1] = 'Ocupado'
            # reescrevendo a linha com o novo status 'Ocupado'
            Linhas[int(SelecionaAssento) -1] = f'{TextoDividido[0].strip()} - {TextoDividido[1]}\n'

            NovoArquivo = open(Arqv,'w')
            NovoArquivo.truncate(0)
            NovoArquivo.writelines(Linhas)

            NovoArquivo.close()
            Arquivo.close()
            print('Assento selecionado!')
            print(f'Número de assento: {TextoDividido[0]} Situação: {TextoDividido[1]}\n')
            print('A Viação União Santa Cruz deseja uma boa viagem!')

        OpcaoRota = int(input('Qual será seu destino? '))
        if OpcaoRota == 1:
            GerencimanetoAssentos('GerenciamentoAssentos1.txt')
        elif OpcaoRota == 2:
            GerencimanetoAssentos('GerenciamentoAssentos2.txt')
        elif OpcaoRota == 3:
            GerencimanetoAssentos('GerenciamentoAssentos3.txt')
        elif OpcaoRota == 4:
            GerencimanetoAssentos('GerenciamentoAssentos4.txt')
        elif OpcaoRota == 5:
            GerencimanetoAssentos('GerenciamentoAssentos5.txt')
        elif OpcaoRota == 6:
            GerencimanetoAssentos('GerenciamentoAssentos6.txt')


    if OpcaoUsuario == "2":
        print('''
        |-----------------------------------------------------|
        |               ROTA               | HORÁRIO | VALOR  |
        |-----------------------------------------------------|
        |[1] Porto Alegre -> Florianópolis |   6H    | R$19,45|
        |[2] Porto Alegre -> Florianópolis |   16H   | R$23,50|
        |[3] Porto Alegre -> Criciúma      |   6H    | R$12,90|
        |[4] Porto Alegre -> Criciúma      |   16H   | R$15,90|
        |[5] Criciúma -> Florianópolis     |   10H   | R$7,30 |
        |[6] Criciúma -> Florianópolis     |   20H   | R$10,30|
        |-----------------------------------------------------|
        ''')
        def LiberarAssento(Arqv = ''):
            Arquivo = open(Arqv)
            Linhas = Arquivo.readlines()
            for linha in Linhas:
                print(linha,'\n')
            print('Numero total de assentos: 46')
    
            AssentoaserLiberado = int(input("Por favor, diga o número do assento que deseja liberar: "))
            if AssentoaserLiberado > len(Linhas):
                print("Este assento não existe")
                exit()

            AssentoSelecionado = Linhas[int(AssentoaserLiberado) - 1]
            TextoDividido = AssentoSelecionado.split('-')

            if TextoDividido[1].strip() != 'Ocupado':
                print('Este assento já está livre')
                exit()
            TextoDividido[1] = 'Livre'

            # reescrevendo a linha com o novo status 'Livre'
            Linhas[int(AssentoaserLiberado) - 1] = f'{TextoDividido[0].strip()} - {TextoDividido[1]}\n'

            NovoArquivo = open(Arqv,'w')
            NovoArquivo.truncate(0)
            NovoArquivo.writelines(Linhas)

            NovoArquivo.close()
            Arquivo.close()
            print(f'Número de assento: {TextoDividido[0]} Situação: {TextoDividido[1]}\n')

        OpcaoLiberarAssento = int(input('De qual rota o assento será liberado? '))
        if OpcaoLiberarAssento == 1:
            LiberarAssento('GerenciamentoAssentos1.txt')
        elif OpcaoLiberarAssento == 2:
            LiberarAssento('GerenciamentoAssentos2.txt')
        elif OpcaoLiberarAssento == 3:
            LiberarAssento('GerenciamentoAssentos3.txt')
        elif OpcaoLiberarAssento == 4:
            LiberarAssento('GerenciamentoAssentos4.txt')
        elif OpcaoLiberarAssento == 5:
            LiberarAssento('GerenciamentoAssentos5.txt')
        elif OpcaoLiberarAssento == 6:
            LiberarAssento('GerenciamentoAssentos6.txt')

    elif OpcaoUsuario == "3":
        print("A Viação União Santa Cruz agradece!!")
        break