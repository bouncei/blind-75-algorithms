/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let numToIndex = new Map(); // Creates a hash-map/dict to reduce BigO

  for (let key in nums) {
    if (numToIndex.has(target - nums[key])) {
      return [numToIndex.get(target - nums[key]), key];
    }

    numToIndex.set(nums[key], key);
  }
  return [];
};
