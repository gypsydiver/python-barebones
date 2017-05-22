from flask import Flask

app = Flask(__name__)

@app.route('/hello/hell')
def hello_world():
    return 'Hell-o World!'

if __name__ == '__main__':
    app.run()
