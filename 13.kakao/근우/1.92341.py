## https://school.programmers.co.kr/learn/courses/30/lessons/92341/
## 8:20

class Car:
    IN = 0
    OUT = 1
    LAST_TIME = 24*60 -1
    def __init__(self, init_time, fees):
        self._in(init_time)
        self.base_time, self.base_fee, self.unit_time, self.unit_cost = fees
        self.total_time = 0

    def out(self, cur_time):
        self.state = Car.OUT
        self.total_time += cur_time - self.in_time

    def _in(self, cur_time):
        self.state =Car.IN
        self.in_time = cur_time

    def calculate_total(self):
        if self.state == Car.IN:
            self.total_time += Car.LAST_TIME - self.in_time

        if self.total_time <= self.base_time:
            return self.base_fee

        if self.total_time > self.base_time:
            quotient, remainder = divmod(self.total_time - self.base_time, self.unit_time)
            if remainder != 0: # 올림 처리
                quotient +=1
            return self.base_fee + quotient * self.unit_cost

def solution(fees, records):
    car_info = dict()
    for record in records:
        time, car_num, state = record.split()
        # time : "XX:XX"
        time = int(time[:2])*60 + int(time[3:])
        if not car_num in car_info:
            car_info[car_num] = Car(time,fees)

        car = car_info[car_num]
        if state =='IN':
            car._in(time)
        if state == 'OUT':
            car.out(time)

    return [f[1] for f in sorted([[num, car.calculate_total()] for num, car in car_info.items()])]


print(solution(
    [180, 5000, 10, 600],
    ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
# print(solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
# print(solution([1, 461, 1, 10],["00:00 1234 IN"]))