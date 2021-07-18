FROM python:3.8

WORKDIR /usr/app/

# копируем файл в контейнер и устанавливаем зависимости
COPY requirements.txt ./app_requirements/requirements.txt
RUN pip install --no-cache-dir -r ./app_requirements/requirements.txt

# копируем папку в контейнер
COPY src ./src
# обучаем модель, сериализуем объекты
RUN python ./src/model_train.py
# Запускаем Flask приложение через uwsgi
CMD uwsgi --http 0.0.0.0:8000 --wsgi-file ./src/server.py --callable app --processes 2 --master
