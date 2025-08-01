function getScore (answers, exam) {
     return answers.filter((e, i) => e === exam[i % exam.length]).length;
}

function solution(answers) {
    const answer = [];
    const firstExam = [1, 2, 3, 4, 5];
    const secondExam = [2, 1, 2, 3, 2, 4, 2, 5];
    const thirdExam = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    
    
    const scores = [
        getScore(answers, firstExam),
        getScore(answers, secondExam),
        getScore(answers, thirdExam)
    ];
    
    const highScore = Math.max(...scores);
    
    for (let i = 0; i < scores.length; i++) {
        if (scores[i] === highScore) {
            answer.push(i + 1);
        }
    }
    return answer;
}