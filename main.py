from flask import Flask, request, make_response, redirect, abort, render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html', user_agent=user_agent)


@app.route('/cookie')
def route_with_cookie():
    response = make_response('response with cookie')
    response.set_cookie('moj cookie', 54)
    return response


@app.route('/redirect_to_google')
def redirect():
    return redirect('http://www.google.com')


@app.route('/abort')
def abort():
    return abort(404)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    manager.run()