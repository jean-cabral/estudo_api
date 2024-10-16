# Use a imagem oficial do Python como base
FROM python:3.10.2

# Defina a variável de ambiente para desabilitar o buffering
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Atualiza o PIP
RUN pip install --upgrade pip

# Copia o arquivo de requisitos para o contêiner
COPY requirements.txt .

# Instala as dependências do requirements.txt
RUN pip install -r requirements.txt

# Copia o código da aplicação para o contêiner
COPY . .

# Copiando o script de entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expondo a porta em que o servidor Django estará rodando
EXPOSE 8000

# Definindo o entrypoint
ENTRYPOINT ["/entrypoint.sh"]