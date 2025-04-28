FROM python:3.13-slim

# 1. Diretório de trabalho onde seu código será montado
WORKDIR /workspace

# 2. Copia apenas o requirements para instalar dependências
COPY requirements.txt .

# 3. Cria o venv em /opt/venv e instala as libs
RUN python -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip setuptools wheel \
    && if [ -f requirements.txt ]; then /opt/venv/bin/pip install -r requirements.txt; fi

# 4. Expõe o venv no PATH e define HOME
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:${PATH}"
ENV HOME=/workspace