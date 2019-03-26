let arr = [10, 8, 4, 7, 8, 10, 2, 9, 7, 8, 12];
let n = arr.length;
let temp = 0;

let solution = arr => {
  for (let i = 0; i < n; i++) {
    let j = 1;
    if (arr[i] > arr[j]) {
      temp = arr[i];
      j++;
    } else {
      j++;
    }
  }
  console.log(temp);
};

solution(arr);
