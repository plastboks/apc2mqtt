"""
apc2mqtt.__main__
"""

import argparse
import os
import time

from apc2mqtt import apcaccess
from apc2mqtt import publish


def main():
    """Get status from APC NIS and print output on stdout."""
    p = argparse.ArgumentParser()

    p.add_argument('--mhost', default=os.environ.get('MQTT_HOST', "localhost"))
    p.add_argument('--muser', default=os.environ.get('MQTT_USER', "user"))
    p.add_argument('--mpass', default=os.environ.get('MQTT_PASS', "passwd"))
    p.add_argument('--mport', type=int, default=os.environ.get('MQTT_PORT', 1883))
    p.add_argument('--mpath', default=os.environ.get('MQTT_PATH', "ups"))
    p.add_argument('--mfreq', type=int, default=os.environ.get('MQTT_FREQ', 60))
    p.add_argument("--uhost", default=os.environ.get('APC_HOST', "localhost"))
    p.add_argument("--uport", type=int, default=os.environ.get('APC_PORT', 3551))
    p.add_argument("--strip-units", action="store_true", default=True)
    args = p.parse_args()

    client = publish.connect(args.muser, args.mpass, args.mhost, args.mport)

    while True:
        buffer = apcaccess.get(args.uhost, args.uport)
        d = apcaccess.parse(buffer, args.strip_units)
        for key, value in d.items():
            topic = "%s/%s/%s" % (args.mpath, d['HOSTNAME'], key.lower().replace(" ", "_"))
            publish.to_topic(client, topic, value)
        time.sleep(args.mfreq)


if __name__ == "__main__":
    main()
