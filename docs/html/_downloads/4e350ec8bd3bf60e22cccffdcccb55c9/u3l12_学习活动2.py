#mPythonType:0
from educore import servo

import time
sv=servo(1)
sv.angle(180)
time.sleep(2)
sv.angle(0)