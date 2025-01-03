FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y \
    unixodbc-dev \
    curl \
    gnupg && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y \
    msodbcsql17 \
    mssql-tools && \
    apt-get clean

ENV PATH="${PATH}:/opt/mssql-tools/bin"

RUN pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]