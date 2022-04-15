function nextPermutation(nums) {
  const swap = (arr, a, b) => ([arr[a], arr[b]] = [arr[b], arr[a]]);

  let i = nums.length - 2; //1
  while (i >= 0 && nums[i] >= nums[i + 1]) i--;

  if (i >= 0) {
    let j = nums.length - 1;
    while (nums[i] >= nums[j]) j--;
    swap(nums, i, j);
  }
  nums.push(...nums.splice(i + 1).reverse());
}

nextPermutation([1, 2, 3]);
