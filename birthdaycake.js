// function birthdayCakeCandles(arr) {

//     const velas = arr.filter(value => Math.max(...arr) === value)
//     return velas.length;
// }

function birthdayCakeCandles(ar) {
    var maxHeight = Math.max(...ar);
    var maxHeightCount = 0;  
    for(var i = 0; i < ar.length; i++){
        if (ar[i] == maxHeight){
            maxHeightCount = maxHeightCount + 1;
        }
    }
    console.log(maxHeightCount);
    return maxHeightCount;
}
birthdayCakeCandles(require("readline-sync").questionInt("enter"))