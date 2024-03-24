import os

from flask import Flask, json, request
from pprint import pprint

from application import Application
from dto import OrderCardDto

flask_app = Flask(__name__)
application = Application()


@flask_app.route("/order_physical_card", methods=['POST'])
def order_card():
    try:
        data = json.loads(request.data)
        pprint(request.data)

        dto = OrderCardDto()
        dto.color = data['color']
        dto.name = data['name']
    except Exception as e:
        pprint(e)
        return {
            "status": "failure",
            "message": "Invalid input"
        }, 400

    try:
        application.order_physical_card(dto)
    except Exception:
        return {
            "status": "failure",
            "message": "Server error"
        }, 500

    message = "Ordered a new {} card for {}.".format(data['color'], data['name'])

    return {
        "status": "success",
        "message": message
    }, 200


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    # application.debug = True

    app_host = os.getenv("APP_HOST")
    app_port = os.getenv("APP_PORT")

    flask_app.run(host=app_host, port=app_port)
