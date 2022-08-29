function getSecondLargest(nums) {
    // Complete the function
    nums.sort(function(a,b){return a - b});
    for (let i = 1; i < nums.length; i++){
        while (nums[i] === nums[i-1]){
            nums.splice(i, 1);
        }
    };
    nums.reverse();
    return nums[1];
}


function main() {
    const n = +(readLine());
    const nums = readLine().split(' ').map(Number);
    
    console.log(getSecondLargest(nums));
}