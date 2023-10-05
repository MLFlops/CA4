FROM python:3.8

WORKDIR /calc

COPY requirements.txt /calc
RUN pip install -r requirements.txt

COPY . /calc

EXPOSE 5000

CMD ["python", "app.py"]