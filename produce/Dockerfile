FROM python:3.9
RUN apt-get update && apt-get install -y --no-install-recommends gcc git libssl-dev g++ make && cd /tmp
RUN git clone https://github.com/edenhill/librdkafka && cd librdkafka && git checkout tags/v1.9.0
RUN cd librdkafka && ./configure && make && make install && ldconfig
RUN pip install confluent-kafka
RUN pip install Faker
EXPOSE 9092
COPY producer.py /
CMD ["python", "/producer.py"]