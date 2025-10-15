# hello_pandas

Este repositório contém um pequeno projeto Python que usa pandas. Este arquivo explica como instalar as dependências e como executar o projeto.

## Requisitos

- Python 3.8+ instalado
- pip (vem com o Python)
- (Opcional) virtualenv/venv para criar um ambiente isolado

> Observação: os exemplos abaixo usam o terminal bash (por exemplo Git Bash, WSL) no Windows. Se preferir PowerShell ou CMD, os comandos de ativação do ambiente virtual mudam um pouco (veja notas abaixo).

## Opção A — Instalar dependências uma-a-uma

1. (Opcional, recomendado) Crie e ative um ambiente virtual:

```bash
# criar ambiente (venv)
python -m venv .venv

# ativar no bash (Git Bash / WSL)
source .venv/Scripts/activate

# No PowerShell:
# .\.venv\Scripts\Activate.ps1

# No CMD:
# .\.venv\Scripts\activate.bat
```

2. Instale as dependências individualmente com pip. Por exemplo, se o projeto precisa de `pandas` e `numpy`:

```bash
pip install pandas
pip install numpy
```

3. Verifique que as instalações funcionaram:

```bash
python -c "import pandas as pd; import numpy as np; print(pd.__version__, np.__version__)"
```

4. (Opcional) Gere um `requirements.txt` a partir do ambiente atual:

```bash
pip freeze > requirements.txt
```

## Opção B — Usar o arquivo `requirements.txt`

Se o repositório já contém um arquivo `requirements.txt` (veja `requirements.txt` na raiz), você pode instalar tudo de uma vez:

1. Criar e ativar ambiente virtual (recomendado):

```bash
python -m venv .venv
source .venv/Scripts/activate
```

2. Instalar todas as dependências do `requirements.txt`:

```bash
pip install -r requirements.txt
```

3. Verifique a instalação:

```bash
python -c "import pandas as pd; print(pd.__version__)"
```

## Como executar o projeto

O repositório contém `main.py` e `install_and_run.py`.

- Para executar o arquivo principal (caso use `main.py`):

```bash
python main.py
```

- Para executar o utilitário `install_and_run.py` (se existir uma rotina de instalação/execução lá):

```bash
python install_and_run.py
```

Se você estiver usando um ambiente virtual, certifique-se de que ele está ativado antes de rodar os comandos acima.

## Notas sobre Windows

- No Git Bash, a ativação do `venv` normalmente funciona com `source .venv/Scripts/activate`.
- No PowerShell (recomendado no Windows moderno), use `.\.venv\Scripts\Activate.ps1`.
- No CMD clássico, use `.\.venv\Scripts\activate.bat`.

Se encontrar problemas de permissão ao ativar o script no PowerShell, execute `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` antes de ativar (abrir PowerShell como administrador pode ser necessário).

## Perguntas frequentes (curtas)

- Posso instalar as dependências globalmente? Sim, mas usar um `venv` é altamente recomendado para evitar conflitos com outras projecten e com pacotes do sistema.
- Como saber quais pacotes instalar manualmente? Abra `requirements.txt` e veja a lista; instale somente os nomes sem versões (ou com versões, se preferir).

## Exemplo rápido

```bash
# clonar o repositório
git clone <repo-url>
cd hello_pandas

# criar e ativar venv (bash)
python -m venv .venv
source .venv/Scripts/activate

# instalar dependências
pip install -r requirements.txt

# executar
python main.py
```

---

Se quiser, eu posso também:

- ajustar o `README.md` com instruções específicas para a sua versão do Windows;
- adicionar um pequeno script `run.sh`/`run.ps1` que automatize ativação + execução.
