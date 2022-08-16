/*
*   Problem: 01 - Increase value of a counter based on the items of a given array
*   Given an array of integers, keep a total score based on the following:
*       1. Add 1 point for every even number in the array
*       2. Add 3 points for every odd number in the array
*       3. Add 5 points for every time you encounter a 5 in the array
*   Note that 0 is considered even.
*   Please write a function to achieve this in javascript.
* */


let arr = [1, 2, 3, 4, 5];

function arrayCounter(arr) {
    let result = 0;
    arr.map(item => {
        if (item === 5) {
            result += 5;
        } else if (item % 2 === 0) {
            result += 1;
        } else if (item % 2 !== 0) {
            result += 3;
        }
    });
    return result;
}

console.log(arrayCounter([1, 0, 3, 4, 5]));
console.log(arrayCounter([17, 19, 21]));
console.log(arrayCounter([5, 5, 5]));
