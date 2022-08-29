var n=8;
// for (let i = 1; i <= n; i++) {
//         console.log(" ".repeat(n-i) + "#".repeat(i))
//       }    

// for (const x of Array(5).keys())

let i=0;
let output = ''
for (let s = n - 1; s >= i; s--) {
        output += ' '
    }
    
    // inner for loop to keep track of the #s on each line
        // h should start at one because the first line will always have one #
        // h should be less than or equal to the row that we are on since h will approach and eventually equal n
        // h increases since we increment h to equal i which will eventually equal n
    for (let h = 1; h <= i; h++) {
        output += '#'
    }
    // new line
    output += "\n"
   

// log the final result
console.log(output)