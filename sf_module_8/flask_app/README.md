# Что в папке?

Пыталась пройти по шагам по вебинару [Михаила Чеснокова](https://github.com/mike-chesnokov/sf_webinar_ds_prod_template)

1. Обучение и сериализация модели, сериализация данных
2. Flask приложение
3. Flask приложение в docker контейнере
4. Flask + uwsgi приложение в docker контейнере
5. Flask + uwsgi приложение и nginx в двух разных контейнерах

С примером линейной регрессии все получилось.
Но при попытке запустить обучение в файле model_train.py, постоянно вываливалась ошибка -

tensorflow.python.framework.errors_impl.InvalidArgumentError: Node 'training/Adam/gradients/gradients/block14_sepconv2_bn/cond_grad/StatelessIf': Connecting to invalid output 3 of source node block14_sepconv2_bn/cond which has 3 outputs. 

Оставила пока папку с файлами для flask, может подскажите в какую сторону копать для ее решения и я доделаю прототип.
