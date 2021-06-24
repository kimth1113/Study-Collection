function solution(nums) {
  const N = nums.length;
  const result = [];
  
  for (let i = 0; i < N-2; i++) {
      for (let j = i+1; j < N-1; j++) {
          for (let k = j+1; k < N; k++) {
              result.push(nums[i] + nums[j] + nums[k]);
          }
      }
  }
  
  const checkDevide = number => {
      for (let num = 2; num < number; num++) {
          if (number % num === 0) {
              return 0
          }
      }
      return number
  }
  
  const ans = result.map(checkDevide);
  
  let cnt = 0;
  
  ans.forEach((num) => {
      if (num > 0) {
          cnt += 1;
      }
  })
  
  return cnt;
}