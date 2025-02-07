import serial
from plot_race_line import plot_line

#Must be updated based on computer running program.
source = serial.Serial('/dev/ttyACM0', 9600, timeout = .1)

lapping = True
lines = list()

while lapping:
    data = source.readline()

    if data:
        lines.append(str(data))

print("Lap complete\nWriting logs...")
# Add processing logic to build csv based on output from telemetry

print("Logging complete\nCreating visualization...")

plot_line("lap.csv")