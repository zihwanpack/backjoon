function solution(bridge_length, weight, truck_weights) {
    let answer = 0;
    let sumOfWeight = 0;
    // queue 만들기
    const queue = Array(bridge_length).fill(0);
    
    while (truck_weights.length > 0 || sumOfWeight > 0) {
        answer++;
        const left = queue.shift();
        sumOfWeight -= left;
        if (truck_weights.length > 0 && sumOfWeight + truck_weights[0] <= weight) {
            const truck = truck_weights.shift();
            sumOfWeight += truck;
            queue.push(truck);
        } else {
            queue.push(0);
        }
        
    }
    return answer;
}