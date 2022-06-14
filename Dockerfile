FROM python:3.10.2-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /pythoncrud

RUN pip install requests==2.27.1 Django==4.0.5 django-cors-headers==3.13.0 djangorestframework==3.13.1 djongo==1.3.5 pymongo==3.12.3 python-dotenv==0.20.0 dnspython==2.2.1 django-bootstrap-form==3.4


COPY . /pythoncrud/

RUN python manage.py runserver