function solution(gems) {
  const gemsMap = new Map();
  const cnt = new Set(gems).size;

  let l = 0,
    r = 0;
  let min = 100000;
  let result;

  gemsMap.set(gems[0], 1);

  while (l <= r && r < gems.length) {
    if (gemsMap.size === cnt) {
      if (r - l < min) {
        min = r - l;
        result = [l + 1, r + 1];
      }
      if (gemsMap.get(gems[l]) > 1) {
        gemsMap.set(gems[l], gemsMap.get(gems[l]) - 1);
      } else gemsMap.delete(gems[l]);
      l++;
    } else {
      r++;
      const gemsR = gemsMap.get(gems[r]);
      gemsMap.set(gems[r], gemsR ? gemsR + 1 : 1);
    }
  }

  return result;
}
