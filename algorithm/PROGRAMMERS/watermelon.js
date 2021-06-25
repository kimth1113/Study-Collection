// 수박수박수박수박수박수? level1

function solution(n, f1, f2) {
    let word = ''
    
    let cnt = 1;
    while (n > 0) {
        if (cnt % 2 === 1){
            word += '수'
        } else {
            word += '박'
        }
        n--;   
        cnt++;
    }
    return word;
}





