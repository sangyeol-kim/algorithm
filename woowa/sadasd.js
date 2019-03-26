// int main()
// {
//     int count;

//     scanf("%d", &count);    // 값을 입력받음

//     for (int i = 1; i <= count; i++)    // 1부터 증가하면서 count보다 작거나 같을 때까지 반복
//     {
//         if (i % 2 != 0)                 // i를 2로 나누었을 때 나머지가 0이 아니면 홀수
//             continue;                   // 아래 코드를 실행하지 않고 건너뜀

//         printf("%d\n", i);
//     }

//     return 0;
// }

let solution = arr => {
  let a = arr[0];
  let b = arr[1];
  let evenSumA = 0;
  let oddSumA = 0;
  let evenMultiA = 1;
  let oddMultiA = 1;
  let resultA = 0;
  let resultArr = [];

  let evenSumB = 0;
  let oddSumB = 0;
  let evenMultiB = 1;
  let oddMultiB = 1;
  let = resultB = 0;
  let resultArr2 = [];

  for (let i = 2; i <= a; i++) {
    if (i % 2 == 0) {
      //짝수
      oddSumA = oddSumA + i;
      oddMultiA *= i;
    }
    if (i % 2 != 0) {
      evenSumA += i;
      evenMultiA *= i;
    }
  }

  resultArr.push(evenSumA, oddSumA, evenMultiA, oddMultiA);
  resultA = Math.max.apply(null, resultArr); // 최대값

  console.log(resultA);




  for (let i = 2; i <= b; i++) {
    if (i % 2 == 0) {
      //짝수
      oddSumB = oddSumB + i;
      oddMultiB *= i;
    }
    if (i % 2 != 0) {
      evenSumB += i;
      evenMultiB *= i;
    }
  }

  resultArr2.push(evenSumB, oddSumB, evenMultiB, oddMultiB);
  resultB = Math.max.apply(null, resultArr2); // 최대값
  
    console.log(resultB);
};

let arr = [10, 30];

solution(arr);
