import csv
import json
import os.path
import sys

from modals.elevator import Elevator

TIME = 1
SRC_FLOOR = 2
DEST_FLOOR = 3
ELEVATOR_ID = 5


def read_csv(file: str):
    """
    Convert csv file to python list
    :param file: file name
    :return: list contains csv data
    """
    data = []
    with open(file, newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data


def write_csv(file: str, data: []):
    """
    Create new csv file which contains data
    :param file: file path
    :param data: list of data
    :return:
    """
    with open(file, 'w+', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)


def read_json(file: str):
    """
    Convert json file to python list
    :param file: file name
    :return: dict contains json data
    """
    with open(file) as json_file:
        data = json.load(json_file)
        return data


BUILDING = os.path.join('Ex1_Buildings', sys.argv[1])
CALLS = os.path.join('Ex1_Calls', sys.argv[2])
OUTPUT = 'output.csv'


def assign_call_to_elev(elevators: list[Elevator], c) -> int:
    index = 0
    lowest_time = elevators[0].call_time + elevators[0].time_for_call(c[SRC_FLOOR], c[DEST_FLOOR])
    for elev in elevators:
        is_lowest = elev.call_time + elev.time_for_call(c[SRC_FLOOR], c[DEST_FLOOR])
        if is_lowest < lowest_time:
            lowest_time = is_lowest
            index = elev.id
    return index


if __name__ == '__main__':
    building_data = read_json(BUILDING)
    calls = read_csv(CALLS)
    Elevators = []
    for e in building_data['_elevators']:
        elev = Elevator(e)
        Elevators.append(elev)

    for call in calls:
        call[ELEVATOR_ID] = assign_call_to_elev(Elevators, call)
        Elevators[call[ELEVATOR_ID]].call_time += Elevators[call[ELEVATOR_ID]].time_for_call(
            call[SRC_FLOOR], call[DEST_FLOOR])

    write_csv(OUTPUT, calls)
