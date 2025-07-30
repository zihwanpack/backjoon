function solution(array, commands) {
    const answer = [];
    
    for (let command of commands) {
        const [first, end, targetIdx] = command;
        answer.push(array.slice(first - 1, end).sort((a, b) => a - b)[targetIdx - 1]);
    }
    
    return answer;
}