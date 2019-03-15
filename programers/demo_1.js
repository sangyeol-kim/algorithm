function solution(v) {
  let answer = [];

  for (let i = 0; i < v.length - 1; i++) {
    if (v[0][i] === v[1][i]) {
      answer[i] = v[2][i];
    } else if (v[1][i] === v[2][i]) {
      answer[i] = v[0][i];
    } else if (v[2][i] === v[0][i]) {
      answer[i] = v[1][i];
    }
  }

  console.log("Hello Javascript");

  console.log(answer);
}

let arr = [[1, 1], [2, 2], [2, 1]];

solution(arr);
