function solution(k, tangerine) {
    let answer = 0;
    let count = {};

    // 개수 세기
    tangerine.forEach(guul => count[guul] ? count[guul]++ : count[guul] = 1);

    // 개수를 기준으로 내림차순 정렬
    const sortedCounts = Object.entries(count).sort((a, b) => b[1] - a[1]);

    let total = 0;
    for (let [, value] of sortedCounts) {
        if (total >= k) break;
        total += value;
        answer++;
    }

    return answer;
}