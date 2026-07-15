# 트럭은 1초에 다리 길이 1씩 전진한다.
# 트럭은 올라갈수 있으면 1초에 한 대씩 다리에 올라갈 수 있다.
from collections import deque

def solution(bridge_length, weight, truck_weights):
    # time이다
    answer = 0
    truck_weight = 0
    # 대기 트럭과 동일
    waiting_trucks = deque(truck_weights)
    # 다리
    bridge = deque([0] * bridge_length)
    bridge_weight = 0
    
    while waiting_trucks or bridge_weight > 0:
        answer += 1
        # 다리에서 트럭 내리기
        out_truck = bridge.popleft()
        bridge_weight -= out_truck
        # 대기 트럭에서 다리로 트럭 올리기
        if waiting_trucks:
            # 무게 제한 검사
            if waiting_trucks[0] + bridge_weight <= weight:
                in_truck = waiting_trucks.popleft()
                bridge.append(in_truck)
                bridge_weight += in_truck
            else:
                bridge.append(0)
    return answer