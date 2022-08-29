const ages = [32, 33, 18, 40];

ages.every(checkAge)

function checkAge(age) {
  return age > 18;
}
console.log(checkAge())