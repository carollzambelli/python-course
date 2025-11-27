# Python Course

Repositório destinado ao ensino da linguagem python para iniciantes.

### Conteúdo
---
1. Warmup 
    - Estruturas Fundamentais
    - Paths e leitura de arquivos
    - Funções 
2. Manipulação de Dados
    - Numpy
    - Pandas
3. Análise de Dados
    - Matplotlip, Searborn
    - Sckitlearn
4. Projeto

### Comandos básicos
---
1. Ambiente virtual
```
python -m venv env 
source env/bin/activate
## Windows
>> python -m venv env 
>> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
>> .\env\Scripts\Activate.ps1 
```

2. Requirements
```
## Para gerar o arquivo de dependências
>> pip freeze >> requirements.txt
## Para instalar os pacotes
>> pip install -r requirements.txt 
```

3. Criação do PYTHONPATH na raiz do projeto
```
>> export PYTHONPATH=$PYTHONPATH:./
## For Windows
>> $env:PYTHONPATH = "$env:PYTHONPATH;$(Get-Location)"
```

### Referências
---
1. https://python-guide-pt-br.readthedocs.io/pt-br/latest/
2. https://greenteapress.com/thinkpython/html/index.html
3. https://www.hackerrank.com/
4. https://peps.python.org/pep-0008/

### Links Úteis
---
1. https://www.anaconda.com/download
2. https://git-scm.com/install/windows
3. https://code.visualstudio.com/download