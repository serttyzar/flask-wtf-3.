from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title.lower())


@app.route('/list_prof/<_type>')
def training(_type):
    return render_template('training.html', type=_type)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')