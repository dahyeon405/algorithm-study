function solution(n, t, m, timetable) {
  var answer = "";

  let sortedTable = timetable.sort((a, b) => {
    if (a > b) return -1;
    return 1;
  }); //역순으로 정렬

  let k = 1; // k번째 셔틀

  function calculateDptTime(k, t) {
    const h = 9 + Math.floor(((k - 1) * t) / 60);
    const min = ((k - 1) * t) % 60;
    return h.toString().padStart(2, "0") + ":" + min.toString().padStart(2, "0");
  }

  let lastEl = "";
  while (k <= n) {
    let dptTime = calculateDptTime(k, t);
    let ppl = 0;
    if (sortedTable.length === 0) {
      lastEl = "";
      break;
    }
    while (ppl < m) {
      let last = sortedTable[sortedTable.length - 1];
      if (last <= dptTime) {
        lastEl = sortedTable.pop();
        ppl++;
      } else break;
    }
    if (k === n && ppl < m) return dptTime;
    k++;
  }

  if (!lastEl) {
    return calculateDptTime(n, t);
  }

  let [hr, min] = lastEl.split(":");

  if (min !== "00") {
    let newM = (Number(min) - 1).toString().padStart(2, "0");
    return hr + ":" + newM;
  } else {
    let newH = (Number(hr) - 1).toString().padStart(2, "0");
    return newH + ":" + "59";
  }
}
