FROM python:3.9.10

WORKDIR /app

COPY app.py routers.py serializers.py swagger.py main.py requirements.txt ./

RUN python -m pip install --upgrade pip

RUN python -m pip install -r requirements.txt

CMD [ "python", "main.py" ]
