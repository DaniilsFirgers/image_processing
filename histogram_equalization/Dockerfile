FROM python:3
WORKDIR /app
COPY . /app
COPY ./images /app/images
RUN pip install -r requirements.txt
CMD [ "python", "./main.py" ]