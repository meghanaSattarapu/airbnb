from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hotel1')
def hotel1():
    return render_template('hotel1.html')

@app.route('/hotel2')
def hotel2():
    return render_template('hotel2.html')

@app.route('/hotel3')
def hotel3():
    return render_template('hotel3.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)