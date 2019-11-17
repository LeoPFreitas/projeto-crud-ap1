import os

# =====================================================================
# MENUS


def mostrarMenu():
    print('=' * 60)
    print("CRUD Academia: \n")
    print("1 - Submenu de Alunos.")
    print("2 - Submenu de Modalidades.")
    print("3 - Submenu de Práticas.")
    print("4 - Submenu de Relatórios.")
    print("5 - Sair.")


def submenuOps():
    print("1. Listar todos")
    print("2. Listar um")
    print("3. Incluir")
    print("4. Alterar")
    print("5. Excluir")


def submenuAlunos():
    print("\nSubmenu Alunos: \n")
    submenuOps()


def submenuModalidades():
    print("\nSubmenu Modalidades: \n")
    submenuOps()


def submenuPraticas():
    print("\nSubmenu Práticas: \n")
    subOpsPratica()


def submenurRelatorios():
    print("\nSubmenu Relatórios: \n")
    print("1. Mostrar todos os dados de todas as modalidades que são oferecidas mais do que 2 vezes na semana\n")
    print("2. Mostrar todos os dias-horários-professores de uma dada modalidade fornecida pelo usuário\n")
    print("3. Mostrar todos os dados de todos os alunos que praticam mais do que X modalidades diferentes na academia, onde X deve ser fornecido pelo usuário. Mostrar também quais modalidades o aluno pratica.\n")


def subOpsPratica():
    print("1. Listar todos alunos\n")
    print("2. Listar aluno\n")
    print("3. Incluir aluno em modalidade\n")
    print("4. Alterar dia-hora de prática\n")
    print("5. Excluir aluno de 1 prática\n")
    print("6. Excluir aluno de todas práticas\n")

# =====================================================================
# ARQUIVO


def salvaAlunos(dic):
    ref = open('alunos.txt', 'w')
    if len(dic):
        for chave in dic:
            cpf = str(chave)

            valor = list(dic[chave])
            nome = valor[0]
            data = valor[1]
            sexo = valor[2]
            peso = valor[3]
            altura = valor[4]
            email = valor[5]  # lista
            tel = valor[6]  # lista

            nome = nome.split()
            nome = '-'.join(nome)

            email = '-'.join(email)
            tel = '-'.join(tel)

            linha = str(cpf) + '\t' + str(nome) + '\t' + str(data) + '\t' + str(sexo) + \
                '\t' + str(peso) + '\t' + str(altura) + \
                '\t' + str(email) + '\t' + str(tel) + '\n'
            ref.write(linha)
    ref.close()


def lerAlunos(dic):
    ref = open('alunos.txt', 'r')

    for linha in ref:
        linha = linha.split()

        cpf = linha[0]
        nome = linha[1]
        nasc = linha[2]
        sexo = linha[3]
        peso = linha[4]
        altura = linha[5]
        email = linha[6]
        tel = linha[7]

        email = email.split('-')
        tel = tel.split('-')

        chave = cpf
        valor = (nome, nasc, sexo, peso, altura, email, tel)
        x = {chave: valor}

        dic.update(x)

    ref.close()


def salvaModalidades(dic):
    ref1 = open('modalidades.txt', 'w')
    if len(dic):
        for chave in dic:
            cod = str(chave)
            valor = list(dic[chave])

            # receber descrição
            desc = valor[0]
            desc = desc.split()
            desc = '-'.join(desc)

            # receber duração
            dura = valor[1]

            # receber dias
            dias = valor[2]
            dias = '-'.join(dias)

            # receber horas
            horas = valor[3]
            horas = '-'.join(horas)

            # receber profs
            profs = valor[4]
            for i in range(len(profs)):
                profs[i] = profs[i].split()
                profs[i] = '+'.join(profs[i])
            profs = '-'.join(profs)

            # valores
            val = valor[5]

            # linha
            linha = str(cod) + '\t' + str(desc) + '\t' + str(dura) + '\t' + \
                str(dias) + '\t' + str(horas) + \
                '\t' + str(profs) + '\t' + str(val) + '\n'

            ref1.write(linha)
        ref1.close()


