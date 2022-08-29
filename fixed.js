var price=2;
var VAT=3;
let total=`Total: ${(price * (1 + VAT)).toFixed(1)}`;
console.log(total)