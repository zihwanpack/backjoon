function solution(clothes) {
    let answer = 1;
    const map = new Map();
    
    clothes.forEach(cloth => {
        const [name, type] = cloth;
        map.set(type, (map.get(type) || 0) + 1);
    })
    
     map.forEach(count => {
        answer *= (count + 1);
    });

    return answer - 1;
}