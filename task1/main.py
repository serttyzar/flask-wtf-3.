from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title.lower())


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof, it_img="{url_for('static', filename='img/it')}",
                           hc_img="{url_for('static', filename='img/hc')}")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')