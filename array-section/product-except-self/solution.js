/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  let n = nums.length;
  let ans = new Array(n).fill(0);
  let product = 1;
  let zeros = 0;

  for (let num of nums) {
    if (num === 0) {
      zeros++;
      continue;
    }

    product *= num;
  }

  // When there is one "0" in tha array
  if (zeros === 1) {
    for (let index in nums) {
      ans[index] = nums[index] === 0 ? product : 0;
    }
  }
  // When there is no "0" in tha array
  else if (zeros === 0) {
    for (let index in nums) {
      ans[index] = Math.floor(product / nums[index]);
    }
  }

  return ans;
};
