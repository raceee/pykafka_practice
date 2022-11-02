FROM python:3.7-alpine
RUN pwd
WORKDIR /
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 9092
COPY . .
CMD ["python", "./"]