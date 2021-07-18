FROM python:3.8

WORKDIR /usr/app/

# Копируем файл requirements.txt в контейнер и установим python зависимости
# копируем папку src в контейнер
# Обучаем модель, сериализуем объекты запуском скрипта model_train.py


# ******** НИЖЕ НАПИШИТЕ КОД ВЫПОЛНЯЮЩИЙ 3 ДЕЙСТВИЯ ОПИСАННЫЕ ВЫШЕ
# копируем файл в контейнер и устанавливаем зависимости
COPY requirements.txt ./app_requirements/requirements.txt
RUN pip install --no-cache-dir -r ./app_requirements/requirements.txt

# копируем папку в контейнер
COPY src ./src
# обучаем модель, сериализуем объекты
RUN python ./src/model_train.py
# Запускаем Flask приложение через uwsgi
CMD uwsgi --http 0.0.0.0:8000 --wsgi-file ./src/server.py --callable app --processes 2 --master
