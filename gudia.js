const axios=require("axios")
async function request(){
response= await fetch("https://saral.navgurukul.org/api/courses")
let d=response.data;
console.log(d) 
}
request()


// const axios=require("axios")
// async function request(){
// response=fetch("https://saral.navgurukul.org/api/courses")
// response.then(res =>
//     res.json()).then(d => {
//         console.log(d)
//     })
// let d=response.data;
// console.log(d) 
// }
// request()