def lerModalidades(dic):
    ref1 = open('modalidades.txt', 'r')

    for linha in ref1:
        linha = linha.split()

        cod = linha[0]
        desc = linha[1]
        dura = linha[2]
        dias = linha[3]
        horas = linha[4]
        profs = linha[5]
        val = linha[6]

        desc = desc.split('-')
        desc = ' '.join(desc)

        dias = dias.split('-')
        horas = horas.split('-')

        # profs
        profs = profs.split('-')
        for i in range(len(profs)):
            profs[i] = profs[i].split('+')
            profs[i] = ' '.join(profs[i])

        # update dic
        chave = str(cod)
        valor = [desc, dura, dias, horas, profs, val]
        x = {chave: valor}
        dic.update(x)

    ref1.close()


def salvaPratica(lista):
    ref = open('praticas.txt', 'w')
    if len(lista):
        for cpf in lista:

            # Escreve o cpf do aluno
            cpfAluno = cpf[0]
            ref.write(cpfAluno + '\t')

            # quantidade de modalidades que o cpf pratica
            i = len(cpf) - 1

            # Escrever cada modalidade
            while i > 0:
                string = '-'.join(cpf[i])
                ref.write(string + '\t')
                i -= 1

            # mudou de cpf
            ref.write('\n')

    ref.close()


def lerPraticas(lista):
    ref = open('praticas.txt', 'r')

    for linha in ref:

        aluno = []

        # Receber cpf
        listAluno = linha.split()
        cpf = listAluno[0]
        aluno.append(cpf)

        # Separar modalidades em lista
        mods = listAluno[1:]
        for mod in mods:
            mod = mod.split('-')
            aluno.append(mod)

        # carregar na lista principal
        lista.append(aluno)

    ref.close()


# =====================================================================
# FUNÇÕES ALUNOS


def isAluno(dic, cpf):
    for chave in dic:
        if cpf == chave:
            return True
    return False


def cadAluno(dic):
    cpf = input("Digite o cpf: [xxxxxxxxxxx] ")

    if isAluno(dic, cpf):
        print("Aluno ja cadastrado.")
    else:
        # receber dados
        nome = input("Digite o nome: ")
        nasc = input("Digite o nascimento: [xx/xx/xxxx] ")
        sexo = input("Digite o sexo: [M/F] ")
        peso = input("Digite o peso: ")
        altura = input("Digite a altura: ")

        # lista de email
        emails = []
        email = input("Digite o primeiro e-mail: ")
        while email != '':
            emails.append(email)
            email = input("Digite o próximo e-mail: ")

        # lista de tel
        tels = []
        tel = input("Digite o telefone (sem espaço): ")
        while tel != '':
            tels.append(tel)
            tel = input("Digite o próximo telefone (sem espaço): ")

        # criar dic
        chave = cpf
        valor = (nome, nasc, sexo, peso, altura, emails, tels)

        # gerar dic
        x = {chave: valor}
        dic.update(x)
        print("Aluno cadastrado com sucesso!! \n\n")


def listarAlunoFormatado(dic):
    for aluno in dic:
        cpf = aluno

        string = dic[aluno]
        nome = string[0]
        data = string[1]
        sexo = string[2]
        peso = string[3]
        altura = string[4]

        emails = string[5]
        emails = ', '.join(emails)

        tels = string[6]
        tels = ', '.join(tels)

        print('CPF:', cpf, 'NOME:', nome, 'DATA DE NASCIMENTO:', data, 'SEXO:', sexo,
              'PESO:', peso, 'ALTURA:', altura, 'EMAILS: ', emails, 'TELEFONES:', tels)


def listarUmAluno(dic):
    cpf = input("Digite o cpf do aluno: ")
    if isAluno(dic, cpf):
        print("Segue dados do aluno: ")

        string = dic[cpf]
        nome = string[0]
        data = string[1]
        sexo = string[2]
        peso = string[3]
        altura = string[4]

        emails = string[5]
        emails = ', '.join(emails)

        tels = string[6]
        tels = ', '.join(tels)

        print('CPF:', cpf, 'NOME:', nome, 'DATA DE NASCIMENTO:', data, 'SEXO:', sexo,
              'PESO:', peso, 'ALTURA:', altura, 'EMAILS: ', emails, 'TELEFONES:', tels)
    else:
        print("Aluno não existente.")
        print('=' * 60)


