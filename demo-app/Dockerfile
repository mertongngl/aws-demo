FROM python:3.7-stretch
ADD . /home/test
WORKDIR /home/test
RUN pip install -r requirements.txt
RUN export FLASK_APP=app.py
ENTRYPOINT [ "python", "app.py" ]