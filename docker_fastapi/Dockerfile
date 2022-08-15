FROM python:3.9

WORKDIR /code

COPY ./requirments.txt /code/requirments.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirments.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "90"]