function solution(phone_book) {
    const hash = new Map();
    
    for (let i = 0; i < phone_book.length; i++) {
        hash.set(phone_book[i], true);
    }
    
    for (let j = 0; j < phone_book.length; j++) {
        let prefix = '';
        for (let k = 0; k < phone_book[j].length; k++) {
            prefix += phone_book[j][k];
            if (prefix !== phone_book[j] && hash.has(prefix)) {
                return false;
            }
        }
    }
    

    return true;
}