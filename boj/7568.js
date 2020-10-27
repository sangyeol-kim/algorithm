const fs = require('fs');

const input = fs
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split('\n');

const totalPerson = parseInt(input[0], 10);

const persons = input.slice(1, totalPerson + 1);

const ranks = new Array(totalPerson).fill(1);

for (let i = 0; i < totalPerson; i++) {
  const person = persons[i].split(' ').map((p) => parseInt(p, 10));
  for (let j = 0; j < totalPerson; j++) {
    const comparePerson = persons[j].split(' ').map((p) => parseInt(p, 10));
    if (i !== j) {
      if (person[0] < comparePerson[0] && person[1] < comparePerson[1]) {
        ranks[i] += 1;
      }
    }
  }
}

console.log(ranks.join(' '));
