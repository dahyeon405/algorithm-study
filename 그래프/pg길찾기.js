class Node {
  constructor(number, x, y) {
    this.val = number;
    this.x = x;
    this.y = y;
    this.left = null;
    this.right = null;
  }
}

class Tree {
  constructor() {
    this.head = null;
  }

  add(node, index) {
    let [x, y] = node;
    const newNode = new Node(index, x, y);

    if (!this.head) {
      this.head = newNode;
      return;
    }

    let cur = this.head;
    while (true) {
      if (cur.x > newNode.x) {
        if (!cur.left) {
          cur.left = newNode;
          break;
        }
        cur = cur.left;
      } else {
        if (!cur.right) {
          cur.right = newNode;
          break;
        }
        cur = cur.right;
      }
    }
  }

  preorder() {
    const order = [];
    function dfs(node) {
      if (!node) return;
      order.push(node.val);
      dfs(node.left);
      dfs(node.right);
    }
    dfs(this.head);
    return order;
  }

  postorder() {
    const order = [];
    function dfs(node) {
      if (!node) return;
      dfs(node.left);
      dfs(node.right);
      order.push(node.val);
    }
    dfs(this.head);
    return order;
  }
}

function solution(nodeinfo) {
  var answer = [[]];
  const tree = new Tree();

  // 우선 index 삽입
  let nodeinfoIndex = nodeinfo.map((el, index) => [...el, index + 1]);
  // 정렬
  nodeinfoIndex.sort((a, b) => b[1] - a[1]);

  // 그래프에 추가
  for (let i = 0; i < nodeinfoIndex.length; i++) {
    tree.add([nodeinfoIndex[i][0], nodeinfoIndex[i][1]], nodeinfoIndex[i][2]);
  }

  // 순회
  answer = [tree.preorder(), tree.postorder()];

  return answer;
}
