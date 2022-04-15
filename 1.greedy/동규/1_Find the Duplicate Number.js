function findDuplicate(nums) {
  let obj = {};
  for (let i of nums) {
    if (!obj[i]) {
      obj[i] = 1;
    } else {
      return i;
    }
  }
}

console.log(findDuplicate([1, 3, 4, 2, 2]));
