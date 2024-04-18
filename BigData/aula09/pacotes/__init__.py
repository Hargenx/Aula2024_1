'''Para definir um módulo, que é um bloco de código destinado a ser reutilizado em outras partes de um projeto, você pode seguir os seguintes passos:

Crie uma pasta com o nome do módulo desejado.
Dentro dessa pasta, crie um arquivo chamado __init__.py. 
Em seguida, crie o arquivo que conterá o código-fonte do módulo, por exemplo, module.py.'''

# Arquivo __init__.py

# Aqui você pode inicializar seu pacote, importar módulos,
# definir variáveis globais ou configurar comportamentos padrão.

# Por exemplo, vamos importar o módulo `module.py` neste pacote.
from . import module
