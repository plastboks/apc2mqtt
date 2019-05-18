"""
apc2mqtt.mqtt

Contains functions to publish apcaccess info to mqtt
"""

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


def connect(user, password, host, port):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(user, password=password)
    client.connect(host, port, 60)
    return client


def to_topic(client, topic, payload):
    client.publish(topic, payload)

