from flask import Flask, render_template

app = Flask(__name__)

forms = [
    {
        'name': 'Sergio',
        'email': 'sergiovera@whatever.com',
        'password': 'funkified',
        'confirm': 'funkified'
    },

    {
        'name': 'Yared',
        'email': 'yaredtorres@whatever.com',
        'password': 'partychu',
        'confirm': 'partychu'
    }
]

'''
numbers = [
    {
        'nmbr': [1, 2]
    }
]
'''

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', forms=forms, title='Artist')


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
