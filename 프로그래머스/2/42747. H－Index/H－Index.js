function solution(citations) {
    let answer = 0;
    citations.sort((a, b) => b - a);
    citations.forEach((citation, i) => {
        if (citation > i) answer++;
    })
    return answer
    }