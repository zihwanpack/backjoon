function solution(participant, completion) {
    let answer = '';
    const participantMap = new Map();
    
    participant.forEach(man => {
        participantMap.get(man) ? participantMap.set(man, participantMap.get(man) + 1) : participantMap.set(man, 1);
    })
    
    completion.forEach(man => {
        participantMap.get(man) && participantMap.set(man, participantMap.get(man) - 1);
    })
    for (let man of participantMap) {
        const [name, count] = man;
        if (count === 1) answer += name;
    }
    
    return answer;
}