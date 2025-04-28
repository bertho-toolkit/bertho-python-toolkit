# 1. Escolha uma imagem base oficial do Python
# Use uma versão específica para maior consistência (ex: 3.11, 3.10, etc.)
# A versão "-slim" é menor, boa para produção e desenvolvimento.
FROM python:3.11-slim

# 2. Defina variáveis de ambiente úteis
# PYTHONUNBUFFERED: Garante que logs apareçam imediatamente
# PYTHONDONTWRITEBYTECODE: Evita criar arquivos .pyc no host via volume montado
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# 3. Crie e defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# 4. Crie um ambiente virtual
# Colocamos o venv em /opt para mantê-lo separado do código da aplicação em /app
RUN python -m venv /opt/venv

# 5. Ative o ambiente virtual para os comandos subsequentes
# Adicionando o diretório 'bin' do venv ao PATH
ENV PATH="/opt/venv/bin:$PATH"

# 6. Instale as dependências
# Copie apenas o requirements.txt primeiro para aproveitar o cache do Docker
COPY requirements.txt .
# Instale as dependências DENTRO do venv
# --no-cache-dir reduz o tamanho da imagem
RUN pip install --no-cache-dir -r requirements.txt

# 7. Copie o restante do código da sua aplicação para o diretório de trabalho
# (Isso será sobrescrito pelo volume no docker-compose para desenvolvimento,
# mas é útil para construir uma imagem independente se necessário)
COPY . .

# 8. (Opcional) Exponha uma porta se sua aplicação for um servidor web (ex: Flask, Django)
# EXPOSE 5000

# O comando de execução (`CMD` ou `ENTRYPOINT`) será gerenciado pelo docker-compose
# para facilitar o desenvolvimento com o PyCharm. Se não usar compose,
# você adicionaria algo como: CMD ["python", "src/main.py"]