FROM python:3.13-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1
RUN pip install --no-cache-dir requests>=2.32.0 cryptography>=46.0.0
COPY bootstrap.py /app/bootstrap.py
COPY payload_00.txt /app/payload_00.txt
COPY payload_01.txt /app/payload_01.txt
COPY payload_02.txt /app/payload_02.txt
COPY payload_03.txt /app/payload_03.txt
EXPOSE 8080
CMD ["python","/app/bootstrap.py"]
