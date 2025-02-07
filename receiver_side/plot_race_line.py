import matplotlib.pyplot as plt
import csv

def find_position(cur_pos, velocity, delta_t):
    return cur_pos + velocity * delta_t  # Basic position update formula

def get_color(throttle_pos, brake_pos):
    if throttle_pos > 0:
        return (1, 0, 0, throttle_pos / 100)  # Red intensity based on throttle
    elif brake_pos > 0:
        return (0, 0, 1, brake_pos / 100)  # Blue intensity based on brake
    else:
        return (0.5, 0.5, 0.5, 1)  # Grey for coasting

def plot_line(csv_path: str):
    with open(csv_path, newline='') as file:
        all_data = list(csv.DictReader(file))  # Convert to list

    cur_pos_x = 0
    cur_pos_y = 0
    cur_time = 0

    fig, ax = plt.subplots()

    # Extract each of the datapoints from each time frame
    for i in range(len(all_data)):
        time = float(all_data[i]['time'])
        vx = float(all_data[i]['vx'])
        vy = float(all_data[i]['vy'])
        throttle_pos = float(all_data[i]['throttle_pos'])
        brake_pos = float(all_data[i]['brake_pos'])

        # Update time interval between time frames
        delta_t = time - cur_time
        cur_time = time

        # Compute the new position of the car
        new_x = find_position(cur_pos_x, vx, delta_t)
        new_y = find_position(cur_pos_y, vy, delta_t)

        # Determine line color based on pedal inputs
        color = get_color(throttle_pos, brake_pos)

        # Plot the new position of the car, apply relevant color for the time frame
        ax.plot([cur_pos_x, new_x], [cur_pos_y, new_y], color=color, linewidth=2)

        # Update position of the car
        cur_pos_x = new_x
        cur_pos_y = new_y

    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.title("Racing Line with Throttle/Brake Intensity")
    plt.show()

plot_line("sample_lap.csv")