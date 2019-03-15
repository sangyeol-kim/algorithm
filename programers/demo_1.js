// 세 점의 좌표가 주어지고, v가 매개변수로 주어졌을 때 나머지 한 점의 좌표를 구하라.
// 단, 직사각형의 각 변은 x축, y축에 평행하며, 반드시 직사각형을 만들 수 있는 경우만 입력으로 주어짐.

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
  return answer;
  // console.log(answer);
}

let arr = [[1, 1], [2, 2], [2, 1]];

// solution(arr);
