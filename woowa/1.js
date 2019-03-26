// #include <stdio.h>

// int main()
// {
//     int money; //  입력 받은 수
//     int currency[7] = {10000,5000,1000,500,100,50,10}; //화폐단위 배열
//     int i,a[7],b; // a = 단위별매수 저장, b = 돈의 나머지

//     printf("<화폐 단위별로 화폐의 매수를 계산하는 프로그램입니다.> \n\n");

//     printf("금액을 입력해주세요 :");
//     scanf("%d",&money);

//     for(i=0;i<7;i++)
//     {
//         a[i] = money/currency[i]; //  매수
//         b = money%currency[i]; // 나머지를 구해서 매수를 제외
//         money = b; // 돈의 나머지를 다시 돈으로 바꿈
//         printf("%7d원 : %d매 \n",currency[i],a[i]);
//     }

//     return 0;
// }
// Colored by Color Scripter
// [출처] [C언어] 화폐 단위별로 화폐의 매수를 계산하는 프로그램|작성자 gktmdwls1346

function solution(money) {
  var answer = [];

  if (money / 50000 >= 1) {
    let a = parseInt(money / 50000); //5만원권
    money = money - 50000;
    console.log(a);
  } else if (money / 50000 < 1 && money / 10000 >= 1) {
    let b = parseInt(money / 10000); //1만원권
    money = money - 10000 * b;
    console.log(b);
  } else if (money / 10000 < 1 && money / 5000 >= 1) {
    let c = parseInt(money / 5000); //5천원권
    money = money - 5000;
  }
  if (money / 5000 < 1 && money / 1000 >= 1) {
    let d = parseInt(money / 1000); //1천원권
    money = money - 1000 * d;
  }
  if (money / 1000 < 1 && money / 500 >= 1) {
    let e = parseInt(money / 500); //5백원
    money = money - 500;
  }
  if (money / 500 < 1 && money / 100 >= 1) {
    let f = parseInt(money / 100); //백원
    money = money - 100 * f;
  }
  if (money / 100 < 1 && money / 50 >= 1) {
    let g = parseInt(money / 50); //50원
    money = money - 50;
  }
  if (money / 50 < 1 && money / 10 >= 1) {
    let h = parseInt(money / 10); // 10원
    money = money - 10 * h;
  }
  if (money / 10 < 1 && money / 1 >= 1) {
    let i = parseInt(money / 1);
  }
}

let money = 50237;

solution(money);

// [1, 0, 0, 0, 0, 2, 0, 3, 7]

// 오만 원권, 만 원권, 오천 원권, 천 원권, 오백원 동전, 백원 동전, 오십원 동전, 십원 동전, 일원 동전 각 몇 개로 변환
