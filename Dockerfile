FROM python:latest
COPY ./requirements.txt /local/requirements.txt
WORKDIR /local
RUN pip install -r requirements.txt
COPY . /local
CMD ["python", "app.py"]