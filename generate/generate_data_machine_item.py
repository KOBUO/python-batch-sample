# -*- coding: utf-8 -*-
import random
from enum import Enum
from typing import List
import pandas as pd

DATE_RANGE_START = '2018-01-01'
DATE_RANGE_END = '2018-12-31'
ITEM_NUM = 10
ITEM_PRICE = 1500
# SAMPLE_SIZE = 10000000
SAMPLE_SIZE = 1000000


class MachineType(Enum):
    BD = 1000
    BH = 1000


def generate_machine_id_master(machine_type: MachineType) -> List[str]:
    machine_num = machine_type.value
    machine_id_list = list(
        (f"{machine_type.name}{str(i).zfill(len(str(machine_num)))}" for i in range(1, machine_num + 1)))
    return machine_id_list


def generate_date_master(start_date: str, end_date: str) -> List[pd.Timestamp]:
    tmp_date_list = pd.date_range(start=start_date, end=end_date).tolist()
    date_list = [d.strftime('%Y-%m-%d') for d in tmp_date_list]
    return date_list


def generate_angle_master(angle_num: int) -> List[float]:
    angle_master = list({random.uniform(-90, 90) for _ in range(angle_num)})
    return angle_master


def generate_machine_item(machine_type: MachineType):
    machine_id_master = generate_machine_id_master(machine_type)
    date_master = generate_date_master(DATE_RANGE_START, DATE_RANGE_END)
    angle_master = generate_angle_master(ITEM_NUM)

    machine_id_list = []
    date_list = []
    angle_list = []
    for machine_id in machine_id_master:
        for date in date_master:
            machine_id_list.extend([machine_id] * ITEM_NUM)
            date_list.extend([date] * ITEM_NUM)
            angle_list.extend(angle_master)

    master = pd.DataFrame(
        data={
            'machine_id': machine_id_list,
            'date': date_list,
            'angle': angle_list
        },
        columns=['machine_id', 'date', 'angle']
    )
    data = master.sample(n=SAMPLE_SIZE, random_state=0, replace=True)
    return data


def main():
    try:
        data_bd = generate_machine_item(MachineType.BD)
        data_bh = generate_machine_item(MachineType.BH)
        data_bd.append(data_bh).to_csv(
            path_or_buf='./data/machine_item.csv',
            index=False,
            encoding='utf-8'
        )
    except Exception as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    main()
