FROM python:alpine3.18

WORKDIR /app

COPY . .

RUN python3 -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r requirements.txt

CMD /venv/bin/python manage.py migrate && \
  /venv/bin/python manage.py runserver 0.0.0.0:8000