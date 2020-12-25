FROM python:latest

ARG APP_NAME=cosmological-constant
ENV APP_NAME=${APP_NAME}

WORKDIR /${APP_NAME}

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY src/ .
ENTRYPOINT ["python", "main.py"]