FROM python:3.6-alpine

ADD . /code
WORKDIR /code
RUN pip install -r req.txt
CMD [ "python", "app.py" ]