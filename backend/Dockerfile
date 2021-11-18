FROM python:3.9.7-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update
RUN apt-get install -y --no-install-recommends gcc libpq-dev python-dev
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

COPY . /usr/src/app/

EXPOSE 8000

ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod a+x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# ENTRYPOINT ["./wait_for_db.sh"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]