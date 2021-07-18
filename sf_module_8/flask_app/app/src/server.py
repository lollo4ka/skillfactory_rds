# Скрипт flask сервера для предикта
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

MODEL_FILE = '_webinar_model.pkl'
FEATURE_ORDER_FILE = '_feature_order.pkl'
TEST_DATA_FILE = '_test_data.pkl'

# Загружаем сериализованные объекты
# Обученная модель
# Лист с порядком признаков
# Признаки для тестового датасета


# ******** НИЖЕ НАПИШИТЕ КОД ЗАГРУЗКИ ТРЕХ СЕРИАЛИЗОВАННЫХ ОБЪЕКТОВ
# ........
with open(MODEL_FILE, 'rb') as inp:
    model = pickle.load(inp)

with open(TEST_DATA_FILE, 'rb') as inp:
    X_test = pickle.load(inp)

with open(FEATURE_ORDER_FILE, 'rb') as inp:
    feature_order = pickle.load(inp)

# ******** НИЖЕ НАПИШИТЕ КОД FLASK МЕТОДА ДЛЯ ПРОВЕРКИ РАБОТЫ СЕРВЕРА
# ........
@app.route('/hello', methods=['GET'])
def hello_chek():
    param = request.args.get('param')
    return jsonify({'param': param, 'result': 'SERVER OK'})

@app.route('/predict', methods=['GET'])
def predict():
    obj_id = request.args.get('obj_id')
    try:
        obj_id = int(obj_id)
        test_features = X_test[X_test['obj_id'] == obj_id][feature_order].values
        print(test_features)
        print(test_features.shape)
        res = model.predict(test_features)[0]
        return jsonify({'prediction': res,
                        'obj_id': obj_id,
                        'response_status': 'OK'})
    except:
        return jsonify({'prediction': -1,
                        'obj_id': obj_id,
                        'response_status': 'ERROR'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)
