function pick (nums, pickChance) {
    const set = new Set();
    for (let poncketmon of nums) {
        set.add(poncketmon);
    }
    return set.size;
    
}

function solution(nums) {
    const maxPickChance = nums.length / 2;
    const pickChance = pick(nums, maxPickChance);
    return Math.min(pickChance, maxPickChance);
}