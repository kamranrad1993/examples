from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    print("++++++++++++++++++++++++++++++++++")
    print("1111111111111111111111111111111111")
    app.run(debug=False, host="0.0.0.0", port=5000)
