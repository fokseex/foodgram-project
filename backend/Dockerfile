FROM python:3.8.10-slim
WORKDIR /code
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN python -m pip install --upgrade pip
COPY . .
CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000"]