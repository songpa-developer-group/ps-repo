function longestPalindrome(s) {
  const counts = {};
  let sum = 0;
  let oddPresent = false;

  for (let i = 0; i < s.length; i++) {
    counts[s[i]] = (counts[s[i]] || 0) + 1;
  }

  for (let letter in counts) {
    if (counts[letter] % 2 === 0) {
      sum += counts[letter];
    } else {
      oddPresent = true;
      sum += counts[letter] - 1;
    }
  }

  if (oddPresent) sum += 1;

  return sum;
}

console.log(longestPalindrome("abccccdd"));
