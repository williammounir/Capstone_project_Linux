import random
import time
from datetime import datetime

while True:
    temp = random.uniform(20.0, 30.0)
    timestamp = datetime.now()

    print(f"time: {timestamp} - temp: {temp:.2f}")
    time.sleep(25)

