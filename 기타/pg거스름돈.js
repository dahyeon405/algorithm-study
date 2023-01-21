// 처음 풀이. 효율성 통과 못함
function getCounts(index, amount, money) {
  if (amount === 0) return 1;
  if (index >= money.length) return 0;

  const k = money[index];
  const q = Math.floor(amount / k);

  let count = 0;
  for (let i = q; i >= 0; i--) {
    count += getCounts(index + 1, amount - k * i, money);
  }

  return count;
}

function solution(n, money) {
  let sortedMoney = money.sort((a, b) => b - a);
  const result = getCounts(0, n, sortedMoney);

  return result;
}
