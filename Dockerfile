FROM python:3.9.0

WORKDIR /home/

RUN echo "lksmdofinasdf"

RUN git clone https://github.com/P-ws/Django-shoppingProject.git

WORKDIR /home/Django-shoppingProject/

RUN echo "SECRET_KEY=django-insecure-lus+u=xm628%tb$h&+uhgou^68hu6s98)i!8440kugsfjf@q9h" > .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "Shopping_Project.wsgi", "--bind", "0.0.0.0:8000"]
