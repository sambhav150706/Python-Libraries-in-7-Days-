import os
import sys
import math
import random
from datetime import datetime

# OS
print("Current Directory:", os.getcwd())

# SYS
print("Python Version:", sys.version)

# MATH
print("Square Root:", math.sqrt(25))

# RANDOM
print("OTP:", random.randint(1000, 9999))

# DATETIME
now = datetime.now()
print("Today:", now.strftime("%d-%m-%Y"))
