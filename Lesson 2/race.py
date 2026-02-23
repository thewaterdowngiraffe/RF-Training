import sys
import time
import os
from vehicles import car, motorcycle, plane
LINE_UP = '\033[F'    # Move cursor up one line
LINE_CLEAR = '\033[K'  # Clear from cursor to the end of the line

length = 50000

STR_OFFSET = 0

print("distance:", length, "meters\n\n\n")


class Color:
    R = '\033[91m'
    G = '\033[92m'
    B = '\033[94m'
    clr = '\033[0m'


def get_width():
    global STR_OFFSET
    # Get the terminal size as a named tuple (columns, lines)
    size = os.get_terminal_size()
    return size.columns-20 - STR_OFFSET


def racer(iter, speed, colour) -> tuple[str, bool]:
    space = ((iter*speed)/length)

    unit = get_width()
    # print(space)
    string = "="*int(unit*min(space, 1))

    finished = False
    if int(space) >= 1:
        finished = True
    if string == "":
        string = f"{colour}■{Color.clr}"
    else:
        string = string[:-1]+f"{colour}■{Color.clr}"
    string = string+"="*(get_width()-len(string)+9)
    return ("|"+string+"|", finished)


def overwrite_lines(lines_to_overwrite, new_line_text):
    # Move up the required number of lines
    for _ in range(lines_to_overwrite):
        sys.stdout.write(LINE_UP)
        sys.stdout.write(LINE_CLEAR)

    # Print the new, single line
    sys.stdout.write(new_line_text + '\n')
    sys.stdout.flush()


def race(*racers):
    global STR_OFFSET
    winner = False
    colours = [Color.R, Color.G, Color.B]
    iteration = 0
    finished = []

    STR_OFFSET = max([len(y.vehicle_type) for y in racers]) + 1
    finished_list = []
    while not winner:

        data = [racer(racers[i].get_speed(), iteration, colours[i])
                for i in range(len(racers))]
        iteration += 0.25
        strs, finished = zip(*data)
        winner = all(finished)
        strs = [racers[i].vehicle_type.center(STR_OFFSET, " ")+" "+strs[i]+f"{racers[i].speed:07.2f}"
                for i in range(len(racers))]
        # print(list(finished))
        for i in range(len(list(finished))):
            if finished[i] and racers[i].vehicle_type not in finished_list:
                finished_list.append(racers[i].vehicle_type)
                racers[i].done = True

        time.sleep(0.05)
        overwrite_lines(len(racers),  "\n".join(strs))

    for i in range(len(list(finished_list))):
        print(f"rank {i+1}:", finished_list[i], "\n\t", racers[i])

    # print("winner:", racers[finished.index(True)].vehicle_type)
