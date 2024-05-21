/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  if (nums.length === 0) {
    return -1;
  }

  numsToIndex = new Map();

  for (let index in nums) {
    numsToIndex.set(nums[index], index);

    if (numsToIndex.get(target)) {
      return numsToIndex.get(target);
    }
  }

  return -1;
};
