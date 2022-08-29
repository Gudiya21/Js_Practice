const ages = [3, 10, 18, 20];

function checkAge(age) {
  return age > 18;
}

function myFunction() {
  let co=ages.find(checkAge);
  return co
}
console.log(myFunction())