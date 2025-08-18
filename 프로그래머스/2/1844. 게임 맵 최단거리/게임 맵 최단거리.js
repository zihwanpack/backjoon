function solution(maps) {
    const N = maps.length;
    const M = maps[0].length;
    // 상하좌우
    const moveX = [-1, 1, 0, 0];
    const moveY = [0, 0, -1, 1];
    
    const visited = Array(N).fill().map(e => Array(M).fill(0));
    visited[0][0] = 1;
    const queue = [[0, 0]];
    
    
    while (queue.length > 0) {
        const [X, Y] = queue.shift();
        
        
        if (X === N - 1 && Y === M - 1) {
            return visited[X][Y];
        }
        for (let i = 0; i < moveX.length; i++) {
            const nextX = X + moveX[i];
            const nextY = Y + moveY[i];
            if (nextX >= 0 && nextX < N && nextY >= 0 && nextY < M && maps[nextX][nextY] === 1 && visited[nextX][nextY] === 0) {
                visited[nextX][nextY] = visited[X][Y] + 1;
                queue.push([nextX, nextY]); 
            }
        }
    }
    
    return -1;
}