import serial

source = serial.Serial('/dev/ttyACM0', 9600, timeout = .1)

lapping = True
lines = list()

while lapping:
    data = source.readline()

    if data:
        lines.append(str(data))

# Add processing logic to build csv based on output from telemetry