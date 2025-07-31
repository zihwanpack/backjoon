function solution(sizes) {
    let maxRow = 0;
    let maxColumn = 0;
    
    for (let [row, column] of sizes) {
        const [big, small] = row > column ? [row, column] : [column, row];
        maxRow = Math.max(big, maxRow);
        maxColumn = Math.max(small, maxColumn);
        
        }
    return maxRow * maxColumn;
    }
    
