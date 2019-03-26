function solution(clothes) {
  let answer = 1;

  let myMap = new Map();

  for (i in clothes) {
    let key = clothes[i][1];
    if (!myMap.get(key)) myMap.set(key, 1);
    else myMap.set(key, myMap.get(key) + 1);
  }

  for (let value of myMap.values()) {
    answer *= value + 1;
  }

  console.log(answer - 1);
}

let clothes = [
  ["yellow_hat", "headgear"],
  ["blue_sunglasses", "eyewear"],
  ["green_turban, headgear"]
];
// [[crow_mask, face], [blue_sunglasses, face], [smoky_makeup, face]]	3

solution(clothes);
