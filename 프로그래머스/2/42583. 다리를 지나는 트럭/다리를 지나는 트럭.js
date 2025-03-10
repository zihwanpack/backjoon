function solution(bridge_length, weight, truck_weights) {
    const bridge = Array.from({length : bridge_length}, _ => 0);
    let count = 0, curWeight = 0;
    
    while (truck_weights.length) {
        count++;
        curWeight -= bridge.shift();
        if (curWeight + truck_weights[0] > weight) {
            bridge.push(0);
        } else {
            const curTruck = truck_weights.shift();
            bridge.push(curTruck);
            curWeight += curTruck;
        }
    }
    return count + bridge_length;
}