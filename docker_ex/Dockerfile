FROM python:3.9-slim

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY api_3.py .

CMD ["python3", "api_3.py"]
