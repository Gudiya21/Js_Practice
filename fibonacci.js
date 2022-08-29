// var user=require("readline-sync").questionInt("Enter");
// let a=0;
// let b=1;
// let c=a+b;
// console.log(a)
// console.log(c)
// while(c<=user){
//     console.log(c)
//     a=b
//     b=c
//     c=a+b
// }


var user=require("readline-sync").questionInt("Enter: ");
let fibonacci=(() => {
    let a=0;
    let b=1;
    let c=a+b;
    console.log(a)
    console.log(c)
    while(c<=user){
        console.log(c)
        a=b
        b=c
        c=a+b
    }
})
fibonacci()