def alterarAluno(dic):
    cpf = input("Digite o cpf do aluno: ")

    if isAluno(dic, cpf):
        print("Vamos alterar o aluno.")

        # receber dados
        nome = input("Digite o nome: ")
        nasc = input("Digite o nascimento: ")
        sexo = input("Digite o sexo: ")
        peso = input("Digite o peso: ")
        altura = input("Digite a altura: ")

        emails = []
        email = input("Digite o primeiro e-mail: ")
        while email != '':
            emails.append(email)
            email = input("Digite o próximo e-mail: ")

        # lista de tel
        tels = []
        tel = input("Digite o telefone (sem espaço): ")
        while tel != '':
            tels.append(tel)
            tel = input("Digite o próximo telefone (sem espaço): ")

        # criar dic
        chave = cpf
        valor = (nome, nasc, sexo, peso, altura, emails, tels)

        # gerar dic
        x = {chave: valor}
        dic.update(x)
        print("Aluno atualizado com sucesso!!")
        print('=' * 60)

    else:
        print("Aluno inexistente.")


def excluirAluno(dic):
    cpf = input("Digite o cpf do aluno: ")

    if isAluno(dic, cpf):
        print("Vamos escluir o aluno do cadastro.")
        dic.pop(cpf)
        print("Aluno escluido! ")
        print('=' * 60)
    else:
        print("Aluno não existente.")


# =====================================================================
# FUNÇÕES MODALIDADE


def isModalidade(dic, cod):
    for chave in dic:
        if cod == chave:
            return True
    return False


def cadModalidades(dic):

    cod = input("Digite o código da modalidade: ")

    if isModalidade(dic, cod):
        print("Modalidade já cadastrada. ")
    else:
        # receber dados
        desc = input("Digite a descrição: ")
        dura = input("digite a duração da aula (minutos): ")

        # Receber dias
        dias = []
        print("Para dos dias de oferecimento utilize as seguintes opções")
        opDias = ['segunda', 'terça', 'quarta',
                  'quinta', 'sexta', 'sabado', 'domingo']
        for value in opDias:
            print(value)
        dia = input("\nDigite o primeiro dia: ")
        while dia != '':
            dias.append(dia)
            dia = input("Digite o proximo dia: ")

        # Receber horarios
        horas = []
        hora = input("\nDigite o primeiro horário [xx:xx]")
        while hora != '':
            horas.append(hora)
            hora = input("Digite o próximo horário [xx:xx]")

        # receber professores
        profs = []
        prof = input("Digite o nome do professor responsável: ")
        while prof != '':
            profs.append(prof)
            prof = input("Digite o nome do próximo professor: ")

        # receber valor
        val = input("Digite o valor da modalidade: ")

        # gerar dic
        chave = cod
        valor = [desc, dura, dias, horas, profs, val]

        x = {chave: valor}
        dic.update(x)
        print("\n\nModalidade adicionada com sucesso!!")


def listarModalidades(dic):
    for modalidade in dic:
        cod = modalidade

        string = dic[modalidade]

        desc = string[0]
        dura = string[1]

        dias = string[2]
        dias = ','.join(dias)

        horas = string[3]
        horas = ','.join(horas)

        profs = string[4]
        profs = ','.join(profs)

        val = string[5]

        print('CODIGO:', cod, 'DESCRIÇÃO:', desc, 'DURAÇÃO:', dura, 'DIAS OFERECIDOS:', dias,
              'HORARIOS OFERECIDOS:', horas, 'PROFESSORES RESPONSÁVEIS:', profs, 'VALOR:', val)


def listarUmaModalidade(dic):
    cod = input("Digite o código: ")

    if isModalidade(dic, cod):
        string = dic[cod]

        desc = string[0]
        dura = string[1]

        dias = string[2]
        dias = ','.join(dias)

        horas = string[3]
        horas = ','.join(horas)

        profs = string[4]
        profs = ','.join(profs)

        val = string[5]

        print('CODIGO:', cod, 'DESCRIÇÃO:', desc, 'DURAÇÃO:', dura, 'DIAS OFERECIDOS:', dias,
              'HORARIOS OFERECIDOS:', horas, 'PROFESSORES RESPONSÁVEIS:', profs, 'VALOR:', val)
    else:
        print("Modalidade inexistente. ")


