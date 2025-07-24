function solution(participant, completion) {
    const answer = [];
    const sortedP = participant.sort();
    const sortedC = completion.sort();
    
    for (let i = 0; i < sortedP.length; i++) {
        if (sortedP[i] !== sortedC[i]) {
            answer.push(sortedC[i]);
        }
    }
    console.log(...answer);
    // return answer;
}