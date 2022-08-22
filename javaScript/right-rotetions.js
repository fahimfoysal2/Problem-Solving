// Write a function that returns an updated array with r right rotations on an array of integers a. Output the last rotation.
//    Sample: [2,3,4,5,7]
//    Perform 3 right rotations:
//      1. [7,2,3,4,5]
//      2. [5,7,2,3,4]
//      3. [4,5,7,2,3]
//      4. [3,4,5,7,2]
//      5. [2,3,4,5,7]
//      6. [7,2,3,4,5]
//      7. [5,7,2,3,4]
//    Output: [4,5,7,2,3]

/**
 * 
 * @param {Array<Int>} a array of integers
 * @param {Int} r rotations
 * @returns right rotated array
 */
function rightRotations(a, r) {
    for (var i = 0; i < r; i++) {
        var temp = a.pop();
        a.unshift(temp);
    }
    return a;
}

console.log(rightRotations([2, 3, 4, 5, 7], 3));