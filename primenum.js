// FIRST LOGIC

let isprime = (num) => {
    for(let i = 2; i < num; i++)
        if(num % i===0) return false;
    return true
}

let arr=[1,2,3,4,5];
let filteredArr=arr.filter((val) => isprime(val));
console.log(filteredArr)


// SECOND LOGIC

let isprime2 = (num) => {
    if(num<=3) return true;
    if(num%2===0) return false;
    for(let i = 3; i < num; i+=2)
        if(num % i===0) return false;
    return true
}

let arr2=[1,2,3,4,5];
let filteredArr2=arr.filter((val)=> isprime(val));
console.log(filteredArr)