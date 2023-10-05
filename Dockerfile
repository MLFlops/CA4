
FROM python:3.8

WORKDIR /calc

COPY requirements.txt /calc
RUN pip install -r requirements.txt

COPY . /calc

ENV MYSQL_ROOT_PASSWORD bmsmlops123
ENV MYSQL_DATABASE Users

EXPOSE 5000

CMD ["python", "app.py"]

