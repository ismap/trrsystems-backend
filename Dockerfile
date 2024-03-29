FROM python:3.10.10
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip install -r requirements.txt
EXPOSE 8001
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]