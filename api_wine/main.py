import os
import pickle
from flask_cors import CORS
from flask import Flask, request
from pandas import json_normalize
from clickhouse_connect import get_client

app: Flask = Flask(__name__)
CORS(app)


def parse_data(query):
    result = {}
    for row in query:
        result[row[5].strftime("%Y-%m-%d")] = {
            "temperature": row[6] or None,
            "airHumidity": row[7] or None,
            "windSpeed": row[8] or None,
            "precipitation": row[9] or None,
            "fixed_acidity": row[10] or None,
            "volatile_acidity": row[11] or None,
            "citric_acid": row[12] or None,
            "residual_sugar": row[13] or None,
            "chlorides": row[14] or None,
            "free_sulfur_dioxide": row[15] or None,
            "total_sulfur_dioxide": row[16] or None,
            "density": row[17] or None,
            "pH": row[18] or None,
            "sulphates": row[19] or None,
            "alcohol": row[20] or None,
            "winecolor": row[21] or None
        }

    return result


def impute_color(x):
    return 0 if x == 'white' else 1


@app.post("/predict")
def get_house_prediction_price():
    response = request.json
    dataset = json_normalize(response)
    dataset['winecolor'] = dataset['winecolor'].apply(impute_color)
    model_file = f"{os.environ['PATH_PREDICTION_DOCKER']}/model_prediction_quality_wine.sav"
    loaded_model = pickle.load(open(model_file, 'rb'))
    return {"data": str(round(loaded_model.predict(dataset)[0], 2))}


@app.post("/map")
def get_data_map():
    response = request.json
    client = get_client(host=os.getenv('CLICKHOUSE_HOST'), database=os.getenv('CLICKHOUSE_DB'),
                        username=os.getenv('CLICKHOUSE_USER'), password=os.getenv('CLICKHOUSE_PASSWORD'))
    query = client.query(
        f"SELECT * FROM wine_map WHERE id='{response['id']}'").result_rows
    return parse_data(query)


@app.post("/last_date")
def get_last_data_map():
    response = request.json
    client = get_client(host=os.getenv('CLICKHOUSE_HOST'), database=os.getenv('CLICKHOUSE_DB'),
                        username=os.getenv('CLICKHOUSE_USER'), password=os.getenv('CLICKHOUSE_PASSWORD'))
    query = client.query(
        f"SELECT * FROM wine_map WHERE id='{response['id']}' and date=(SELECT MAX(date) FROM wine_map "
        f"WHERE id='{response['id']}')").result_rows
    return parse_data(query)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
