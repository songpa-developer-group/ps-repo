var largestNumber = function (nums) {
  return (
    nums
      .sort((a, b) => "" + b + a - ("" + a + b))
      .join("")
      .replace(/^0*/g, "") || "0"
  );
};

console.log(largestNumber([10, 2]));
