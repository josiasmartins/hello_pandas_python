# hello_pandas — guia simples

Resumo rápido: como preparar ambiente, instalar dependências e executar o projeto.

1) Criar e ativar um ambiente virtual (recomendado)

```bash
python -m venv .venv
# Bash (Git Bash / WSL)
source .venv/Scripts/activate
# PowerShell
.\.venv\Scripts\Activate.ps1
# CMD
.\.venv\Scripts\activate.bat
```

2) Instalar dependências

- Usando o `requirements.txt` do projeto (recomendado):

```bash
pip install -r requirements.txt
```

- Ou instalar pacotes únicos:

```bash
pip install pandas requests
```

3) Onde as dependências são salvas

- Se estiver usando o Python do sistema (sem `venv`):
	- Exemplo no seu caso: `C:\Users\Josias\Documents\Jonas\Anaconda-Python\lib\site-packages` (pasta principal)
	- Local para `--user`: `C:\Users\Josias\AppData\Roaming\Python\Python39\site-packages`
- Se estiver usando um `venv`: dentro do próprio venv, por exemplo `.venv\Lib\site-packages` (não commite isso)
- No Databricks: as instalações via init script ou UI vão para o driver/workers do cluster (não para o repositório)

Comandos úteis para ver onde um pacote está instalado:

```bash
pip -V
pip show pandas
python -c "import pandas; print(pandas.__file__)"
```

O que significa `-r`?

O argumento `-r` do pip significa "read" (ler). Quando você executa `pip install -r requirements.txt`, o pip lê a lista de pacotes e versões dentro desse arquivo e instala cada uma delas. Use `-r` sempre que quiser instalar todas as dependências listadas num `requirements.txt` de uma vez.

Limpar/ver cache do pip

O pip mantém um cache de pacotes baixados para acelerar instalações futuras. Para ver onde fica esse cache use:

```bash
pip cache dir
```

Para limpar o cache:

```bash
pip cache purge
```

4) Executar o projeto

```bash
python main.py
# ou
python install_and_run.py
```

5) Não commite o `.venv` no repositório

Adicione ao `.gitignore`:

```
.venv/
__pycache__/
*.pyc
dist/
build/
```

Se já comitou, remova do git e ignore:

```bash
git rm -r --cached .venv
echo ".venv/" >> .gitignore
git add .gitignore
git commit -m "Remove .venv do repositório"
```

6) Notas rápidas para Databricks

- Use `databricks/libs/requirements.txt` ou envie um wheel para DBFS e instale como library no cluster.
- Exemplo rápido com Databricks CLI (requere configuração):

```bash
cd databricks
./deploy.sh
```

---
---

Se quiser, eu simplifico ainda mais ou adiciono um `run.sh`/`run.ps1` para automatizar ativação + execução.

## Git: configurar user/email e adicionar chave SSH ao GitHub

1) Configurar nome e e-mail do Git

- Global (para todos os repositórios):

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

- Só neste repositório:

```bash
git config user.name "Seu Nome"
git config user.email "seu@email.com"
```

2) Criar uma chave SSH (ed25519 recomendado)

```bash
# ed25519 (recomendado)
ssh-keygen -t ed25519 -C "seu@email.com"

# ou RSA (compatibilidade ampla)
ssh-keygen -t rsa -b 4096 -C "seu@email.com"
```

Aceite o local padrão (por exemplo `~/.ssh/id_ed25519`) e defina uma passphrase se desejar.

3) Adicionar a chave ao ssh-agent

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

4) Copiar a chave pública e adicionar ao GitHub

```bash
# Windows (Git Bash):
cat ~/.ssh/id_ed25519.pub | clip

# macOS:
cat ~/.ssh/id_ed25519.pub | pbcopy

# Linux (com xclip):
cat ~/.ssh/id_ed25519.pub | xclip -sel clip
```

No GitHub: vá em Settings → SSH and GPG keys → New SSH key → cole a chave pública.

Alternativa com GitHub CLI (`gh`):

```bash
gh auth login
gh ssh-key add ~/.ssh/id_ed25519.pub -t "Minha chave"
```

5) Testar a conexão

```bash
ssh -T git@github.com
```

6) Atualizar o README com seus dados

Se quiser que eu escreva o `user.name` e `user.email` usados em uma seção do README (por exemplo, um rodapé "autor"), diga o nome e email que deseja incluir e eu atualizo o arquivo.
