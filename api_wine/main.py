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
        vineyard_name = row[0]
        coordinates = [[float(row[1]), float(row[2])], [float(row[3]), float(row[4])]]

        if vineyard_name not in result:
            result[vineyard_name] = {
                "coordinates": coordinates,
                "history": {}
            }

        result[vineyard_name]["history"][row[5].strftime("%Y-%m-%d")] = {
            "temperature": row[6],
            "airHumidity": row[7],
            "windSpeed": row[8],
            "precipitation": row[9]
        }

    return result


@app.post("/")
def get_house_prediction_price():
    response = request.json
    dataset = json_normalize(response)
    model_file = "model_prediction_quality_wine.sav"
    loaded_model = pickle.load(open(model_file, 'rb'))
    return loaded_model.predict(dataset)[0]


@app.post("/map")
def get_data_map():
    response = request.json
    client = get_client(host=os.getenv('CLICKHOUSE_HOST'), database=os.getenv('CLICKHOUSE_DB'),
                        username=os.getenv('CLICKHOUSE_USER'), password=os.getenv('CLICKHOUSE_PASSWORD'))
    query = client.query(
        f"SELECT * FROM wine_map WHERE id='{response['id']}'").result_rows
    return parse_data(query)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