def alterarModalidade(dic):
    cod = input("Digite o código da modalidade: ")

    if isModalidade(dic, cod):

        desc = input("Digite a descrição: ")
        dura = input("digite a duração da aula (minutos): ")

        # Receber dias
        dias = []
        print("Para dos dias de oferecimento utilize as seguintes opções")
        opDias = ['segunda', 'terça', 'quarta',
                  'quinta', 'sexta', 'sabado', 'domingo']
        for value in opDias:
            print(value)
        dia = input("\nDigite o primeiro dia: ")
        while dia != '':
            dias.append(dia)
            dia = input("Digite o proximo dia: ")

        # Receber horarios
        horas = []
        hora = input("\nDigite o primeiro horário [xx:xx]")
        while hora != '':
            horas.append(hora)
            hora = input("Digite o próximo horário [xx:xx]")

        # receber professores
        profs = []
        prof = input("Digite o nome do professor responsável: ")
        while prof != '':
            profs.append(prof)
            prof = input("Digite o nome do próximo professor: ")

        # receber valor
        val = input("Digite o valor da modalidade: ")

        # gerar dic
        chave = cod
        valor = [desc, dura, dias, horas, profs, val]

        x = {chave: valor}
        dic.update(x)
        print("\n\nModalidade atualizada com sucesso!!")
    else:
        print("Modalidade inexistente.")


def excluirModalidade(dic):
    cod = input("Digite o código da modalidade: ")

    if isModalidade(dic, cod):
        print("Vamos escluir essa modalidade")
        dic.pop(cod)
        print("Modalidade excluida!")
        print('=' * 60)
    else:
        print("Modalidade não existe.")


# =====================================================================
# FUNÇÕES PRATICAS


def listarPraticas(lista):
    print("\nLista de práticas:\n")

    for aluno in lista:
        # printar cpf do aluno
        print('CPF aluno:', aluno[0], end=' --MODALIDADES-- ')

        # Varrer as práticas do aluno
        praticas = aluno[1:]
        for pratica in praticas:
            print('COD: ', pratica[0], 'DIA: ', pratica[1],
                  'HORA:', pratica[2], end=' --- ')
        print()


def listarUmaPratica(lista):
    cpf = input("Digite o cpf do aluno: ")

    if isPratica(cpf, lista):
        # buscar o aluno pedido
        for aluno in lista:
            if aluno[0] == cpf:
                alunoPedido = aluno

        # Encotnrou o aluno
        print('CPF aluno:', alunoPedido[0], end=' --MODALIDADES-- ')

        # varrer modalidades do aluno
        praticas = alunoPedido[1:]
        for pratica in praticas:
            print('COD: ', pratica[0], 'DIA: ', pratica[1],
                  'HORA:', pratica[2], end=' --- ')
        print()

    else:
        print('Aluno não pratica nenhuma modalidade! \n')


def isPratica(cpf, lista):
    for aluno in lista:
        if aluno[0] == cpf:
            return True
    return False


def returnAluno(cpf, lista):
    for aluno in lista:
        if aluno[0] == cpf:
            return aluno


def cadPratica(lista, dic_modalidade, dic_academia):

    # ver se a modalidade existe no sistema
    cod = input("Digite o código da modalidade: ")
    cpf = input("Digite o cpf do aluno: ")

    # aluno existe e modalidade existe
    if isModalidade(dic_modalidade, cod) and isAluno(dic_academia, cpf):
        # aluno esta cadastrado aqui em alguma coisa?
        if isPratica(cpf, lista):
            # verificar se ele ja pratica a modalidade passada
            alunoPedido = returnAluno(cpf, lista)
            alunoPedido = alunoPedido[1:]
            mods = []
            for mod in alunoPedido:
                mods.append(mod[0])

            if cod in mods:
                # aluno ja pratica essa modalidade
                return print("Aluno já pratica essa modalidade")
            else:
                # aluno não pratica ESSA modalidade
                # Verificar o horario e data desejado
                valores = dic_modalidade[cod]
                dias = ', '.join(valores[2])
                print("Os dias disponíveis são: ", end=' ')
                print(dias)

                # receber dia
                dia = input("Digite o dia desejado: ")
                if dia not in valores[2]:
                    return print("\nDia indisponível ou digitado errado, tente outra vez.")

                print("\nAs horas disponíveis são: ", end=' ')
                horas = ', '.join(valores[3])
                print(horas)
                hora = input("Digite a hora desejada: ")
                if hora not in valores[3]:
                    return print("\nHora indisponível ou digitada errado, tente outra vez!")

                # se voce chegou até aqui, bora cadastrar pois!
                alunoCadastrar1 = [cod, dia, hora]
                for aux in lista:
                    if aux[0] == cpf:
                        aux.append(alunoCadastrar1)
                return print("Aluno cadastrado nessa modalidade! ")
        else:
            # ele com ctz nao pratica NENHUMA MODALIDADE
            print(
                "Esse aluno ainda não esta matriculado em nenhuma modalidade, borá matriculado ae!!\n")
            valores = dic_modalidade[cod]
            print("Os dias disponíveis são: ", end=' ')
            print(valores[2])

            # receber dia
            dia = input("Digite o dia desejado: ")
            if dia not in valores[2]:
                return print("\nDia indisponível ou digitado errado, tente outra vez.")

            print("\nAs horas disponíveis são: ", end=' ')
            print(valores[3])
            hora = input("Digite a hora desejada: ")
            if hora not in valores[3]:
                return print("\nHora indisponível ou digitada errado, tente outra vez!")

            # Se voce chegou até aqui, bora cadastra
            alunoCadastrar2 = [cpf, [cod, dia, hora]]
            lista.append(alunoCadastrar2)
            return print('Aluno cadastrado na modalidade!\n')
    else:
        return print("Aluno ou modalidade não existente!")


