function solution(brown, yellow) {
    let sum = brown + yellow;
    
    for (let width = 3; width <= brown; width++) {
        if (sum % width === 0) {
            const height = sum / width;
            if ((height - 2) * (width - 2) === yellow) {
                return [height, width]
            }
        }
    }
    
}