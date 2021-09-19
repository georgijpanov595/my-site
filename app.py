from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    context = {
        'hello': 'Привет, меня зовут Георгий.',
        'title': 'Jinja2'
    }
    return render_template('index.html', **context)

@app.route('/blog/')
def blog():
    context = {
    'head': 'История о себе(Моя истрия начинается с родного города, где я родился)',
    'text': 'Я родился в городе',
    'text1': 'Этот город находится в',
    'text2': 'В этом году я закончил школу под названием',
    'text3': 'И в этом году поступаю в колледж под названием ItHub.',
    'text4': 'В городе',
    'text5': 'Этот колледж находится в столице Свердовсой облости.',
    }
    return render_template('blog.html', **context)

@app.route('/about/')
def about():
    context = {
    'hio': 'Сайт Сухого Лога и Свердловской области:',
    'hey': 'Группа вк  Свердловской области:',
    'hit': 'Телефон создателя:',
    'hir': 'Почта создателя сата: ',
    'title': 'Jinja2'
    }
    return render_template('about.html', **context)

if __name__ == '__main__':
    app.run()