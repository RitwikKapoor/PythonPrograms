FROM python:3.9.16-bullseye

WORKDIR /poke-app

COPY ./myapp ./myapp

RUN pip install -r ./myapp/requirements.txt

CMD ["python3", "./myapp/poke.py"]

