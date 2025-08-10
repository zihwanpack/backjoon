function solution(n, computers) {
    let answer = 0;
    const isVisited = Array(n).fill(false);
    
    
    for (let index = 0; index < n; index++) {
        if (!isVisited[index]) {
            answer++;
            dfs(index);
        }
    }
    
    function dfs (index) {
        isVisited[index] = true;
        for (let i = 0; i < n; i++) {
            const isConnected = computers[index][i] === 1 ? true : false;
            
            if (isConnected && !isVisited[i]) {
                dfs(i);
            }
        }
        
    }
    
    return answer;
}