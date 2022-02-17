from turtle import title
from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Дмитрий Купин',
        'title': 'Пост в блоге № 1',
        'content': 'Содержание 1_го поста',
        'date_posted': '17 02 2022'
    },
    {
        'author': 'Сергей Нечаев',
        'title': 'Пост в блоге № 2',
        'content': 'Содержание 2_го поста',
        'date_posted': '18 02 2022'
    },
    {
        'author': 'Евгений Егиоя',
        'title': 'Пост в блоге № 3',
        'content': 'Содержание 3_го поста',
        'date_posted': '19 02 2022'
    }

]


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title="О нас...")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
