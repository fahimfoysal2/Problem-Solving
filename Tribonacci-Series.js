// Create a “tribonacci” function in javascript implementing the tribonacci sequence.This is a variation on the Fibonacci sequence, in which every next number is found by adding up the two preceding numbers. The tribonacci sequence is similar, but instead of starting with two predetermined numbers, the sequence starts with three predetermined numbers and each subsequent number is the sum of the three preceding numbers.
// The function has two parameters:
// A signature array of 3 elements containing the predetermined starting numbers of the tribonacci sequence.
// A non-negative integer of the first n elements that the functions should return.
// If n == 0, return 0.

/**
 *
 * @param sequence - array of 3 elements containing the predetermined starting numbers of the tribonacci sequence
 * @param n - number of elements to return
 * @returns {number / array} - returns 0 or an array of the nth elements of the tribonacci sequence
 */
function tribonacci(sequence, n) {
    if (n === 0) return 0;

    let tribonacciArray = [];
    for (let i = 0; i < n; i++) {
        if (i < 3) {
            tribonacciArray.push(sequence[i]);
        } else {
            tribonacciArray.push(tribonacciArray[i - 1] + tribonacciArray[i - 2] + tribonacciArray[i - 3]);
        }
    }
    return tribonacciArray;
}

console.log(tribonacci([1, 1, 1], 5));
console.log(tribonacci([0, 0, 1], 9));
console.log(tribonacci([1, 2, 3], 2));
console.log(tribonacci([1, 2, 3], 0));