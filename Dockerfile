FROM python:alpine3.18

WORKDIR /app

COPY . .

RUN python3 -m venv /venv

ENV PATH="/venv/bin:$PATH"

RUN pip install --upgrade pip && \
  pip install -r requirements.txt

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000