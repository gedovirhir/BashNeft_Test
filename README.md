# Клонировать репозиторий
git clone https://github.com/gedovirhir/BashNeft_Test

# Перейти в папку с проектом
cd ./BashNeft_Test

# Запуск докер сервиса
docker-compose build

docker-compose up -d

# REST Api сервис будет запущен на localhost:8000 (порт можно поменять в файле .env).

Тестирование и документация Api:

http://localhost:8000/api/doc

http://localhost:8000/api/redoc
