const fs = require('fs');

const input = fs
  .readFileSync("/dev/stdin", "utf8")
  .trim();

const number = parseInt(input, 10);

if (number === 1) {
  console.log(666);
  return;
}

let seriesSequence = 1;

let defaultNumber = 667;

while (true) {
  const stringValue = defaultNumber.toString();

  if (stringValue.includes('666')) {
    seriesSequence++;
    if (seriesSequence === number) {
      console.log(defaultNumber);
      return;
    }
  }

  defaultNumber++;
}
