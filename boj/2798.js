const fs = require('fs');

const input = fs
  .readFileSync("/dev/stdin", "utf8")
  .trim()
  .split('\n');

const cardCount = parseInt(input[0].split(' ')[0], 10);
const targetNumber = parseInt(input[0].split(' ')[1], 10);
const sortedSpreadCard = input[1].split(' ').sort().map((cardNumber) => parseInt(cardNumber, 10));

let result = 0;

for (let i = 0; i < cardCount; i++) {
  for (let j = 1; j < cardCount; j++) {
    for (let k = 2; k < cardCount; k++) {
      if ([...new Set([sortedSpreadCard[i], sortedSpreadCard[j], sortedSpreadCard[k]])].length === 3) {
        const totalCard = sortedSpreadCard[i] + sortedSpreadCard[j] + sortedSpreadCard[k];

        if (totalCard <= targetNumber && totalCard > result) {
          result = totalCard;
        }
      }
    }
  }
}

console.log(result);
