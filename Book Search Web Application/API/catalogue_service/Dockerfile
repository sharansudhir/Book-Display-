FROM python:latest

WORKDIR /usr/local/bin

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "catalogue_api.py"]