# https://school.programmers.co.kr/learn/courses/30/lessons/92341/

import math


def solution(fees, records):

    def time_to_min(time):
        hour = int(time[:2])
        min = int(time[3:])
        return hour*60 + min

    def calculate_fees(fees, time):
        default_time, default_fee, unit, fees_per_min = fees
        calculate_fees = default_fee + \
            math.ceil((time - default_time)/unit) * fees_per_min
        if calculate_fees < default_fee:
            return default_fee
        else:
            return calculate_fees

    answer = []
    parking = dict()

    TIME = 0
    CAR_NUMBER = 1
    TIME_LIMIT = 1439

    # 1. create dict by parking history
    for record in records:
        info = record.split(' ')
        if info[CAR_NUMBER] in parking:
            parking[info[CAR_NUMBER]].append(time_to_min(info[TIME]))
        else:
            parking[info[CAR_NUMBER]] = [time_to_min(info[TIME])]
    # print(1, parking)

    # 2. sort array with min car number
    car_number = list(parking.keys())
    car_number.sort()
    # print(2, car_number)

    # 3. calculate times and fees
    for car in car_number:
        parking_time = parking[car]
        entire_time = 0
        for idx in range(len(parking_time) - 1, -1, -2):
            if(len(parking_time) % 2 == 1):
                if idx == len(parking_time) - 1:
                    entire_time += TIME_LIMIT - parking_time[idx]
                else:
                    entire_time += parking_time[idx + 1] - parking_time[idx]
            else:
                entire_time += parking_time[idx] - parking_time[idx-1]
        # print(3, entire_time)
        # print(4, calculate_fees(fees, entire_time))
        answer.append(calculate_fees(fees, entire_time))
    return answer


solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
         "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
