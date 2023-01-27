function solution(n, build_frame) {
  const frame = Array.from({ length: n + 1 }, () => new Array(n + 1).fill(-1));
  // -1 : 아무것도 없음
  // 0: 기둥
  // 1: 둘 다
  // 2: 보

  function isColumn(x, y) {
    if (x < 0 || x > n) return false;
    if (y < 0 || y > n) return false;
    if (frame[x][y] === 2 || frame[x][y] === 0) return true;
    return false;
  }

  function isBo(x, y) {
    if (x < 0 || x > n) return false;
    if (y < 0 || y > n) return false;
    if (frame[x][y] === 2 || frame[x][y] === 1) return true;
    return false;
  }

  // 설치
  function canBuild(x, y, type) {
    // 기둥
    if (type === 0) {
      if (y === 0 || isColumn(x, y - 1)) return true;
      if (isBo(x, y) || isBo(x - 1, y)) {
        return true;
      }
      return false;
    } else {
      // 보
      if (isColumn(x, y - 1) || isColumn(x + 1, y - 1)) return true;
      if (isBo(x + 1, y) && isBo(x - 1, y)) return true;
      return false;
    }
  }

  function checkValidity(x, y) {
    for (let i = 0; i <= n; i++) {
      for (let k = 0; k <= n; k++) {
        if (frame[i][k] === -1) continue;
        if (frame[i][k] !== 2) {
          if (!canBuild(i, k, frame[i][k])) return false;
        } else {
          if (!canBuild(i, k, 0) || !canBuild(i, k, 1)) return false;
        }
      }
    }
    return true;
  }

  build_frame.forEach((element) => {
    let [x, y, type, action] = element;
    if (action === 0) {
      let originalValue = frame[x][y];
      if (originalValue === 2) frame[x][y] = type === 0 ? 1 : 0;
      else frame[x][y] = -1;
      if (!checkValidity(x, y)) frame[x][y] = originalValue;
    } else {
      if (canBuild(x, y, type)) {
        if (frame[x][y] !== -1) frame[x][y] = 2;
        else frame[x][y] = type;
      }
    }
  });

  const answer = [];
  for (let i = 0; i <= n; i++) {
    for (let k = 0; k <= n; k++) {
      if (frame[i][k] === -1) continue;
      if (frame[i][k] !== 2) answer.push([i, k, frame[i][k]]);
      else {
        answer.push([i, k, 0]);
        answer.push([i, k, 1]);
      }
    }
  }

  return answer;
}
