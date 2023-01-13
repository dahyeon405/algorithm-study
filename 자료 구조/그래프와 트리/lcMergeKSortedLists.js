/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */

// 하나하나 합치는 방법. O(kn)
var mergeKLists = function (lists) {
  function merge(a, b) {
    if (!b) return a;
    if (!a) return b;
    let root = null;
    let node = null;
    while (a && b) {
      if (a.val < b.val) {
        if (!root) root = a;
        else node.next = a;
        node = a;
        a = a.next;
      } else {
        if (!root) root = b;
        else node.next = b;
        node = b;
        b = b.next;
      }
    }
    while (a) {
      node.next = a;
      node = a;
      a = a.next;
    }
    while (b) {
      node.next = b;
      node = b;
      b = b.next;
    }
    return root;
  }

  if (lists[0] === undefined) return null;
  let mergedRoot = lists[0];
  for (let i = 0; i < lists.length - 1; i++) {
    mergedRoot = merge(mergedRoot, lists[i + 1]);
  }

  return mergedRoot;
};
