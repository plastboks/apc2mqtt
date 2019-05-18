"""
apc2mqtt.__main__
"""

import os
import time
import json

from apc2mqtt import apcaccess
from apc2mqtt import publish


def main():
    mhost = os.environ.get('MQTT_HOST', "localhost")
    muser = os.environ.get('MQTT_USER', "user")
    mpass = os.environ.get('MQTT_PASS', "passwd")
    mport = os.environ.get('MQTT_PORT', 1883)
    mpath = os.environ.get('MQTT_PATH', "ups")
    mfreq = os.environ.get('MQTT_FREQ', 60)

    uhost = os.environ.get('APC_HOST', "localhost")
    uport = os.environ.get('APC_PORT', 3551)

    client = publish.connect(muser, mpass, mhost, mport)

    while True:
        buffer = apcaccess.get(uhost, uport)
        d = apcaccess.parse(buffer, True)
        apcaccess.convert_values(d)
        publish.to_topic(client, "%s/%s/json" % (mpath, d['HOSTNAME']), json.dumps(d))
        time.sleep(mfreq)

        # for key, value in d.items():
        #     topic = "%s/%s/%s" % (mpath, d['HOSTNAME'], key.lower().replace(" ", "_"))
        #     publish.to_topic(client, topic, value)


if __name__ == "__main__":
    main()
