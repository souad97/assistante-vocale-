from subprocess import *
import time
Popen("python open_door.py")
time.sleep(3)
Popen("python detect_mask_video.py")