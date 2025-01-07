function solution(progresses, speeds) {
    const answer = [];
    const array = [];
    let count = 0;
    
    
    for (let i = 0; i < progresses.length; i++) {
        const date = Math.ceil((100 - progresses[i]) / speeds[i]);
        array.push(date);
    }
    
    let maxDate = array[0];
    
    for (let j = 0; j < array.length; j++) {
        if (array[j] <= maxDate) {
            count++;
        } else {
            answer.push(count);
            count = 1;
            maxDate = array[j];
        }
    }
    answer.push(count);
    return answer;
}