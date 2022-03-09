from flask import render_template, request, Blueprint


main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
@main.route('/home', methods=['GET', 'POST'])
def home():
    """
    def landing page route using only domain or route in browser
    """
    return render_template('home.html', title='Home')
