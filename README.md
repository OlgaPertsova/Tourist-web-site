# Tourist Web site

Учебный многостраничный сайт, выполненный в рамках дипломного проекта. Это туристический веб-сайт с информацией о городах, экскурсиях и турах. Есть возможность отправить заявку на участие в туре со стороны пользователя, заявки сохраняются в телеграмм-бот и в базу данных. Также есть возможность регистрации пользователей и редактирования личных аккаутов.

## Функции приложения index

    def index - выводит отфильтрованные данные из разных таблиц БД

## Функции приложения cities

    def cities - выводит весь список городов из БД в алфавитном порядке
    def city - выводит информацию из БД по id об одном городе на отдельной странице 

## Функции приложения events

    def events - выводит отфильтрованные данные из разных таблиц БД

## Функции приложения directions

    def directions - выводит все туры из БД, фильтрует по типу, пагинация 6 туров на 1 стр.
    def direction - выводит информацию из БД по id об одном туре на отдельной странице 
                    ReviewForm - форма для отзыва на тур
    def book_tour - отправляет заполненную заявку в телеграм-бот и БД
                    OrderForm - форма для заявки на тур

## Функции приложения users

    def login_user - авторизация пользователя
    def register_user - регистрация пользователя
    def logout_user - выход из аккаунта пользователя
    def profile - выводит информацию профиля вошедшего пользователя 
                    (применяется декоратор login_required)
    def profile_form - редактирование информации профиля пользователя
                        в форме ProfileForm
    class VerificationView - верификация аккаунта по почте
    def create_place - создание записи в днвник путешественика 
                        в форме TravelDiaryForm
    def travel_diary - выводит все созданные пользователем записи на отдельной стр.
    def place - выводит всю информацию из БД по id об одной записи на отдельной стр.
                + добавить больше фото в форме AddMorePhotoForm

## Функции приложения telegram

    sendmessage.py - def send_tg
        отправляет полученную информацию из формы OrderForm в телеграмм-бот


## Quickstart

Run the following commands to bootstrap your environment:

    sudo apt-get install -y git python-venv python-pip
    git clone 
    cd tourist-web-site

    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

    cp .env

Run the app locally:
    
    python manage.py runserver

Run the app docker:

    git clone 
    cd tourist-web-site
    docker build . --tag docker-tourist-web-site
    docker images
    docker run -p 8004:8001 image_id/image_tag
    