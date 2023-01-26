function solution(n, cores) {
  var answer = 0;
  const time = Array.from({ length: cores.length }, () => 0);

  /* 직접 돌면서 배정하기 - 시간 초과
    let left = n;
    let t = 0;
    let last = 0;
    while (left > 0){
        for (let i = 0; i < cores.length; i++){
            if (t === 0 || (t - time[i] >= cores[i])){
                time[i] = t;
                left--;
                last = i + 1;
                if (left === 0) break;
            }
        }
        t++;
    }*/

  /* 더 오래 걸린 풀이..
    function jobDone(t, cores){
        let total = 0;
        cores.forEach((i)=>{
            total += Math.floor(t/i) + 1;
        })
        return total;
    }
    
    let t = Math.ceil(n/cores.length);
    while (true){
        if (jobDone(t, cores) >= n) break;        
        t++;
    }

    let left = n - jobDone(t-1, cores);
    for (let i = 0; i < cores.length; i++){
        if (t%cores[i] === 0){
            left--;
            if (left === 0) return i+1;
        }
    }    
    */

  // 위 풀이를 이분 탐색으로 개선!!!!!

  function jobDone(t, cores) {
    let total = 0;
    cores.forEach((i) => {
      total += Math.floor(t / i) + 1;
    });
    return total;
  }

  let left = Math.ceil(n / cores.length);
  let right = left * Math.max(...cores);

  while (left < right - 1) {
    let mid = left + Math.floor((right - left) / 2);
    if (jobDone(mid, cores) >= n) {
      right = mid;
    } else left = mid;
  }

  let t = right;
  if (jobDone(left, cores) >= n) t = left;

  let jobLeft = n - jobDone(t - 1, cores);
  for (let i = 0; i < cores.length; i++) {
    if (t % cores[i] === 0) {
      jobLeft--;
      if (jobLeft === 0) return i + 1;
    }
  }

  return 0;
}
