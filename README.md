# deploy-ml-bentoml 

Esse projeto foi um estudo desenvolvimento para implementar o deploy de um modelo machine learning usando bentoml, e publicando no heroku, todavia decidir por não publicar no heroku, e usar somente o streamlit para uma interação amizagavel com o modelo.

**PS**: Para implementar no streamlit não é necessário utilizar o `bentoml`.

##  Project Structure
`src`: consists of Python scripts
`config`: consists of configuration files
`data`: consists of data
`processors`: consists of all scikit-learn's transformers used to process the new input

## Configuração do Projeto usando Poetry

### Clone o Repositório

Clone este repositório específico (branch `bentoml_demo`):

```bash
git clone --branch bentoml_demo https://github.com/khuyentran1401/customer_segmentation.git
```
## Configuração do Ambiente Virtual com Poetry

### Criar um Ambiente Virtual

Para criar um novo ambiente virtual Python usando Poetry, execute o seguinte comando:

```bash
poetry env use python3
```

## Ativar o Ambiente Virtual
Para ativar o ambiente virtual recém-criado, use o comando:

```bash
poetry shell
```

## Instalação das Dependências do Projeto

Depois de configurar o ambiente virtual com Poetry, instale todas as dependências listadas no arquivo pyproject.toml (gerenciado pelo Poetry) com o comando:

```bash
poetry install
```
## Para treinar o modelo use

1. Ative o ambiente virtual 
2. Rode o código **`main.py`**

## Para fazer classificanção usando Bentoml

1. Ative o ambiente virtual 
2. Rode o código **`bentoml serve src.bentoml_app:service --reload`**
3. Acesse o link indicado no terminal ou use: http://127.0.0.1:3000/

## Para fazer classificanção usando Streamlit

1. Ative o ambiente virtual 
2. Rode o código **`streamlit run src/streamlit_app.py`**
    > O link de acesso será fornecido ou abrirá automaticamente



## Ferramaentas usadas nesse projeto
* [hydra](https://hydra.cc/): Gerencia arquivos de configuração - [article](https://mathdatasimplified.com/stop-hard-coding-in-a-data-science-project-use-configuration-files-instead/)

* [Poetry](https://towardsdatascience.com/how-to-effortlessly-publish-your-python-package-to-pypi-using-poetry-44b305362f9f): Gerenciamento de dependências - [article](https://mathdatasimplified.com/poetry-a-better-way-to-manage-python-dependencies/)
