const fs = require('fs');

const input = fs
    .readFileSync("/dev/stdin", "utf8")
    .toString()
    .trim()
    .split('\n').map((i) => parseInt(i, 10));

const count = input[0];
const numbers = input.slice(1, input.length);

const zero = [1, 0];
const one = [0, 1];


for (let i = 0; i < count; i++) {
    for (let j = 2; j <= numbers[i]; j++) {
        zero[j] = zero[j - 1] + zero[j - 2];
        one[j] = one[j - 1] + one[j - 2];
    }

    console.log(`${zero[numbers[i]]} ${one[numbers[i]]}`);
}
