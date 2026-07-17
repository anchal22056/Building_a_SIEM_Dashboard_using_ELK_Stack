import random
import time

users=["root","admin","ubuntu","test"]

ips=[
"192.168.1.2",
"10.0.0.3",
"172.16.0.5"
]

while True:

    success=random.choice([True,False])

    if success:

        log=f"Accepted password for {random.choice(users)} from {random.choice(ips)}"

    else:

        log=f"Failed password for {random.choice(users)} from {random.choice(ips)}"

    print(log)

    with open("ssh.log","a") as f:
        f.write(log+"\n")

    time.sleep(1)
