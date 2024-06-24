from flask import Flask, render_template, request
from algorithm import astar as AStar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    return f'Test connect Flask'

if __name__ == '__main__':
    app.run(debug=True, port=8000)  # Chạy trên cổng 8000
