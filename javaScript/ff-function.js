// Write a function that would allow you to do the ff: multiply(5)(6)
// Output: 30

function multiply(x) {
    return function(y) {
        return x * y;
    }
}

console.log(multiply(5)(6));