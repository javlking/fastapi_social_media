FROM python:latest

WORKDIR /social_media

COPY . /social_media

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=5430"]