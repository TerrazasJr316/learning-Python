"""
Ha un reloj que se actualiza cada segundo
"""

import time
import os

while True:
    hora = time.strftime("%H:%M:%S")
    os.system("")
    print(hora)
    time.sleep(1)