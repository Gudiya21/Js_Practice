// let prom= new Promise(function())
// let onfulfilment=(result)=>{
//     console.log(result)
// }
// let onRejection=(error)=>{
//     console.log(error)
// }


// let myPromise = new Promise(function(myResolve, myReject) {
//     // "Producing Code" (May take some time)
    
//       myResolve(); // when successful
//       myReject();  // when error
//     });
    
//     // "Consuming Code" (Must wait for a fulfilled Promise)
//     myPromise.then(
//       function(value) { /* code if successful */ },
//       function(error) { /* code if some error */ }
//     );


// const count = true;

// let countValue = new Promise(function (resolve, reject) {
//     if (count) {
//         resolve("There is a count value.");
//     } else {
//         reject("There is no count value");
//     }
// });

// console.log(countValue);
// let onfulfilment=(result)=>{
//     console.log(result)
// }
// let onRejection=(error)=>{
//     console.log(error)
// }
// const count=true;
// let prom= new Promise(function(truly,falsy){
//     if(count){
//         truly("Here is a success");
//     }
//     else{
//         falsy("Here is a failure");

//     }
// });
// prom.then(onfulfilment);
// prom.catch(onRejection); 


let pro=new Promise(function(fun1,func2){
    if(8<5){
        fun1("8 is big than 5")
    }
    else{
        func2("5 is less than 8")
    }
})
let resolve=(truly)=>{
    console.log(truly);
}
let reject=(falsy)=>{
    console.log(falsy);
}
pro.then(resolve);
pro.catch(reject);


