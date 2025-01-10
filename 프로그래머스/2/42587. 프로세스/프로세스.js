function solution(priorities, location) {
    let answer = 0;
    const indexArr = priorities.map((_, index) => index);
    
    while (priorities.length !== 0) {
        const priority = priorities.shift()
        const index = indexArr.shift()
        const maxPriority = Math.max(...priorities);
        
        if (maxPriority > priority) {
            priorities.push(priority);
            indexArr.push(index);
        } else {
            answer++;
            if (index === location) return answer;
        }
    }
    return answer;
}