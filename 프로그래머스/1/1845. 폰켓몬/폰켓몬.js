function solution(nums) {
    let answer = 0;
    const sortedNums = nums.sort((a, b) => (a - b));
    const set = new Set(sortedNums);
    const limit = nums.length / 2;
    
    return limit < set.size ? limit : set.size;
}