def alterDiaHoraPratica(lista, dic_modalidade):
    cpf = input("Digite o cpf do aluno: ")
    cod = input("Digite o código da modalidade a ser alterada: ")

    # Verificar se esse esta na lista de modalidades
    if isPratica(cpf, lista):
        # aluno esta matriculado em alguma pratica
        for aluno in lista:
            if aluno[0] == cpf:
                if aluno[1][0] == cod:
                    print("Ok, vamos alterar\n")

                    # receber novo dia
                    valores = dic_modalidade[cod]
                    print("Os dias disponíveis são: ", end=' ')
                    print(valores[2])
                    dia = input("Digite o dia desejado: ")
                    if dia not in valores[2]:
                        return print("\nDia indisponível ou digitado errado, tente outra vez.")

                    # Receber hora
                    print("\nAs horas disponíveis são: ", end=' ')
                    print(valores[3])
                    hora = input("Digite a hora desejada: ")
                    if hora not in valores[3]:
                        return print("\nHora indisponível ou digitada errado, tente outra vez!")

                    # alterar
                    aluno[1][0] = cod
                    aluno[1][1] = dia
                    aluno[1][2] = hora
    else:
        return print("Aluno não está cadastrado em nenhuma pratica ou algum dado foi inserido errado.")


def removerAlunoPratica(lista):

    cpf = input("Digite o cpf do aluno: ")
    cod = input("Digite o código da modalidade: ")

    # verificar se ele está matriculado em alguma prática
    if isPratica(cpf, lista):

        # aluno esta matriculado em alguma pratica
        for aluno in lista:
            if aluno[0] == cpf:

                # Verificar se ele pratica ess modalidade
                for i in range(1, len(aluno)):
                    if aluno[i][0] == cod:
                        print("\n\nVamos remover o aluno dessa pratica")

                        # verificar se essa é a unica pratica dele.
                        if len(aluno) == 2:
                            # Ele só pratica isso, logo esxcluir tudo
                            idx = lista.index(aluno)
                            del lista[idx]
                            return print("Aluno removido dessa pratica e da lista de praticas")

                        else:
                            # remover somente a pratica pedida
                            idx = 0
                            for mod in aluno:
                                if mod[0] == cod:
                                    del aluno[idx]
                                    return print("Aluno removido da pratica\n")
                                idx += 1


def remoerAlunoTodasPraticas(lista):
    cpf = input("Digite o cpf do aluno: ")

    # verificar se ele esta matriculado em alguma prática
    if isPratica(cpf, lista):
        for aluno in lista:
            if aluno[0] == cpf:
                idx = lista.index(aluno)
                del lista[idx]
                return print("Aluno removido de todas as práticas.")

# =====================================================================
# FUNÇÕES RELTÓRIOS


def relatorio1(dic_modalidade):
    print("As modalidades que são ofertadas mais de 2 vezes na semana sao: \n")

    for k in dic_modalidade.items():
        chave = k[0]
        valores = k[1]

        profs = ' , '.join(valores[4])
        hora = ' , '.join(valores[3])
        dias = ' , '.join(valores[2])

        if len(valores[2]) > 2:
            print('COD:', chave)
            print('\t DESCRIÇÃO:', valores[0])
            print('\t DURAÇÃO DA AULA:', valores[1])
            print('\t DIAS OFERTADOS:', dias)
            print('\t HORARIOS:', hora)
            print('\t PROFS RESPONSÁVEIS:', profs)
            print('\t VALOR:', valores[5])
            print('\t', '===')

    print('=' * 60)


