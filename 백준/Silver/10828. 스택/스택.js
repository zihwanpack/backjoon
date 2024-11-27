const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let N;
const stack = [];
let count = 0;
const output = [];

rl.on('line', (line) => {
    if (!N) {
        N = parseInt(line);
        return;
    }

    const [instruction, value] = line.split(' ');

    switch (instruction) {
        case 'push':
            stack.push(value);
            break;
        case 'pop':
            output.push(stack.length ? stack.pop() : -1);
            break;
        case 'top':
            output.push(stack.length ? stack[stack.length - 1] : -1);
            break;
        case 'size':
            output.push(stack.length);
            break;
        case 'empty':
            output.push(stack.length === 0 ? 1 : 0);
            break;
    }

    count++;
    if (count === N) {
        console.log(output.join('\n'));
        rl.close();
    }
});