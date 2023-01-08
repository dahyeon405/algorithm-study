var findMedianSortedArrays = function (nums1, nums2) {
  let nums1ptr = 0;
  let nums2ptr = 0;
  let mergedArr = [];
  while (nums1[nums1ptr] !== undefined && nums2[nums2ptr] !== undefined) {
    if (nums1[nums1ptr] < nums2[nums2ptr]) {
      mergedArr.push(nums1[nums1ptr]);
      nums1ptr++;
    } else {
      mergedArr.push(nums2[nums2ptr]);
      nums2ptr++;
    }
  }
  while (nums1[nums1ptr] !== undefined) {
    mergedArr.push(nums1[nums1ptr]);
    nums1ptr++;
  }
  while (nums2[nums2ptr] !== undefined) {
    mergedArr.push(nums2[nums2ptr]);
    nums2ptr++;
  }
  const length = mergedArr.length;
  let median;
  if (length % 2 === 0) {
    median = (mergedArr[length / 2] + mergedArr[length / 2 - 1]) / 2;
  } else median = mergedArr[Math.floor(length / 2)];
  return median;
};
