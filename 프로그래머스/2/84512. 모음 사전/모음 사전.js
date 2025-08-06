function solution(word) {
    let answer = 0;
    let isFinish = false;
    const vowels = ['A', 'E', 'I', 'O', 'U'];
    
    function dfs (curStr) {
        if (curStr.length > 5 || isFinish) {
            return;
        }
        
        if (curStr === word) {
            isFinish = true;
            return;
        }
        answer += 1;
        for (let i = 0; i < vowels.length; i++) {
            dfs(curStr + vowels[i]);
        }
    }
    dfs('');
    return answer;
}