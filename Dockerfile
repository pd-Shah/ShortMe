From python:3-slim-stretch
# RUN echo "curdir: " $PWD
ADD . /ShortMe
WORKDIR /ShortMe
# COPY . /APIProvider
RUN pip install --trusted-host pypi.python.org -r requirements.txt
ENV FLASK_APP=app
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
ENV FLASK_RUN_PORT=5000
# CMD flask run -h "0.0.0.0"
# CMD ["python", "./app.py"]