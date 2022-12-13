import time
import os

timestr = time.strftime("%Y%m%d")
print(timestr[-6:])

print(os.getenv("BROKER_URL"))
print(os.getenv("BROKER_PORT"))
print(os.getenv("BROKER_USER"))
print(os.getenv("BROKER_PASSWORD"))
