function reverseString(s) {
    try{
let a = s.split("");
    a.reverse();
    s = a.join("");
}
 catch (ex) {
    console.log("s.split is not a function") 
 }
 finally {
     console.log(s);
 }

}


function main() {
const s = eval(readLine());

reverseString(s);
}