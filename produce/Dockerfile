FROM python:3.9
RUN apt-get update && \
  apt-get install -y --no-install-recommends gcc git libssl-dev g++ make && \
  cd /tmp && git clone https://github.com/edenhill/librdkafka.git && \
  cd librdkafka && git checkout tags/v1.9.0 && \
  ./configure && make && make install && \
  cd ../ && rm -rf librdkafka
RUN python -m pip install --no-binary confluent-kafka confluent-kafka
RUN pip install Faker
EXPOSE 9092
COPY producer.py /
CMD ["python", "/producer.py"]