from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('main.html')


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
