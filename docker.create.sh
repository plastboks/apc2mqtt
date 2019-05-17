#!/bin/bash

docker create \
	--name=apc2mqtt \
	-e MQTT_HOST="localhost" \
	-e MQTT_USER="user" \
	-e MQTT_PASS="pass" \
	-e APC_HOST="localhost" \
	apc2mqtt
