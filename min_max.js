function miniMaxSum(arr) {   

    var arrClone1 = arr.slice() 
    var arrClone2 = arr.slice() 
  
    var arrMinor = arrClone1.sort(function(a, b){return a - b;})
    arrMinor.pop()
  
    var arrMajor = arrClone2.sort(function(a, b){return b - a;})
    arrMajor.pop()
  
    function getSum(a, b) {
      return a + b;
    }
  
    var result1 = arrMinor.reduce(getSum) 
    var result2 = arrMajor.reduce(getSum)    
  
    console.log(`${result1} ${result2}`)
}