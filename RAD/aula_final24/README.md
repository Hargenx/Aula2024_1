# CRUD Simples com Python, SQLite e Tkinter
<p>Este é um exemplo de aplicação CRUD (Create, Read, Update, Delete) simples desenvolvido em Python utilizando o padrão MVC (Model-View-Controller), com interface gráfica construída usando Tkinter e armazenamento de dados feito em um banco de dados SQLite.</p>

## Funcionalidades
- Adicionar novos itens com nome e quantidade.
- Visualizar todos os itens cadastrados.
- Atualizar informações de um item existente.
- Excluir itens cadastrados.

## Requisitos
- Python 3.x instalado
- Biblioteca Tkinter e SQLite3 (normalmente já vem instalada com Python)

## Como executar
1- Clone o repositório para sua máquina local:
```python
git clone https://github.com/professorRaphael/crud-python-sqlite-tkinter.git
```
2- Navegue até o diretório do projeto:
```python
cd crud-python-sqlite-tkinter
```

3- Execute o arquivo main.py:
```python
python main.py
```

## Estrutura do Projeto
- model.py: Contém a definição do modelo de dados e as operações de CRUD no banco de dados SQLite.
- controller.py: Implementa a lógica de negócios e intermedia a comunicação entre a visão e o modelo.
- view.py: Responsável pela interface gráfica e interação com o usuário, utilizando Tkinter.
- main.py: Ponto de entrada da aplicação, onde a visão é instanciada e a aplicação é iniciada.

## Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues relatando problemas ou sugerir melhorias. Se preferir, faça um fork do projeto, implemente as alterações e envie um pull request.