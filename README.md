# CRUD Academia

Projeto de CRUD para academia desenvolvido para a disciplina de Algoritmos e Programação.

## Pré-requisitos

* Python3 
* Pip 3 [tutorial-instalação](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/)

## Instalação

Crie um ambiente virtual
```bash
$ python3 -m venv [nome_da_pasta]
$ source [nome_da_pasta]/bin/activate
$ pip3 freeze > requeriments.txt
```

Verifique se está utilizando o interpretador do ambiente virtual
```bash
$ which python3
```

Instale as dependências do projeto
```bash
$ pip3 install --requirement requirements.txt
```

## Utilização

Inicialize o programa na pasta raiz
```bash
python3 src/crud.py
```

## License
[MIT](LICENSE.md)
