const fs = require('fs');

const input = fs
    .readFileSync("/dev/stdin", "utf8")
    .toString()
    .trim()
    .split('\n').map((i) => parseInt(i, 10));

const numbers = input.slice(1, input.length);

console.log([...new Set(numbers)].sort((a, b) => a - b).join('\n'));
