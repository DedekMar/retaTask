FROM python:latest
WORKDIR /loader
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python", "m", "loader"]