from flask import request, make_response, redirect, abort, render_template, session, url_for, flash
from forms import NameForm

from blueprints import blueprint as app_bp


@app_bp.route('/old_index', methods=['GET', 'POST'])
def index():
    name_form = NameForm()
    if name_form.validate_on_submit():
        name = name_form.name.data
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html', user_agent=user_agent, name=name, form=name_form)


@app_bp.route('/', methods=['GET', 'POST'])
def index_with_session_and_post_redirect():
    name_form = NameForm()
    if name_form.validate_on_submit():
        if name_form.name.data == 'stevo':
            flash('Enter another name, stevo is reserved.')
        session['name'] = name_form.name.data
        return redirect(url_for('.index_with_session_and_post_redirect'))
    return render_template('index.html', name=session.get('name'), form=name_form)


@app_bp.route('/cookie')
def route_with_cookie():
    response = make_response('response with cookie')
    response.set_cookie('moj cookie', 54)
    return response


@app_bp.route('/redirect_to_google')
def redirect_example():
    return redirect('http://www.google.com')


@app_bp.route('/abort')
def abort():
    return abort(404)


@app_bp.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

