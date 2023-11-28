# SecTask

## NO UBUNTU ou DEBIAN:
---

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