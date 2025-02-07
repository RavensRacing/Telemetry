import matplotlib.pyplot as plt
import csv
import geopy.distance
import math

def find_position(cur_pos, velocity, delta_t):
    return cur_pos + velocity * delta_t  # Basic position update formula

def get_color(throttle_pos):
    if throttle_pos > 0:
        return (1, 0, 0, throttle_pos / 100)  # Red intensity based on throttle
    else:
        return (0.5, 0.5, 0.5, 1)  # Grey for coasting

def plot_line(csv_path: str):
    with open(csv_path, newline='') as file:

        all_data = list(csv.DictReader(file))

        pos_lat = list()
        pos_long = list()

        fig, ax = plt.subplots()

        for i in range(len(all_data) - 1):
        
            lat = float(all_data[i]['lat'])
            long = float(all_data[i]['long'])
            throttle_pos = float(all_data[i]['throttle'])

            lat_next = float(all_data[i + 1]['lat'])
            long_next = float(all_data[i]['long'])

            ax.plot([lat, lat_next], [long, long_next], color=get_color(throttle_pos))

        plt.show()

plot_line("sample_lap - UofT-GPS-velo.csv")