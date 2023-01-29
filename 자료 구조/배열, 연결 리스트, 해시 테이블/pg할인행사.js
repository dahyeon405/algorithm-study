function solution(want, number, discount) {
  var answer = 0;

  const countMap = new Map();

  function isPossible(map) {
    let ispossible = true;
    want.forEach((el, index) => {
      if (!map.has(el) || map.get(el) < number[index]) ispossible = false;
    });
    return ispossible;
  }

  const sum = number.reduce((a, b) => a + b, 0);

  let i = 0;
  let k = 0;
  while (k < 9) {
    if (countMap.has(discount[k])) countMap.set(discount[k], countMap.get(discount[k]) + 1);
    else countMap.set(discount[k], 1);
    k++;
  }

  let count = 0;
  while (k < discount.length) {
    if (countMap.has(discount[k])) countMap.set(discount[k], countMap.get(discount[k]) + 1);
    else countMap.set(discount[k], 1);
    if (isPossible(countMap)) count++;
    countMap.set(discount[i], countMap.get(discount[i]) - 1);
    i++;
    k++;
  }

  return count;
}
