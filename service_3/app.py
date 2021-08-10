from flask import Flask
import random

app = Flask(__name__)

@app.route('/get/damage')
def get_damage():
    return random.randint(5, 30)

if __name__ == '__main__':
    app.run(host='0.0.0.0')