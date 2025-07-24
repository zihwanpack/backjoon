function enter (map, participant) {
    for (let i = 0; i < participant.length; i++) {
        const man = participant[i];
        map.set(man, (map.get(man) || 0) + 1);
    }
    return map;
}

function checking (participantMap, completion) {
    for (let j = 0; j < completion.length; j++) {
        const completionMan = completion[j];
        participantMap.set(completionMan, participantMap.get(completionMan) - 1);
    }
    return participantMap;
}

function solution (participant, completion) {
    const map = new Map();
    const participantMap = enter(map, participant);
    const checkedMap = checking(participantMap, completion);
    for (let [man, isCompletion] of checkedMap) {
        if (isCompletion > 0) return man;
    }
}