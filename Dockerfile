FROM python:3.11
ADD mqtt_envir.py /
ADD requirements.txt /
RUN pip install -r requirements.txt

CMD [ "python3", "./mqtt_envir.py" ]
