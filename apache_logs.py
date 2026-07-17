import random
import time

ips = [
    "192.168.1.10",
    "10.0.0.2",
    "172.16.1.5"
]

status = [200, 404, 500]

pages = [
    "/",
    "/login",
    "/admin",
    "/dashboard",
    "/images/logo.png"
]

while True:

    log = '{} - - [17/Jul/2026:10:00:00] "GET {} HTTP/1.1" {} 512'.format(
        random.choice(ips),
        random.choice(pages),
        random.choice(status)
    )

    print(log)

    with open("apache.log","a") as f:
        f.write(log+"\n")

    time.sleep(1)
