# imports
import os
import pty
import sys
import time
import serial
import threading
# ======================================================================

SERIAL_BUAD_RATE = 115200 # this is for the sake of syntax correctness
                          # since we'll be using a virtual port, any
                          # baudrate will work. However, in practice 
                          # both sides should be configured identically.

if os.name == "nt":  # Windows
    print("[Error], this script only works on Mac and Linux")
    print("         Windoes support shall be implemeted later")
    print("         This is because of `pty` package support")
    print("")
    sys.exit(1)


# Create PTY
master_fd, slave_fd = pty.openpty()
slave_name = os.ttyname(slave_fd)

print("Connect to:", slave_name)

# Simulated device (runs in background)
def fake_device():
    while True:
        os.write(master_fd, b"device says hello\n")
        time.sleep(1)

threading.Thread(target=fake_device, daemon=True).start()

# Your "client" code using pyserial
ser = serial.Serial(slave_name, SERIAL_BUAD_RATE)

for _ in range(3):
    print(ser.readline().decode().strip())