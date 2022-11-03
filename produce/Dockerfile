FROM python:3.7
RUN apt-get update && \
  apt-get install -y --no-install-recommends gcc git libssl-dev g++ make && \
  cd /tmp && git clone https://github.com/edenhill/librdkafka.git && \
  cd librdkafka && git checkout tags/v1.9.0 && \
  ./configure && make && make install && \
  cd ../ && rm -rf librdkafka
WORKDIR /
# RUN apt-get gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN python -m pip install --no-binary confluent-kafka confluent-kafka
RUN pip install Faker
EXPOSE 9092
COPY . .
CMD ["python", "./produce/producer.py"]