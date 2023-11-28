import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='0000',
    database='sectask',
    )

cursor = conexao.cursor()

#CREATE - criar uma informação na tabelas

def criar_funcionario():
    nomeFuncionario = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    telefone = input("Digite seu telefone: ")
    endereco = input("Digite seu endereço: ")
    dtCadastro = input("Digite a data do seu cadastro: ")
    idSupervisor = input("Digite o ID do seu Supervisor: ")
    createfuncionario = 'INSERT INTO Funcionario (nomeFuncionario, email, telefone, endereco, dtCadastro, idSupervisor) VALUES (%s, %s, %s, %s, %s, %s)'
    valores = (nomeFuncionario, email, telefone, endereco, dtCadastro, idSupervisor)
    cursor.execute(createfuncionario, valores)
    conexao.commit()
    print("Registro criado com sucesso!")

def criar_tarefa():
    tituloTarefa = input("Digite o titulo da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    dtVencimento = input("Digite a data de vencimento: ")
    prioridade = input("Digite a prioridade: ")
    dtCriacao = input("Digite a data da criação da tarefa: ")
    dtConclusao = input("Digite a data da conclusão da tarefa: ")
    createtarefa = 'INSERT INTO Tarefa (tituloTarefa, descricao, dtVencimento, prioridade, dtCriacao, dtConclusao) VALUES (%s, %s, %s, %s, %s, %s)'
    valores = (tituloTarefa, descricao, dtVencimento, prioridade, dtCriacao, dtConclusao)
    cursor.execute(createtarefa, valores)
    conexao.commit()
    print("Registro criado com sucesso!")


def criar_projeto():
    nomeProjeto = input("Digite o nome do Projeto: ")
    descricao = input("Digite a descrição do Projeto: ")
    dtConclusao = input("Digite a data da conclusão do Projeto: ")
    dtInicio = input("Digite a data de inicio do Projeto: ")
    createprojeto = 'INSERT INTO Projeto (nomeProjeto, descricao, dtConclusao, dtInicio) VALUES (%s, %s, %s, %s)'
    valores = (nomeProjeto, descricao, dtConclusao, dtInicio)
    cursor.execute(createprojeto, valores)
    conexao.commit()
    print("Registro criado com sucesso!")

def criar_equipe():
    nomeEquipe = input("Digite o nome da Equipe: ")
    descricao = input("Digite a descrição da Equipe: ")
    dtFormacao = input("Digite a data de formação da equipe: ")
    apoio = input("Digite S ou N para equipe Apoio: ")
    createquipe = 'INSERT INTO Equipe (nomeEquipe, descricao, dtFormacao, apoio) VALUES (%s, %s, %s, %s)'
    valores = (nomeEquipe, descricao, dtFormacao, apoio)
    cursor.execute(createquipe, valores)
    conexao.commit()
    print("Registro criado com sucesso!")

def criar_categoria():
    nomeCategotia = input("Digite o nome da Categoria: ")
    descricao = input("Digite a descrição da Categoria: ")
    createcategoria = 'INSERT INTO Categoria (nomeCategoria, descricao) VALUES (%s, %s)'
    valores = (nomeCategoria, descricao)
    cursor.execute(createcategoria, valores)
    conexao.commit()
    print("Registro criado com sucesso!")

def criar_documento():
    tituloDocumento = input("Digite o titulo do Documento: ")
    dtPublicacao = input("Digite a data da publicaçao: ")
    createdocumento = 'INSERT INTO Documentacao (tituloDocumento, dtPublicacao) VALUES (%s, %s)'
    valores = (tituloDocumento, dtPublicacao)
    cursor.execute(createdocumento, valores)
    conexao.commit()
    print("Registro criado com sucesso!")



#READ - ler dados nas tabelas

def ler_funcionario():
    readfuncionario = f'SELECT * FROM Funcionario'
    cursor.execute(readfuncionario)
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(resultado)


def ler_tarefa():
    readtarefa = f'SELECT * FROM Tarefa'
    cursor.execute(readtarefa)
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(resultado)


def ler_projeto():
    readprojeto = f'SELECT * FROM Projeto'
    cursor.execute(readprojeto)
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(resultado)

def ler_categoria():
    readcategoria = 'SELECT * FROM Categoria'
    cursor.execute(readcategoria)
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(resultado)

def ler_equipe():
    readequipe = 'SELECT * FROM Equipe'
    cursor.execute(readequipe)
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(resultado)


def ler_documentacao():
    readocumento = 'SELECT * FROM Documentacao'
    cursor.execute(readocumento)
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(resultado)


#DELETE - deletar informações do banco

def deletar_funcionario(nomeFuncionario):
    deletefuncionario = f'DELETE FROM Funcionario WHERE nomeFuncionario = "{nomeFuncionario}"'
    cursor.execute(deletefuncionario)
    conexao.commit()


def deletar_tarefa(idTarefa):
    deletetarefa = f'DELETE FROM Tarefa WHERE idTarefa = "{idTarefa}"'
    cursor.execute(deletetarefa)
    conexao.commit()

def deletar_projeto(idProjeto):
    deleteprojeto = f'DELETE FROM Projeto WHERE idProjeto = "{idProjeto}"'
    cursor.execute(deleteprojeto)
    conexao.commit()

def deletar_equipe(nomeEquipe):
    deletequipe = f'DELETE FROM Equipe WHERE nomeEquipe = "{nomeEquipe}"'
    cursor.execute(deletequipe)
    conexao.commit()

def deletar_categoria(idCategoria):
    deletecategoria = f'DELETE FROM Categoria WHERE idCategoria = "{idCategoria}"'
    cursor.execute(deletecategoria)
    conexao.commit()

def deletar_documentacao(idDocumento):
    deletedocumento = f'DELETE FROM Documentacao WHERE idDocumento = "{idDocumento}"'
    cursor.execute(deletedocumento)
    conexao.commit()

#UPDATE - Atualizar informações do banco

def atualizar_funcionario():
    nomeFuncionario = input("Digite o nome do funcionário a ser atualizado: ")
    novo_email = input("Digite o novo e-mail: ")
    novo_telefone = input("Digite o novo telefone: ")
    novo_endereco = input("Digite o novo endereço: ")
    nova_data_cadastro = input("Digite a nova data de cadastro: ")
    novo_id_supervisor = input("Digite o novo ID do supervisor: ")

    update_funcionario = '''
        UPDATE Funcionario
        SET 
            email = %s,
            telefone = %s,
            endereco = %s,
            dtCadastro = %s,
            idSupervisor = %s
        WHERE nomeFuncionario = %s
    '''

    valores = (novo_email, novo_telefone, novo_endereco, nova_data_cadastro, novo_id_supervisor, nomeFuncionario)
    cursor.execute(update_funcionario, valores)
    conexao.commit()
    print("Registro atualizado com sucesso!")

def atualizar_tarefa():
    idTarefa = input("Digite o ID da tarefa a ser atualizada: ")
    novo_titulo = input("Digite o novo título da tarefa: ")
    nova_descricao = input("Digite a nova descrição da tarefa: ")
    novo_dtVencimento = input("Digite a nova data de vencimento da tarefa: ")
    nova_prioridade = input("Digite a nova prioridade da tarefa: ")
    novo_dtCriacao = input("Digite a nova data de criação da tarefa: ")
    novo_dtConclusao = input("Digite a nova data de conclusão da tarefa: ")

    update_tarefa = '''
        UPDATE Tarefa
        SET 
            tituloTarefa = %s,
            descricao = %s,
            dtVencimento = %s,
            prioridade = %s,
            dtCriacao = %s,
            dtConclusao = %s
        WHERE idTarefa = %s
    '''

    valores = (novo_titulo, nova_descricao, novo_dtVencimento, nova_prioridade, novo_dtCriacao, novo_dtConclusao, idTarefa)
    cursor.execute(update_tarefa, valores)
    conexao.commit()
    print("Registro de tarefa atualizado com sucesso!")

def atualizar_projeto():
    idProjeto = input("Digite o ID do projeto a ser atualizado: ")
    novo_nome = input("Digite o novo nome do projeto: ")
    nova_descricao = input("Digite a nova descrição do projeto: ")
    nova_dtConclusao = input("Digite a nova data de conclusão do projeto: ")
    nova_dtInicio = input("Digite a nova data de início do projeto: ")

    update_projeto = '''
        UPDATE Projeto
        SET 
            nomeProjeto = %s,
            descricao = %s,
            dtConclusao = %s,
            dtInicio = %s
        WHERE idProjeto = %s
    '''

    valores = (novo_nome, nova_descricao, nova_dtConclusao, nova_dtInicio, idProjeto)
    cursor.execute(update_projeto, valores)
    conexao.commit()
    print("Registro de projeto atualizado com sucesso!")

def atualizar_categoria():
    nomeCategoria = input("Digite o nome da categoria a ser atualizada: ")
    nova_descricao = input("Digite a nova descrição: ")

    update_categoria = '''
        UPDATE Categoria
        SET descricao = %s
        WHERE nomeCategoria = %s
    '''

    valores = (nova_descricao, nomeCategoria)
    cursor.execute(update_categoria, valores)
    conexao.commit()
    print("Registro de categoria atualizado com sucesso!")


def atualizar_equipe():
    nomeEquipe = input("Digite o nome da equipe a ser atualizada: ")
    nova_descricao = input("Digite a nova descrição da equipe: ")
    nova_dtFormacao = input("Digite a nova data de formação da equipe: ")
    novo_apoio = input("Digite S ou N para a nova condição de equipe de apoio: ")

    update_equipe = '''
        UPDATE Equipe
        SET 
            descricao = %s,
            dtFormacao = %s,
            apoio = %s
        WHERE nomeEquipe = %s
    '''

    valores = (nova_descricao, nova_dtFormacao, novo_apoio, nomeEquipe)
    cursor.execute(update_equipe, valores)
    conexao.commit()
    print("Registro de equipe atualizado com sucesso!")


#encerrar o cursor e a conexão
cursor.close()
conexao.close()