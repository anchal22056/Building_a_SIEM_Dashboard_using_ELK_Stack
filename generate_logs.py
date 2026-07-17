import random
import time
from datetime import datetime

ips = [
    "192.168.1.10",
    "192.168.1.15",
    "192.168.1.20",
    "10.0.0.5",
    "172.16.0.8"
]

events = [
    "LOGIN_SUCCESS",
    "LOGIN_FAILED",
    "PORT_SCAN",
    "APACHE_ACCESS"
]

while True:
    ip = random.choice(ips)
    event = random.choice(events)

    log = f"{datetime.now()} {ip} {event}"

    with open("siem_logs.log", "a") as file:
        file.write(log + "\n")

    print(log)

    time.sleep(1)
