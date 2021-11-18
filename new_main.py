import csv
import json
import os
import random
import sys

from modals.call import Call
from modals.building import Building
from modals.elevator import Elevator


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
TIME = 1
SRC_FLOOR = 2
DEST_FLOOR = 3
ELEVATOR_ID = 5

def find_fastest_elev(Elevators: list[Elevator]) -> int:
    id = 0
    fastest = Elevators[0].speed
    for i in range(1, len(Elevators)):
        if Elevators[i].speed > fastest:
            fastest = Elevators[i].speed
            id = Elevators[i].id
    return id

def Elevators_Update(Elev: list[Elevator])->list[Elevator]:
    for elev in Elev:
        if(elev.call_counter==int(elev.calls_n)):
            Elev.remove(elev)
    return Elev

if __name__ == '__main__':
    building_data = read_json(BUILDING)
    calls = read_csv(CALLS)
    speed_sum = 0
    # output = read_csv(OUTPUT)
    Elevators = []
    for e in building_data['_elevators']:
        elev = Elevator(e)
        Elevators.append(elev)
        speed_sum += elev.speed
    avg = len(calls) / speed_sum
    for el in Elevators:
        el.calls_num(avg)
    index = 0
    print(Elevators[6].calls_n)
    elel = Elevators.copy()
    for call in calls:
    #     if Elevators[6].call_counter==26:
    #         print("check")
        elel=Elevators_Update(elel).copy()
        for i in range(len(elel)):
            call[ELEVATOR_ID] = elel[i].id
            elel[i].call_counter += 1
            if i == len(elel)-1:
                i = 0
        #
        # if index >= len(elel):
        #     index=0
        # call[ELEVATOR_ID]=elel[index].id
        # elel[index].call_counter += 1
        # index+=1

    #     el = Elevators[index]
    #     while el.call_counter <= el.calls_n:
    #         call[5] = index
    #
    #     index += 1
    #
    # for elev in Elevators:
    #     for i in range(int(elev.calls_n)):
    #         calls[call_index][5] = elev.id
    #         call_index += 1
    #
    # for i in range(call_index, len(calls)):
    #     calls[i][5] = find_fastest_elev(Elevators)


    # for call in calls:
    #     if abs(call[SRC_FLOOR] - call[DEST_FLOOR]) < 0.5 * abs(
    #             int(building_data['_minFloor']) - int(building_data['_maxFloor'])):
    #         call[ELEVATOR_ID] = Elevators[len(Elevators) - 1].id
    #
    # print(Elevators[len(Elevators) - 1].id)
    # print(len(Elevators))
    # print(building_data['_elevators'][0]['_id'])
    #
    # # print(calls)
    # print(building_data['_minFloor'])
    for elev in elel:
        print(elev.call_counter)
    write_csv(OUTPUT, calls)
