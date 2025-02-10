import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
from geopy.distance import geodesic
import json

def load_track():
    with open("track_map_uoft.json") as file:
        data = dict(json.load(file))

        track_points = [[], []]

        inner = True

        for i in data['features']:
            for point in i['boundary']['coordinates']:
                if inner:
                    track_points[0].append(point)
                else:
                    track_points[1].append(point)

        return track_points


def write_laps(mylaps, lap_count):
    with open(f"lap {lap_count}.csv", "w+") as file:
        fieldnames = ["time", "lat", "long", "throttle"]
        lap_log = csv.DictWriter(file, fieldnames)
        lap_log.writeheader()
        lap_log.writerows(mylaps)    

def find_lap_times():
    # Adjust lap detection by ensuring a minimum separation between detections
    laps = []
    current_lap = []
    lap_count = 0
    away_from_start = False
    last_lap_time = -float("inf")  # Track the last lap's start time
    file_path = "sample_lap - UofT-GPS-velo.csv"  # Replace with your actual file path
    df = pd.read_csv(file_path)
    time_gap_threshold = 5  # Minimum time difference before counting a new lap

    lap_times = list()

    # Check the first recorded GPS position (potential start/finish line)
    start_lat, start_long = df.iloc[60]["lat"], df.iloc[60]["long"]

    # Compute the Euclidean distance from the start position for all points
    df["distance_from_start"] = np.sqrt((df["lat"] - start_lat)**2 + (df["long"] - start_long)**2)

    # Identify potential lap completions when the car returns near the start line
    lap_threshold = 0.0003  # A small threshold to consider "near" (adjustable)
    df["is_near_start"] = df["distance_from_start"] < lap_threshold

    # Display when the car returns near the start position

    mylaps = list()

    for _, row in df.iterrows():

        if _ == len(df) - 1:  # Check if it's the last row
            lap_times.append(row["time"] - last_lap_time)
            lap_count += 1
            write_laps(mylaps, lap_count)

        if row["is_near_start"]:
            if away_from_start and (row["time"] - last_lap_time > time_gap_threshold):
                lap_times.append(row["time"] - last_lap_time)

                if current_lap:
                    laps.append(pd.DataFrame(current_lap))  # Save the completed lap
                    lap_count += 1

                    write_laps(mylaps, lap_count)
                    mylaps = []

                current_lap = []  # Start a new lap segment
                last_lap_time = row["time"]  # Update last lap time
                away_from_start = False  # Reset flag
        else:
            away_from_start = True  # Car has moved away from start line

        current_lap.append(row)
        lap_data = {
            'time': row['time'],
            'lat': row['lat'],
            'long': row['long'],
            'throttle': row['throttle']
        }
        mylaps.append(lap_data)

    # Save the last lap if it exists
    if current_lap:
        laps.append(pd.DataFrame(current_lap))

    return [lap_count, lap_times]


def get_color(throttle_pos):
    if throttle_pos > 0:
        return (1, 0, 0, throttle_pos / 100)  # Red intensity based on throttle
    else:
        return (0.5, 0.5, 0.5, 1)  # Grey for coasting

def plot_lap(lap_data, lap_num):
    fig, ax = plt.subplots()

    for lap in range(len(lap_data) - 1):
        cur_x = float(lap_data[lap]['lat'])
        next_x = float(lap_data[lap]['long'])
        cur_y = float(lap_data[lap + 1]['lat'])
        next_y = float(lap_data[lap + 1]['long'])
        throttle_pos = float(lap_data[lap]['throttle'])

        ax.plot([cur_x, next_x], [cur_y, next_y], color = get_color(throttle_pos))

    plt.savefig(f"lap {lap_num}")
    plt.close()

def latlon_to_meters(lat, lon, lat_ref, lon_ref):
    """ Convert GPS coordinates to local meters using geopy. """
    east = geodesic((lat_ref, lon_ref), (lat_ref, lon)).meters  # Longitude distance
    north = geodesic((lat_ref, lon_ref), (lat, lon_ref)).meters  # Latitude distance
    if lon < lon_ref:
        east = -east  # Adjust for westward movement
    if lat < lat_ref:
        north = -north  # Adjust for southward movement
    return (east, north)

for i in range(find_lap_times()[0] + 1):

    lap_time = find_lap_times()[1][i - 1]

    if not i:
        continue

    with open(f"lap {i}.csv") as file:
        all_data = list(csv.DictReader(file))

        lat_ref = float(all_data[0]['lat'])
        long_ref = float(all_data[0]['long'])

        fig, ax = plt.subplots()

        for j in range(len(all_data) - 1):
        
            lat = float(all_data[j]['lat'])
            long = float(all_data[j]['long'])
            throttle_pos = float(all_data[j]['throttle'])

            meters = latlon_to_meters(lat, long, lat_ref, long_ref)
            cur_x = meters[0]
            cur_y = meters[1]

            lat_next = float(all_data[j + 1]['lat'])
            long_next = float(all_data[j + 1]['long'])

            meters = latlon_to_meters(lat_next, long_next, lat_ref, long_ref)
            next_x = meters[0]
            next_y = meters[1]

            ax.plot([cur_x, next_x], [cur_y, next_y], color=get_color(throttle_pos))

            ax.set_title(f"Lap Time: {lap_time}")
        
        track_points = load_track()

        for boundary in track_points:
            x_vals, y_vals = [], []

            for point in boundary:
                meters = latlon_to_meters(point[1], point[0], lat_ref, long_ref)  # GeoJSON uses lon, lat
                x_vals.append(meters[0])
                y_vals.append(meters[1])
    
            ax.plot(x_vals, y_vals, color="black")  # Ensure track is visible

        
        plt.savefig(f"lap {i}")