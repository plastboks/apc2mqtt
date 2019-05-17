#!/bin/bash

docker run \
	--name=apc2mqtt \
	-e MQTT_HOST="localhost" \
	-e MQTT_USER="user" \
	-e MQTT_PASS="pass" \
	-e APC_HOST="localhost" \
	-i -t apc2mqtt
