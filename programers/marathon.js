// 참가자 중 단 한 명의 선수를 제외하고는 모든 참가자가 마라톤을 완주

// 마라톤에 참가한 선수의 명단이 담긴 배열 participant와 안주한 선수들의 명단이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성.

function solution(participant, completion) {
  let answer = "";
  let count = 0;

  participant.sort();
  completion.sort();

  for (i in participant) {
    if (participant[i] === completion[count]) {
      count++;
    } else {
      answer = participant[i];
    }
  }
  return answer;
  // console.log(answer);
}

let allPeople = ["leo", "kiki", "eden"];

let comPeople = ["eden", "kiki"];

// solution(allPeople, comPeople);
