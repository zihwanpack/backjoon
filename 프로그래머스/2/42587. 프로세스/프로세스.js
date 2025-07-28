function isHigherPriority(queue, currentPriority) {
    return queue.some(process => process.priority > currentPriority);
}

function solution(priorities, location) {
    let answer = 0;
    const queue = priorities.map((priority, index) => ({ priority, index }));
    
    while (queue.length > 0) {
        const currentProcess = queue.shift();
        if (isHigherPriority(queue, currentProcess.priority)) {
            queue.push(currentProcess);
        } else {
            answer++;
            if (currentProcess.index === location) {
                return answer;
            }
        }
    }
}