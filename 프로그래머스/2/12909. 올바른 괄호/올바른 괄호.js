function solution(s){
    let answer = true;
    const stack = [];
    
    for (let i = 0; i < s.length; i++) {
        (stack[stack.length - 1] === '(' && s[i] === ')') ? stack.pop() : stack.push(s[i]);
    }
    
    return stack.length ? false : true
}