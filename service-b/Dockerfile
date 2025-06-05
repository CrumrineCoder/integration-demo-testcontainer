FROM python:3.13-slim
WORKDIR /app
COPY app.py .
RUN pip3 install flask requests
CMD ["python", "app.py"]