FROM python:3

ADD /apc2mqtt /apc2mqtt
ADD requirements.txt /

RUN pip install -r /requirements.txt

CMD [ "python", "-m", "apc2mqtt" ]