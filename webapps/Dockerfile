FROM python:3.10

WORKDIR /app

COPY ../requirements.txt /app
RUN pip install -r requirements.txt

COPY microservice_is_prime.py ./

EXPOSE 5001

CMD ["python", "microservice_is_prime.py"]

