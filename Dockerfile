FROM python:3.6.3

ADD . .
RUN mkdir xmls

RUN pip install --verbose -r requirements.txt

CMD [ "python", "./watch_for_changes.py", "/xmls" ]