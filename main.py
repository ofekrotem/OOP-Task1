import csv
import json
import os.path
import sys

from modals.building import Building
from modals.call import Call
from modals.elevator import Elevator

from typing import List


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


# def Who_Less_Busy(call:Call, elevList:[]):
#     numCalls = elevList[0].Calls
#     distI = 0
#
#
# def allocate_elevator(call:Call):
#     if(len(building.elevators)==1):
#         building.elevators[0].calls.append(call)
#         return 0
#
#     elevUp=[]
#     elevDown=[]
#     if len(building.elevators) % 2 ==0 :
#         for el in range(len(building.elevators)/2):
#             elevUp.append(el)
#         for el in range((len(building.elevators)/2),len(building.elevators)):
#             elevDown.append(el)
#         if (call.src > call.dest):
#             Who_Is_Closest(call,elevDown)
#         else:
#             Who_Is_Closest(call,elevUp)
#
#
#
#
#
#
#
#
#
#
#     Available_Elevators =[]
#     for el in building.elevators:
#         if(len(calls)==0):
#             Available_Elevators.append(el)
#
#     if (len(Available_Elevators==1)):
#         building.elevators[Available_Elevators[0].id].append(call)
#         return Available_Elevators[0].id
#     elif(len(Available_Elevators==0)):
#         index = Who_Is_Closest(call)
#         building.elevators[index].append(call)
#         return index
#     else:
def find_similar_calls(call: Call, callList: List[Call]) -> List[Call]:
    calls_to_assign = []
    time_for_call = ((abs(call.src - call.dest)) / building.elevators[call.elevator_id].speed)
    if call.type == 1:
        for c in callList:
            if c.time < call.time:
                pass
            if c.time >= (call.time + time_for_call):
                break
            if c.type == 1:
                if c.src > call.src:
                    calls_to_assign.append(c)
    elif call.type == -1:
        for c in callList:
            if c.time < call.time:
                pass
            if c.time > (call.time + time_for_call):
                break
            if c.type == -1:
                if c.src <= call.src:
                    calls_to_assign.append(c)
    if len(calls_to_assign > 0):
        return calls_to_assign
    else:
        return -1


def find_close_elevator(dest: int, elevators: List[Elevator]) -> Elevator:
    """
    Find the closet elevator to the destination between all
    :param dest: destination floor
    :param elevators: list of elevators
    :return: id of the chosen elevator
    """
    elevator = elevators[0]
    prev_distance = abs(dest - elevator.currPosition)

    for elev in elevators:
        distance = abs(dest - elev.currPosition)
        if distance < prev_distance:
            elevator = elev

    return elevator


BUILDING = os.path.join('Ex1_Buildings', sys.argv[1])
CALLS = os.path.join('Ex1_Calls', sys.argv[2])
OUTPUT = 'output.csv'

if __name__ == '__main__':
    building_data = read_json(BUILDING)
    calls = read_csv(CALLS)
    # output = read_csv(OUTPUT)
    building = Building(building_data)

    TIME = 1
    SRC_FLOOR = 2
    DEST_FLOOR = 3
    ELEVATOR_ID = 5

    for call in calls:
        if call[ELEVATOR_ID] == -1:
            src_floor = int(call[SRC_FLOOR])
            dest_floor = int(call[DEST_FLOOR])
            elev = find_close_elevator(src_floor, building.elevators)
            elev.currPosition = dest_floor
            call[ELEVATOR_ID] = elev.id
            # res = find_similar_calls(call, calls)
            # if res != -1:
            #     for c in res:
            #         c[ELEVATOR_ID] = elev.id



    write_csv(OUTPUT, calls)
