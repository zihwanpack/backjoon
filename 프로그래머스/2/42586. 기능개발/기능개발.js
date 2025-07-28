function makeDays(progresses, speeds) {
    const days = progresses.map((progress, i) => Math.ceil((100 - progress) / speeds[i]));
    return days;
}

function makeAnswer (days) {
    const answer = [];
    let standardDay = days[0];
    let count = 1;
    
    for (let i = 1; i < days.length; i++) {
        if (standardDay >= days[i]) {
            count++;
        } else {
            answer.push(count);
            count = 1;
            standardDay = days[i];
        }
    }
    
    answer.push(count);
    return answer;
}

function solution(progresses, speeds) {
    const days = makeDays(progresses, speeds);
    const answer = makeAnswer(days);   
    return answer;
}