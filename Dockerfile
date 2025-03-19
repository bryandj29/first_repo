FROM python:alpine3.21
WORKDIR /app
COPY app.py .
RUN pip install --upgrade pip
RUN pip install flask
CMD ["python","app.py"]