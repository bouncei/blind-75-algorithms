var containsDuplicate = function (nums) {
  const numSet = new Set(); // Hash map

  for (const num of nums) {
    if (numSet.has(num)) {
      return true;
    }
    numSet.add(num);
  }

  return false;
};
