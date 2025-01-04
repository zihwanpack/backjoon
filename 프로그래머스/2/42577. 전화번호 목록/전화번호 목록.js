function solution(phone_book) {
    let answer = true;
    const sortedBook = phone_book.sort()
    
    for (let i = 0; i < sortedBook.length - 1; i++) {
        const currentNum = sortedBook[i];
        const nextNum = sortedBook[i + 1];
        if (nextNum.startsWith(currentNum)) answer = false;
    }
    
    return answer;
}