def relatorio2(dic_modalidade):
    cod = input("Digite o código da modalidade a ser consultada: ")

    # verificar se é modalidade valida
    if isModalidade(dic_modalidade, cod):
        print("A disponibilidade da modalidade é:\n")

        for chave in dic_modalidade:
            if chave == cod:

                valores = dic_modalidade[chave]

                dias = ', '.join(valores[2])
                horas = ', '.join(valores[3])
                profs = ', '.join(valores[4])

                print('\tDIAS:', dias)
                print('\tHORAS:', horas)
                print('\tPROFESSORES:', profs)

    else:
        return print("Esse código de modalidade é inválido.")


def relatorio3(praticas, dic_modalidade, dic_academia):

    x = int(input("Digite o número de modalidade: "))

    for aluno in praticas:
        # verificar se é maior que x
        tam = len(aluno) - 1
        if tam > x:

            # printar dados do aluno
            cpf = str(aluno[0])
            for chave in dic_academia:
                if chave == cpf:
                    valores = dic_academia[chave]

                    modalidades = aluno[1:]

                    print('\nDados do aluno:')
                    emails = ', '.join(valores[5])
                    tels = ', '.join(valores[6])
                    print('CPF:', chave, 'NOME:', valores[0], 'DATA DE NASCIMENTO:', valores[1], 'SEXO:', valores[2],
                          'PESO:', valores[3], 'ALTURA:', valores[4], 'EMAILS: ', emails, 'TELEFONES:', tels)
                    print('Modalidades que ele pratica:')
                    for mod in modalidades:
                        print("MODALIDADE:", mod[0], 'DIA:',
                              mod[1], 'HORARIO:', mod[2])
                    print('='*10)

    return print("Fim dos alunos nessa categoria.")


# =====================================================================
# MAIN


def main():

    # declarar dicionarios
    dic_academia = {}
    dic_modalidade = {}
    praticas = []

    # Verificar existencia
    if os.path.exists('alunos.txt'):
        lerAlunos(dic_academia)
        print("Dicionário alunos carregado!")
    if os.path.exists('modalidades.txt'):
        lerModalidades(dic_modalidade)
        print("Dicionario modalidades carregado!")
    if os.path.exists('praticas.txt'):
        lerPraticas(praticas)
        print("Lista de praticas carregada!")
    menu = True
    while menu:
        mostrarMenu()
        op1 = input("\n Escolha uma opção: ")

        if op1 == '1':
            print("="*50)
            submenuAlunos()
            op2 = input("Digite sua opção: ")

            # submenu
            if op2 == '1':
                print('Segue a lista de todos os aluno.\n\n')
                listarAlunoFormatado(dic_academia)

            elif op2 == '2':
                listarUmAluno(dic_academia)

            elif op2 == '3':
                cadAluno(dic_academia)

            elif op2 == '4':
                alterarAluno(dic_academia)

            elif op2 == '5':
                excluirAluno(dic_academia)

        elif op1 == '2':
            print("="*50)
            submenuModalidades()
            op2 = input("Digite sua opção: ")

            # submenu
            if op2 == '1':
                listarModalidades(dic_modalidade)

            elif op2 == '2':
                listarUmaModalidade(dic_modalidade)

            elif op2 == '3':
                cadModalidades(dic_modalidade)

            elif op2 == '4':
                alterarModalidade(dic_modalidade)

            elif op2 == '5':
                excluirModalidade(dic_modalidade)

        elif op1 == '3':
            print("="*50)
            submenuPraticas()
            op2 = input("Digite sua opção: ")

            # submenu
            if op2 == '1':
                listarPraticas(praticas)

            elif op2 == '2':
                listarUmaPratica(praticas)

            elif op2 == '3':
                cadPratica(praticas, dic_modalidade, dic_academia)

            elif op2 == '4':
                alterDiaHoraPratica(praticas, dic_modalidade)

            elif op2 == '5':
                removerAlunoPratica(praticas)

            elif op2 == '6':
                remoerAlunoTodasPraticas(praticas)

        elif op1 == '4':
            print("="*50)
            submenurRelatorios()
            op2 = input("Digite sua opção: ")

            # submenu
            if op2 == '1':
                relatorio1(dic_modalidade)

            elif op2 == '2':
                relatorio2(dic_modalidade)

            elif op2 == '3':
                relatorio3(praticas, dic_modalidade, dic_academia)

        else:
            salvaAlunos(dic_academia)
            salvaModalidades(dic_modalidade)
            salvaPratica(praticas)
            print("\nTerminando a execução do programa!!!")
            menu = False


#### MAIN ####
main()
