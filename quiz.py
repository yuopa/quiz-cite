# Здесь будет код веб-приложения
from flask import Flask, redirect, url_for, request, render_template
from random import randint, shuffle
from db_scripts import get_question, get_quises
import os 

last_id = 0
vict_id = 0

def show_quises_form():
    quizes = get_quises()
    print(len(quizes))
    return render_template('start.html', quizes=quizes)



def start():
    global vict_id

    if request.method == 'GET':
        return show_quises_form()
    else:
        # Получить ид викторины
        vict_id = request.form.get('vict')
        # перейти на страницу теста
        return redirect(url_for("test"))


def test():
    global last_id
    global vict_id

    q = get_question(last_id, vict_id)
    if q:
        last_id = q[0]

        return render_template('test.html', q=q)
    else:
        return redirect(url_for('result'))


def result():
    return '<h1>Спасибо за прохождение!</h1>'






folder = os.getcwd()
app = Flask(__name__, template_folder=folder, static_folder=folder)


app.add_url_rule('/', 'start', start, methods=['GET', 'POST']) # правило главной стр
app.add_url_rule('/test', 'test', test,  methods=['GET', 'POST']) # правило стр вопросов
app.add_url_rule('/result', 'result', result) # правило стр с результатом












if __name__ == "__main__":
    app.run()
