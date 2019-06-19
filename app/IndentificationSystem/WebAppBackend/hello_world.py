from flask import *

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('name')
        return redirect(url_for('success', name=user))


@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name=user)


if __name__ == '__main__':
    app.run('127.0.0.1', '5001', debug=True)
