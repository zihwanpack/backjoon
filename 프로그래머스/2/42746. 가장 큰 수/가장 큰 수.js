function solution(numbers) {
    let answer = numbers.map(number => String(number)).sort((a, b) => (b + a) - (a + b)).join('')
    return answer.at(0) === '0' ? '0' : answer;
}