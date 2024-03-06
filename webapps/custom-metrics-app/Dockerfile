FROM python:3.10

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY custom-metrics-app.py ./

EXPOSE 5001

CMD ["python", "custom-metrics-app.py"]

