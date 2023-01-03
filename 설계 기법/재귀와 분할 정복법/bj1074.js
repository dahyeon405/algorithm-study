// const fs = require("fs");
// const input = fs.readFileSync("/dev/stdin").toString().split(" ").map(Number);

// 풀이 1.
function solution(N, r, c) {
  let [k, curr_r, curr_c] = arguments;
  let orderArr = [];

  while (k >= 1) {
    if (curr_r < Math.pow(2, k - 1) && curr_c < Math.pow(2, k - 1)) orderArr.push(0);
    else if (curr_r >= Math.pow(2, k - 1) && curr_c < Math.pow(2, k - 1)) orderArr.push(2);
    else if (curr_r < Math.pow(2, k - 1) && curr_c >= Math.pow(2, k - 1)) orderArr.push(1);
    else orderArr.push(3);

    curr_r = curr_r >= Math.pow(2, k - 1) ? curr_r - Math.pow(2, k - 1) : curr_r;
    curr_c = curr_c >= Math.pow(2, k - 1) ? curr_c - Math.pow(2, k - 1) : curr_c;

    k--;
  }

  let answer = orderArr.reduce((a, b, index) => {
    return a + b * Math.pow(Math.pow(2, N - 1 - index), 2);
  }, 0);

  return answer;
}

// 재귀를 적용한 풀이 2.
function solution2(N, r, c) {
  let answer = 0;

  function search(N, r, c) {
    if (N === 0) return;

    if (r < Math.pow(2, N - 1) && c < Math.pow(2, N - 1)) {
      search(N - 1, r, c);
    } else if (r >= Math.pow(2, N - 1) && c < Math.pow(2, N - 1)) {
      answer += 2 * Math.pow(Math.pow(2, N - 1), 2);
      search(N - 1, r - Math.pow(2, N - 1), c);
    } else if (r < Math.pow(2, N - 1) && c >= Math.pow(2, N - 1)) {
      answer += Math.pow(Math.pow(2, N - 1), 2);
      search(N - 1, r, c - Math.pow(2, N - 1));
    } else {
      answer += 3 * Math.pow(Math.pow(2, N - 1), 2);
      search(N - 1, r - Math.pow(2, N - 1), c - Math.pow(2, N - 1));
    }
  }

  search(N, r, c);

  return answer;
}

// console.log(solution2(...input));
