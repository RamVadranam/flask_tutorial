from flask_swagger_ui import get_swaggerui_blueprint
from flask import request, jsonify

from flask import Flask

app = Flask(__name__)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###


numbers_to_add = []


@app.route('/total', methods=['GET'])
def get_numbers():
    try:
        if len(numbers_to_add) > 0:
            return jsonify(sum(numbers_to_add))
        else:
            return jsonify(error="Not Found"), 404
    except Exception as error:
        return jsonify(error=str(error)), 500


@app.route('/total/<number>', methods=['POST'])
def add_numbers(number):
    try:
        numbers_to_add.append(int(number))
        return jsonify(sum(numbers_to_add)), 201
    except Exception as error:
        return jsonify(error=str(error)), 400


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
