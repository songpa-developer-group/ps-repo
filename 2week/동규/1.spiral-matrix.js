function spiralOrder(matrix) {
  let top = 0;
  let left = 0;
  let bottom = matrix.length - 1;
  let rigth = matrix[0].length - 1;
  const result = [];
  const size = matrix.length * matrix[0].length;

  while (result.length < size) {
    for (let i = left; i <= rigth && result.length < size; i++) {
      result.push(matrix[top][i]);
    }
    top++;
    for (let i = top; i <= bottom && result.length < size; i++) {
      result.push(matrix[i][rigth]);
    }
    rigth--;
    for (let i = rigth; i >= left && result.length < size; i--) {
      result.push(matrix[bottom][i]);
    }
    bottom--;
    for (let i = bottom; i >= top && result.length < size; i--) {
      result.push(matrix[i][left]);
    }
    left++;
  }
  return result;
}
