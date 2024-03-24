# Small http/cli app that communicates with kafka

<p>
This app is written with python, it uses flask to expose HTTP server. 
When a message is received it sends an event to kafka topic.
The reasoning behind it is that some other app would listen on that kafka topic.
When receiving such event it would for example start the production of physical card with chosen color.
</p>

## Start web server

```shell
cd app 
flask --app WebServer run
```
 
It starts a flask http server that listens on port 5000.

Available endpoints are:
- POST /order_physical_card
> {
>   "name": "Damian", "color": "blue"
> }

ex. curl
```shell
curl --location 'http://localhost:5000/order_physical_card' --header 'Content-Type: application/json' --data '{"name": "Damian","color": "Blue"}'
```

## Start dev environment

```shell
docker compose up
```

It runs kafka on port 9092 and kafka-UI on HTTP on port 8080

