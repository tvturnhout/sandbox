FROM tiangolo/uwsgi-nginx-flask
RUN apt-get update -y
RUN apt-get install -y python-pip 
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]