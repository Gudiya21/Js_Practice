// let t="Hello everyone my name is gudia";
// let r=

// let chars = ['A', 'B', 'A', 'C', 'B'];
// let uniqueChars = [...new Set(chars)];

// console.log(uniqueChars);



// ES6 Implementation
// var array = [1, 2, 3, 5, 1, 5, 9, 1, 2, 8];

// b=Array.from(new Set(array)); // [1, 2, 3, 5, 9, 8]
// console.log(b)

// // ES5 Implementation
// var array = [1, 2, 3, 5, 1, 5, 9, 1, 2, 8];

// uniqueArray(array); // [1, 2, 3, 5, 9, 8]

// function uniqueArray(array) {
//   var hashmap = {};
//   var unique = [];

//   for(var i = 0; i < array.length; i++) {
//     // If key returns undefined (unique), it is evaluated as false.
//     if(!hashmap.hasOwnProperty(array[i])) {
//       hashmap[array[i]] = 1;
//       unique.push(array[i]);
//     }
//   }

//   console.log(unique);
// }

// function modifyArray(arr, callback) {
//     // do something to arr here
//     arr.push(100);
//     // then execute the callback function that was passed
//     callback();
//   }
  
//   var arr = [1, 2, 3, 4, 5];
  
//   modifyArray(arr, function() {
//     console.log("array has been modified", arr);
//   });


// for (let i = 1; i <= 100; i++) {
//     let f = i % 3 == 0,
//       b = i % 5 == 0;
//     console.log(f ? (b ? 'FizzBuzz' : 'Fizz') : b ? 'Buzz' : i);
//   }


var firstWord = "Mary";
var secondWord = "Army";

isAnagram(firstWord, secondWord); // true

function isAnagram(first, second) {
  // For case insensitivity, change both words to lowercase.
  var a = first.toLowerCase();
  var b = second.toLowerCase();

  // Sort the strings, and join the resulting array to a string. Compare the results
  a = a.split("").sort().join("");
  b = b.split("").sort().join("");

  console.log(a === b);
}