FROM python:3.12-slim

WORKDIR /source

COPY ./source /source/
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["/bin/bash"]

