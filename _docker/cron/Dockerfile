FROM python:3.11

WORKDIR /usr/src/app

COPY requirements.cron.txt ./
RUN pip install -r requirements.cron.txt

COPY . .

ENV PYTHONPATH=/usr/src/app/app

CMD ["python", "cron.py"]
