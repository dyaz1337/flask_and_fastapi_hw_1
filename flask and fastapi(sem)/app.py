from flask import Flask, render_template, request, redirect
from dataclasses import dataclass

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.post('/index/')
def redirect_url():
    print(request.form)
    x, y = request.form.get('x'), request.form.get('y')
    if x and y:
        return redirect(f'/task3/{x}/{y}')
    else:
        return redirect(f"/task4/{request.form['text']}/")


# Напишите простое веб-приложение на Flask, которое будет выводить на экран текст "Hello, World!".
@app.route('/task1/')
@app.route('/task1/index/')
def task1_index():
    return "Hello world"


# Добавьте две дополнительные страницы в ваше веб-приложение: страницу "about" и страницу "contact".
@app.route('/task2/about_me/')
def task2_about():
    return "About me"


@app.route('/task2/contact/')
def task2_contact():
    return "My contacts"


# Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму.
@app.route('/task3/<int:x>/<int:y>')
def task3_sum_numbers(x, y):
    return str(x + y)


# Написать функцию, которая будет принимать на вход строку и выводить на экран ее длину.
@app.route('/task4/<line>/')
def task4_length(line: str):
    return str(len(line))


# Написать функцию, которая будет выводить на экран HTML страницу с заголовком "Моя первая HTML страница"
# и абзацем "Привет, мир!".
@app.route('/task5/')
@app.route('/task5/index/')
def task5_index():
    return render_template('task5/index.html')


# Написать функцию, которая будет выводить на экран HTML страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через контекст.
@app.route('/task6/people/')
def task6_people():
    names = [{'name': 'IVAN', 'Lastname': 'IVANOV', 'age': 48},
             {'name': 'Fedor', 'Lastname': 'Vasiliev', 'age': 22}]
    return render_template('task6/people.html', names=names)


# Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через контекст.
@app.route('/task7/')
def task7_index():
    news = [('Indian police clear a suspected Chinese spy pigeon after 8 months in bird lockup.',
             'The pigeon’s ordeal began in May when it was captured near a port in Mumbai '
             'with two rings tied to its legs, carrying words that looked like Chinese.',
             '01.02.2024'),
            ('Surfer dog Efruz, a Jack Russell terrier, loves to ride the waves in Peru!',
             'Efruz is a 4-year-old Jack Russell terrier and '
             'he is a common sight these hot days of the Southern Hemisphere summer. '
             '"He loves the sea," his owner says.',
             '26.01.2024')]
    return render_template('task7/news.html', news=news)


# Создать базовый шаблон для всего сайта, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для каждой отдельной страницы.
# Например, создать страницу "О нас" и "Контакты", используя базовый шаблон.
@app.route('/task8/contacts/')
def task8_contacts():
    return render_template('task8/contacts.html')


@app.route('/task8/about_me/')
def task8_about_me():
    return render_template('task8/about_me.html')


# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон.
@dataclass
class Product:
    name: str
    price: float
    img_link: str


flowers = [Product('10 Pink Oriental Lilies', 43, 'img/flowers/flower1.jpg'),
           Product('12 White Roses', 46, 'img/flowers/flower2.jpg'),
           Product('Signature Box', 38, 'img/flowers/flower3.jpg'),
           Product('Purple and Pink Mixed Flowers', 49, 'img/flowers/flower4.jpg'),
           Product('5 Roses, 10 Daisies, 5 Astemaria', 49, 'img/flowers/flower5.jpg')]

toys = [Product("LUKE SKYWALKER'S LANDSPEEDER - UCS EDITION", 249.99, 'img/toys/toy1.jpg'),
        Product('CHEWBACCA', 249.99, 'img/toys/toy2.jpg')]

teas = [Product('Chocolate Orange - Black Tea', 5.99, 'img/teas/tea1.jpg'),
        Product('Strawberry Papaya - Green Tea', 6.99, 'img/teas/tea2.jpg'),
        Product('Blue Sapphire Afternoon - Black Tea', 4.99, 'img/teas/tea3.jpg')]


@app.route('/task9/')
@app.route('/task9/home/')
def task9_home():
    return render_template('task9/home.html')


@app.route('/task9/contact/')
def task9_contact():
    return render_template('task9/contact.html')


@app.route('/task9/about/')
def task9_about():
    return render_template('task9/about.html')


@app.route('/task9/products/flowers')
def task9_flowers():
    return render_template('task9/flowers.html', flowers=flowers, title='Flowers')


@app.route('/task9/products/toys')
def task9_toys():
    return render_template('task9/toys.html', toys=toys, title='Toys')


@app.route('/task9/products/teas')
def task9_teas():
    return render_template('task9/teas.html', teas=teas, title='Tea')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
