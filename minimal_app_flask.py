from flask import Flask, request, url_for, render_template
from utils import id_generator
app = Flask(__name__)

@app.route('/index')
@app.route('/index/<name>')
def index(name=None):
    return render_template('hello.html', name=name)

@app.route('/gen')
def generate():
    gen_len = request.args.get('len')
    return id_generator(size=gen_len)

@app.route('/user/<username>')
def show_user_profile(username):
    if username == 'ValikVasilkovskiy':
        return 'User: {} Profile: new user'.format(username)
    return 'User %s' % username
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)

@app.route('/login')
def login():
    return 'Login'

@app.route('/static')
def static_with_style():
    return url_for('static', filename='style.css')

with app.test_request_context():
    print(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
