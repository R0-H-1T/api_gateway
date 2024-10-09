from python:3.10

workdir /api_gateway

copy ./requirements.txt /api_gateway/requirements.txt

run pip install --no-cache-dir --upgrade  -r /api_gateway/requirements.txt

copy ./app /api_gateway/app

expose 80

cmd ["uvicorn", "app.main:app", "--port", "80", "--host", "0.0.0.0"]
