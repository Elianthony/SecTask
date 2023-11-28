import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='0000',
    database='sectask',
    )

cursor = conexao.cursor()

#CREATE - criar uma informação na tabela Funcionario
nomeFuncionario = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
telefone = input("Digite seu telefone: ")
endereco = input("Digite seu endereço: ")
dtCadastro = input("Digite a data do seu cadastro: ")
idSupervisor = input("Digite o ID do seu Supervisor: ")
createfuncionario = f'INSERT INTO Funcionario (nomeFuncionario, email, telefone, endereco, dtCadastro) VALUES ({nomeFuncionario}, {email}, {telefone}, {endereco}, {dtCadastro})'
cursor.execute(createfuncionario)
conexao.commit()

#CREATE - criar uma informação na tabela Tarefa
tituloTarefa = input("Digite o titulo da tarefa: ")
descricao = input("Digite a descrição da tarefa: ")
dtVencimento = input("Digite a data de vencimento: ")
prioridade = input("Digite a prioridade: ")
dtCriacao = input("Digite a data da criação da tarefa: ")
dtConclusao = input("Digite a data da conclusão da tarefa: ")
createtarefa = f'INSERT INTO Tarefa (tituloTarefa, descricao, dtVencimento, prioridade, dtCriacao, dtConclusao) VALUES ({tituloTarefa}, {descricao}, {dtVencimento}, {prioridade}, {dtCriacao}, {dtConclusao})'
cursor.execute(createtarefa)
conexao.commit()

#CREATE - criar uma informação na tabela Projeto
nomeProjeto = input("Digite o nome do Projeto: ")
descricao = input("Digite a descrição do Projeto: ")
dtConclusao = input("Digite a data da conclusão do Projeto: ")
dtInicio = input("Digite a data de inicio do Projeto: ")
createprojeto = f'INSERT INTO Projeto (nomeProjeto, descricao, dtConclusao, dtInicio) VALUES ({nomeProjeto}, {descricao}, {dtConclusao}, {dtInicio})'
cursor.execute(createprojeto)
conexao.commit()

#CREATE - criar uma informação na tabela Equipe
nomeEquipe = input("Digite o nome da Equipe: ")
descricao = input("Digite a descrição da Equipe: ")
dtFormacao = input("Digite a data de formação da equipe: ")
apoio = input("Digite S ou N para equipe Apoio: ")
createquipe = f'INSERT INTO Equipe (nomeEquipe, descricao, dtFormacao, apoio) VALUES ({nomeEquipe}, {descricao}, {dtFormacao}, {apoio})'
cursor.execute(createquipe)
conexao.commit()

#CREATE - criar uma informação na tabela Categoria
nomeCategotia = input("Digite o nome da Categoria: ")
descricao = input("Digite a descrição da Categoria: ")
createcategoria = f'INSERT INTO Categoria (nomeCategotia, descricao) VALUES ({nomeCategotia}, {descricao})'
cursor.execute(createcategoria)
conexao.commit()

#CREATE - criar uma informação na tabela Documentacao
tituloDocumento = input("Digite o titulo do Documento: ")
dtPublicacao = input("Digite a data da publicaçao: ")
createdocumento = f'INSERT INTO Documentacao (tituloDocumento, dtPublicacao) VALUES ({tituloDocumento}, {dtPublicacao})'
cursor.execute(createdocumento)
conexao.commit()


#READ - ler dados na tabela Funcionario
readfuncionario = f'SELECT * FROM Funcionario'
cursor.execute(readfuncionario)
resultado = cursor.fetchall()
print(resultado)

#READ - ler dados na tabela Tarefa
readtarefa = f'SELECT * FROM Tarefa'
cursor.execute(readtarefa)
resultado = cursor.fetchall()
print(resultado)

#READ - ler dados na tabela Projeto
readprojeto = f'SELECT * FROM Projeto'
cursor.execute(readprojeto)
resultado = cursor.fetchall()
print(resultado)

#READ - ler dados na tabela Funcionario
readfuncionario = f'SELECT * FROM Funcionario'
cursor.execute(readfuncionario)
resultado = cursor.fetchall()
print(resultado)

#UPDATE - editar o banco de dados
nome_produto = "todynho"
valor = 6
update = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(update)
conexao.commit()

#DELETE - deletar informações banco
nome_produto = "todynho"
delete = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(delete)
conexao.commit()

#encerrar o cursor e a conexão
cursor.close()
conexao.close()