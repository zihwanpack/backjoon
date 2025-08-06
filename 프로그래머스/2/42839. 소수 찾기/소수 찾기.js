function isPrime(number) {
    if (number < 2) return false;
    for (let i = 2; i * i <= number; i++) {
        if (number % i === 0) return false;
    }
    return true;
}

function getPermutation(arr, number) {
    let result = [];
    const visited = Array(arr.length).fill(false); 
    
    function dfs(current) {
        if (current.length === number) {
            result.push([...current]);
            return;
        }
        for (let i = 0; i < arr.length; i++) {
            if (!visited[i]) {
                visited[i] = true;
                current.push(arr[i]);
                dfs(current);
                current.pop();
                visited[i] = false;
            }
        }
    }

    dfs([]);
    return result;
}

function solution(numbers) {
    let answer = 0;
    const numberSet = new Set();
    const numArr = [...numbers];

    for (let i = 1; i <= numArr.length; i++) {
        const permutations = getPermutation(numArr, i);
        permutations.forEach(numArr => {
            const num = Number(numArr.join(''));
            numberSet.add(num);
        });
    }
    numberSet.forEach(num => {
        if (isPrime(num)) answer++;
    });

    return answer;
}