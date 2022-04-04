from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/')
def rgtuj():
    return 'Миссия Колонизация Марса'


@app.route('/promotion')
def rgtudthfbdfvfvdfvj():
    return 'Человечество вырастает из детства.<br>Человечеству мала одна планета.' \
           '<br>Мы сделаем обитаемыми безжизненные пока планеты.<br>И начнем с Марса!<br>Присоединяйся!'


@app.route('/image_mars')
def fwefwefwefwefwefwefwefwefwef():
    return '''<h1>Заголовок первого уровня</h1>
    <img src="https://cdn.vashurok.ru/system/news/images/000/006/582/og/kolonist.jpg?1620984458"><br> Вот она какая, красная планета!'''


@app.route('/promotion_image')
def promotion_image():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" href="style.css">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1 class="title">Жди нас марс</h1>
                    <img src="https://sun6-20.userapi.com/s/v1/ig2/qFa1Fc7Wd2mP_UHpG-XFY690gm-rNTgFQE2q_HACpfYvVOOxX_NvInxhPAd3J18tgZ_OVIufE4FiyHI5TEKKuwMQ.jpg?size=400x0&quality=96&crop=1,294,718,718&ava=1">
                    <p class="alert alert-primary">Человечество вырастает из детства.</p>
                    <p class="alert alert-primary">Человечеству мала одна планета.</p>
                    <p class="alert alert-primary">Мы сделаем обитаемыми безжизненные пока планеты.</p>
                    <p class="alert alert-primary">И начнем с Марса!</p>
                    <p class="alert alert-primary">Присоединяйся!</p>
                  </body>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <h1>Анкета претендента</h1>
                                <h3>На участие в миссии</h3>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                        <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у вас образование?</label>
                                            <select class="form-control" id="educationSurname" name="education">
                                              <option>начальное</option>
                                              <option>неполное среднее</option>
                                              <option>полное среднее</option>
                                              <option>неполное высшее</option>
                                              <option>высшее</option>
                                            </select>
                                         </div>
                                        <p>Какие у вас профессии?</p>
                                        <div class="form-group form-check">
                                            <input type="radio" class="form-check-input" id="acceptRules1" name="accept">
                                            <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                                         </div>
                                         <div class="form-group form-check">
                                            <input type="radio" class="form-check-input" id="acceptRules2" name="accept">
                                            <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
                                          </div>
                                          <div class="form-group form-check">
                                            <input type="radio" class="form-check-input" id="acceptRules3" name="accept">
                                            <label class="form-check-label" for="acceptRules">Пилот</label>
                                         </div>
                                         <div class="form-group form-check">
                                            <input type="radio" class="form-check-input" id="acceptRules4" name="accept">
                                            <label class="form-check-label" for="acceptRules">Метеоролог</label>
                                         </div>
                                         <div class="form-group form-check">
                                            <input type="radio" class="form-check-input" id="acceptRules5" name="accept">
                                            <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечению</label>
                                         </div>
                                         <div class="form-group form-check">
                                            <input type="radio" class="form-check-input" id="acceptRules6" name="accept">
                                            <label class="form-check-label" for="acceptRules">Инженер по радиационной защите</label>
                                         </div>
                                         <div class="form-group form-check">
                                            <input type="radio" class="form-check-input" id="acceptRules7" name="accept">
                                            <label class="form-check-label" for="acceptRules">Врач</label>
                                         </div>
                                         <div class="form-group form-check">
                                            <input type="radio" class="form-check-input" id="acceptRules8" name="accept">
                                            <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                         </div>
                                         <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <div class="form-group">
                                            <label for="about">Почему вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на марсе?</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')