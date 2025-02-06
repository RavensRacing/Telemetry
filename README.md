# Telemetry
Source code for real time telemetry system for the RR25

File is broken down into receiver side code and transmitter side code. Transmitter side includes logic running on the microcontroller used to read CAN signals off the can and transmit
their data to the receiver. Receiver side code collects that data on another microcontroller and transmits it serially to a PC. The PC runs Python 3 to build lap representations
and data insights in real time.
