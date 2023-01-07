/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function (path) {
  const splitedPath = path.split("/");
  const resultPath = [];
  for (let i = 0; i < splitedPath.length; i++) {
    const curPath = splitedPath[i];
    if (i === 0 && curPath === "") continue;
    if (curPath === "..") {
      resultPath.pop();
      continue;
    }
    if (curPath === ".") continue;
    if (i !== 0 && curPath == "") continue;
    resultPath.push(curPath);
  }

  return "/" + resultPath.join("/");
};
