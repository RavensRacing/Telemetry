import csv
import matplotlib.pyplot as plt

def plot_line(csv_path: str):

    with open(csv_path) as file:

        all_data = csv.DictReader(file)

        pos_x = list()
        pos_y = list()

        cur_pos_x = 0
        cur_pos_y = 0
        cur_time = 0

        for i in all_data:
            time = float(i['time'])
            vx = float(i['vx'])
            vy = float(i['vy'])

            delta_t = time - cur_time

            new_x = cur_pos_x + vx * delta_t
            new_y = cur_pos_y + vy * delta_t

            pos_x.append(new_x)
            pos_y.append(new_y)

            cur_time = time
            cur_pos_x = new_x
            cur_pos_y = new_y

        
        fig, ax = plt.subplots()
        ax.plot(pos_x, pos_y)
        plt.show()
