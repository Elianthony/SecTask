# SecTask

## NO UBUNTU ou DEBIAN:

Confira a versão do python se se encontra na versão 3.10.6

```
python --version
```

Se não se encontrar verifique o caminho das variáveis de ambiente no ~/.bashrc e inclua no fim do arquivo o comando:

```
alias python=python3
```

Para desenvolver é necessário executar o ambiente virtual do python 3.10.6 e instalar os requisitos, não esqueça de no ubuntu executar o pip install instalando o virtualenv com o super-usuário; para tal execute o commando:

```
sudo pip install virtualenv
```

Para inciar o ambiente virtual execute o comando dentro da pasta:

```
virtualenv standard
```

Para ativar o ambiente:
```
. standard/bin/activate
```

Para instalar os requerimentos:
```
pip install -r requirements.txt
```

Confirme que todos as bibliotecas do python estão instalados
```
pip freeze
```

Para desativar o ambiente:
```
deactivate
```

Para conectar no MySQL Server no windows via WSL2 é preciso verificar como o seu subsistema do linux está resolvendo a conexão com o servidor local, essa variável está armazenada no seguinte arquivo

```
nano /etc/resolv.conf
```

*Copie o valor de nameserver para o host de conexão do servidor do banco com a porta configurada (normalmente a padrão é 3306) e o usuário e senha que você criou no seu servidor MySQL e poderá se conectar.

**LEMBRE-SE! Esse valor altera toda vez que o subsistema do Linux é iniciado.

Verifique no seu Mysql Server pelo CLI se ele tem usuário cadastrado:

```
SELECT user, host FROM mysql.user;
```

Apague qualquer usuário que você criou acidentalmente apenas deixando os padrões do sistema com:

```
DROP USER '<user>'@'%';
```

Crie o novo usuário que usará para conexão para permitir acesso dele de qualquer ip

```
CREATE USER '<user>'@'%' IDENTIFIED BY '<passwd>';
```

Garanta o acesso dele a qualquer banco ou schema construído dentro do servidor:

```
GRANT ALL PRIVILEGES ON *.* TO '<user>'@'%' WITH GRANT OPTION;
```