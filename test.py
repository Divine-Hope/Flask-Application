from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def welcome():
    return f"Nonsense: ip is {request.form.get('ip')}", 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
