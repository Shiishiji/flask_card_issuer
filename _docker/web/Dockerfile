FROM python:3.11

WORKDIR /usr/src/app

COPY requirements.web.txt ./
RUN pip install -r requirements.web.txt

COPY . .

ENV PYTHONPATH=/usr/src/app/app

CMD ["python", "main.py"]
