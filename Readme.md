# Small app that communicates with kafka

<p>
This app is written with python, it uses flask to expose HTTP server. 
When a message is received it sends an event to kafka topic.
The reasoning behind it is that some other app would listen on that kafka topic.
When receiving such event it would for example start the production of physical card with chosen color.
</p>

## The flow
This app works with "card_ordered" topic on kafka. \
While POST /order_physical_card request is received it sends an event to that topic. \
Cron is using a consumer app that subscribes the topic and receives these events.

## About the environment
Kafka UI is working in browser on port 8080.\
Flask API is exposed on port 5000.

## Start web server & environment

```shell
docker compose up -d --build
```
 
It starts a flask http server that listens on port 5000. \
It starts kafka on port 9092 and kafka UI on port 8080. \
It builds and starts a cron container that consumes topic card_ordered.

Available endpoints are:
- POST /order_physical_card
> {
>   "name": "Damian", "color": "blue"
> }

ex. curl
```shell
curl --location 'http://localhost:5000/order_physical_card' --header 'Content-Type: application/json' --data '{"name": "Damian","color": "Blue"}'
```
