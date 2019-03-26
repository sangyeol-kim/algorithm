function solution(pobi, crong) {
  var answer = 0;
  let arr = [];

  for (i in pobi) {
    arr = [...(pobi[i] + "")].map(n => +n);
    console.log(arr[0]);

    console.log(arr);
  }

  return answer;
}

pobi = [97, 98];
crong = [197, 198];

solution(pobi, crong);

// let num = 12345;

// [...num+''] //["1", "2", "3", "4", "5"]

// [...num+''].map(n=>+n) //[1, 2, 3, 4, 5]
