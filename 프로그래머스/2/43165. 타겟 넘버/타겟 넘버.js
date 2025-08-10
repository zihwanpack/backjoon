function solution(numbers, target) {
    let answer = 0;
    let queue = [0];
    
    for (let number of numbers) {
        const tempQueue = [];
        for (let sum of queue) {
            tempQueue.push(sum + number);
            tempQueue.push(sum - number);
        }
        queue = tempQueue;
    }
    for (const sum of queue) {
        if (sum === target) {
        answer++;
        }
    }

    return answer;
}