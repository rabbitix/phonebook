FROM python:3.10

WORKDIR /app_code

COPY ./requirements.txt /app_code/requirements.txt

RUN pip install -r /app_code/requirements.txt

COPY ./phonebook /app_code/phonebook

CMD ["uvicorn", "phonebook.main:app","--host","0.0.0.0","--port","80"]