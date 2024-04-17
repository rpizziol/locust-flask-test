FROM python:3.10

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY busy_waiting_webapp.py ./

EXPOSE 5001

CMD ["python", "busy_waiting_webapp.py"]

