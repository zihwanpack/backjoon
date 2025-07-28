function solution(s){
    let count = 0;
    
    for (let str of s) {
        if (count === -1) return false
        str === '(' ? count++ : count--; 
    }
    
    return count === 0 ? true : false;
}