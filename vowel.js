function vowelsAndConsonants(s) {
    let c = [];
    for (let letter of s) {
      'aeiou'.includes(letter) ? console.log(letter) : c.push(letter);
    } console.log(c.join("\n"))
}
    


function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}