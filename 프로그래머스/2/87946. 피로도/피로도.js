function solution(k, dungeons) {
    const visited = Array(dungeons.length).fill(false);
    let maxCount = 0; 
    function dfs(currentK, count) {
        maxCount = Math.max(maxCount, count);
        
        for (let i = 0; i < dungeons.length; i++) {
            const [need, use] = dungeons[i]
            if (!visited[i] && currentK >= need) {
                visited[i] = true;
                dfs(currentK - use, count + 1)
                visited[i] = false;
            }
        }
        
    }
    dfs (k, 0);
    return maxCount
    
}