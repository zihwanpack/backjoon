function getClothes (clothes) {
    const hash = new Map();
    for (let [name, category] of clothes) {
        hash.set(category, (hash.get(category) || 0) + 1);
    }
    return hash;
}

function countCombination (hash) {
    let answer = 1;
    for (let [category, count] of hash) {
        answer *= (count + 1);
    }
    return answer - 1;
}

function solution(clothes) {
    const hash = getClothes(clothes);
    return countCombination(hash);
}