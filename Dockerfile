FROM python:3.9-slim


WORKDIR /data

COPY . /data

RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Define environment variable
ENV AIPROXY_TOKEN=eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjI0ZjIwMDA4ODRAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.jmire3KggtFdRDagWXXzy0KT0XlyLpxqjPAbX6ZtjzM

CMD ["python", "api.py"]
