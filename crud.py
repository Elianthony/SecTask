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




#UPDATE - editar o banco de dados
nome_produto = "todynho"
valor = 6
update = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(update)
conexao.commit()


#encerrar o cursor e a conexão
cursor.close()
conexao.close()